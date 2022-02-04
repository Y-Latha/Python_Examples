First_Num = int(input("Please enter a number between 1 and 100: "))
Second_Num = int(input("Please enter another number between 1 and 100: "))
print("\n 1> If you want to add the numbers type 1  \n 2> If you want the difference between the numbers type 2 \n 3> If you want product of the numbers type 3 \n 4> If you want to divide first with second number type 4 ")
User_Choice= int(input("\n Please enter the number according to the menu above : "))
if User_Choice == 1:
     print(First_Num + Second_Num )
elif  User_Choice == 2:
     if First_Num > Second_Num:
      print(First_Num - Second_Num )
     else:
      print(Second_Num - First_Num )   
elif User_Choice == 3:
     print(First_Num * Second_Num )
else :
     print(First_Num / Second_Num )