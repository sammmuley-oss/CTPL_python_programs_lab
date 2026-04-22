''' Write a python program to copy the contents of source.txt into destination.txt.
    ensure the program handles the case where source.txt does not exist , displaying an appropriate message to the user using exception handling.'''

source_file = 'source.txt'
destination_file = 'destination.txt'

try :
    file=open(source_file,"r")
    content=file.read()
    file.close()

    file=open(destination_file,"w")
    file.write(content)
    file.close()
    print("file copied successfully")

except FileNotFoundError:
    print("Error occurred while writing to destination file.")

else:
    print("Program is about to exit.....")

finally:
    print("Program execution completed.")