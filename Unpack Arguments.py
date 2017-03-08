def health_calculator(age,apples,cigs):
    answer=(100-age)+(apples*3.5)-(cigs*2)
    print(answer)

data=[20,1,0]
health_calculator(data[0],data[1],data[2])
health_calculator(*data)     #unpacking by passing each element of a list all the time