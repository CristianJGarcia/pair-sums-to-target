def pairs_sum_to_target(list1, list2, target):
    # Write your code here.
    sums = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] + list2[j] == target:
                sums.append([i,j])
    return sums

list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5

print(pairs_sum_to_target(list1,list2, target))