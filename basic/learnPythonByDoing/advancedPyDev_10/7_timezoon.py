from datetime import datetime

print(datetime.now(),'\n\n\n')





from datetime import datetime, timezone
print(datetime.now(timezone.utc), '\n\n\n')



from datetime import datetime, timezone, timedelta
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow,'\n\n\n')

# convert to string_format_time()
print(today.strftime('%d-%m-%Y %H:%M:%S'))
print(today.strftime('%d-%h-%y %H:%M:%S'))
print(today.strftime('%D %H:%M:%S'))

# convert string_parse_time()
user_data = input('Enter the data in YYYY-MM-DD formate: ')
user_data = datetime.strptime(user_data, '%Y-%m-%d')
print(user_data)







