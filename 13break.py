for i in range(1,21):
    if i == 56:
        print("break statement is executed")
        break                                                  # break agar run kiya to else nai karega, aur agar else kiya to break nai run karega 
    print(i)

else:
    print("Break statement is not executed")