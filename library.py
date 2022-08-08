import pymongo


class Library:
    def __init__(self):
        self.server = pymongo.MongoClient('mongodb+srv://Hariram:1khwWsQK8Zw9FwrX@cluster0.lnmsi0i.mongodb.net/test')
        self.Database = self.server['LibraryManagement']
        self.Collection = self.Database['Data']
        self.Collection_Users = self.Database['LendedUsers']

    def viewbooks(self):
        count=1
        for i in self.Database.get_collection('Data').find({}):
            print("---------------------------------------")
            print(f'S:No: {count}')
            for k,v in i.items():
                print(f"{k}:  {v}")
            count=count+1
        print("---------------------------------------")
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
            print(f"Exception Created {e}")

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


l=Library()
while True:
    print("1.Add Book\n2.View Book\n3.Remove Book\n4.Lend Book\n5.Return Book\n6.Exit")
    ch=int(input("Enter the Choice for the Selection:"))
    if ch==1:
        l.addbook()
    elif ch==2:
        l.viewbooks()
    elif ch==3:
        'l.deletebook()'
    elif ch==4:
        l.lendbook()
    elif ch==5:
        l.returnbook()
    elif ch==6:
        exit()