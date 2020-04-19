from invoice import Invoice

products = {}
total_amount = 0

while True:
    product = input("enter your product: ")
    unit_price = Invoice().input_number("enter unit price: ")
    qnt = Invoice().input_number("enter quantity: ")
    discount = Invoice().input_number("discount percent [x]%: ")
    repeat = Invoice().input_answer("another product? [y / n] ")
    result = Invoice().add_product(qnt, unit_price, discount)
    products[product] = result

    if repeat == "n":
        break

total_amount = Invoice().total_pure_price(products)

print("total pure price: $" + str(total_amount))
