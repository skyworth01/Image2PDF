from tkinter import *
from tkinter import filedialog
from fpdf import FPDF				#	External Module -- Need to install if not installed


root = Tk()
root.title('IMAGE2PDF')
root.geometry("600x500")
root['bg'] = '#4fbda3'



title = Label(root,text = "Select images:")			# title label
title.place(x = 15,y = 15)



#-------Function for selecting files and Corresponding Button----------------------#

def selectFile():
	filename  = filedialog.askopenfilenames()
	for files in filename:
		listbox.insert(1,files)


selectButton = Button(root, text = "Open",command = selectFile)
selectButton.place(x = 15,y = 50)

#----------------------------------------------------------------------------------#

selectedFile = Label(root,text = "Selected Files:")		# selected files label
selectedFile.place(x = 15,y = 110)




#--------------------------Listbox and its Functions------------------------------#

listbox = Listbox(root,bd = 3,height = 5,width = 60)
listbox.place(x = 15,y = 135)


def selectItems(event):
	selection = event.widget.curselection()
	index = selection[0]
	print(index)			# Sample printing just to know the index

	def changeOrderUp():
		if(index!=0):
			temporary_save = listbox.get(index)
			listbox.delete(index)
			listbox.insert(index-1,temporary_save)

	def changeOrderDown():
			if(index<listbox.size()):
				temporary_save = listbox.get(index)
				listbox.delete(index)
				listbox.insert(index+1,temporary_save)


	upButton = Button(root,text = 'Up',command = changeOrderUp)
	upButton.place(x=120,y=250)

	downButton = Button(root,text = 'Down',command = changeOrderDown)
	downButton.place(x=185,y=250)

listbox.bind('<<ListboxSelect>>',selectItems)



def removeFiles():
	selected_checkbox = listbox.curselection()
	listbox.delete(selected_checkbox)

removeButton = Button(root,text = 'Remove',command = removeFiles)
removeButton.place(x=15,y=250)

#---------------------------------------------------------------------------------#



#-----------------------Main Function - Convert Image to PDF ---------------------#

def fileConvert():
	tuple_lists = listbox.get(0,END)
	listItems = list(tuple_lists)			#Converting tuple to list
	if(listItems!=[]):
		pdf = FPDF()						#External Module used - FPDF
		for files in listItems:
			print(files)
			pdf.add_page()
			pdf.image(files)
		pdf.output(name = 'OutputPdf',dest='F')
	else:
		print("No Files Selected")

button = Button(root,text = "Convert",command  = fileConvert)
button.place(x = 15,y = 400)

#--------------------------------------------------------------------------------#

root.mainloop()