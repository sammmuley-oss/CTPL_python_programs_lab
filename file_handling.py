file=open("file_handling.txt","w")
file.write("This is a file handling example.")
file.close()

file=open("file_handling.txt","r")
print(file.read())
file.close()

file=open("file_handling.txt","a")
file.write("\nThis line is appended to the file.")
file.close()

file=open("file_handling.txt","r")
print(file.read())
file.close()