print("This program is for calculating your income and expenses.")

def cal():
    try:
        income = float(input("Please Enter Your income: "))
        i = 0
        z = 0
    
        ie = int(input("Enter Number  of your expenses: "))
        l = []
        x = []
        while True:
                
                ya = input("Please Enter Your Expenses(Name): ")
                ye = float(input("Please Enter Your Expenses(Price): "))
                z += ye

                l.append(ya)
                x.append(ye)
                i += 1
                if i == ie:
                    p = list(zip(l,x))
                    res = income - z
                    return (
                    f"Your expenses = {p} \n"
                    f"Your remainder or savings = {res}"
        )
                    break
                else:
                         pass     

                
        
    
    except:
         print("somehnigs Wrong ,Please Try Again!")




print(cal())