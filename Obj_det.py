# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:47:16 2022

@author: Fahim
"""

#@title Imports and function definitions

# For running inference on the TF-Hub module.
import tensorflow as tf
from tensorflow_estimator.python.estimator.canned.dnn import dnn_logit_fn_builder
import tensorflow_hub as hub
import Image_import as ii
import Drawing_box as db
# For measuring the inference time.
import time
import numpy as np

# Print Tensorflow version
""" format the classes, boxes and score for returning"""
def get_res( boxes, class_names, scores, max_boxes=10, min_score=0.1):

  box_list = []
  class_list= []
  score_list = []
  for i in range(min(boxes.shape[0], max_boxes)):
    if scores[i] >= min_score:
      box_list.append(tuple(boxes[i]))
      class_list.append(class_names[i].decode("ascii"))
      score_list.append((int(100 * scores[i])))
  unique_classes = np.unique(np.array(class_list))
  #print(unique_classes)
  for i in range(len(unique_classes)):
      c=0    
      for j in range(len(class_list)):
          if class_list[j] == unique_classes[i]:
              c = c+1
              class_list[j] = class_list[j] + "-"+str(c)
    
  return box_list, class_list, score_list

""" running the detector"""
def run_detector(detector, path):
  img = ii.load_img(path)

  converted_img  = tf.image.convert_image_dtype(img, tf.float32)[tf.newaxis, ...]
    
  start_time = time.time()
  result = detector(converted_img)
  end_time = time.time()


  result = {key:value.numpy() for key,value in result.items()}
  class_names = []
  
  for i in range(len(result)):
    if result["detection_scores"][i]> .1:  
      class_names.append(result["detection_class_entities"][i].decode("ascii"))
  print(class_names)
  #print(result["detection_class_entities"])
    
  print("Found %d objects." % len(result["detection_scores"]))
  print("Inference time: ", end_time-start_time)
  
  
  box_list, class_list, score_list =get_res(result["detection_boxes"],
  result["detection_class_entities"], result["detection_scores"]) 
  
  image_with_boxes = db.draw_boxes(
      img.numpy(), result["detection_boxes"],
      class_list, result["detection_scores"])
  
  box_list, class_list, score_list =get_res(result["detection_boxes"],
  result["detection_class_entities"], result["detection_scores"])      
  
  return image_with_boxes, box_list, class_list, score_list

""" running detection """ 
def objts(image, detector):
    
    pil_image = image
    downloaded_image_path = ii.load_and_resize_image(pil_image, 1280, 856, False)
    
    image_with_boxes, box_list, class_list, score_list = run_detector(detector, downloaded_image_path)
    
    return image_with_boxes, box_list, class_list, score_list
  
