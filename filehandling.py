import numpy as np

with open("text.txt", "a") as file_object:
    loans = file_object.readlines()

all_loan_amounts = []
for row in loans:
    loan_amount = row.split(",")[8]
    if loan_amount == "":
        continue
    all_loan_amounts.append(int(loan_amount))
    all_loan_amounts = loan_amount

print(all_loan_amounts)

loan_array = np.array(all_loan_amounts)