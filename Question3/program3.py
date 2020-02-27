import math

def fun(amount):
  assert amount > 0 and amount < pow(10,6)
  bills = [100.00,50.00,20.00,10.00,5.00,2.00]
  print ("R$ %.2f:"%(amount))
  for x in bills:
    if amount/x >= 1:
      print ("%i nota(s) de R$ %.2f"%((amount/x),x))
    amount %= (x)

  amount = int(round(amount * 100))
  coins = [100, 50, 25, 10, 5, 1]
  for x in coins:
    if (amount/x) >= 1:
      print ("%i moeda(s) de R$ %.2f"%((amount/x),x/100))
    amount %= (x)
