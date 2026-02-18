annual_salary=int(input("enter annual salary"))
sal=annual_salary/12
saving=float(input("enter your per of  savings"))
cost=int(input("enter cost of dream house"))
down_payment=cost/4
money=0
m=0
annual_return=0.04
while money<down_payment :
    money+=money*(annual_return/12)
    money+=sal*saving
    m+=1
print(f"months{m}")