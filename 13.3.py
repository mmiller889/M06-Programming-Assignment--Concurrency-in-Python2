from datetime import datetime


today_string = "2023-12-4"  

parsed_date = datetime.strptime(today_string, '%Y-%m-%d').date()


print(parsed_date)