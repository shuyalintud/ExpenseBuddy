# expense_buddy.py
import pandas as pd
import numpy as np

def load_expense_data(file_path):
    """
    Load expense data from a CSV file.

    Parameters:
        file_path (str): The path to the CSV file containing expense data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded expense data.
    """
    return pd.read_csv(file_path)

def prepare_data(df):
    """
    Clean and prepare the expense data by parsing participants into lists.

    Parameters:
        df (pd.DataFrame): DataFrame containing raw expense data.

    Returns:
        pd.DataFrame: DataFrame with participants parsed into lists.
    """
    df['Participants'] = df['Participants'].apply(lambda x: x.split(','))
    return df

def calculate_shares(df):
    """
    Calculate the share of each participant for each expense.

    Parameters:
        df (pd.DataFrame): DataFrame with parsed participant data.

    Returns:
        pd.DataFrame: DataFrame with added 'Share' column, indicating each participant's share of each expense.
    """
    df['Share'] = df['Amount'] / df['Participants'].apply(len)
    return df

def calculate_balances(df):
    """
    Calculate total balance for each roommate based on expenses.

    Parameters:
        df (pd.DataFrame): DataFrame with expense and participant share data.

    Returns:
        dict: Dictionary with roommate names as keys and their total balance as values.
              Positive values indicate amounts owed to the roommate, while negative values indicate debts.
    """
    roommates = set(df['Payer'].unique()).union(*df['Participants'])
    balances = {roommate: 0 for roommate in roommates}

    for _, row in df.iterrows():
        payer = row['Payer']
        participants = row['Participants']
        share = row['Share']

        # Update payer balance
        balances[payer] += row['Amount'] - share * len(participants)

        # Update participants' balances
        for participant in participants:
            if participant != payer:
                balances[participant] -= share

    return balances

def generate_settlements(balances):
    """
    Generate settlement instructions based on calculated balances.

    Parameters:
        balances (dict): Dictionary with roommate names as keys and their balance as values.

    Returns:
        list: List of tuples in the format (debtor, creditor, amount) representing each settlement.
    """
    settlements = []
    creditors = {k: v for k, v in balances.items() if v > 0}
    debtors = {k: -v for k, v in balances.items() if v < 0}

    creditors = sorted(creditors.items(), key=lambda x: -x[1])
    debtors = sorted(debtors.items(), key=lambda x: -x[1])

    while debtors and creditors:
        debtor, debt = debtors.pop(0)
        creditor, credit = creditors.pop(0)
        amount = min(debt, credit)

        settlements.append((debtor, creditor, amount))

        if credit > amount:
            creditors.insert(0, (creditor, credit - amount))
        if debt > amount:
            debtors.insert(0, (debtor, debt - amount))

    return settlements

def display_results(balances, settlements):
    """
    Display the final balances and settlement instructions.

    Parameters:
        balances (dict): Dictionary with roommate names as keys and their balance as values.
        settlements (list): List of tuples in the format (debtor, creditor, amount) representing each settlement.

    Returns:
        None
    """
    print("Final Balances:")
    for roommate, balance in balances.items():
        print(f"{roommate}: {'Owes' if balance < 0 else 'Is owed'} ${abs(balance):.2f}")

    print("\nSettlement Instructions:")
    for debtor, creditor, amount in settlements:
        print(f"{debtor} should pay {creditor} ${amount:.2f}")

def main(file_path):
    """
    Main function to run the Expense Buddy program.

    Parameters:
        file_path (str): The path to the CSV file containing expense data.

    Returns:
        None
    """
    df = load_expense_data(file_path)
    df = prepare_data(df)
    df = calculate_shares(df)
    balances = calculate_balances(df)
    settlements = generate_settlements(balances)
    display_results(balances, settlements)

