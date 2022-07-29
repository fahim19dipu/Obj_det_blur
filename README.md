# Obj_det_blur
Detect all available objects from a image and blur the whole image except one selected object
## Description
This project uses TKinter based GUI that imports an image from local disk. Then it detects all available object from the images. The list of detected objects that are shown in a dropdown menu. From the dropdown menu user can select any object. After selecting the object by clickinng the "Apply blur" button, user can save a copy of the image where everything except the selected object is blurred.  
Object detection is done using openimages_v4_ssd_mobilenet which is a SSD-based object detection model trained on Open Images V4 with ImageNet pre-trained MobileNet V2 as image feature extractor. This model is publicly available as a part of TensorFlow Object Detection API. The MobileNet V2 feature extractor was trained on ImageNet and fine-tuned with SSD head on Open Images V4 dataset, containing 600 classes.
Image is then blurred using Pillow ImageFilter. 

## Install
The project uses follwing libraries: tensorflow, tensorflow_hub, numpy, Pillow, matplotlib, six, time, tkinter, os, datetime, tempfile. Thay can be insalled manually or by using the [requirement file](requirements.txt). Then download the object detection module from [here](https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1) and extact the folder. Set the path of the extracted folder in **objts** method in this [module](Obj_det.py). 

## Running the project
Run the project by running the **UI.py** file. It will take some time to open the UI due to loadinf the model. After opening select the desired image for object detection by clicking **Import Image** buttton from the left panel. After that the loaded model will detect the objects from the image. After compeleting detection the image with drawn boxes highlighting all detected objects along with the names of the objects will aprear on the UI Under Preview section. 
A dropdown menu containg all the object names and a button named **Apply Blur** wil also aprear. Clicking **Apply Blur** button after selecting an object from the dropdown menu  will result in an image where everything except the selected object is blurred will be saved in in your local disk.
To create a new session at any time, click on the **Refesh** Button on the left panel.
