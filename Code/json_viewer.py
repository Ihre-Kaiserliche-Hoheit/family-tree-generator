from tkinter import *
import json
from os import listdir

top = Tk()
top.resizable(False, False)
top.geometry("450x350")
top.wm_title("Viewer")

file = "../Output/"
entries = None

#Searchbar
def searchbar_pressed():
    input = searchbar_entry.get()
    try:
        entries[input]
        getEntry(input)
        searchbar_entry["bg"] = "green2"
    except KeyError:
        searchbar_entry["bg"] = "red"
    except TypeError:
        searchbar_entry["bg"] = "red"

    print(input)

def update_searchbar():
    searchbar_entry["bg"] = "white smoke"
    top.after(5000, update_searchbar)

#Json selection and import
def select_file():
    outer_top = Toplevel()
    outer_top.resizable(False, True)
    outer_top.geometry("400x50")
    outer_top.wm_title("Choose File")
    files = listdir("../Output")
    site_box = Frame(outer_top)
    site_box.pack(side=RIGHT)
    global file_list
    file_list = Listbox(outer_top, height=(len(files)+1), selectmode=SINGLE, width=30)
    for i in range(len(files)):
        file_list.insert(0, files[i])
    file_list.pack(side=LEFT)
    selection_label = Label(site_box, text="Select a .json in /Output")
    selection_label.pack(side=TOP)
    confirm_file = Button(site_box, text="Confirm", command=import_file)
    confirm_file.pack()

def import_file():
    try:
        filename_input = str(file_list.get(ANCHOR))
        global entries
        with open(file+filename_input) as json_file:
            entries = json.load(json_file)
        entries = entries["Entries"]
        file_list["bg"]="green2"
    except IsADirectoryError:
        file_list["bg"]="red"
    except json.JSONDecodeError:
        file_list["bg"]="red"

def getEntry(_id:str):
    entry = entries[_id]
    ID_label2["text"] = entry["ID"]
    WholeName_label2["text"] = entry["Name"] + " ’" + entry["Patronym"] + "’ " + entry["Surname"]
    Sex_label2["text"] = entry["Sex"]
    Race_label2["text"] = entry["Race"]
    Culture_label2["text"] = entry["Culture"]
    Father_label2["text"] = entry["Father"]
    Mother_label2["text"] = entry["Mother"]
    Spouse_label2["text"] = entry["Spouse"]
    children = ""
    children_entry = entry["Children"]
    if children_entry != None:
        for i in range(len(children_entry)):
            child = children_entry[i]
            children += str(child)
            if i+1 < len(children_entry):
                children += "|"
    Children_label2["text"] = children
    BirthDate_label2["text"] = entry["Birth Date"]
    BirthPlace_label2["text"] = entry["Birth Place"]
    DeathDate_label2["text"] = entry["Death Date"]
    DeathPlace_label2["text"] = entry["Death Place"]
    Age_label2["text"] = entry["Age"]

#Menu
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Import File", command=select_file)
menubar.add_cascade(label="File", menu=filemenu)


#Searchbar
searchbar_frame = Frame(top)
searchbar_frame.pack(side=TOP)
searchbar_subframe2 = Frame(searchbar_frame)
searchbar_subframe2.pack()
searchbar_subframe1 = Frame(searchbar_frame)
searchbar_subframe1.pack()
searchbar_entry = Entry(searchbar_subframe1)
searchbar_entry.pack(side=LEFT)
searchbar_button = Button(searchbar_subframe1, text="Search", command=searchbar_pressed)
searchbar_button.pack(side=RIGHT)
searchbar_label = Label(searchbar_subframe2, text="Input Character ID")
searchbar_label.pack(side=BOTTOM)


#Person Entry
ID_frame = Frame(top)
ID_frame.pack()
ID_label = Label(ID_frame, text="ID")
ID_label.pack(side=LEFT)
ID_label2 = Label(ID_frame)
ID_label2.pack(side=LEFT)

WholeName_frame = Frame(top)
WholeName_frame.pack()
WholeName_label = Label(WholeName_frame, text="Name")
WholeName_label.pack(side=LEFT)
WholeName_label2 = Label(WholeName_frame)
WholeName_label2.pack(side=LEFT)

Sex_frame = Frame(top)
Sex_frame.pack()
Sex_label = Label(Sex_frame, text="Sex")
Sex_label.pack(side=LEFT)
Sex_label2 = Label(Sex_frame)
Sex_label2.pack(side=LEFT)

Race_frame = Frame(top)
Race_frame.pack()
Race_label = Label(Race_frame, text="Race")
Race_label.pack(side=LEFT)
Race_label2 = Label(Race_frame)
Race_label2.pack(side=LEFT)

Culture_frame = Frame(top)
Culture_frame.pack()
Culture_label = Label(Culture_frame, text="Culture")
Culture_label.pack(side=LEFT)
Culture_label2 = Label(Culture_frame)
Culture_label2.pack(side=LEFT)

Father_frame = Frame(top)
Father_frame.pack()
Father_label = Label(Father_frame, text="Father")
Father_label.pack(side=LEFT)
Father_label2 = Label(Father_frame)
Father_label2.pack(side=LEFT)

Mother_frame = Frame(top)
Mother_frame.pack()
Mother_label = Label(Mother_frame, text="Mother")
Mother_label.pack(side=LEFT)
Mother_label2 = Label(Mother_frame)
Mother_label2.pack(side=LEFT)

Spouse_frame = Frame(top)
Spouse_frame.pack()
Spouse_label = Label(Spouse_frame, text="Spouse")
Spouse_label.pack(side=LEFT)
Spouse_label2 = Label(Spouse_frame)
Spouse_label2.pack(side=LEFT)

Children_frame = Frame(top)
Children_frame.pack()
Children_label = Label(Children_frame, text="Children")
Children_label.pack(side=LEFT)
Children_label2 = Label(Children_frame)
Children_label2.pack(side=LEFT)

BirthDate_frame = Frame(top)
BirthDate_frame.pack()
BirthDate_label = Label(BirthDate_frame, text="Birth Date")
BirthDate_label.pack(side=LEFT)
BirthDate_label2 = Label(BirthDate_frame)
BirthDate_label2.pack(side=LEFT)

BirthPlace_frame = Frame(top)
BirthPlace_frame.pack()
BirthPlace_label = Label(BirthPlace_frame, text="Birth Place")
BirthPlace_label.pack(side=LEFT)
BirthPlace_label2 = Label(BirthPlace_frame)
BirthPlace_label2.pack(side=LEFT)

DeathDate_frame = Frame(top)
DeathDate_frame.pack()
DeathDate_label = Label(DeathDate_frame, text="Death Date")
DeathDate_label.pack(side=LEFT)
DeathDate_label2 = Label(DeathDate_frame)
DeathDate_label2.pack(side=LEFT)

DeathPlace_frame = Frame(top)
DeathPlace_frame.pack()
DeathPlace_label = Label(DeathPlace_frame, text="Death Place")
DeathPlace_label.pack(side=LEFT)
DeathPlace_label2 = Label(DeathPlace_frame)
DeathPlace_label2.pack(side=LEFT)

Age_frame = Frame(top)
Age_frame.pack()
Age_label = Label(Age_frame, text="Age")
Age_label.pack(side=LEFT)
Age_label2 = Label(Age_frame)
Age_label2.pack(side=LEFT)

top.config(menu=menubar)

update_searchbar()
top.mainloop()