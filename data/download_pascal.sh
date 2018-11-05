echo "Creating data directory..."
mkdir -p data && cd data
mkdir weights
mkdir pascal_voc

echo "Downloading Pascal VOC 2012 data..."
wget http://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar

echo "Extracting VOC data..."
tar -zvxf VOCtrainval_06-Nov-2007.tar -C pascal_voc

echo "Done."
