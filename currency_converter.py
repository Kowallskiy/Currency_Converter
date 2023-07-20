from requests import get

API_KEY = 'fca_live_9Qflc2q16etMSw7R6rF4ER2rOeWsIhzSNI5wcUFI'
BASE_URL = 'https://api.freecurrencyapi.com/'

# This function extracts all currencies available for converting
def get_currencies():

    endpoint = f"v1/latest?apikey={API_KEY}"

    url = BASE_URL + endpoint
    data = get(url).json()['data']
    
    data = list(data.items())
    return data

# This function sorts the data and makes it look user-friendly
def print_currencies(currencies):
    for i in currencies:
        name, currency = i
        print(f"{name} - {currency}")


def converter(currencies):
    name = input('To what currency do you want to convert? ').upper()
    while True:
        amount = input("How much do you want to convert? $")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print('Please, enter a valid number')
# this loop goes through the data and finds a name of a currency (n) and its exchange rate (c)
    for i in currencies:
        n, c = i
        # if requested name (name) matches the currency in the data (n) this converter function
        # gives us current exchange rate from USD$ to chosen currency
        if name == n:
            print(f"The rate is {c}")
            print(f"{amount}$ is {amount * c} {n}")
            return
    print('There is no such currency')

def main():
    currencies = get_currencies()
    print_currencies(currencies)
    converter(currencies)

main()