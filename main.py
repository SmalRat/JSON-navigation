"""
Module for convenient navigation through the json file
"""
import json


def json_read(path):
    with open(path, mode="r", encoding="utf-8") as file:
        res = json.load(file)
    return res


def choice(obj, obj_path):
    def direction_choice(container=True):
        if container:
            while True:
                print("Do you want to go up or down?")
                print("U - up, D- down, E - exit")
                response = input("U/D/E? ")
                if response not in ("U", "D", "E"):
                    print("Incorrect input!")
                else:
                    return response
        else:
            while True:
                print("Do you want to go up or exit?")
                print("U - up, E - exit")
                response = input("U/E? ")
                if response not in ("U", "E"):
                    print("Incorrect input!")
                else:
                    return response

    def enter_obj_path(obj, obj_path):
        for key in obj_path:
            obj = obj[key]
        return obj

    def header():
        head = "path: json -> " + str(type(obj))
        for key in obj_path:
            head += " -> " + str(key)
        return head

    current_obj = enter_obj_path(obj, obj_path)
    print(header())

    if isinstance(current_obj, type([])):

        print("Current object is a list")
        length = str(len(current_obj))
        print("List length: " + length)
        response = direction_choice()
        if response == "U":
            try:
                obj_path.pop()
            except IndexError:
                print("Can't go up since it is the upper object in json!")

            return obj, obj_path

        elif response == "D":
            try:
                response = int(input("Enter the index of element you want to\
                 visit (int from 1 to " + length + ")"))
            except:
                print("Incorrect input! Repeating...")
                return obj, obj_path
            obj_path.append(response-1)
            return obj, obj_path
        else:
            return

    elif isinstance(current_obj, type({})):

        print("Current object is a dictionary")
        keys_list = list(current_obj.keys())
        print("Dictionary keys: ")
        for key in keys_list:
            print(key)
        response = direction_choice()
        if response == "U":
            try:
                obj_path.pop()
            except IndexError:
                print("Can't go up since it is the upper object in json!")

            return obj, obj_path

        elif response == "D":

            response = input("Enter the key, which value you want to visit: ")

            if response not in keys_list:
                print("Incorrect input! Repeating...")
                return obj, obj_path

            obj_path.append(response)

            return obj, obj_path
        else:
            return

    else:

        print("Current object is not container...")
        print("Object type: " + str(type(current_obj)))
        print("Object value: " + str(current_obj))

        response = direction_choice(False)
        if response == "U":
            obj_path.pop()

            return obj, obj_path

        else:
            return


def main(path):
    res = json_read(path)
    obj_path = []
    while True:
        print("-" * 100)
        temp = choice(res, obj_path)
        if not temp:
            break
        res, obj_path = temp


if __name__ == "__main__":
    main("twitter1.json")
