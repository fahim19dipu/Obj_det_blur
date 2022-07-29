# Obj_det_blur
Detect all available objects from a image and blur the whole image except one selected object
## Description
This project uses TKinter based GUI that imports an image from local disk. Then it detects all available object from the images. The list of detected objects that are shown in a dropdown menu. From the dropdown menu user can select any object. After selecting the object by clickinng the "Apply blur" button, user can save a copy of the image where everything except the selected object is blurred.  
Object detection is done using openimages_v4_ssd_mobilenet which is a SSD-based object detection model trained on Open Images V4 with ImageNet pre-trained MobileNet V2 as image feature extractor. This model is publicly available as a part of TensorFlow Object Detection API. The MobileNet V2 feature extractor was trained on ImageNet and fine-tuned with SSD head on Open Images V4 dataset, containing 600 classes.
Image is then blurred using Pillow ImageFilter. 

## Install
The project uses follwing libraries: tensorflow, tensorflow_hub, numpy, Pillow, matplotlib, six, time, tkinter, os, datetime, tempfile. Thay can be insalled manually or by using the [requirement file](requirements.txt)

