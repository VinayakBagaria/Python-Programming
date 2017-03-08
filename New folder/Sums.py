mealCost=float(input())
tip_p=float(input())
tax_p=float(input())
tip=mealCost*tip_p/100;
tax=mealCost*tax_p/100;
ans=str(round(mealCost+tip+tax))
print('The total meal cost is '+ ans +' dollars')