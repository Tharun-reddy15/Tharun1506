file=open("f1.txt","a")
file.write("\n New Line Added")

file.close()

file=open("f1.txt","w")
file.write("Hello Python\n")
file.write("This is my write example")
file.close()