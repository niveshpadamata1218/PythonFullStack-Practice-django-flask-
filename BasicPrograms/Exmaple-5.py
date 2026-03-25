while True:
    try:
        num1 = int(input("enter num1:"))
        num2 = int(input("enter num2:"))
        z=num1/num2
        break
    except Exception as e:
        print("not an integer")
        print(e)
    except ValueError:
        print("not an integer vaule error")
    finally:
        print("you succsesfully enter a integer")

