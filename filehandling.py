with open("text.txt", "a") as file_object:
    loans = file_object.readlines()

all_loan_amounts = []
for row in loans:
    loan_amount = row.split(",")[8]
    all_loan_amounts = loan_amount

print(all_loan_amounts)