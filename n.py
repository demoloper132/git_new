start = int(input("enter start number :"))
end = int(input("enter end number :"))
for x in range(start,end+1):
    for y in range(start,end+1):
        result = x* y
        print (f" {x}X{y} ={result}")
    print("------------")
    print ("........")
