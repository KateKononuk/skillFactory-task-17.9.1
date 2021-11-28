def insert_sort(array):
    '''
        Insert Sort for input numbers
    '''
    for i in range(len(array)):
        element = array[i]
        while i > 0 and array[i - 1] > element:
            array[i] = array[i - 1]
            i -= 1
        array[i] = element
        print(array)
    return array


# бинарный поиск
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    # Если target не в списке, будем искать в словаре с ближайшими элементами
    dict_elements = {}  # индекс: разность между искомым и текущим элементами

    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            print(f"Индекс элемент меньше искомого {mid - 1}\
                \nИндекс искомого элемента {mid}")
            return True
        elif target < array[mid]:
            dict_elements[mid] = (target - array[mid])
            high = mid - 1
        else:
            dict_elements[mid] = (target - array[mid])
            low = mid + 1
    dict_indexes(dict_elements)

    
def dict_indexes(pairs: dict):
    keys = list(pairs.keys())
    low = keys[-2]
    hight = keys[-1]
    print(f"Искомый элемент не содержится в списке, но\
        \nИндекс элемента меньше искомого {low}\
        \nИндекс элемента больше искомого {hight}")


try:
    data = [int(i) for i in input("Введите последовательность чисел через пробел: ").split()]
    n = int(input("Введите искомое число:\n"))
except  ValueError:
    print("Пожалуйста, вводите только числа")


data = insert_sort(data)
if n == data[0]:
    print("Искомый элемент является минимальным в списке")
elif n < data[0]:
    print("Искомый элемент меньше минимального в списке")
elif n == data[-1]:
    print("Искомый элемент является максимальным в списке")
elif n > data[-1]:
    print("Искомый элемент больше максимального в списке")
else:
    binary_search(data, n)
