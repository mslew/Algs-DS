#Author: Maximus Lewis

#This program will traverse directories. Printing the directory and file. Using os library. NOT utilizing walk function

import os 


def find(path, file):
    dir_list = os.listdir(path)
    print(dir_list)
    return


if __name__ == '__main__':
    filename = 'test.txt'
    path = r'C:\Users\epicx\Desktop\Test\Test 2b'
    find(path, filename)