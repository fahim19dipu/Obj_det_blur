#The image modifier functions


from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
import Obj_det as det
import os 
from datetime import datetime 
import numpy as np
from tkinter import messagebox

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
    blured = image.filter(ImageFilter.GaussianBlur(radius=17))
    blured.paste(croped,((int(left), int(top), int(right), int(bottom))))
    #blured.show()   

    file_name= os.path.join(os.getcwd(),'Output',  datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    
    
    im1 = blured.save(file_name+".jpg")
    res="The image is saved at "+str(os.getcwd())
    #from tkinter import messagebox
    messagebox.showinfo("Output", res)
    root.destroy()
    window()
    
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
            image, box_list, class_list, score_list = det.objts(image)
            print(class_list)
            # for i in range(len(box_list)):
            #     print("{} {} {}".format(class_list[i], score_list[i],box_list[i]))
            image = Image.fromarray(np.uint8(image)).convert("RGB")
            image=image.resize((900, 650))
            img = ImageTk.PhotoImage(image)
            ###############################################
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
            drop.config(font=("Helvetica", 11))
            drop.place(x=1250, y=300, anchor="center")
                        
            #################################################
            button2 = tk.Button(root,text="Apply Blur",bg = '#537487',fg = '#FFFFFF',command=detection_function,height =2 , width = 10)
            button2.config(font=("Helvetica", 11))
            button2.place(x=1400, y=300,anchor="center")

        except OSError:
            messagebox.showinfo("Error", "Not an image")
            refresh1()
        
    
        
def window():       
    global root
    root = tk.Tk()
    root.title("Detection")
    root.geometry("1920x1080")
    root.configure(background='gray40')
    ########---------------------Manu bar-------------------######################
    
    menu = Menu(root)
    root.config(menu=menu)
    
    
    ######################################################

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
    #
    
    #button1 = tk.Button(topframe,text="Import")
    #button1.bind("<Button-1>",importImages)
    #button1.pack()
    
    button = Button(topframe, text="Import image", height =2, width = 12,bg="#0096C7")
    #img = PhotoImage(file="E:/ml/1-Project/import_test.png") # make sure to add "/" not "\"
    button.config(font=("Helvetica", 11))
    button.bind("<Button-1>",importImages2)
    #button.pack() # Displaying the button
    #button.grid(row=1 ,column=0)
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
window()