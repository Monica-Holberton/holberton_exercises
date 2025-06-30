
def process_order(items, discount_code=None):
    print("Items ordered:")
    for item in items:
        print("-", item)

    price_per_item = 10
    total_before = len(items) * price_per_item

    print("Price before discount:", total_before)

    if discount_code == "SAVE10":
        total_after = total_before * 0.9
        print("Discount applied: 10%")
    else:
        total_after = total_before
        print("No discount applied.")

    print("Price after discount:", total_after)
process_order(["Apple", "Chocolate"], "SAVE10")
