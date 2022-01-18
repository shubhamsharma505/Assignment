


def max_profit(weight,profit,N):
    result=[]
    for i in range(len(weight)):
        res=(profit[i]/weight[i])*N
        result.append(int(res))
    output=max(result)
    index_value=result.index(output)
    print("Maximum profit is " + str(output))
    return index_value
    

N=int(input("Enter the maximum capacity of items_weight"))
n=int(input("Enter the No of items"))
items=[]
weight=[]
profit=[]
for i in range(n):
    items.append(input("Enter Item Name"))
    weight.append(int(input("Enter weight of item")))
    profit.append(int(input("Enter the profit")))

res=max_profit(weight,profit,N)
print("By selling "+ str(N) ,items[res])

