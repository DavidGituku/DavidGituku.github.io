User=input("Enter your Name>>  ").upper()
Age=int(input("Enter your age>>  "))
Guess_count=0
Guess_limit=3
if Age>=18:
    while Guess_count < Guess_limit :
        Guess_count=Guess_count+1
        Lucky_Number=int(input('Enter your lucky Number>>  '))
        if Lucky_Number<100:
            print("The number must exceed 100")
        elif Lucky_Number>4000:
            print("The number cannot exceed 4000")
        elif 100<Lucky_Number<4000 and Lucky_Number==1042:
            print("Cogratulation "+(User)+" You just won the lottery! ")
            break
    else:
        print("Sorry",(User),",Try again later ")
else:
    print("This lottery is not open to people under the age of 18 yrs")
    
        
    