__author__ = "Akash Maniar"

# from os import path
import os

# sPath = "F:/Python"
#
# # print("The current directory is: %s" % path.abspath(strPath))
# # print("Absolute path is: %s" % path.abspath(strPath))
# # print("Dir name: %s" % path.dirname(strPath))
# # print("Base Name: %s" % path.basename(strPath))
# # print("Exist: %s" % path.exists(strPath))
# # print("isDir = %s" %path.isdir(strPath))
# # print("isFile %s" %path.isfile(strPath))
#
# #List of contents
# print(os.listdir(sPath))
#
# #Get everythings split by roots directory and files
# # for roots, dirs, files in os.walk(sPath):
# #     for file in files:
# #         print("File = %s" % file)
# #     for dir in dirs:
# #         print("Directory = %s" % dir)
#
# #Only roots
# roots = next(os.walk(sPath))[0]
# print("Roots = %s" % roots)
#
# #Only dirs
# roots = next(os.walk(sPath))[1]
# print("Dirs = %s" % roots)
#
# #Only files
# roots = next(os.walk(sPath))[2]
# print("Files = %s" % roots)
#
# def writeFile(sfile):
#     if os.path.exists(sfile):
#         print("File already exists")
#         return
#     f = open(sfile, "w")
#     try:
#         f.write("Hello world \r\nThis is a new line!!")
#         f.flush()
#     except Exception as e:
#         print(e)
#     finally:
#         if f is not None:
#             f.close()
#
# writeFile("F:/Python/demo.txt")
#
#
# def readfile(filePath):
#     print("_________Reading the whole file using read()")
#     if os.path.exists(filePath):
#        with open(filePath) as file:
#            print(file.read())
#     print("___________Reading multiple lines at once using readlines()_________________")
#     if os.path.exists(filePath):
#         with open(filePath) as file:
#            for f in file.readlines():
#                print(f.strip("\n"))
#     print("___________Reading individual line by iteration using readline()______________")
#     if os.path.exists(filePath):
#         with open(filePath) as f:
#             line = f.readline()
#             while line:
#                 print(line.strip("\n"))
#                 line = f.readline()
#
#
# readfile("F:/Python/demo.txt")

#Working with Binary files

lst = [12,34,200,255]

strfile = "F:/Python/hexa.txt"
buffer = bytes(lst)
print("__Buffer __", buffer)
with open(strfile, "bw") as f:
    f.write(buffer)

with open(strfile, "br") as f:
    print("Readed text is:- ", f.read(16))