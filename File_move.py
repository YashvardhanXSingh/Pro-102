from distutils import extension
import os
import shutil

from_dir='C:\Users\Sushe\OneDrive\Desktop\Whitehat'
to_dir= 'C:\Users\Sushe\OneDrive\Desktop\CODING'


list_of_files = os.listdir(from_dir)
#print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                          # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Document_Files"                     # Example path2 : D:/My Files/Document_Files      
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Example path3 : D:/My Files/Document_Files/ImageName1.jpg
        print("path1: " , path1)
        print("path3: ", path3)

    print(os.path.exists(path1))
    print(os.path.exists(path2))
    print(os.path.exists(path3))

    if os.path.exists(path2):
        print("moving"+file_name+"...")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("moving"+file_name+"...")
        shutil.move(path1,path3)