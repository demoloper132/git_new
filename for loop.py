attendees =["Alice" , "Bob" , "Charlie"]
for person in attendees:
    print (person)
    confirming = input("Is this person attending ? (yes/no): ")
    if confirming == "yes" :
        print("Attendance confirmed!")
    else:
        print("Attendance not confirmed")
    print("---------") 
