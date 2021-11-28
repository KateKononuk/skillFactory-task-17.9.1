def insert_sort(array: list):
    for i in range(len(array)):
        current = array[i]
        while i > 0 and array[i - 1] > current:
            array[i] = array[i - 1]
            i -= 1
        array[i] = current
        print(array)
    return array


# Итеративный бинарный поиск
def binary_search(array: list, target: int):
    low = 0
    high = len(array) - 1
    # Если target не в спике, будем искать в словаре с ближайщими элементами
    nearest = {}  # индекс: разность между искомым и текущим элементами

    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            print(f"Индекс элемента меньшего искомого {mid - 1}\
                \nИндекс искомого элемента {mid}")
            return True
        elif target < array[mid]:
            nearest[mid] = (target - array[mid])
            high = mid - 1
        else:
            nearest[mid] = (target - array[mid])
            low = mid + 1
    nearest_indexes(nearest)


# Если искомого элемента нет в списке, то мы ищем ближайщие
def nearest_indexes(pairs: dict):
    keys = list(pairs.keys())
    low = keys[-2]
    hight = keys[-1]
    print(f"Искомый элемент не содержится в списке, но\
        \nИндекс элемента меньше искомого {low}\
        \nИндекс элемента больше искомого {hight}")


try:
    data = [int(i) for i in input("Введите числа через пробел:\n").split()]
    n = int(input("Введите искомое число:\n"))
except TypeError:
    print("Вводимая строка должна состоять только из чисел")


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
