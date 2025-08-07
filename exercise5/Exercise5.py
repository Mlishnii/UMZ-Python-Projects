import sqlite3


con = sqlite3.connect('mydatabase.db')
cur = con.cursor()

while True:
    choice = int(input("""
    Which action Do you want to DO?
    1: Add new expense
    2: view 
    3: Update
    4: Delete
    5: Exit
    """))

    if choice == 1:
        date = input("Enter the Date: ")
        category = input("Enter the category: ")
        price = input("Enter the Cost: ")
        description = input("Enter the description: ")

        # cur.execute("""CREATE TABLE Expenses(
        # id INTEGER PRIMARY KEY AUTOINCREMENT,
        # date TEXT, category TEXT, price REAL, description TEXT)
        # """)
        cur.execute("""INSERT INTO Expenses(
                    date, category, price, description)
                    VALUES (?,?,?,?)
        """, (date, category, price, description))
        con.commit()
#----------------------------------------------------
    elif choice == 2:
        cur.execute("SELECT * FROM Expenses")
        rows = cur.fetchall()
        for i in rows :
            print(i)
        con.commit()
#----------------------------------------------------
    elif choice == 3 :
        idd = input("Enter the id: ")
        date = input("Enter the Date: ")
        category = input("Enter the category: ")
        price = input("Enter the price: ")
        description = input("Enter the description: ")

        cur.execute("""UPDATE Expenses SET 
                    date = ?, category = ?, price = ?, description = ?
                    WHERE id = ?""",(date, category, price, description,idd))
        con.commit()
#----------------------------------------------------
    elif choice == 4 :
        idd = input("Enter the id: ")
        cur.execute("DELETE FROM Expenses WHERE id = ?",(idd))
        con.commit()
#----------------------------------------------------
    elif choice == 5 :
        break
#----------------------------------------------------
    else:
        print("Bro, just enter a number from 1 to 5.")

con.commit()
con.close()