import pymongo
from tkinter import *
from tkinter import  ttk


class Library(Tk):
    def __init__(self,):
        super().__init__()
        self.title("Library Management")
        self.geometry('1250x400')
        self.resizable(0, 0)
        self.mainFrame= LabelFrame(self)
        self.mainFrame.grid(row=0,column=1)


        self.label=Label(self.mainFrame,text='Welcome To Library').grid(row=0,column=3)

        self.label = Label(self.mainFrame, text="Book Name")
        self.label.grid(row=1, column=0,padx=10,pady=10)

        self.entry_book=Entry(self.mainFrame,width=15)
        self.entry_book.grid(row=1, column=1, padx=10, pady=10)

        self.label = Label(self.mainFrame, text='User').grid(row=1, column=2,padx=10,pady=10)
        self.entry_user=Entry(self.mainFrame,width=15)
        self.entry_user.grid(row=1,column=3,padx=10,pady=10)

        self.server = pymongo.MongoClient('mongodb+srv://Hariram:1khwWsQK8Zw9FwrX@cluster0.lnmsi0i.mongodb.net/test')
        self.Database = self.server['LibraryManagement']
        self.Collection = self.Database['Data']
        self.Collection_Users = self.Database['LendedUsers']

        self.button_add_book = Button(self.mainFrame, text='Add Book',command=lambda:self.addbook()).grid(row=1, column=4, padx=10, pady=10)
        self.button_View_book = Button(self.mainFrame,text='View Books',command=lambda:self.viewbooks()).grid(row=2, column=0, padx=10, pady=10)

        self.button_view_lend_books = Button(self.mainFrame, text='View Lended Books',command=lambda:self.View_books_lended()).grid(row=2, column=1, padx=10, pady=10)
        self.button_Lend_books = Button(self.mainFrame, text='Lend Books',command=lambda:self.lendbook()).grid(row=2, column=2, padx=10, pady=10)
        self.button_Return_books = Button(self.mainFrame, text='Return Books',command=lambda:self.returnbook()).grid(row=2, column=3, padx=10, pady=10)
        self.button_Delete_books = Button(self.mainFrame, text='Delete Books',command=lambda:self.deletebook()).grid(row=2, column=4, padx=10, pady=10)

        self.frame = ttk.LabelFrame(self)
        self.frame.grid(row=1,column=1,padx=10,pady=10)

        self.columns = ("S:NO", "Book Name", "Quantity")
        self.treeview = ttk.Treeview(self.frame, columns=self.columns, show='headings')
        self.treeview.grid(row=5, column=1, padx=10, pady=10)
        self.treeview.heading("S:NO", text="S:NO")
        self.treeview.heading("Book Name", text="Book Name")
        self.treeview.heading("Quantity", text="Quantity")
        self.treeview.columnconfigure(0, weight=1)

        self.columns = ("S:NO", "Book Name", "User")
        self.treeview_lend = ttk.Treeview(self.frame, columns=self.columns, show='headings')
        self.treeview_lend.grid(row=5, column=2, padx=10, pady=10)
        self.treeview_lend.heading("S:NO", text="S:NO")
        self.treeview_lend.heading("Book Name", text="Book Name")
        self.treeview_lend.heading("User", text="User")
        self.treeview_lend.columnconfigure(1, weight=1)

    def viewbooks(self):
        main_count=0
        count=1
        self.treeview.delete(*self.treeview.get_children())
        for i in self.Database.get_collection('Data').find({}):
            self.treeview.insert(parent='', index=main_count, iid=main_count, text='', values=(count,i['Book'],i['Volume']))
            count=count+1
            main_count=main_count+1


    def View_books_lended(self):
        count = 1
        main_count = 0
        self.treeview_lend.delete(*self.treeview_lend.get_children())
        for i in self.Database.get_collection('LendedUsers').find({}):

            self.treeview_lend.insert(parent='', index=main_count, iid=main_count, text='', values=(count,i['Book'],i['User']))

            count = count + 1
            main_count = main_count + 1

    def addbook(self):
        count=1
        book=self.entry_book.get().title()
        print(book)
        searchquery = self.Database.get_collection('Data').find({"Book":book})
        value =[x for x in searchquery]
        if len(value)==0:
            Docs = {"Book": book, "Volume": 1}
            self.Document = self.Collection.insert_one(Docs)
            self.entry_book.delete(0, END)
        else:
            count = value[0].get("Volume") + 1
            self.Database.get_collection('Data').find_one_and_update({"Book": book}, {"$set": {"Volume": count}})
            self.entry_book.delete(0, END)

        self.viewbooks()
        self.View_books_lended()


    def lendbook(self):
        book=self.entry_book.get().title()
        user = self.entry_user.get().title()
        searchquery = self.Database.get_collection('LendedUsers').find({"Book": book,"User":user})
        searchquery_book = self.Database.get_collection('Data').find({"Book": book})
        value=[x for x in searchquery]
        value_book = [x for x in searchquery_book]
        if bool(value_book)==True and value_book[0].get("Volume")>0 and bool(value)==True:
            print(f"{book} Book which you are Requesting is Already Lended By You.")
            self.entry_book.delete(0, END)
            self.entry_user.delete(0, END)

        elif bool(value_book)==True and value_book[0].get("Volume")==0 and bool(value)==True:
            print(f"{book} Book Which you are Requesting for Is Out Of Stock and also Lended By You.")
            self.entry_book.delete(0, END)
            self.entry_user.delete(0, END)

        elif bool(value_book) == True and value_book[0].get("Volume")==0:
            print(f"{book} Book which you are Requesting is Out of Stock. Please Check Back Again!")
            self.entry_book.delete(0, END)
            self.entry_user.delete(0, END)

        elif bool(value_book) == False :
            print(f"{book} Book which you are Requesting is Not Available in This Library!")
            self.entry_book.delete(0, END)
            self.entry_user.delete(0, END)

        elif bool(value_book)==True and value_book[0].get("Volume")>0 and value==[]:
            count = value_book[0].get("Volume") - 1
            self.Database.get_collection('Data').find_one_and_update({"Book": book}, {"$set": {"Volume": count}})
            self.Database.get_collection('LendedUsers').insert_one({"Book": book, "User": user})
            self.entry_book.delete(0, END)
            self.entry_user.delete(0, END)

        self.viewbooks()
        self.View_books_lended()


    def returnbook(self):
        try:
            book = self.entry_book.get().title()
            user = self.entry_user.get().title()
            searchquery = self.Database.get_collection('LendedUsers').find({"Book": book,"User":user})
            searchquery_book = self.Database.get_collection('Data').find({"Book": book})
            value=[x for x in searchquery]
            value_book = [x for x in searchquery_book]
            if bool(value) == False:
                print(f"{book} which you are Searching to return is Not Lended By Any User!")
                self.entry_book.delete(0, END)
                self.entry_user.delete(0, END)

            elif bool(value)== True and bool(value_book)== False:
                print(f'{book} which you are Trying to Return is removed from Library Permantly.Now Cannot Return.')

            else:
                count_1 = value_book[0].get("Volume") + 1
                self.Database.get_collection('Data').find_one_and_update({"Book": book},{"$set": {"Volume": count_1}})
                self.Database.get_collection('LendedUsers').delete_one({"Book": book, "User": user})
                self.entry_book.delete(0, END)
                self.entry_user.delete(0, END)
            self.viewbooks()
            self.View_books_lended()

        except Exception as e:
            print(f"Exception Created {e}")

    def deletebook(self):
        book = self.entry_book.get().title()
        delete_query=self.Database.get_collection('Data').find({"Book": book})
        value_del = [x for x in delete_query]
        if len(value_del)==0:
            print(f"{book} you are searching to delete is not Is Not in Database!")
            self.entry_book.delete(0, END)
        else:
            self.Database.get_collection('Data').delete_one({"Book": book})
            self.entry_book.delete(0, END)

    def deleteAllLendedBooks(self):
        self.Database.get_collection('LendedUsers').delete_many({})



if __name__ == "__main__":
    l=Library()
    l.viewbooks()
    l.View_books_lended()
    l.mainloop()



