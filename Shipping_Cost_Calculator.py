
## input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## calculate shipping cost
shipping_cost = weight * rate

print(f"shipping_cost: {shipping_cost} USD")

