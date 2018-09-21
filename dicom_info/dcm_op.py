"""
Python处理医学影像学中的DICOM
2017年01月22日 13:17:18 11866人阅读 评论(7) 收藏 举报
分类：
图像处理（9） Python（52）

版权声明：本文为博主原创文章，未经博主允许不得转载。 http://blog.csdn.net/langb2014/article/details/54667905

    DICOMDICOM（Digital Imaging and Communications in Medicine）即医学数字成像和通信，是医学图像和相关信息的国际标准（ISO 12052）。它定义了质量能满足临床需要的可用于数据交换的医学图像格式，可用于处理、存储、打印和传输医学影像信息。DICOM可以便捷地交换于两个满足DICOM格式协议的工作站之间。目前该协议标准不仅广泛应用于大型医院，而且已成为小型诊所和牙科诊所医生办公室的标准影像阅读格式。


DICOM被广泛应用于放射医疗、心血管成像以及放射诊疗诊断设备（X射线，CT，核磁共振，超声等），并且在眼科和牙科等其它医学领域得到越来越深入广泛的应用。在数以万计的在用医学成像设备中，DICOM是部署最为广泛的医疗信息标准之一。当前大约有百亿级符合DICOM标准的医学图像用于临床使用。

目前，越来越多的DICOM应用程序和分析软件被运用于临床医学，促使越来越多的编程语言开发出支持DICOM API的框架。今天就让我来介绍一下Python语言下支持的DICOM模块，以及如何完成基本DICOM信息分析和处理的编程方法。


    Pydicom

    Pydicom是一个处理DICOM文件的纯Python软件包。它可以通过非常容易的“Pythonic”的方式来提取和修改DICOM数据，修改后的数据还会借此生成新的DICOM文件。作为一个纯Python包，Pydicom可以在Python解释器下任何平台运行，除了必须预先安装Numpy模块外，几乎无需其它任何配置要求。其局限性之一是无法处理压缩像素图像（如JPEG），其次是无法处理分帧动画图像（如造影电影）。

    SimpleITK
    Insight Segmentation and Registration Toolkit (ITK)是一个开源、跨平台的框架，可以提供给开发者增强功能的图像分析和处理套件。其中最为著名的就是SimpleITK，是一个简化版的、构建于ITK最顶层的模块。SimpleITK旨在易化图像处理流程和方法。
    PIL
    Python Image Library (PIL) 是在Python环境下不可缺少的图像处理模块，支持多种格式，并提供强大的图形与图像处理功能，而且API却非常简单易用。
    OpenCV
    OpenCV的全称是：Open Source Computer Vision Library。OpenCV是一个基于BSD许可（开源）发行的跨平台计算机视觉库，可以运行在Linux、Windows和Mac OS操作系统上。它轻量级而且高效——由一系列 C 函数和少量 C++ 类构成，同时提供了Python、Ruby、MATLAB等语言的接口，实现了图像处理和计算机视觉方面的很多通用算法。

"""
下面Python代码来演示如何编程处理心血管冠脉造影DICOM图像信息。


1. 导入主要框架：SimpleITK、pydicom、PIL、cv2和numpy

    import SimpleITK as sitk
    from PIL import Image
    import pydicom
    import numpy as np
    import cv2


2. 应用SimpleITK框架来读取DICOM文件的矩阵信息。如果DICOM图像是三维螺旋CT图像，则帧参数则代表CT扫描层数；而如果是造影动态电影图像，则帧参数就是15帧/秒的电影图像帧数。

    def loadFile(filename):
           ds = sitk.ReadImage(filename)
           img_array = sitk.GetArrayFromImage(ds)
           frame_num, width, height = img_array.shape
          return img_array, frame_num, width, height


3. 应用pydicom来提取患者信息。

    def loadFileInformation(filename):
           information = {}
           ds = pydicom.read_file(filename)    
           information['PatientID'] = ds.PatientID
           information['PatientName'] = ds.PatientName

           information['PatientBirthDate'] = ds.PatientBirthDate

           information['PatientSex'] = ds.PatientSex

           information['StudyID'] = ds.StudyID

           information['StudyDate'] = ds.StudyDate

           information['StudyTime'] = ds.StudyTime

           information['InstitutionName'] = ds.InstitutionName

           information['Manufacturer'] = ds.Manufacturer

           information['NumberOfFrames'] = ds.NumberOfFrames    

          return information


4. 应用PIL来检查图像是否被提取。

    def showImage(img_array, frame_num = 0):
            img_bitmap = Image.fromarray(img_array[frame_num])
           return img_bitmap


5. 采用CLAHE (Contrast Limited Adaptive Histogram Equalization)技术来优化图像。

    def limitedEqualize(img_array, limit = 4.0):
            img_array_list = []

            for img in img_array:

                  clahe = cv2.createCLAHE(clipLimit = limit, tileGridSize = (8,8))

                  img_array_list.append(clahe.apply(img))

           img_array_limited_equalized = np.array(img_array_list)

           return img_array_limited_equalized

"""
这一步对于整个图像处理起到很重要的作用，可以根据不同的原始DICOM图像的窗位和窗宽来进行动态调整，以达到最佳的识别效果。
原始图像：
经过自动窗位窗宽调节，生成：
再经过CLAHE优化，则生成：
最后应用OpenCV的Python框架cv2把每帧图像组合在一起，生成通用视频格式。
"""
    def writeVideo(img_array):

           frame_num, width, height = img_array.shape

           filename_output = filename.split('.')[0] + '.avi'    

           video = cv2.VideoWriter(filename_output, -1, 16, (width, height))    

           for img in img_array:

                      video.write(img)

       video.release()

由于我没有数据，微信图片无法复制过来，只能看看代码了，详细图片请看参考。
======================================================================================================

VTK加载DICOM数据

[cpp] view plain copy

    import vtk  
    from vtk.util import numpy_support  
    import numpy  
      
    PathDicom = "./dir_with_dicom_files/"  
    reader = vtk.vtkDICOMImageReader()  
    reader.SetDirectoryName(PathDicom)  
    reader.Update()  
      
    # Load dimensions using `GetDataExtent`  
    _extent = reader.GetDataExtent()  
    ConstPixelDims = [_extent[1]-_extent[0]+1, _extent[3]-_extent[2]+1, _extent[5]-_extent[4]+1]  
      
    # Load spacing values  
    ConstPixelSpacing = reader.GetPixelSpacing()  
      
    # Get the 'vtkImageData' object from the reader  
    imageData = reader.GetOutput()  
    # Get the 'vtkPointData' object from the 'vtkImageData' object  
    pointData = imageData.GetPointData()  
    # Ensure that only one array exists within the 'vtkPointData' object  
    assert (pointData.GetNumberOfArrays()==1)  
    # Get the `vtkArray` (or whatever derived type) which is needed for the `numpy_support.vtk_to_numpy` function  
    arrayData = pointData.GetArray(0)  
      
    # Convert the `vtkArray` to a NumPy array  
    ArrayDicom = numpy_support.vtk_to_numpy(arrayData)  
    # Reshape the NumPy array to 3D using 'ConstPixelDims' as a 'shape'  
    ArrayDicom = ArrayDicom.reshape(ConstPixelDims, order='F')  

PYDICOM加载DICOM数据：

可以在https://github.com/darcymason/pydicom的test里面看怎么用代码。

[python] view plain copy

    import dicom  
    import os  
    import numpy  
      
    PathDicom = "./dir_with_dicom_series/"  
    lstFilesDCM = []  # create an empty list  
    for dirName, subdirList, fileList in os.walk(PathDicom):  
        for filename in fileList:  
            if ".dcm" in filename.lower():  # check whether the file's DICOM  
                lstFilesDCM.append(os.path.join(dirName,filename))  
                  
    # Get ref file  
    RefDs = dicom.read_file(lstFilesDCM[0])  
      
    # Load dimensions based on the number of rows, columns, and slices (along the Z axis)  
    ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))  
      
    # Load spacing values (in mm)  
    ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))  
      
    # The array is sized based on 'ConstPixelDims'  
    ArrayDicom = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)  
      
    # loop through all the DICOM files  
    for filenameDCM in lstFilesDCM:  
        # read the file  
        ds = dicom.read_file(filenameDCM)  
        # store the raw image data  
        ArrayDicom[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array  

转换VTK built-in types to SimpleITK/ITK built-ins and vice-versa
[python] view plain copy

    import vtk  
    import SimpleITK  
      
    dctITKtoVTK = {SimpleITK.sitkInt8: vtk.VTK_TYPE_INT8,  
                   SimpleITK.sitkInt16: vtk.VTK_TYPE_INT16,  
                   SimpleITK.sitkInt32: vtk.VTK_TYPE_INT32,  
                   SimpleITK.sitkInt64: vtk.VTK_TYPE_INT64,  
                   SimpleITK.sitkUInt8: vtk.VTK_TYPE_UINT8,  
                   SimpleITK.sitkUInt16: vtk.VTK_TYPE_UINT16,  
                   SimpleITK.sitkUInt32: vtk.VTK_TYPE_UINT32,  
                   SimpleITK.sitkUInt64: vtk.VTK_TYPE_UINT64,  
                   SimpleITK.sitkFloat32: vtk.VTK_TYPE_FLOAT32,  
                   SimpleITK.sitkFloat64: vtk.VTK_TYPE_FLOAT64}  
    dctVTKtoITK = dict(zip(dctITKtoVTK.values(),   
                           dctITKtoVTK.keys()))  
                             
    def convertTypeITKtoVTK(typeITK):  
        if typeITK in dctITKtoVTK:  
            return dctITKtoVTK[typeITK]  
        else:  
            raise ValueError("Type not supported")  
      
    def convertTypeVTKtoITK(typeVTK):  
        if typeVTK in dctVTKtoITK:  
            return dctVTKtoITK[typeVTK]  
        else:  
            raise ValueError("Type not supported")  

VTK-SimpleITK绘制数据

[python] view plain copy

    #!/usr/bin/python  
      
    import SimpleITK as sitk  
    import vtk  
    import numpy as np  
      
    from vtk.util.vtkConstants import *  
      
    def numpy2VTK(img,spacing=[1.0,1.0,1.0]):  
        # evolved from code from Stou S.,  
        # on http://www.siafoo.net/snippet/314  
        importer = vtk.vtkImageImport()  
          
        img_data = img.astype('uint8')  
        img_string = img_data.tostring() # type short  
        dim = img.shape  
          
        importer.CopyImportVoidPointer(img_string, len(img_string))  
        importer.SetDataScalarType(VTK_UNSIGNED_CHAR)  
        importer.SetNumberOfScalarComponents(1)  
          
        extent = importer.GetDataExtent()  
        importer.SetDataExtent(extent[0], extent[0] + dim[2] - 1,  
                               extent[2], extent[2] + dim[1] - 1,  
                               extent[4], extent[4] + dim[0] - 1)  
        importer.SetWholeExtent(extent[0], extent[0] + dim[2] - 1,  
                                extent[2], extent[2] + dim[1] - 1,  
                                extent[4], extent[4] + dim[0] - 1)  
      
        importer.SetDataSpacing( spacing[0], spacing[1], spacing[2])  
        importer.SetDataOrigin( 0,0,0 )  
      
        return importer  
      
    def volumeRender(img, tf=[],spacing=[1.0,1.0,1.0]):  
        importer = numpy2VTK(img,spacing)  
      
        # Transfer Functions  
        opacity_tf = vtk.vtkPiecewiseFunction()  
        color_tf = vtk.vtkColorTransferFunction()  
      
        if len(tf) == 0:  
            tf.append([img.min(),0,0,0,0])  
            tf.append([img.max(),1,1,1,1])  
      
        for p in tf:  
            color_tf.AddRGBPoint(p[0], p[1], p[2], p[3])  
            opacity_tf.AddPoint(p[0], p[4])  
      
        # working on the GPU  
        # volMapper = vtk.vtkGPUVolumeRayCastMapper()  
        # volMapper.SetInputConnection(importer.GetOutputPort())  
      
        # # The property describes how the data will look  
        # volProperty =  vtk.vtkVolumeProperty()  
        # volProperty.SetColor(color_tf)  
        # volProperty.SetScalarOpacity(opacity_tf)  
        # volProperty.ShadeOn()  
        # volProperty.SetInterpolationTypeToLinear()  
      
        # working on the CPU  
        volMapper = vtk.vtkVolumeRayCastMapper()  
        compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()  
        compositeFunction.SetCompositeMethodToInterpolateFirst()  
        volMapper.SetVolumeRayCastFunction(compositeFunction)  
        volMapper.SetInputConnection(importer.GetOutputPort())  
      
        # The property describes how the data will look  
        volProperty =  vtk.vtkVolumeProperty()  
        volProperty.SetColor(color_tf)  
        volProperty.SetScalarOpacity(opacity_tf)  
        volProperty.ShadeOn()  
        volProperty.SetInterpolationTypeToLinear()  
          
        # Do the lines below speed things up?  
        # pix_diag = 5.0  
        # volMapper.SetSampleDistance(pix_diag / 5.0)      
        # volProperty.SetScalarOpacityUnitDistance(pix_diag)   
          
      
        vol = vtk.vtkVolume()  
        vol.SetMapper(volMapper)  
        vol.SetProperty(volProperty)  
          
        return [vol]  
      
      
    def vtk_basic( actors ):  
        """ 
        Create a window, renderer, interactor, add the actors and start the thing 
         
        Parameters 
        ---------- 
        actors :  list of vtkActors 
         
        Returns 
        ------- 
        nothing 
        """       
          
        # create a rendering window and renderer  
        ren = vtk.vtkRenderer()  
        renWin = vtk.vtkRenderWindow()  
        renWin.AddRenderer(ren)  
        renWin.SetSize(600,600)  
        # ren.SetBackground( 1, 1, 1)  
       
        # create a renderwindowinteractor  
        iren = vtk.vtkRenderWindowInteractor()  
        iren.SetRenderWindow(renWin)  
      
        for a in actors:  
            # assign actor to the renderer  
            ren.AddActor(a )  
          
        # render  
        renWin.Render()  
         
        # enable user interface interactor  
        iren.Initialize()  
        iren.Start()  
      
              
      
    #####  
      
    filename = 'toto.nii.gz'  
      
      
    img = sitk.ReadImage( filename ) # SimpleITK object  
    data = sitk.GetArrayFromImage( img ) # numpy array  
      
    from scipy.stats.mstats import mquantiles  
    q = mquantiles(data.flatten(),[0.7,0.98])  
    q[0]=max(q[0],1)  
    q[1] = max(q[1],1)  
    tf=[[0,0,0,0,0],[q[0],0,0,0,0],[q[1],1,1,1,0.5],[data.max(),1,1,1,1]]  
      
    actor_list = volumeRender(data, tf=tf, spacing=img.GetSpacing())  
      
    vtk_basic(actor_list)  

下面一个不错的软件：

https://github.com/bastula/dicompyler
还有一个python的库mudicom，https://github.com/neurosnap/mudicom

[python] view plain copy

    import mudicom  
    mu = mudicom.load("mudicom/tests/dicoms/ex1.dcm")  
      
    # returns array of data elements as dicts  
    mu.read()  
      
    # returns dict of errors and warnings for DICOM  
    mu.validate()  
      
    # basic anonymization  
    mu.anonymize()  
    # save anonymization  
    mu.save_as("dicom.dcm")  
      
    # creates image object  
    img = mu.image # before v0.1.0 this was mu.image()  
    # returns numpy array  
    img.numpy # before v0.1.0 this was mu.numpy()  
      
    # using Pillow, saves DICOM image  
    img.save_as_pil("ex1.jpg")  
    # using matplotlib, saves DICOM image  
    img.save_as_plt("ex1_2.jpg")  
