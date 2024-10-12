#Expense Buddy

i. Brief Description:

Expense Buddy is a tool designed to simplify the process of sharing and settling expenses among roommates. It takes a CSV file as input, containing details about shared expenses such as the amount, payer, and participants. Expense Buddy calculates how much each roommate owes to or is owed by others, ensuring a fair and accurate split of expenses. This tool helps roommates keep track of shared costs and manage reimbursements efficiently. The output is a detailed summary of individual balances, making it easy for everyone to see who owes what and to settle payments accordingly.

ii. Algorithm and Libraries:

Algorithm: The core algorithm involves parsing and aggregating the expense data to identify total payments made and amounts owed by each participant. It calculates the fair share of each expense for all involved roommates, then determines the net balance by comparing individual contributions and liabilities. Based on these calculations, it provides a breakdown of amounts owed between roommates.

Libraries:
Pandas: For reading, organizing, and analyzing the CSV data.
NumPy: For numerical computations, such as calculating totals and balancing payments.
Matplotlib (optional): For creating visual representations of the expense breakdown and settlement.
Flask/Django (optional): To develop a web-based interface, allowing users to upload expense files and view results online.

iii. Data Needed:

Expense Data:

CSV File: Should contain the following columns:
Date: The date the expense was incurred.
Amount: The total amount of the expense.
Payer: The roommate who paid for the expense.
Participants: The roommates who shared in the expense.
Roommate Information: A list of all roommates included in the expense-sharing arrangement.

iv. Expected Outcome:

Expense Buddy will provide users with a detailed breakdown of shared expenses, including:

Individual Balances: The amount each roommate owes or is owed.
Settlement Instructions: Clear recommendations on how roommates can settle their balances with one another.
Expense Summary: A detailed view of each person’s contributions and share of the expenses.
This tool will streamline the management of shared costs among roommates, ensuring transparency and promoting fairness. The output will help roommates easily understand and settle debts, enhancing financial harmony in shared living spaces.









