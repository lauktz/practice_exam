def get_cars(cars):
    for car in cars:
        print(car)

def add_car(cars:list):
    new_model = input("Enter model: ")
    new_brand = input("Enter brand: ")
    new_color = input("Enter color: ")


    new_car = {"model": new_model, "brand": new_brand, "color": new_color}
    cars.append(new_car)
    return print("New car added ", new_car)


def delete_car(cars:list):
    car_select = int(input("choose car number: "))
    cars.pop(car_select)
    return print("car deleted")


def edit_car(cars:list):
    car_select = int(input("choose car number: "))
    print("You are editing: " ,cars[car_select])
    edit_model = input("Enter model: ")
    edit_brand = input("Enter brand: ")
    edit_color = input("Enter color: ")

    edited_car = {"model": edit_model, "brand": edit_brand, "color": edit_color}
    cars[car_select] = edited_car
    return print("car changed to: ", edited_car)

