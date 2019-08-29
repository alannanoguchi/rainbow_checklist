# Create our Checklist
checklist = list()

# Define Functions: CRUD
# CREATE
def create(item):
    # create item code here
    checklist.append(item)

# READ
def read(index):
    # Read code here
    return checklist[index]

# UPDATE
def update(index, item):
    # Update code here
    checklist[index] = item

# DESTROY
def destroy(index):
    # Destroy code here
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

#Test
def test():
    # List of Colored Clothing Items
    create("purple sock")
    create("black sock")
    create("yellow shoe")
    create("red shoe")
    create("blue beanie")
    create("green pants")
    create("orange shirt")


    mark_completed(2)

    list_all_items()

test()
