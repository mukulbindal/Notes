cap, mil, dis = map(int, input().split(","))

travelled = 0
fuel = 0
if(cap*mil >= dis):
    while travelled < 1000:
        fuel+=1
        travelled += cap * mil 
    print("Yes", fuel)
else:
    print("No")