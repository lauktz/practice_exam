from helper.helper import menu_selection
from json_helper import read_json

# cars = [{"model": 2000, "brand": "Kia", "color": "blue"}, {"model": 2001, "brand": "bmw", "color": "silver"}]

try:
    def menu(cars):
        while True:
            print("Laura's Garage")
            print('Choose one of the following actions: ')
            print("1 - Get all cars")
            print("2 - Add car")
            print("3 - Delete car")
            print("4 - Edit car")
            print("5 - Save cars")
            print("6 - Exit")
            choice = input("")
            menu_selection(cars,choice)
 
    def main():
        cars = read_json();
        menu(cars)

    if __name__ == "__main__":
        main()


except Exception as err:
    print(err)