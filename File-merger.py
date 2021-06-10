import tkinter as tk
from tkinter import filedialog
import PyPDF2 

root=tk.Tk()

# setting the windows size
root.geometry("420x300")

# declaring string variable
# for storing name and password
name1_var=tk.StringVar()
name2_var=tk.StringVar()
name3_var=tk.StringVar()

f1_var= tk.IntVar()
t1_var=tk.IntVar()
f2_var=tk.IntVar()
t2_var=tk.IntVar()

# defining a function that will
# get the name and password and
# print them on the screen

global file1, file2

def file_opener1():
    global file1
    input1 = filedialog.askopenfile(initialdir="/")
    name1_var.set(input1.name)
    file1=input1.name 

def file_opener2():
    global file2
    input2 = filedialog.askopenfile(initialdir="/")
    name2_var.set(input2.name)
    file2=input2.name


def submit():
    # Open the files that have to be merged one by on
    global file1, file2
    pdf1File = open(file1, 'rb')
    pdf2File = open(file2, 'rb')
    
    # Read the files that you have opened
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    
    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()
    
    # Loop through all the pagenumbers for the first document
    for pageNum in range(f1_var.get(),t1_var.get()):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
    # Loop through all the pagenumbers for the second document
    for pageNum in range(f2_var.get(),t2_var.get()):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
    # Now that you have copied all the pages in both the documents, write them into the a new document
    s = name3_var.get()+ ".pdf"
    pdfOutputFile = open(s, 'wb')
    pdfWriter.write(pdfOutputFile)
    
    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    name1_var.set("")
    name2_var.set("")
    name3_var.set("")
    f1_var.set("")
    t1_var.set("")
    f2_var.set("")
    t2_var.set("")

	
# creating a label for
# name using widget Label
name_label1 = tk.Label(root, text = 'First File Path', font=('calibre',15, 'bold'))
name_label2 = tk.Label(root, text = 'Second File Path', font=('calibre',15, 'bold'))
name_label3 = tk.Label(root, text = 'New File Name', font=('calibre',15, 'bold'))
form1 = tk.Label(root, text = 'From (Page No.)', font=('calibre',15, 'bold'))
to1 = tk.Label(root, text = 'To (Page No.)', font=('calibre',15, 'bold'))
form2 = tk.Label(root, text = 'From (Page No.)', font=('calibre',15, 'bold'))
to2 = tk.Label(root, text = 'To (Page No.)', font=('calibre',15, 'bold'))
# creating a entry for input
# name using widget Entry
name_entry1 = tk.Entry(root,textvariable = name1_var, font=('calibre',15,'normal'))
from1_entry = tk.Entry(root,textvariable = f1_var, font=('calibre',15,'normal'))
to1_entry = tk.Entry(root,textvariable = t1_var, font=('calibre',15,'normal'))
name_entry2 = tk.Entry(root,textvariable = name2_var, font=('calibre',15,'normal'))
from2_entry = tk.Entry(root,textvariable = f2_var, font=('calibre',15,'normal'))
to2_entry = tk.Entry(root,textvariable = t2_var, font=('calibre',15,'normal'))
name_entry3 = tk.Entry(root,textvariable = name3_var, font=('calibre',15,'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
first_file_btn=tk.Button(root,text = 'Browse', command = lambda:file_opener1())
Second_file_btn=tk.Button(root,text = 'Browse', command = lambda:file_opener2())

# placing the label and entry in
# the required position using grid
# method
name_label1.grid(row=0,column=0)
form1.grid(row=1,column=0)
to1.grid(row=2,column=0)
name_label2.grid(row=3,column=0)
form2.grid(row=4,column=0)
to2.grid(row=5,column=0)
name_label3.grid(row=6,column=0)
name_entry1.grid(row=0,column=1)
from1_entry.grid(row=1,column=1)
to1_entry.grid(row=2,column=1)
name_entry2.grid(row=3,column=1)
from2_entry.grid(row=4,column=1)
to2_entry.grid(row=5,column=1)
name_entry3.grid(row=6,column=1)

sub_btn.grid(row=7,column=1)
first_file_btn.grid(row=0,column=2)
Second_file_btn.grid(row=3,column=2)
# performing an infinite loop
# for the window to display
root.mainloop()
