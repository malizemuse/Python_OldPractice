""" Computes age in seconds for 2 people and the age difference between them """

# necessary for getting current date 
import datetime

# Greeting
print("Compute the difference of ages (in seconds) of two people\n")

month1 = int(input('Person 1 - Enter month of birth: '))
day1 = int(input('Person 1 - Enter day of birth: '))
year1 = int(input('Person 1 - Enter year of birth: '))
print('') 

month2 = int(input('Person 2 - Enter month of birth: '))
day2 = int(input('Person 2 - Enter day of birth: '))
year2 = int(input('Person 2 - Enter year of birth: '))
print('')
# Gets current month/day/year
date_month = datetime.date.today().month
date_day = datetime.date.today().day
date_year = datetime.date.today().year

# Seconds per day/year and per average day/year
secs_day = 24 * 60 * 60
secs_year = 365 * secs_day

# Average seconds per month/year (accounts for Leap year)
avg_secs_year = ((4 * secs_year) + secs_day) // 4
avg_secs_month = avg_secs_year // 12

# Calculation (approximate age in seconds)
# However, only accurate for birthdates in 19XX
dob1 = ((year1 - 1900) * avg_secs_year ) + \
        ((month1 - 1) * avg_secs_month) + \
        (day1 * secs_day)
dob2 = ((year2 - 1900) * avg_secs_year ) + \
        ((month2 - 1) * avg_secs_month) + \
        (day2 * secs_day)

current_date = ((date_year - 1900) * avg_secs_year) + \
                ((date_month - 1) * avg_secs_month) + \
                (date_day * secs_day)

age_in_secs1 = current_date - dob1
age_in_secs2 = current_date - dob2
diff_in_secs = abs(age_in_secs1 - age_in_secs2) 

# Outputs ages in secs of person 1 and person 2 then shows the difference
print('')
print('Calculation:')
print('  Person 1\'s age:', format(age_in_secs1, ','), 'secs')
print('  Person 2\'s age:', format(age_in_secs2, ','), 'secs')
print('  Age difference:', format(diff_in_secs, ','), 'secs')