class Library:
    def __init__(self):
        self.bookslist=dict()
        self.lendedbook=dict()
    def viewbooks(self):
        count=1
        for i in self.bookslist:
            print(f'{count}.{i}---{self.bookslist[i]}')
            count=count+1
        print("---------------------------------------")
    def addbook(self):
        book=input("Enter the Book name to add to Shelf:").title()
        if book in self.bookslist:
            self.bookslist[book]=self.bookslist[book]+1
        else:
            self.bookslist[book]=1
    def lendbook(self,lenders,users):
        book=input("Enter the Book Name to Lend the Book:").title()
        print(self.bookslist[book])
        if book in self.bookslist:
            user = input("Enter the User Name Who is Lending the Book:").title()
            if user in self.lendedbook:
                print(f"Sorry {user} has already Lended {book} Book!")
            else:
                self.bookslist[book]=self.bookslist[book]-1
                self.lendedbook[book] =lenders[book[users.append(user)]]
        else:
            print(f"{book} Book Not in Shelf!")
    def returnbook(self):
        book=input("Enter the Book Name to Return:").title()
        print(self.lendedbook[book])
        user = input("Enter the UserName Used While Lending the Book:").title()
        if user in self.lendedbook[book]:
            self.addbook()
            self.lendedbook[book]=list.remove(user)
        else:
            print(f"Sorry {user} not Found In Lender List of {book} Book!")
    def deletebook(self):
        book=input("Enter the Book Name To delete from the DataBase:").title()
        print(f"{self.bookslist.pop(book)} Stocked Books Have Been Removed from The Library!")

l=Library()
lenders=dict()
users=[]
while True:
    print("1.Add Book\n2.View Book\n3.Remove Book\n4.Lend Book\n5.Return Book\n6.Exit")
    ch=int(input("Enter the Choice for the Selection:"))
    if ch==1:
        l.addbook()
    elif ch==2:
        l.viewbooks()
    elif ch==3:
        l.deletebook()
    elif ch==4:
        l.lendbook(lenders,users)
        print(lenders)
    elif ch==5:
        l.returnbook()
    elif ch==6:
        exit()