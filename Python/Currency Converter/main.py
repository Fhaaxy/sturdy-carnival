import requests

print("Currency Converter")

#10 most important currencies in the world and their exchange rates to USD
rates = {
    "USD": 1.00,
    "EUR": 0.93,
    "GBP": 0.76,
    "JPY": 154.00,
    "CAD": 1.40,
    "CHF": 0.80,
    "AUD": 0.66,
    "CNY": 7.12,
    "NZD": 0.57,
    "SGD": 1.30,
    "INR": 88.20
}

amount = 0.0
converted_amount = 0.0


#Get user input for currency conversion
while True:
    choice1 = input ("What currency do you want to convert? (USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR): ").upper()
                    
    if choice1 in rates:
        break
    else:
        print("Invalid currency. Please choose from USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR.")


#Get user input for amount to convert
while True:
    amount = input("Enter the amount you want to convert: ")

    try:
        amount = float(amount)
        break
    except ValueError:
        print("Invalid amount. Please enter a numeric value (Use dot for decimal numbers).")


#Get user input for currency to convert to
while True:
    choice2 = input ("What currency do you want to convert to? (USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR): ").upper()
                    
    if choice2 in rates:
        break
    else:
        print("Invalid currency. Please choose from USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR.")


#Convert currency
converted_amount = (amount / rates[choice1]) * (rates[choice2])

print("The converted amout from", choice1, "to", choice2, "is:", converted_amount, choice2)