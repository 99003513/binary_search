"""
Program for Binary searching
Author:R.Phanindra Reddy
Date:21/06/2021
"""


def bin_search(list1, ele):
    ''' Describing the function
                     for binary search'''
    low = 0
    high = len(list1)-1
    mid = 0
    while low <= high:
        mid = (high+low)//2
        if list1[mid] < ele:
            low = mid+1
        elif list1[mid] > ele:
            high = mid-1
        else:
            return mid
    return -1
list_1 = []
no_of_elements=int(input("Enter the no of elements in list"))
for i in range(0,no_of_elements):
    x=int(input("enter number"))
    list_1.append(x)
print(list_1)
element= int(input("Enter  the element to search"))
RES_1 = bin_search(list_1, element)
if RES_1 != -1:
    print("Element is present at index", str(RES_1))
else:
    print("Element is not present")
