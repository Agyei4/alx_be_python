# function for managing shopping list
from logging import exception


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input("Enter the item name: "))
            
        elif choice == '2':
            # Prompt for and remove an item
            feedback = input("Enter the item name or index: ")
            try:
                shopping_list.remove(feedback)
            except ValueError:
                shopping_list.pop(int(feedback)-1)

            
        elif choice == '3':
            # Display the shopping list
            for i, item in enumerate(shopping_list):

                print(i+1, item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()