# get user age and tell them how month and how meny second they live..
user_age_year = int(input("Enter your age by year : "))
user_age_exmonth = int(input("Enter your age by extra month after given year : "))
user_age_exday = int(input("Enter your age by extra day after given year & month : "))

monthFromYear = (user_age_year * 12)
totalMonth = (monthFromYear + user_age_exmonth)
print(f'\n you live {totalMonth} month And {user_age_exday} day from bron.')

day_to_sec = (24 * 60 * 60)
total_day_to_sec = (day_to_sec * user_age_exday)

month_to_sec = (30 * 24 * 60 * 60 )
total_month_to_sec=(month_to_sec * totalMonth )
total_sec = (total_day_to_sec + total_month_to_sec)

print(f'\n you live {total_sec} seconds from barth')

#