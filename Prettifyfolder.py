import os

path = "D:\\python"


def prettify(filepath, dictfile, fileext):
    os.chdir(filepath)
    i = 1
    list_of_files = os.listdir(filepath)
    list_of_untouchable = []

    f = open(dictfile, "r")
    for line in f:
        stripped_line = line.strip("\n")
        list_of_untouchable.append(stripped_line)
    f.close()

    for key in list_of_files:
        if key not in list_of_untouchable:
            os.rename(key, key.capitalize())

    for value in list_of_files:
        if os.path.splitext(value)[-1] == fileext:
            os.rename(value, f"{i}.{fileext}")
            i += 1


prettify(path, "D:\python\Imp.txt", ".jpg")
