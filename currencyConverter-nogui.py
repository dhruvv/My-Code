from forex_python.converter import CurrencyRates

currency = CurrencyRates()

currency1 = input("Please enter convert from currency in form - USD, INR, GBP etc")
currency2 = input("Enter final currency")
value = int(input("Enter Value"))
print(currency.convert(currency1,currency2,value))
