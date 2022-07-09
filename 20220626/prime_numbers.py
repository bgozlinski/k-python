#  Z zestawu liczb wybierz liczby pierwsze i zapisz je w liscie prime_numbers

numbers = [1, 11, 2, 15, 3, 65, 13, 8, 29]

prime_numbers = []

for number in numbers:
    if number <= 1:
        continue
    else:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)

print(prime_numbers)
