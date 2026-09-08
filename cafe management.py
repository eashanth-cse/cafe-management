menu = {
    'pizza':50, 'salad':30, 'burger':100, 'pop corn':150
}

print('welcome to our lucky cafe')
print('pizza:50\nsalad:30\nburger:100\npop corn:150')#\n is used to arrange the menu vertically
order_item = input('enter your item:')

order_total = 0

if order_item in menu:
   order_total+= menu[order_item]
   order = input('do you want anything else(Yes/No):')
   if order == 'Yes':
      order_item2 = input('enter your second item:')
      if order_item2 in menu:
         order_total += menu[order_item2]
         print(f'your order value {order_total}')
   else:
      print(f'your order value: {order_total}')#f is used because it is  format printer 
else:
   print('you enterd a worng item')



