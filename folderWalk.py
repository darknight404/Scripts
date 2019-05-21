import os

for folderName, subfolders, filenames in os.walk('/home/gerald/Desktop/delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF '+ folderName + ': ' + subfolder)

    for filename in filenames:
       print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
    
