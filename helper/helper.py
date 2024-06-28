from services.crud import get_cars, add_car, delete_car, edit_car
from json_helper import save_json

def menu_selection(cars, choice):
    if choice == "1":
        return get_cars(cars)
    elif choice == "2":
        return add_car(cars)
    elif choice == "3":
        return delete_car(cars)
    elif choice == "4":
        return edit_car(cars)
    elif choice == "5":
        return save_json(cars)
    elif choice == "6":
        print("exit")
        exit()
