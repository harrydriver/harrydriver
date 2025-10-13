from math import pi

# 

pizza_size = int(input("Enter the size of the pizza in inches. (9, 11 or 13): "))
pizza_num = int(input("Enter how pizzas you would like: "))

if pizza_size in [9, 11, 13]:
    if pizza_num > 0:
            pizza_area = pi * (pizza_size / 2) ** 2
            total_area = pizza_area * pizza_num

            print(
                  f"A {pizza_size}-inch pizza has an area of {pizza_area:.2f} square inches."
            )
            print(
                  f"So in total you have over {total_area:.2f} square inches of pizza!"
            )
    else:
        print("You must order a minimum of one pizza.")
else:
    print(
            "You have not selected an available pizza size, please choose an 9, 11 or 13 inch pizza"
        )