import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        # Variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        # Title
        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE', font=('times new roman', 35, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, width=1530, height=70)

        # NCR Logo
        img_logo = Image.open('ncr_logo.jpg')
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=80, y=5, width=60, height=60)

        # Image Frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=70, width=1530, height=130)

        img1 = Image.open('1.jpg')
        self.photo1 = ImageTk.PhotoImage(img1)
        self.img1 = Label(img_frame, image=self.photo1)
        self.img1.place(x=0, y=0, width=540, height=160)

        img2 = Image.open('2.jpg')
        self.photo2 = ImageTk.PhotoImage(img2)
        self.img2 = Label(img_frame, image=self.photo2)
        self.img2.place(x=540, y=0, width=540, height=160)

        img3 = Image.open('3.jpg')
        self.photo3 = ImageTk.PhotoImage(img3)
        self.img3 = Label(img_frame, image=self.photo3)
        self.img3.place(x=1080, y=0, width=540, height=160)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=200, width=1500, height=560)

        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # Labels and Entries
        self.create_label_entry(upper_frame, "Case ID:", self.var_case_id, 0, 0)
        self.create_label_entry(upper_frame, "Criminal NO:", self.var_criminal_no, 0, 2)
        self.create_label_entry(upper_frame, "Criminal Name:", self.var_name, 1, 0)
        self.create_label_entry(upper_frame, "NickName:", self.var_nickname, 1, 2)
        self.create_label_entry(upper_frame, "Arrest Date:", self.var_arrest_date, 2, 0)
        self.create_label_entry(upper_frame, "Date Of Crime:", self.var_date_of_crime, 2, 2)
        self.create_label_entry(upper_frame, "Address:", self.var_address, 3, 0)
        self.create_label_entry(upper_frame, "Age:", self.var_age, 3, 2)
        self.create_label_entry(upper_frame, "Occupation:", self.var_occupation, 4, 0)
        self.create_label_entry(upper_frame, "BirthMark:", self.var_birthMark, 4, 2)
        self.create_label_entry(upper_frame, "Crime Type:", self.var_crime_type, 0, 4)
        self.create_label_entry(upper_frame, "Father Name:", self.var_father_name, 1, 4)

        # Gender
        lbl_gender = Label(upper_frame, font=('arial', 12, 'bold'), text="Gender:", bg='white')
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=730, y=90, width=190, height=30)
        self.create_radiobutton(radio_frame_gender, 'Male', 'male', self.var_gender, 0, 0)
        self.create_radiobutton(radio_frame_gender, 'Female', 'female', self.var_gender, 0, 1)
        self.var_gender.set('male')

        # Wanted
        lbl_wanted = Label(upper_frame, font=('arial', 12, 'bold'), text="Most Wanted:", bg='white')
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)
        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=730, y=130, width=190, height=30)
        self.create_radiobutton(radio_frame_wanted, 'Yes', 'yes', self.var_wanted, 0, 0)
        self.create_radiobutton(radio_frame_wanted, 'No', 'no', self.var_wanted, 0, 1)
        self.var_wanted.set('yes')

        # Buttons
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        self.create_button(button_frame, 'Save', self.add_data, 0, 0)
        self.create_button(button_frame, 'Update', self.update_data, 0, 1)
        self.create_button(button_frame, 'Delete', self.delete_data, 0, 2)
        self.create_button(button_frame, 'Clear', self.clear_data, 0, 3)

        # Background right side image
        img_crime = Image.open('background.jpg')
        self.photocrime = ImageTk.PhotoImage(img_crime)
        self.img_crime = Label(upper_frame, image=self.photocrime)
        self.img_crime.place(x=1000, y=0, width=470, height=245)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information Table', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        down_frame.place(x=10, y=280, width=1480, height=270)

        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, font=("arial", 11, "bold"), text="Search By:", bg="red", fg="white")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=("arial", 11, "bold"), width=18, state='readonly')
        combo_search_box['value'] = ('Select Option', 'Case_id', 'Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame, textvariable=self.var_search, width=18, font=("arial", 11, "bold"))
        search_txt.grid(row=0, column=2, sticky=W, padx=5)

        # Search and Show All Buttons
        self.create_button(search_frame, 'Search', self.search_data, 0, 3)
        self.create_button(search_frame, 'Show All', self.fetch_data, 0, 4)

        crimeagency = Label(search_frame, font=("arial", 30, "bold"), text="NATIONAL CRIME AGENCY", bg='white', fg='crimson')
        crimeagency.grid(row=0, column=5, sticky=W, padx=50, pady=0)

        # Table Frame
        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        # Scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1", text="CaseID")
        self.criminal_table.heading("2", text="Criminal No")
        self.criminal_table.heading("3", text="Criminal Name")
        self.criminal_table.heading("4", text="NickName")
        self.criminal_table.heading("5", text="Arrest Date")
        self.criminal_table.heading("6", text="Date of Crime")
        self.criminal_table.heading("7", text="Address")
        self.criminal_table.heading("8", text="Age")
        self.criminal_table.heading("9", text="Occupation")
        self.criminal_table.heading("10", text="BirthMark")
        self.criminal_table.heading("11", text="Crime Type")
        self.criminal_table.heading("12", text="Father Name")
        self.criminal_table.heading("13", text="Gender")
        self.criminal_table.heading("14", text="Wanted")

        self.criminal_table["show"] = "headings"

        self.criminal_table.column("1", width=100)
        self.criminal_table.column("2", width=100)
        self.criminal_table.column("3", width=100)
        self.criminal_table.column("4", width=100)
        self.criminal_table.column("5", width=100)
        self.criminal_table.column("6", width=100)
        self.criminal_table.column("7", width=100)
        self.criminal_table.column("8", width=100)
        self.criminal_table.column("9", width=100)
        self.criminal_table.column("10", width=100)
        self.criminal_table.column("11", width=100)
        self.criminal_table.column("12", width=100)
        self.criminal_table.column("13", width=100)
        self.criminal_table.column("14", width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)
        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def create_label_entry(self, parent, text, var, row, col):
        label = Label(parent, text=text, font=('arial', 12, 'bold'), bg='white')
        label.grid(row=row, column=col, sticky=W, padx=2, pady=7)
        entry = ttk.Entry(parent, textvariable=var, width=22, font=('arial', 12, 'bold'))
        entry.grid(row=row, column=col + 1, sticky=W, padx=2, pady=7)

    def create_radiobutton(self, parent, text, value, variable, row, col):
        radio_button = Radiobutton(parent, variable=variable, text=text, value=value, font=('arial', 9, 'bold'), bg='white')
        radio_button.grid(row=row, column=col, padx=2, pady=7, sticky=W)

    def create_button(self, parent, text, command, row, col):
        button = Button(parent, text=text, command=command, font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        button.grid(row=row, column=col, padx=3, pady=5)

    def add_data(self):
        if self.var_case_id.get() == '' or self.var_criminal_no.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Ankur0408', database='temp1')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO criminal VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                               (self.var_case_id.get(),
                                self.var_criminal_no.get(),
                                self.var_name.get(),
                                self.var_nickname.get(),
                                self.var_arrest_date.get(),
                                self.var_date_of_crime.get(),
                                self.var_address.get(),
                                self.var_age.get(),
                                self.var_occupation.get(),
                                self.var_birthMark.get(),
                                self.var_crime_type.get(),
                                self.var_father_name.get(),
                                self.var_gender.get(),
                                self.var_wanted.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}')

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Ankur0408', database='temp1')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM criminal')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in rows:
                self.criminal_table.insert('', END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']
        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    def update_data(self):
        if self.var_case_id.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure you want to update this criminal record?')
                if update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='', database='management')
                    cursor = conn.cursor()
                    cursor.execute('UPDATE criminal SET Criminal_no=%s, Criminal_name=%s, Nickname=%s, Arrest_date=%s, DateOfCrime=%s, Address=%s, Age=%s, Occupation=%s, BirthMark=%s, CrimeType=%s, FatherName=%s, Gender=%s, Wanted=%s WHERE Case_id=%s', (
                        self.var_criminal_no.get(),
                        self.var_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest_date.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthMark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_wanted.get(),
                        self.var_case_id.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record successfully updated')
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}')

    def delete_data(self):
        if self.var_case_id.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you sure you want to delete this criminal record?')
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Ankur0408', database='temp1')
                    cursor = conn.cursor()
                    sql = 'DELETE FROM criminal WHERE Case_id=%s'
                    value = (self.var_case_id.get(),)
                    cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record successfully deleted')
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}')

    def clear_data(self):
        self.var_case_id.set('')
        self.var_criminal_no.set('')
        self.var_name.set('')
        self.var_nickname.set('')
        self.var_arrest_date.set('')
        self.var_date_of_crime.set('')
        self.var_address.set('')
        self.var_age.set('')
        self.var_occupation.set('')
        self.var_birthMark.set('')
        self.var_crime_type.set('')
        self.var_father_name.set('')
        self.var_gender.set('')
        self.var_wanted.set('')

    def search_data(self):
        if self.var_com_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error', 'Please select an option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Ankur0408', database='temp1')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM criminal WHERE ' + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('', END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}')


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()

