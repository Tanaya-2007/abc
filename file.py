fileptr = open("sample.txt","w")


while 1 :
    word = input("Enter data")
    if word == "exit":
        break
    else:
     fileptr.writelines(word + " ")

fileptr.close()    





