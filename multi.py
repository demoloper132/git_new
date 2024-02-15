start = int(input("enter start no :"))
end = int(input("enter end no :"))
for x in range(start,end+1):
    for y in range(1,11):
        result = x*y
        print (f" {x} X {y} = {result}")
    print ("--------")
        
