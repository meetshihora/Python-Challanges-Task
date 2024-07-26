''' Task 2: You are given following list of stocks and their prices in last 3 days,

        Stock	Prices
        info	[600,630,620]
        ril	    [1430,1490,1567]
        mtl	    [234,180,160]

        1. Write a program that asks user for operation. Value of operations could be,
            a. print: When user enters print it should print following,
                info ==> [600, 630, 620] ==> avg:  616.67
                ril ==> [1430, 1490, 1567] ==> avg:  1495.67
                mtl ==> [234, 180, 160] ==> avg:  191.33
            
            b. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks. '''

# Solution

stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}

def print_stocks():
    for stock in stocks:
        prices = stocks[stock]
        print(f"{stock} ==> {prices} ==> avg: {sum(prices) / len(prices):.2f}")

def add_stock():
    stock = input("Enter stock ticker: ")
    if stock in stocks:
        price = int(input("Enter price: "))
        stocks[stock].append(price)
    else:
        price = int(input("Enter price: "))
        stocks[stock] = [price]

op = input("Enter operation (add or print): ")
if op.lower() == 'print':
    print_stocks()
elif op.lower() == 'add':
    add_stock()
