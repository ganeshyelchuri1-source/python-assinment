annual_salary=float(input("enter the annual salary"))
house_cost=1000000
down_payment=house_cost/4
annual_return=0.04
semi_annual_return=0.07
salary=annual_salary
months=36
money=0
for i in range(1,months+1):
    monthly_salary=salary/12
    money+=money*(annual_return/12)
    money+=monthly_salary*1.0
    if i%6==0:
        salary+=salary*(semi_annual_return)
if money<down_payment :
    print("it is not possible to pay the down payment in three years")
else :
    low=0
    high=1
    steps=0
    best_rate=0
    while True:
        steps+=1
        rate=(low+high)/2
        money=0
        salary=annual_salary
        for i in range(1,months+1):
            monthly_salary=salary/12
            money+=money*(annual_return/12)
            money+=monthly_salary*rate
            if i%6==0 :
                salary+=salary*semi_annual_return
        
        if abs(money-down_payment)<=100:
            best_rate=rate
            break
        elif money <down_payment:
            low=rate
        else:
            high=rate
print(f"enter savings rate {round(best_rate,4)}")
print(f"steps in bisection search:{steps}")
