import openpyxl


def create_expense_sheet():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Day'
    sheet['B1'] = 'Expenses'
    sheet['C1'] = 'Daily Budget'
    sheet['D1'] = 'Exceeded Amount'
    sheet['E1'] = 'Total Budget'
    workbook.save('expense_tracker.xlsx')


def main():
    create_expense_sheet()

    workbook = openpyxl.load_workbook('expense_tracker.xlsx')
    sheet = workbook.active

    total_budget = float(input("Enter the total budget: $"))
    daily_budget = float(input("Enter the total daily budget: $"))

    total_expenses = 0
    exceeded_days = []

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
        expense = float(input(f"Enter expenses for {day}: $"))
        total_expenses += expense

        if expense > daily_budget:
            exceeded_days.append((day, expense))
            if day == 'Thursday':
                sheet.append([day, expense, daily_budget, expense - daily_budget, total_budget])
            else:
                sheet.append([day, expense, daily_budget, expense - daily_budget])
        else:
            if day == 'Thursday':
                sheet.append([day, expense, daily_budget, ' ', total_budget])
            else:
                sheet.append([day, expense, daily_budget])

    average_daily_expense = total_expenses / len(days_of_week)

    print("\nExpense Summary:")
    print(f"Total Expenses for the week: ${total_expenses:.2f}")
    print(f"Average Daily Expense: ${average_daily_expense:.2f}")

    if exceeded_days:
        print("Days where expenses exceeded the daily budget:")
        for day, expense in exceeded_days:
            print(f"{day}: ${expense:.2f}")
    else:
        print("No days exceeded the daily budget.")

    workbook.save('expense_tracker.xlsx')


main()
