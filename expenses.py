
# simple project to count expenses
monate_list = ["Januar", "Februar","März", "April", "Mai", "Juni", "Juli", "August","September", "Oktober", "November", "Dezember"]

expenses = []

# function to create expense
def add_expense(month):
    expense_amount = int(input("Bitte Ausgabe eingaben [€] "))
    expense_type = str(input("Bitte Ausgabetyp eingeben (Haus, Spaß, Essen, andere) "))
    expense = (month, expense_amount, expense_type)
    expenses.append(expense)

# function to show expenses list for the month
def show_expense(month):
    for expense_month, expense_amount, expense_type in expenses:
        if month == expense_month:
            print("{} - {}".format(expense_amount, expense_type))

# function to show sum of expenses for the month  
def show_expenses(month):
    total_month_expenses = sum(expense_amount for expense_month, expense_amount, _ in expenses if expense_month == month)
    average_month = sum(1 for expense_month, _,_ in expenses if expense_month == month)
    print("Ausgaben in {} Monat: {} €".format(monate_list[month -1], total_month_expenses))
    print("Mittelwert in {} Monat: {} €".format(monate_list[month -1], total_month_expenses / average_month))

# function to show sum of expenses and average for the year
def show_stats():
    total_expenses = sum(expense_amount for _, expense_amount, _ in expenses)
    average_expenses = sum(1 for _, _, _ in expenses)
    
    print("Deine alle Ausgaben des Jahres: {} €".format(total_expenses))
    print("Mittelwerte des Jahres: {} €".format(total_expenses / average_expenses))


print("Willkommen")

# Menu

while True:
# Start window    
    print()
    print("\t1-12.\tMonat wählen")
    print("\t13.\tAlle Ausgaben und Mittelwert des Jahres")
    print("\t0.\tProgram enden")
    print()

    month = int(input("Bitte eine Aktivität auswählen: "))
    
    if month == 0:
        print("Danke, dass Sie mein Program benutzen. Schönen Tag")
        break
    if month < 0 or month > 13:
        print("Falsche Eingabe. Bitte ein Zahl wählen zwischen 1 und 12")
    if month == 13 :
        if len(expenses) == 0:
            print()
            print("Deine alle Ausgaben des Jahres: 0")
            print("Mittelwerte des Jahres: 0")
            continue
        else:
            print()
            print("Alle Ausgaben des Jahres: ", show_stats())
            continue
    
# Second window
    while True:
        print()
        print("\t0.\tZurück zur Wahl des Monats")
        print("\t1.\tAusgaben anzeigen (Liste)")
        print("\t2.\tAusgaben hinzufügen")
        print("\t3.\tAlle Ausgaben und Mittelwert {} Monat".format(monate_list[month -1]))
        print("\t4.\tStatistik des Jahres")
        print()

        yourChoice = int(input("Bitte eine Aktivität auswählen: "))

        if yourChoice == 0:
            break
        if yourChoice < 0 or yourChoice > 5:
            print("Falsche Eingabe")
        if yourChoice == 1:
            len_expense_amount_month = len(list(expense_amount for expense_month, expense_amount, _ in expenses if expense_month == month))
            if len_expense_amount_month == 0:
                print()
                print("Ausgaben in {} Monat: 0".format(monate_list[month -1]))
            else:
                print()
                show_expense(month)
        if yourChoice == 2:
            add_expense(month)
        if yourChoice == 3:
            len_expense_amount_month = len(list(expense_amount for expense_month, expense_amount, _ in expenses if expense_month == month))
            if len_expense_amount_month == 0:
                print()
                print("Ausgaben in {} Monat: 0".format(monate_list[month -1]))
                print("Mittelwert in {} Monat: 0".format(monate_list[month -1]))
            else:
                print()
                show_expenses(month)
        if yourChoice == 4:
            show_stats()

    