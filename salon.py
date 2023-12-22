# All list items corralates by index
# List of Hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# List of Prices
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# List of Sales during the last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Carly wants to be able to market her low prices.
# Find the average price of a cut. 
total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)
print(f"Average Haircut Price: ${average_price}")
print(" ")

# Average price is more expensive than Carly thought.
# Cut all prices by 5 dollars.
new_prices = [price - 5 for price in prices]
print(f"New Cut Prices: {new_prices}")
print(" ")

# Find out how much revenue was brought in last week.
total_revenue = 0

for i in range(len(hairstyles)):
  total_sales = prices[i] + last_week[i]
  total_revenue += total_sales
  print(f" > Hairstyle {hairstyles[i]} had {last_week[i]} total sales for ${total_sales}.")

print(" ")
print(f"Total Revenue: ${total_revenue}")
print(" ")

# Find the average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: ${average_daily_revenue}")
print(" ")

# Bring in more customers by advertising all of the haircuts under 30 dollars.
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)-1) if new_prices[i] < 30]
print(f"Cuts under $30: {cuts_under_30}")
