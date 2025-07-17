def t2():
    u_input= input("Enter text to enter into file:")
    with open("output.txt","w") as file:
        file.write(u_input +"\n")
    add_input= input("enter additional text to add to file:")
    with open("output.txt",'w') as file:
        file.write(add_input +"\n")
        print("Data successfully appended to file","\n","Thank you")
    print("\n Final contents of file Output.txt")
    with open("output.txt","r") as file:
        content = file.read()
        print(content)

t2()