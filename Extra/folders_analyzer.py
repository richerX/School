import os
import sys


sys.setrecursionlimit(10 ** 6)


def number_of_files(path):
    answer = 0
    all_files = os.listdir(path)
    folders, files = divide(path, all_files)
    answer += len(files)
    for folder in folders:
        answer += number_of_files(path + "/" + folder)
    return answer


def divide(path, all_files):
    files = []
    folders = []
    for file in all_files:
        if os.path.isdir(path + "/" + file):
            folders.append(file)
        else:
            files.append(file)
    return [folders, files]


PATH_TO_CHECK = "folder"
all_files = os.listdir(PATH_TO_CHECK)
folders = divide(PATH_TO_CHECK, all_files)[0]
for folder in folders:
    folder_path = PATH_TO_CHECK + "/" + folder
    indent = 15
    print(f"{folder.ljust(indent)} | {number_of_files(folder_path)}")
