# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:47:45 2022

@author: user
"""
from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt
import tempfile
from six.moves.urllib.request import urlopen
from six import BytesIO
import tensorflow as tf

def load_img(path):
  img = tf.io.read_file(path)
  img = tf.image.decode_jpeg(img, channels=3)
  return img

def display_image(image):
  import os    
  os.environ['KMP_DUPLICATE_LIB_OK']='True'
  fig = plt.figure(figsize=(20, 15))
  plt.grid(False)
  plt.imshow(image)

def download_and_resize_image(url, new_width=256, new_height=256, display=False):
    
  _, filename = tempfile.mkstemp(suffix=".jpg")
  response = urlopen(url)
  image_data = response.read()
  image_data = BytesIO(image_data)
  pil_image = Image.open(image_data)
  pil_image = ImageOps.fit(pil_image, (new_width, new_height), Image.ANTIALIAS)

  pil_image_rgb = pil_image.convert("RGB")
  pil_image_rgb.save(filename, format="JPEG", quality=90)
  print("Image downloaded to %s." % filename)
  if display:
    display_image(pil_image)
  return filename

def load_and_resize_image(pil_image, new_width=256, new_height=256, display=False):
    
  _, filename = tempfile.mkstemp(suffix=".jpg")
  pil_image = ImageOps.fit(pil_image, (new_width, new_height), Image.ANTIALIAS)

  pil_image_rgb = pil_image.convert("RGB")
  pil_image_rgb.save(filename, format="JPEG", quality=90)
  print("Image downloaded to %s." % filename)
  if display:
    display_image(pil_image)
  return filename

