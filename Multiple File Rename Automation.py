# This program is an example of automation which renames multiple files present in a folder.
# Eg. name0.png name1.png name2.png .......
# Remember to use forward slash in the path name.

import os

def main():
    ctr = 0
    pathIsCorrect = True
    while pathIsCorrect:
        path = input('Enter path of the folder which contains the files to be renamed:\
            \nEg. C:/Users/Saransh/Documents/\t:\t ')
        
        # Checks for path error
        if '\\' in path:
            print('\nERROR ! Use forward slash in path name (/)\n')
        elif not '\\' in path:
            pathIsCorrect = False
    
    base = input('\nEnter base file name:\t')
    extension = input('\nEnter file extension name (Eg: .png):\t')
    for filename in os.listdir(path):
        destination = path + base + str(ctr) + extension
        source = path + filename
        os.rename(source, destination)
        ctr += 1
    print('\nSUCCESS!')

if __name__ == '__main__':
    main()        
