# Psudocode example from Wikipedia
#
# procedure bubbleSort( A : list of sortable items )
#     n = length(A)
#     repeat
#         swapped = false
#         for i = 1 to n-1 inclusive do
#             /* if this pair is out of order */
#             if A[i-1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap( A[i-1], A[i] )
#                 swapped = true
#             end if
#         end for
#     until not swapped
# end procedure

def bubbleSort(lst):
    n = len(lst)
    swapped = False
    while not swapped:
        for i in range(1, n):
            swapped = False
            if lst[i-1] > lst[i]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                swapped = True
    return lst
