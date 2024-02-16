basket=[]
price=[]
print("**** Welcome to iShop calculator ****")
items=int(input("\n How many items are there in your basket today? "))
print("\nLet's get to counting them ....")
for x in range(1,items+1):
    item_name=input(f"Please tell me the name of the item number {x} ")
    basket.append(item_name) 
    item_price= float(input(f"What is the price of {item_name} \n $ "))
    price.append(item_price)
basket_items =input("Would you like to see basket items?")
if basket_items =="yes":
        print(basket)
        cost=input("Would you like to see how much it'll cost?")
        if cost == "yes":
            print(sum(price))
        else:
            print("exit")
else:
    print("exit")
