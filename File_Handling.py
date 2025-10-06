import os

if not os.path.exists("Student_Records"):
    os.makedirs("Student_Records")

for _ in range(10):
    print("\n1. Add student record:")
    print("2. Open student record:")
    print("3. Exit:")
    choice = input("Enter your choice: ")

    if choice == "1":
        Student_No = input("Student Number: ")
        Last_Name = input("Last Name: ")
        First_Name = input("First Name: ")
        Middle_Initial = input("Middle Initial: ")
        Program = input("Program: ")
        Age = input("Age: ")
        Gender = input("Gender: ")
        Birthday = input("Birthday: ")
        Contact_No = input("Contact Number: ")

        file_path = os.path.join("Student_Records", f"{Student_No}.txt")
        with open(file_path, "w") as file:
            file.write("Student Number: " + Student_No + "\n")
            file.write("Last Name: " + Last_Name + "\n")
            file.write("First Name: " + First_Name + "\n")
            file.write("Middle Initial: " + Middle_Initial + "\n")
            file.write("Program: " + Program + "\n")
            file.write("Age: " + Age + "\n")
            file.write("Gender: " + Gender + "\n")
            file.write("Birthday: " + Birthday + "\n")
            file.write("Contact Number: " + Contact_No + "\n")
        print("\nStudent record saved in: " + file_path)

    elif choice == "2":
        Student_No = input("Enter Student Number: ")
        file_path = os.path.join("Student_Records", f"{Student_No}.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                print("\nStudent Record:")
                print(content)
        else:
            print("No record found for Student Number: " + Student_No)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
