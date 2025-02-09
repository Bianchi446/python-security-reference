try:
    myfile = open('zfile.txt', 'wt')
    for i in range(10):
        myfile.write("Line #" + str(i+13) + "\n")
    myfile.close()
except IOError as error:
    print("I/O error occurred: ", str(error.errno))