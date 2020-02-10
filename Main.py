import Return
import ListSplit
import dt
import Borrow

def start():
    while(True):
        print("        LIb. Management system ::::    ")
        print("------------------------------------------------------")
        print("Enter 1. Show Book List")
        print("Enter 2. Borrow a book")
        print("Enter 3. Return a book")
        print("Enter 4. Exit")
        try:
            bookselection=int(input("Select a choice from 1-4: "))
            print()
            if(bookselection==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(bookselection==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(bookselection==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(bookselection==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
#calling Function 
start()
