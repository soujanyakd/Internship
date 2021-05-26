import pickle


class Library:
    def oxford(self, o_book):
        print("List of books in Oxford Library")

    def science(self, s_book):
        print("List of books in Science Library")

    def lend(self, name, book, student_list, book_list):
        if name in student_list:
            if book in book_list:
                print(book, "is borrowed by ", name)
                book_list.remove(book)
            else:
                print("Book not available")
        else:
            print("No student found")

    def recieve(self, name, book, student_list, book_list):
        if name in student_list:
            print(book, "is returned by ", name)
            book_list.append(book)
        else:
            print("No student found")


class Student(Library):
    def oxford(self, so_list):
        with open('student_ox.txt', 'wb') as sopickle:
            pickle.dump(so_list, sopickle)
        with open('student_ox.txt', 'rb') as so_pickle:
            mystudent = pickle.load(so_pickle)
            for i in mystudent:
                print(i)

    def science(self, ss_list):
        with open('student_sc.txt', 'wb') as sspickle:
            pickle.dump(ss_list, sspickle)
        with open('student_sc.txt', 'rb') as ss_pickle:
            mystudent = pickle.load(ss_pickle)
            for i in mystudent:
                print(i)


class Book(Library):
    def oxford(self, o_book):
        super().oxford(o_book)
        with open('oxford_book.txt', 'wb') as obpickle:
            pickle.dump(o_book, obpickle)
        with open('oxford_book.txt', 'rb') as ob_pickle:
            mybook = pickle.load(ob_pickle)
        for i in mybook:
            print(i)

    def science(self, o_book):
        super().science(s_book)
        with open('science_book.txt', 'wb') as sbpickle:
            pickle.dump(o_book, sbpickle)
        with open('science_book.txt', 'rb') as sb_pickle:
            mybook = pickle.load(sb_pickle)
        for i in mybook:
            print(i)


o_book = ['Alfred Tennyson', 'My Last Duchess', 'Great Expectations']
s_book = ['A Man in the Moon', 'Atoms and Molecules', 'The Thermodynamics']
so_list = ['Rachel', 'Monica', 'Joey', 'Chandler', 'Phoebe', 'Ross']
ss_list = ['Jim', 'Pam', 'Dwight', 'Michel', 'Rayan', 'Angela']
while True:
    print("______Choose Library______")
    print("1.Oxford\n2.Science\n3.Exit")
    ch = int(input("Enter your choice"))
    if (ch == 1):
        print("______Oxford Library______")
        print("1.Display Books\n2.Lend Book\n3.Recieve Book\n4.Exit")
        ch1 = int(input("Enter your choice"))
        if (ch1 == 1):
            b1 = Book()
            b1.oxford(o_book)
        elif (ch1 == 2):
            l1 = Library()
            sn = input("Enter student name")
            bn = input("Enter Book name")
            l1.lend(sn, bn, so_list, o_book)
        elif (ch1 == 3):
            l1 = Library()
            sn = input("Enter student name")
            bn = input("Enter Book name")
            l1.recieve(sn, bn, so_list, o_book)
        elif (ch1 == 4):
            break
        else:
            print("Invalid choice")

    elif (ch == 2):
        print("______Science Library______")
        print("1.Display Books\n2.Lend Book\n3.Recieve Book\n4.Exit")
        ch1 = int(input("Enter your choice"))
        if (ch1 == 1):
            b1 = Book()
            b1.science(s_book)
        elif (ch1 == 2):
            l1 = Library()
            sn = input("Enter student name")
            bn = input("Enter Book name")
            l1.lend(sn, bn, ss_list, s_book)
        elif (ch1 == 3):
            l1 = Library()
            sn = input("Enter student name")
            bn = input("Enter Book name")
            l1.recieve(sn, bn, ss_list, s_book)
        elif (ch1 == 4):
            break
        else:
            print("Invalid choice")

    elif (ch == 3):
        break
    else:
        print("Invalid Choice")
