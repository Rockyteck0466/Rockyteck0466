import pymongo


class Library:
    def __init__(self):
        self.server = pymongo.MongoClient('mongodb+srv://Hariram:1khwWsQK8Zw9FwrX@cluster0.lnmsi0i.mongodb.net/test')
        self.Database = self.server['LibraryManagement']
        self.Collection = self.Database['Data']
        self.Collection_Users = self.Database['LendedUsers']

    def viewbooks(self):
        count=1
        print("---------------------------------------------")
        for i in self.Database.get_collection('Data').find({}):
            print(f"{count}  {i['_id']}  {i['Book']}({i['Volume']})")
            count=count+1
        print("---------------------------------------------")

    def View_books_lended(self):
        count = 1
        print("---------------------------------------------")
        for i in self.Database.get_collection('LendedUsers').find({}):
            print(f"{count}  {i['_id']}  {i['Book']}({i['Volume']})")
            count = count + 1
        print("---------------------------------------------")

    def addbook(self):
        count=1
        book=input("Enter the Book name to add to Shelf:").title()
        searchquery = self.Database.get_collection('Data').find({"Book":book})
        value =[x for x in searchquery]
        if len(value)==0:
            Docs = {"Book": book, "Volume": 1}
            self.Document = self.Collection.insert_one(Docs)
        else:
            count = value[0].get("Volume") + 1
            self.Database.get_collection('Data').find_one_and_update({"Book": book}, {"$set": {"Volume": count}})


    def lendbook(self):
        try:
            book = input("Enter the Book Name for Lending:").title()
            searchquery = self.Database.get_collection('LendedUsers').find({"Book": book})
            searchquery_book = self.Database.get_collection('Data').find({"Book": book})
            value=[x for x in searchquery]
            value_book = [x for x in searchquery_book]
            if len(value) == 0:
                user = input("Enter the User Name Who is Lending the Book:").title()
                count = value_book[0].get("Volume") - 1
                self.Database.get_collection('Data').find_one_and_update({"Book": book},{"$set": {"Volume": count}})
                self.Database.get_collection('LendedUsers').insert_one({"Book":book,"User":user})
            else:
                user = input("Enter the User Name Who is Lending the Book:").title()
                searchquery_user = self.Database.get_collection('LendedUsers').find({"Book": book,"User":user})
                value_user = [x for x in searchquery_user]
                if len(value_user)==0:
                    count_1 = value_book[0].get("Volume") - 1
                    self.Database.get_collection('Data').find_one_and_update({"Book": book},{"$set": {"Volume":count_1}})
                    self.Database.get_collection('LendedUsers').insert_one({"Book":book,"User":user})
                else:
                    print(f'{book} Has been Lended By {user}')

        except Exception as e:
            print(f"{book} is not in the Library please Visit Again for book! Thank You")

    def returnbook(self):
        try:
            book = input("Enter the Book Name for Lending:").title()
            searchquery = self.Database.get_collection('LendedUsers').find({"Book": book})
            searchquery_book = self.Database.get_collection('Data').find({"Book": book})
            value=[x for x in searchquery]
            value_book = [x for x in searchquery_book]
            if len(value) == 0:
                print(f"{book} which you are Searching to return is Not Lended By Any User!")
            else:
                user = input("Enter the User Name Who is Lending the Book:").title()
                searchquery_user = self.Database.get_collection('LendedUsers').find({"Book": book,"User":user})
                value_user = [x for x in searchquery_user]
                if len(value_user)==0:
                    print(f"{book} has not been Lended By this requesting {user}")
                else:
                    count_1 = value_book[0].get("Volume") + 1
                    self.Database.get_collection('Data').find_one_and_update({"Book": book},{"$set": {"Volume": count_1}})
                    self.Database.get_collection('LendedUsers').delete_one({"Book": book, "User": user})

        except Exception as e:
            print(f"Exception Created {e}")

    def deletebook(self):
        book = input("Enter the Book Name for Deleting:").title()
        delete_query=self.Database.get_collection('Data').find({"Book": book})
        value_del = [x for x in delete_query]
        if len(value_del)==0:
            print(f"{book} you are searching to delete is not Is Not in Database!")
        else:
            self.Database.get_collection('Data').delete_one({"Book": book})

l=Library()
while True:
    print("1.Add Book\n2.View Books Shelf\n3.View Books Lended\n4.Delete Book\n5.Lend Book\n6.Return Book\n7.Exit")
    ch=int(input("Enter the Choice for the Selection:"))
    if ch==1:
        l.addbook()
    elif ch==2:
        l.viewbooks()
    elif ch==3:
        l.View_books_lended()
    elif ch==4:
        l.deletebook()
    elif ch==5:
        l.lendbook()
    elif ch==6:
        l.returnbook()
    elif ch==7:
        exit()
