"""
    Performs a linear search to find a specific target value within an unsorted list.
    
    Explanation:
    - Linear search is a straightforward method of searching where each element in the list is checked sequentially.
    - It starts from the first element and continues until the target is found or the end of the list is reached.

    How it works:
    - Iterates over each element in the list using a 'for' loop.
    - Compares each element with the target value.
    - If a match is found, it prints a message and returns the index of the target.
    - If the loop completes without finding the target, it returns -1, indicating the target is not in the list.

    Parameters:
    - list: The list in which to search for the target. It does not need to be sorted.
    - target: The value that the function attempts to find.

    Returns:
    - The index of the target element in the list if found.
    - '-1' if the target is not found in the list.
"""
    
print("")
print("Linear Search Algorithm - Time Complexity: O(n)")
print("")

def linear_search(list, target):
    """
    Performs a linear search to find the target value in a list.

    Linear search checks every element in the list sequentially until it finds the target.
    If the target is found, it returns the index of the target. If the target is not in the list, it returns -1.

    @param list The list in which to search for the target.
    @param target The value to search for in the list.
    @returns The index of the target in the list, or -1 if the target is not found.
    """
    for i in range(len(list)):
        print("Step", i, ":", list[i])
        if list[i] == target:
            print("Target Found: " + str(target))
            return i
    return -1

print("\nTest Case 1: ")
test_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
test_target=90
linear_search(test_list,test_target)

print("\nTest Case 2: ")
test_list2=[10, 20, 30, 40, 50, 60, 70, 80, 90]
test_target2=50
linear_search(test_list2,test_target2)

print("\nTest Case 3: ")
test_list3=[10, 20, 30, 40, 50, 60, 70, 80, 90]
test_target3=10
linear_search(test_list3,test_target3)