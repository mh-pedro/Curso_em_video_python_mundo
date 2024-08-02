# Make an algorithm to read the product price and show its new price with 5% discount.
n1 = int(input('Into the product price: '))
des = n1*0.05
n2 = n1-des
print('The price of the product is {} and if we buy now, we will get the 5% discount, which is {}. The product is now avaible for {}.'.format(n1,des,n2))
