void cv::meanStdDev( InputArray _src, OutputArray _mean, OutputArray _sdv, InputArray _mask ) {
CV_OCL_RUN(OCL_PERFORMANCE_CHECK(_src.isUMat()) && _src.dims() <= 2,
           ocl_meanStdDev(_src, _mean, _sdv, _mask))

Mat src = _src.getMat(), mask = _mask.getMat();
CV_Assert( mask.empty() || mask.type() == CV_8UC1 );

CV_IPP_RUN(IPP_VERSION_MAJOR >= 7, ipp_meanStdDev(src, _mean, _sdv, mask));

int k, cn = src.channels(), depth = src.depth();

SumSqrFunc func = getSumSqrTab(depth);

CV_Assert( func != 0 );

const Mat* arrays[] = {&src, &mask, 0};
uchar* ptrs[2];
NAryMatIterator it(arrays, ptrs);
int total = (int)it.size, blockSize = total, intSumBlockSize = 0;
int j, count = 0, nz0 = 0;
AutoBuffer<double> _buf(cn*4);
double *s = (double*)_buf, *sq = s + cn;
int *sbuf = (int*)s, *sqbuf = (int*)sq;
bool blockSum = depth <= CV_16S, blockSqSum = depth <= CV_8S;
size_t esz = 0;

for( k = 0; k < cn; k++ )
    s[k] = sq[k] = 0;

if( blockSum )
{
    intSumBlockSize = 1 << 15;
    blockSize = std::min(blockSize, intSumBlockSize);
    sbuf = (int*)(sq + cn);
    if( blockSqSum )
        sqbuf = sbuf + cn;
    for( k = 0; k < cn; k++ )
        sbuf[k] = sqbuf[k] = 0;
    esz = src.elemSize();
}

for( size_t i = 0; i < it.nplanes; i++, ++it )
{
    for( j = 0; j < total; j += blockSize )
    {
        int bsz = std::min(total - j, blockSize);
        int nz = func( ptrs[0], ptrs[1], (uchar*)sbuf, (uchar*)sqbuf, bsz, cn );
        count += nz;
        nz0 += nz;
        if( blockSum && (count + blockSize >= intSumBlockSize || (i+1 >= it.nplanes && j+bsz >= total)) )
        {
            for( k = 0; k < cn; k++ )
            {
                s[k] += sbuf[k];
                sbuf[k] = 0;
            }
            if( blockSqSum )
            {
                for( k = 0; k < cn; k++ )
                {
                    sq[k] += sqbuf[k];
                    sqbuf[k] = 0;
                }
            }
            count = 0;
        }
        ptrs[0] += bsz*esz;
        if( ptrs[1] )
            ptrs[1] += bsz;
    }
}

double scale = nz0 ? 1./nz0 : 0.;
for( k = 0; k < cn; k++ )
{
    s[k] *= scale;
    sq[k] = std::sqrt(std::max(sq[k]*scale - s[k]*s[k], 0.));
}

for( j = 0; j < 2; j++ )
{
    const double* sptr = j == 0 ? s : sq;
    _OutputArray _dst = j == 0 ? _mean : _sdv;
    if( !_dst.needed() )
        continue;

    if( !_dst.fixedSize() )
        _dst.create(cn, 1, CV_64F, -1, true);
    Mat dst = _dst.getMat();
    int dcn = (int)dst.total();
    CV_Assert( dst.type() == CV_64F && dst.isContinuous() &&
               (dst.cols == 1 || dst.rows == 1) && dcn >= cn );
    double* dptr = dst.ptr<double>();
    for( k = 0; k < cn; k++ )
        dptr[k] = sptr[k];
    for( ; k < dcn; k++ )
        dptr[k] = 0;
}
