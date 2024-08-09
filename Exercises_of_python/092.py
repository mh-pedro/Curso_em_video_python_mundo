# Make a program that read the name, birthday and the work wallet (WW), safe then (with the age) in an dict.
# If the WW is different of zero, the dict recive too the year of contratc and the salary. 
# Make a calculation and add how munch year the person need to retire.
import datetime

print('='*50)
print('Work Wallet'.center(50))
print('='*50)

person = dict()
year_now =  datetime.datetime.today().year

person['name'] = str(input('Write your name: '))
birthday = int(input('Year of birth: '))
person['year'] = year_now - birthday
person['WW'] = int(input('Work Wallet (0 if not)? '))
if person['WW'] != 0:
    person['year_of_contratc'] = int(input("What's the year of contraction? "))
    person['salary'] = float(input("What's your salary? R$ "))
    time_work = year_now - person['year_of_contratc']
    person['retire'] = + person['year'] + (35 - time_work)
print('='*50)

for k, v in person.items():
    print(f'{k} has the value {v}.')
print('='*50)
