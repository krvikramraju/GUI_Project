from tkinter import *
from tkinter import messagebox as mb
from RegistrationDB import DataBaseManagement as db
from tkinter import ttk
import tkinter as tk

#Global Variable to display rows only once
display_rows = False
# connecting to the database
my_db = db('Registration.db')


def view_db():
    try:
        global display_rows
        global my_db
        if not display_rows:
            query = "SELECT * FROM Customer"
            rows = my_db.show(query)
            for row in rows:
                tree.insert("", tk.END, values=row)
            display_rows = True
        else:
            mb.showwarning("Warning", "Rows already displayed")
    except Exception as e:
        mb.showerror("Exception Occurred", e.__str__())


def password_validation():
    pass1 = password_var1.get()
    pass2 = password_var2.get()
    if pass1 == pass2:
        if len(pass1) < 8:
            mb.showwarning("Validation Result", "Password must be at least 8 characters long.")
            return FALSE
        else:
            return TRUE
    elif pass1 != pass2:
        mb.showwarning("Validation Result", "Passwords do not match. Please re-enter")
        return FALSE


#clear values in the form
def clear_form():
    global display_rows
    global tree
    global btn

    txtbox_name.set("")
    txtbox_email.set("")
    txtbox_mobile.set("")
    Gender_Radiobtn_Value.set(3)
    Country_Value.set("Select Country")
    password_var1.set("")
    password_var2.set("")
    Language_Radiobtn_Value.set(3)

    display_rows = False
    #Clear the treeview list items
    for item in tree.get_children():
        tree.delete(item)
    btn.focus_set()


#Gender Value determination
def gendervalue():
    val = ""
    match Gender_Radiobtn_Value.get():
        case 1:
            val = "Male"
        case 2:
            val = "Female"
        case 3:
            val = "Others"
    return val


#Language Value determination
def LanguageValue():
    val = ""
    match Language_Radiobtn_Value.get():
        case 1:
            val = "English"
        case 2:
            val = "Hindi"
        case 3:
            val = "Telugu"
    return val


# inserting into the datawindow
def insert_db():
    global display_rows
    global my_db
    try:
        # Passwords validation
        if password_validation() == FALSE:
            return
        Customer_Name = txtbox_name.get()
        Email = txtbox_email.get()
        MobileNo = txtbox_mobile.get()
        Gender = gendervalue()
        Country = Country_Value.get()
        Password = password_var1.get()
        Language = LanguageValue()
        query_str = "INSERT INTO Customer(Name,Email,MobileNumber,Gender,Country,Password,Language) VALUES('" + Customer_Name + "','" + Email + "','" + MobileNo + "','" + Gender + "','" + Country + "','" + Password + "','" + Language + "')"
        #print(query_str)
        my_db.insert(query_str)
        mb.showinfo("Information", "You have successfully Registered")
        display_rows = False
        clear_form()
        view_db()
    except Exception as e:
        mb.showerror("Exception Occurred", e.__str__())


window = Tk()
window.title("Registration Form")
# setting attribute
#window.attributes('-fullscreen', True)
#getting screen width and height of display
#width = window.winfo_screenwidth()
#height = window.winfo_screenheight()
#setting tkinter window size
#window.geometry("%dx%d" % (width, height))
window.state('zoomed')

# Create a style
style = ttk.Style(window)
# Set the theme with the theme_use method
style.theme_use('clam')  # put the theme name here, that you want to use

txtbox_name = StringVar()
lb1 = Label(window, text="Enter Name", width=10, font=("arial", 12))
lb1.place(x=20, y=20)
en1 = Entry(window, textvariable=txtbox_name)
en1.place(x=200, y=20)

txtbox_email = StringVar()
lb3 = Label(window, text="Enter Email", width=10, font=("arial", 12))
lb3.place(x=19, y=60)
en3 = Entry(window, textvariable=txtbox_email)
en3.place(x=200, y=60)

txtbox_mobile = StringVar()
lb4 = Label(window, text="Mobile Number", width=13, font=("arial", 12))
lb4.place(x=19, y=100)
en4 = Entry(window, textvariable=txtbox_mobile)
en4.place(x=200, y=100)

lb5 = Label(window, text="Select Gender", width=15, font=("arial", 12))
lb5.place(x=5, y=140)

Gender_Radiobtn_Value = IntVar()
Radiobutton(window, text="Male", padx=5, variable=Gender_Radiobtn_Value, value=1).place(x=180, y=140)
Radiobutton(window, text="Female", padx=10, variable=Gender_Radiobtn_Value, value=2).place(x=240, y=140)
Radiobutton(window, text="others", padx=15, variable=Gender_Radiobtn_Value, value=3).place(x=310, y=140)
Gender_Radiobtn_Value.set(3)

list_of_cntry = ("United States", "India", "Nepal", "Srilanka")
Country_Value = StringVar()
drplist = OptionMenu(window, Country_Value, *list_of_cntry)
drplist.config(width=15)
#Country_Value.set("Select Country")
lb2 = Label(window, text="Select Country", width=13, font=("arial", 12))
lb2.place(x=14, y=180)
drplist.place(x=200, y=175)
Country_Value.set("India")

# Variable to store the entered password
password_var1 = StringVar()
lb6 = Label(window, text="Enter Password", width=13, font=("arial", 12))
lb6.place(x=19, y=220)
en6 = Entry(window, show='*', textvariable=password_var1)
en6.place(x=200, y=220)

# Variable to store the entered password
password_var2 = StringVar()
lb7 = Label(window, text="Re-Enter Password", width=15, font=("arial", 12))
lb7.place(x=21, y=260)
en7 = Entry(window, show='*', textvariable=password_var2)
en7.place(x=200, y=260)

#Using 'Label' widget to create Language label and using place() method, set its position.
lb8 = Label(window, text="Language", width=10, font=("arial", 12))
lb8.place(x=10, y=300)

Language_Radiobtn_Value = IntVar()
Radiobutton(window, text="English", padx=5, variable=Language_Radiobtn_Value, value=1).place(x=180, y=300)
Radiobutton(window, text="Hindi", padx=10, variable=Language_Radiobtn_Value, value=2).place(x=250, y=300)
Radiobutton(window, text="Telugu", padx=15, variable=Language_Radiobtn_Value, value=3).place(x=310, y=300)
Language_Radiobtn_Value.set(3)

Button(window, command=insert_db, text="Register", width=10, font=("arial", 12), bg="black", fg='white').place(x=100,
                                                                                                               y=350)
Button(window, command=clear_form, text="Clear Form", width=10, font=("arial", 12), bg="black", fg='white').place(x=300,
                                                                                                                  y=350)
#frmtreeborder = tk.LabelFrame(window,text='Recent')
#frmtreeborder.columnconfigure(0, weight=1)
#frmtreeborder.rowconfigure(0, weight=1)
tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=10,
                    selectmode='browse')

tree.column("#1", anchor=tk.CENTER, width=50, stretch=NO)
tree.heading("#1", text="ID")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Customer Name")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Email")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Mobile No")
tree.column("#5", anchor=tk.CENTER, width=50)
tree.heading("#5", text="Gender")
tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="Country")
tree.column("#7", anchor=tk.CENTER)
tree.heading("#7", text="Password")
tree.column("#8", anchor=tk.CENTER)
tree.heading("#8", text="Language")

# Constructing vertical scrollbar
# with treeview
vscrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vscrollbar.set)
#vscrollbar.pack(side='right', fill='y')
#vscrollbar.set(0.2,0.5)
#tree_scr_width = tree.winfo_screenwidth()
vscrollbar.place(x=1324, y=400, height=229)


tree.pack()
tree.place(x=20, y=400)
btn = Button(window, command=view_db, text="Display Data", width=10, font=("arial", 12), bg="black", fg='white')
btn.pack(pady=10)
btn.place(x=400, y=700)
btn1 = Button(window, command=exit, text="Exit", width=10, font=("arial", 12), bg="black", fg='white')
btn1.pack(pady=10)
btn1.place(x=600, y=700)

window.mainloop()
