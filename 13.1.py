from datetime import date

current_date = datetime.now().strftime("08/23/01")

with open('today.txt', 'w') as file:
    file.write(current_date)