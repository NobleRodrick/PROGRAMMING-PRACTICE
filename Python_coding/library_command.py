def main():
    try:
        #initiate books list
        bookList = []
        infile = open("theBookList.txt", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("the <bookList.txt> file is not found")
        print("Starting a new books list....")
        bookList = []

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the Author >>> ")
            nPages = input("Enter the number of pages >>> ")
            bookList.append([nBook, nAuthor, nPages])
        
        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter Search Term: ")
            for book in bookList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(bookList)):
                print(bookList[i])
                      
        elif choice == 4:
            print("Quitting Program ....")
    print("Program terminated") 

    #Saving to external txt file
    outfile = open("theBookList.txt", "w")
    for book in bookList:
        outfile.write(",".join(book) + "\n")
    outfile.close()
        



if __name__ == "__main__":
    main()