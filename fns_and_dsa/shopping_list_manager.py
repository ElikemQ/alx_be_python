shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def check_emptylist(shopping_list):
    """Checks if shopping list is empty"""
    if shopping_list == []:
        print("Shopping list is empty")
        return True
    return False
    

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        # Prompt for and add an item
        item = input("Enter item: ").lower().strip()
        shopping_list.append(item)
        print(item, "has been added to shopping list")
    elif choice == '2':
        # Prompt for and remove an item
        item = input("Enter item: ").lower().strip()
        if check_emptylist(shopping_list):
            pass
        else:
            if item in shopping_list:
                shopping_list.remove(item)
                print(item, "has been removed from shopping list")
            else:
                print(f"{item} does not exist in shopping list")

    elif choice == '3':
        # Display the shopping list
        if check_emptylist(shopping_list=shopping_list) == True:
            pass
        else:
            
            for each_item in shopping_list:
               print(each_item)
            

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

