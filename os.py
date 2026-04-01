import os 
current_dir=os.getcwd()
print("Current Working Dictory:",current_dir)
files=os.listdir(current_dir)
print("/n Files and folders in directory:")
for f in files:
	print(f)

new_folder="MY FOLDER"
os.mkdir(new_folder)
print("/n New Directory created:",new_folder)
