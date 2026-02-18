annual_salary=int(input("enter annual salary"))
percentage=float(input("enter per u want to save"))
Total_price=int(input("enter total cost of dream house"))
down_payment=Total_price/4
semi_annual=float(input("enter  semi_annual value"))
months=0
annual_return=0.04
money=0
semirise=0
while down_payment>money :
    sal_month=annual_salary/12
    #here divided by 12 because they given in years we convert to months
    money+=money*(annual_return/12)
    money+=sal_month*percentage
    months+=1
    if months%6==0 :
        # it was important that semirise is applicable to every six months it increase sal not the sal at months 
        annual_salary+=semi_annual*annual_salary
print(f"count{months}")