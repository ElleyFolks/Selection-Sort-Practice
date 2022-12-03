# organizes by swapping numbers if they are lesser and moving them farther left with index position
def selection_sort(list_numbers):
    index = 0

    for index in range(len(list_numbers)-1):
        least_index = index
        print("current least index: ", least_index)

        # iterates though range just after the index value to check for smaller number
        for next_index in range(index+1, len(list_numbers)):
            print("    current comparative index: ", next_index)

            if (list_numbers[next_index] < list_numbers[least_index]):
                temp1 = list_numbers[least_index]
                temp2 = list_numbers[next_index]
                # swapping smaller value into position of smaller index
                list_numbers[least_index] = temp2
                list_numbers[next_index] = temp1
                print("        swapped {i} and {j}\n updated list:    {list} ".format(
                    i=temp1, j=temp2, list=list_numbers))
            else:
                print("        no new least number found, moving to next index...")
    print("final sorted list: ", list_numbers)


# main program
numbers = [8, 7, 4, 0, 5, 19, 1, 100, 3]
print("initial unsorted list:\n", numbers)

selection_sort(numbers)
