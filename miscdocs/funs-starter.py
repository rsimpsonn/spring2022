# fun pen-cost(num-pens :: Number, message :: String) -> Number:
#   doc: ```total cost for pens, each 25 cents
#        plus 2 cents per message character```
#   num-pens * (0.25 + (string-length(message) * 0.02))
# where:
#   pen-cost(1, "hi") is 0.29
#   pen-cost(10, "smile") is 3.50
# end

# ---------------------------------------------

# fun add-shipping(order-amt :: Number) -> Number:
#   doc: "add shipping costs to order total"
#   if order-amt <= 10:
#     order-amt + 4
#   else if (order-amt > 10) and (order-amt <= 30):
#     order-amt + 8
#   else:
#     order-amt + 12
#   end
# end

# ---------------------------------------------

















def add1v1(x: int) -> int:
    return x + 1

def add1v2(x: int) -> int:
    print(x + 1)

def add1v3(x: int) -> int:
    x + 1
