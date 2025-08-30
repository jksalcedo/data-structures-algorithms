# Import array module
import array as arr

def main():
    my_list = arr.array('i')  # Initialize an integer array
    menu = {
        0: "Exit",
        1: "Insert At Start",
        2: "Insert At End",
        3: "Insert At Position",
        4: "Delete At Start",
        5: "Delete At End",
        6: "Delete At Position",
        7: "Delete Number",
        8: "Search Number",
        9: "Display Number At Position",
        10: "Display List"
    }

    while True:
        print("\n===== List Data Structure Menu =====")
        # Display the menu options
        print("Choose an option:")
        for key, value in menu.items():
            print(f"[{key}] {value}")
            
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                if input("Exit? (y/n): ").lower() == 'y':
                    print("Thank you!")
                    break
            elif choice == 1:  # Insert at start
                value = int(input("Enter the number to insert: "))
                my_list.insert(0, value)
                print(f"\n{value} inserted at the start.")
            elif choice == 2:  # Insert at end
                value = int(input("Enter the number to insert: "))
                my_list.insert(len(my_list), value)
                print(f"\n{value} inserted at the end.")
            elif choice == 3:  # Insert at position
                value = int(input("Enter the number to insert: "))
                position = int(input("Enter position: "))
                if 0 <= position <= len(my_list):
                    my_list.insert(position, value)
                    print(f"\n{value} inserted at position {position}.")
                else:
                    print("Invalid position.")
            elif choice == 4:  # Delete at start
                if my_list:
                    value = my_list[0]
                    my_list.remove(value)
                    print(f"\n{value} removed from the start.")
                else:
                    print("List is empty.")
            elif choice == 5:  # Delete at end
                if my_list:
                    value = my_list[-1]
                    my_list.remove(value)
                    print(f"\n{value} removed from the end.")
                else:
                    print("List is empty.")
            elif choice == 6:  # Delete at position
                position = int(input("Enter position: "))
                if 0 <= position < len(my_list):
                    value = my_list[position]
                    my_list.remove(value)
                    print(f"\n{value} removed from position {position}.")
                else:
                    print("Invalid position.")
            elif choice == 7:  # Delete number
                value = int(input("Enter the number to delete: "))
                if value in my_list:
                    my_list.remove(value)
                    print(f"\n{value} removed from the list.")
                else:
                    print(f"{value} not found in the list.")
            elif choice == 8:  # Search number
                value = int(input("Enter the number to search: "))
                if value in my_list:
                    position = my_list.index(value)
                    print(f"\n{value} found at position {position}.")
                else:
                    print(f"{value} not found in the list.")
            elif choice == 9:  # Display number at position
                position = int(input("Enter the position to display: "))
                if 0 <= position < len(my_list):
                    print(f"\nNumber at position {position}: {my_list[position]}")
                else:
                    print("Invalid position.")
            elif choice == 10:  # Display list
                print("\nCurrent List:", list(my_list))
            else:
                print("Invalid choice. Enter a number between 0 and 10.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    main()