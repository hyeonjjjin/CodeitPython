# Divide and Conquer
def consecutive_sum(start, end):
    if end == start:
        return start
    return consecutive_sum(start, (start+end)//2)+consecutive_sum((start+end)//2+1, end)


# 정렬된 두 리스트를 받아 하나의 정렬된 리스트로 리턴
def merge(list1, list2):
    answer = []
    while len(list1) > 0 or len(list2) > 0:
        if len(list1) == 0:
            answer.append(list2[0])
            del list2[0]
        elif len(list2) == 0:
            answer.append(list1[0])
            del list1[0]
        elif list1[0] < list2[0]:
            answer.append(list1[0])
            del list1[0]
        else:
            answer.append(list2[0])
            del list2[0]
    return answer


# 두 리스트 중 하나만 비어도 반복문을 나오게 하고 나머지를 한번에 넣어줌
def merge_feedback(list1, list2):
    i = 0
    j = 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    merged_list = merged_list + list1[i:] + list2[j:]

    return merged_list


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        return merge(merge_sort(my_list[:len(my_list)//2]), merge_sort(my_list[len(my_list)//2:]))
    # 받은 리스트를 쪼개야 정렬할 수 있어
    # 근데 쪼개진 리스트도 정렬되어있지 않으니 쪼개야 정렬할 수 있어
    # 최종적으로 길이가 0-1인 리스트로 쪼개야 merge 함수를 통해 정렬된 리스트로 합칠 수 있어
    # 길이가 0-1인 리스트로 쪼개진 경우 merge 함수에 보내서 합쳐
    # 합쳐진 리스트는 정렬된 상태일 테니 그대로 다시 merge 함수에 대입될 수 있어
    # 상호반복.. 을 통해 정렬 되는거다!


# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    swap = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = swap
    # my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    b = i = start
    while i < end:
        if my_list[i] <= my_list[end]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, b, end)
    end = b
    return end


def quicksort(my_list, start, end):
    if end-start < 0:
        return
    else:
        newpivot = partition(my_list, start, end)
        quicksort(my_list, start, newpivot-1)
        quicksort(my_list, newpivot+1, end)


# 옵셔널 파라미터(Optional Parameter) 사용!
def quicksort2(my_list, start=0, end=None):
    if end is None:
        end = len(my_list)-1
    if end - start < 0:
        return
    else:
        newpivot = partition(my_list, start, end)
        quicksort(my_list, start, newpivot - 1)
        quicksort(my_list, newpivot + 1, end)




list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort2(list2) # start, end 파라미터 없이 호출
print(list2)
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge([1], []))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))

print(consecutive_sum(1, 10))
