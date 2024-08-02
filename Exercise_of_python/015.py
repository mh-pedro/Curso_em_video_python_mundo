# Make a program that calculates how munch is for rent a car. The price is 0.60 cent for day and 0.15 for km drives.
dias = int(input('How munch days do you use the car? '))
km = int(input('How munc kilometers do you driver? '))

price = dias*0.6+km*0.15
print('You will pay {:.2f}, for {} days and {}Km.'.format(price,dias,km))
