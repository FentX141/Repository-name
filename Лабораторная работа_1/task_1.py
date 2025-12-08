numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
a = numbers[:4] #Числа до None
b = numbers[5:] #Числа после None
count_of_numbers = len(numbers)
srednee_numbers = sum(a+b)/count_of_numbers

numbers [4] = srednee_numbers
print("Измененный список:", numbers)
