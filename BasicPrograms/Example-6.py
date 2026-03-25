try:
    klu1=open("nivesh.txt","a+")
    try:
        klu1.write("thi is fsasd class and your in klu 24.12.25")
    finally:
        klu1.close()
except IOError:
    print("file not exist")
else:
    print("file exist")
    klu1.close()