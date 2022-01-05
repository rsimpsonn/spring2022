from dataclasses import dataclass

@dataclass
class Item:
    descr : str
    price : float

@dataclass
class Order:
    customer : str
    items: list

# Several Items
hp_book = Item("Harry Potter book", 17.95)
cap = Item("baseball cap", 12.95)
radio = Item("radio", 10)
laptop = Item("laptop", 900)

# a catalog is a list of items
catalog = [hp_book, radio, laptop]

# Some orders
k_order = Order("Kathi", [radio, hp_book, laptop])
m_order = Order("Milda", [laptop, Item("radio", 10)])

# The companies list of open orders (that haven't been paid for yet)
open_orders = [k_order, m_order]

def update_price1(for_descr : str, new_price : float) -> None:
    """update the price for the item with the given description"""
    for item in catalog:
        if item.descr == for_descr:
            item.price = new_price


def update_price2(for_descr : str, new_price : float) -> None:
    """update the price for the item with the given description"""
    global catalog
    new_catalog = []
    for item in catalog:
        if item.descr == for_descr:
            new_catalog.append(Item(item.descr, new_price))
        else:
            new_catalog.append(item)
    # Memory point 2
    catalog = new_catalog

# The expressions to run
update_price1("radio", 8.50)
# Memory point 1
update_price2("radio", 7)
# Memory point 3
update_price1("radio", 5)
update_price1("laptop", 1100)
# Memory point 4
