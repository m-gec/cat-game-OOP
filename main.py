from cat_container import cat
import sys

#create a cat
cat_name = input("\nname your cat\n")
cat_color = input("\nenter your cat's color\n")
cat_one = cat(cat_name, cat_color)

#game loop
while True:
    response = input("\nchoose an option from the list:\n1. train\n2. feed\n3. put to sleep\n4. exit\n")
    if not response.isdigit():
        print("\ninvalid input, please retry\n")
        continue

    match response:
        case "1":
            print(f"{cat_one.name} was trained\n")
            cat_one.train()
        case "2":
            print(f"{cat_one.name} was fed\n")
            cat_one.feed()
        case "3":
            print(f"{cat_one.name} was put to sleep\n")
            cat_one.sleep()
        case "4":
            print(f"ended the program\n")
            sys.exit()
        case _:
            print("invalid input, please retry")
            continue
    
    print(f"{cat_one.name}'s stats:\n")
    cat_one.spill()
