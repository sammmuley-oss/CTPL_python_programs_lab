def create_newfile():
    print("creating new file")
    file_name=input("enter the file name: ")
    file_content=input("enter the file content: ")
    with open(file_name, 'w') as file:
        file.write(file_content)
    print("file created successfully")

def read_file():
    print("reading file")
    file_name=input("enter the file name: ")
    with open(file_name, 'r') as file:
        content=file.read()
    print("file content:")
    print(content)

def append_file():
    print("appending to file")
    file_name=input("enter the file name: ")
    additional_content=input("enter the content to append: ")
    with open(file_name, 'a') as file:
        file.write(additional_content)
    print("file written successfully")

while (True):
    print("MENU:")
    print("1. Create New File")
    print("2. Read File")
    print("3. Append to File")
    print("4. Exit")
    choice = input("enter your choice: ")
    if choice == '1':
        create_newfile()
    elif choice == '2':
        read_file()
    elif choice == '3':
        append_file()
    elif choice == '4':
        print("exiting program....")
        break
    else:
        print("invalid !")