import emp_ops

while True:
    print("\n--- Employee Menu ---")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        emp_ops.add_record()
    elif ch == 2:
        emp_ops.search_record()
    elif ch == 3:
        emp_ops.delete_record()
    elif ch == 4:
        emp_ops.edit_record()
    elif ch == 5:
        emp_ops.display_all()
    elif ch == 6:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
