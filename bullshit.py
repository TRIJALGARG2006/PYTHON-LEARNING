# name = input("enter your name :")

# print("hello" , name)


# print(f"good morning {name}")


list = (x**2 for x in range(1,10))

print(list)

for i in list:
    print(i)


# def number(*args,**kwargs):
#     for args in args:
#         print(args , end=" ")
#     print()
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
#     print()

# number("trijal","garg",Section = "a")
# number("kartikeya","narang","bala", section = "a" )


# word = "DataScience"
# print(word[-5:][::-1])



# import matplotlib.pyplot as plt
# import numpy as np

# # 1. Setup Data (Mock data since specific numbers weren't provided)
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
#           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# # Sales data (in thousands)
# electronics = [20, 25, 30, 28, 35, 45, 40, 50, 55, 65, 80, 75]
# clothing =    [15, 18, 20, 25, 30, 32, 35, 30, 28, 35, 40, 45]
# groceries =   [40, 42, 41, 43, 45, 46, 48, 50, 52, 55, 60, 62]
# furniture =   [10, 12, 15, 14, 18, 20, 22, 25, 24, 28, 30, 28]

# # 2. Plot the Multi-line Chart
# plt.figure(figsize=(12, 6))

# plt.plot(months, electronics, label='Electronics', marker='o', color='blue')
# plt.plot(months, clothing, label='Clothing', marker='s', color='orange')
# plt.plot(months, groceries, label='Groceries', marker='^', color='green')
# plt.plot(months, furniture, label='Furniture', marker='d', color='red')

# # 3. Highlight the Max Electronics Sales
# # Logic: Find the max value and its corresponding month index
# max_sales = max(electronics)
# max_index = electronics.index(max_sales)
# max_month = months[max_index]

# # Plot a big red star on that specific point
# plt.plot(max_month, max_sales, marker='*', color='red', markersize=20, label='Highest Elec. Sales')

# # Add an annotation text next to the marker
# plt.annotate(f'Peak: {max_sales}', 
#              (max_month, max_sales), 
#              xytext=(0, 10), 
#              textcoords='offset points', 
#              ha='center', 
#              fontweight='bold')

# # 4. Styling (Titles, Labels, Grid, Legend)
# plt.title('Monthly Sales Trends by Category (Retail Company)')
# plt.xlabel('Month')
# plt.ylabel('Sales (in $1000s)')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()

# # 5. Show Plot
# plt.show()



# def get_fib_number(n):
#     if n <= 0: return 0
#     if n == 1: return 1
#     return get_fib_number(n - 1) + get_fib_number(n - 2)
# for i in range(n):
#     print(get_fib_number(i), end="")



