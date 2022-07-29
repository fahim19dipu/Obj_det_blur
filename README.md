# Obj_det_blur
Detect all available objects from a image and blur the whole image except one selected object
## Intro
I have created an UI using TKinter that imports an image from local disk. Then it detects all available object from the images. From the list of detected objects that are shown in a dropdown menu,from where user can select any object. After selecting the object by clickinng the "Apply blur" button user can save a copy of the image of the image where everything except the selected object is blurred.  
Object detection is done using openimages_v4_ssd_mobilenet which is a open sorce modue creted by google based on SSD and mobilenet that is trained with.....

## Requirements
tensorflow
tensorflow_hub
numpy
Pillow
matplotlib
six
time
tkinter
os
datetime
tempfile
