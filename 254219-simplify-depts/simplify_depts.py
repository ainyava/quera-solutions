import heapq
from collections import defaultdict

payments = []

for i in range(3):
    payments.append([int(item.strip()) for item in input().split(" ")])


def simplify_debts(transactions):
    total = defaultdict(int)

    # linearize the table using a dict
    for giver in range(len(transactions)):
        for receiver in range(len(transactions[giver])):
            amount = transactions[giver][receiver]
            total[giver] -= amount
            total[receiver] += amount

    credit = []
    debit = []

    # credit/depts transactions to heap
    for name, amount in total.items():
        if amount > 0:
            heapq.heappush(credit, (-amount, name))
        if amount < 0:
            heapq.heappush(debit, (amount, name))

    # transfer items by their priority
    answer = [[0 for _ in range(3)] for _ in range(3)]
    while credit and debit:
        credit_value, credit_name = heapq.heappop(credit)
        debit_value, debit_name = heapq.heappop(debit)

        if credit_value < debit_value:
            amount_left = credit_value - debit_value
            answer[debit_name][credit_name] = -1 * debit_value
            heapq.heappush(credit, (amount_left, credit_name))

        elif debit_value < credit_value:
            amount_left = debit_value - credit_value
            answer[debit_name][credit_name] = -1 * credit_value
            heapq.heappush(debit, (amount_left, debit_name))

        else:
            answer[debit_name][credit_name] = -1 * credit_value

    return answer


for row in simplify_debts(payments):
    for col in row:
        print(col, end=" ")
    print()
