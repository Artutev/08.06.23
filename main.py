#1
def find_min_common_divisor(a, b):
    max_value = max(a, b)
    while True:
        if max_value % a == 0 and max_value % b == 0:
            return max_value
        max_value += 1

a = int(input("Введите количество человек в команде биологов: "))
b = int(input("Введите количество человек в команде информатиков: "))

result = find_min_common_divisor(a, b)

print("Минимальное число кусочков пирога:", result)

#2
def find_missing_card(N, remaining_cards):
    total_sum = (N * (N + 1)) // 2
    remaining_sum = sum(remaining_cards)
    missing_card = total_sum - remaining_sum
    return missing_card

N = int(input("Введите общее количество карточек (N): "))
remaining_cards = [int(input()) for _ in range(N - 1)]

result = find_missing_card(N, remaining_cards)
print("Номер потерянной карточки:", result)

