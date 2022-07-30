# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 20:45:20 2022

@author: user
"""

#The image modifier functions
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image, ImageFilter
import Obj_det as det
import os 
import time
from datetime import datetime 
import numpy as np
from tkinter import messagebox
import tensorflow as tf
import threading

from tensorflow_estimator.python.estimator.canned.dnn import dnn_logit_fn_builder
import tensorflow_hub as hub


def load_hub():
    os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.6/bin")
    print(tf.__version__)
    # Check available GPU devices.
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print("The following GPU devices are available: %s" % tf.test.gpu_device_name())
    """
            Change based on the location of downloaded detector module
            faster_rcnn_openimages_v4_inception_resnet_v2_1
            openimages_v4_ssd_mobilenet_v2_1
    """
    global detector
    start_time = time.time()
    print("loading started")
    detector = hub.load(r"F:\Object detection\resources\openimages_v4_ssd_mobilenet_v2_1.tar\openimages_v4_ssd_mobilenet_v2_1").signatures['default']
    end_time = time.time()    

    print("Module loading time: ", end_time-start_time)
    
def save_img():
    file_name= os.path.join(os.getcwd(),'Output',  datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    
    try:
        im1 = blured.save(file_name+".jpg")

    except FileNotFoundError:
        newdir = os.path.join(os.getcwd(),'Output')
        os.mkdir(newdir)
        im1 = blured.save(file_name+".jpg")
    res="The image is saved at "+str(os.getcwd())+"\Output"
    messagebox.showinfo("Output", res)
    button22.destroy()
          
def detection_function():
    path=root.filename

    clss = clicked.get()
    index = class_list.index(clss)
    image= Image.open(path)
    im_width, im_height = image.size

    (ymin, xmin, ymax, xmax) = box_list[index]
    (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                    ymin * im_height, ymax * im_height)

    croped = image.crop((int(left), int(top), int(right), int(bottom)))
    global blured
    blured = image.filter(ImageFilter.GaussianBlur(radius=17))
    blured.paste(croped,((int(left), int(top), int(right), int(bottom))))
    #blured.show()   
        
    img = blured.resize((900, 650))
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img
    
    global button22
    button22 = tk.Button(root,text="Save Image",bg = '#537487',fg = '#FFFFFF',command=save_img,height =2 , width = 10)
    button22.config(font=("Helvetica", 13))
    button22.place(x=1300, y=450,anchor="center")
       
def create_window():
    window = tk.Toplevel(root) 
    
def refresh(self):
    root.destroy()
    window()
def refresh1():
    root.destroy()
    window()    
def client_exit():
        root.destroy()
        
def importImages2(event):
        
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("JEPG files","*.jpg"),("png files","*.png")))
        #print(root.filename)
        #image=Image.open(root.filename)
        try:
            image=Image.open(root.filename)
            global box_list, class_list, score_list
            image, box_list, class_list, score_list = det.objts(image,detector)
            print(class_list)
            # for i in range(len(box_list)):
            #     print("{} {} {}".format(class_list[i], score_list[i],box_list[i]))
            image = Image.fromarray(np.uint8(image)).convert("RGB")
            image=image.resize((900, 650))
            img = ImageTk.PhotoImage(image)
            ###############################################
            global panel
            panel = tk.Label(bottomframe, image = img)
            panel.image = img
            #panel.pack(side = "bottom", fill = "both", expand = "yes")
            panel.place(x=475, y=400, anchor="center")
            ###############################################
             
            #datatype of menu text
            global clicked 
            clicked = tk.StringVar(root)
            options = class_list
            # initial menu text
            clicked.set(options[0])
              
            # Create Dropdown menu
            drop = OptionMenu( root , clicked , *options)
            drop.config(bg = "#537487", fg ='#FFFFFF')
            drop.config(font=("Helvetica", 13))
            drop.place(x=1275, y=300, anchor="center")
                        
            #################################################
            button2 = tk.Button(root,text="Apply Blur",bg = '#537487',fg = '#FFFFFF',command=detection_function,height =2 , width = 10)
            button2.config(font=("Helvetica", 13))
            button2.place(x=1450, y=300,anchor="center")
            
            ######################################################
            label22 = tk.Label(bottomframe,text="Select Object ",bg='Pale Turquoise3')
            label22.config(font=("Helvetica", 16))
            #label2.grid(row = 0,column=10,padx=210,pady=10)
            label22.place(x=1030, y=250, anchor="center")
            ###############################################################

            

        except OSError:
            messagebox.showinfo("Error", "Not an image")
            refresh1()

# Function to check state of thread1 and to update progressbar #
def progress(thread):
    # starts thread #
    thread.start()
    width = root1.winfo_screenwidth()
    height = root1.winfo_screenheight()
    root1.geometry('+%d+%d' % (width*0.45, height*0.4))
    # defines indeterminate progress bar (used while thread is alive) #
    pb1 = ttk.Progressbar(root1, orient='horizontal', mode='indeterminate')

    # defines determinate progress bar (used when thread is dead) #
 
    label13 = tk.Label(root1,text="Loading Module",bg='Pale Turquoise2')
    label13.config(font=("Helvetica", 13))
    #label1.grid(row=0,column=0,padx=20,pady=20)
    
    # places and starts progress bar #
    pb1.pack(pady =20, padx =20)
    label13.pack( padx =20)

    pb1.start()

    # checks whether thread is alive #
    while thread.is_alive():
        root1.update()
        pass

    # once thread is no longer active, remove pb1 and place the '100%' progress bar #
    pb1.destroy()
    root1.destroy()
    #pb2.pack()

       
def window(): 
    global root
    root = tk.Tk()
    root.title("Object Blurring")
    #root.geometry("1920x1080+"% (width*0.5, height*0.5))
    root.geometry('%dx%d+%d+%d' % (1920, 1080, 0, 0))
    root.configure(background='gray40')
    ########---------------------Manu bar-------------------######################
    
    menu = Menu(root)
    root.config(menu=menu)

    ############################################################################################################
    global topframe
    topframe =tk.Frame(root, bg="#344955",highlightbackground="black", highlightcolor="black", highlightthickness=2, width=250, height=1080, bd= 0)
    topframe.pack(side=LEFT)
    global bottomframe
    bottomframe = tk.Frame(root,bg="#ADE8F4", highlightbackground="black", highlightcolor="black", highlightthickness=2, width=1700, height=1080, bd= 0)
    bottomframe.pack(side=RIGHT)
    
    label1 = tk.Label(root,text="Select an image(.jpg/.png)",bg='Pale Turquoise2')
    label1.config(font=("Helvetica", 13))
    #label1.grid(row=0,column=0,padx=20,pady=20)
    label1.place(x=120, y=30, anchor="center")
    
    button = Button(topframe, text="Import image", height =2, width = 12,bg="#0096C7")
    #img = PhotoImage(file="E:/ml/1-Project/import_test.png") # make sure to add "/" not "\"
    button.config(font=("Helvetica", 11))
    button.bind("<Button-1>",importImages2)
    button.place(x=100, y=90, anchor="center")
    
    button6= tk.Button(topframe,text="Refresh",bg="#0096C7",height =2 , width = 12)
    button6.bind("<Button-1>",refresh)
    button6.config(font=("Helvetica", 11,))
    button6.place(x=100, y=160,anchor="center") 

    label2 = tk.Label(bottomframe,text="Preview",bg='Pale Turquoise3')
    label2.config(font=("Helvetica", 17))
    #label2.grid(row = 0,column=10,padx=210,pady=10)
    label2.place(x=550, y=30, anchor="center")
    root.mainloop()
    
######################         Drive    
global root1
root1 = tk.Tk()
thread1 = threading.Thread(target=load_hub) 
work = progress(thread1)
window()
