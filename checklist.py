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
    # for list_items in checklist:
        update(index, "√ " + checklist[index])
    # print("{} {}".format("√", list_item))


#Test
def test():
    create("purple sox")
    create("red cloak")
    create("green pants")
    create("yellow shoe")
    create("red shoe")
    create("orange shirt")
    create("black sock")

    # print(read(0))
    # print(read(1))
    #
    # update(0, "purple socks")
    #
    # destroy(1)
    #
    # print(read(0))

    # list_all_items()

    mark_completed(2)

    list_all_items()

test()
