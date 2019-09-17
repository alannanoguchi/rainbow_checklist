# Creates a new empty list
checklist = list()

# Define Functions: CRUD
# CREATE
def create(item):
    # create item: adds items to the checklist
    checklist.append(item)

# READ
def read(index):
    # Read code here: retrieves a value from the checklist using its index
    return checklist[index]

# UPDATE
def update(index, item):
    # Update code here: Use the index of the item that needs to be updated followed by its change
    checklist[index] = item

# DESTROY
def destroy(index):
    # Destroy code: used to remove the last item in the list
    checklist.pop(index)

#List all items
def list_all_items():
    # loop over every item in the checklist and print the index and item
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    # loop over every item in the checklist to find item to mark as complete
        update(index, "√ " + checklist[index])
        list_all_items()

# Check the validity of the input of the index
def valid_index(index):
    if int(index) > len(checklist):
        print("Invalid input. Insert valid index: ")
        return True
    else:
        return False

def select(function_code):

    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
        list_all_items()

    # Read item
    elif function_code == "R":
        invalid = True
        while invalid:
            item_index = user_input("Index Number? ")
            invalid = valid_index(input)
        print("Item: " + read(int(item_index)))
        list_all_items()

    # Update item
    elif function_code == "U":
        list_all_items()

        invalid = True
        while invalid:
            item_index = user_input("Update item? Select the item's index number: ")
            invalid = valid_index(item_index)


        item = user_input("Change item to: ")
        update(int(item_index), item)
        print("The item has been changed. List of items: " + '/n')

    # Destroy item
    elif function_code == "D":
        list_all_items()
        invalid = True
        while invalid:
            item_index = user_input("Delete item? Select the item's index number: ")
            list_all_items()
        
        # Remove the deleted item 
        destroy(int(item_index))
        print("Item has been deleted. List of items: " + '/n')
        list_all_items()

    elif function_code == "P":
        list_all_items()
        # Print all items here

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    else:
        #Catch all
        print("Unknown Option")
    return True


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for the user
    user_input = input(prompt)
    return user_input

#Test
def test():
    # List of Colored Clothing Items
    create("Purple sox")

    # print(read(0))
    # print(read(1))

    update(0, "Purple socks")

    # destroy(1)
    # print(read(0))

    create("Red cloak")
    create("Brown pants")
    list_all_items()

    mark_completed(2)

    user_value = user_input("Please Enter a value: ")
    print(user_value)
    list_all_items()

# Run all of the tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, U to update list, D to delete items, P to display list, and Q to quit: ")
    running = select(selection.upper()) 
    # .upper makes all user inputs read as upper case to the computer even if input is lowercase