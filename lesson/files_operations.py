#f = open("lesson.txt")
f = open("lesson2.txt",)

# read line by line
print(f.readline(
    """
    with open ("lesson2.txt",'w') as f:
    f.write("this is my new file \n")
    f.write("I am from Nai \n")
    f.write ("today is monday \n")

"""))

# reading the file
print(f.read())
f.close()


