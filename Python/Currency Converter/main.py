import requests

print("Currency Converter")

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

while True:
    choice1 = input ("What currency do you want to convert? (USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR): ").upper()
                    
    if choice1 in rates:
        break
    else:
        print("Invalid currency. Please choose from USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR.")



while True:
    amount = input("Enter the amount you want to convert: ")

    try:
        amount = float(amount)
        break
    except ValueError:
        print("Invalid amount. Please enter a numeric value (Use dot for decimal numbers).")



while True:
    choice2 = input ("What currency do you want to convert to? (USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR): ").upper()
                    
    if choice2 in rates:
        break
    else:
        print("Invalid currency. Please choose from USD, EUR, GBP, JPY, CAD, CHF, AUD, CNY, NZD, SGD, INR.")


converted_amount = (amount / rates[choice1]) * (rates[choice2])

print("The converted amout from", choice1, "to", choice2, "is:", converted_amount, choice2)