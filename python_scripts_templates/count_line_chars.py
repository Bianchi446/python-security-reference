try:
    countlines = countchars = 0
    file = open('zfile.txt', 'r')
    lines = file.readlines()
    for line in lines:
        countlines += 1
        for char in line:
            countchars += 1
    file.close()

    print("Characters in file: ", countchars)
    print("lines in file: ", countlines)
except IOError as error:
    print("I/O error ocurred: ", str(error))
    