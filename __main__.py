# imports
import time

IS_SKUPLT = False

try:
    from csinsc import Colour as Color
    from csinsc import Highlight, Style

    IS_SKUPLT = True
except:
    # Copied from csinsc\__init__.py
    # Source available: https://github.com/toanh/csinsc

    class Color: # correct spelling from original
        grey = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        yellow = '\033[93m'
        blue = '\033[34m'
        magenta = '\033[35m'
        pink = '\033[35m'
        cyan = '\033[36m'
        white = '\033[37m'
        orange = '\033[33m'
        # TODO: fix black
        black = '\033[30m'
        reset = '\033[0m'


    class Highlight:
        grey = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        yellow = '\033[103m'
        blue = '\033[44m'
        magenta = '\033[45m'
        pink = '\033[45m'
        cyan = '\033[46m'
        orange = '\033[43m'
        # TODO: fix black
        black = '\033[40m'
        white = '\033[47m'


    class Style:
        bold = '\033[1m'
        dark = '\033[2m'
        underline = '\033[4m'
        blink = '\033[5m'
        reverse = '\033[7m'
        concealed = '\033[8m'

    def clear():
        print("\033c", end="")
        
# constants

class AsciiArt:
    WELCOME = r''' __          __  _                          _ 
 \ \        / / | |                        | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)'''
    MENU = r'''  __  __                  
 |  \/  |                 
 | \  / | ___ _ __  _   _ 
 | |\/| |/ _ \ '_ \| | | |
 | |  | |  __/ | | | |_| |
 |_|  |_|\___|_| |_|\__,_|'''
    ORDER = r'''   ____          _           
  / __ \        | |          
 | |  | |_ __ __| | ___ _ __ 
 | |  | | '__/ _` |/ _ | '__|
 | |__| | | | (_| |  __| |   
  \____/|_|  \__,_|\___|_|'''
    RECEIPT = r'''  _____               _       _   
 |  __ \             (_)     | |  
 | |__) |___  ___ ___ _ _ __ | |_ 
 |  _  // _ \/ __/ _ | | '_ \| __|
 | | \ |  __| (_|  __| | |_) | |_ 
 |_|  \_\___|\___\___|_| .__/ \__|
                       | |        
                       |_|'''

class Keyboard:
    RETURN = "RETURN ⏎"


MENU_ITEMS: list = [
    {
        "name": "Chicken ramen",
        "price": 12,
        "variables": [
            {
                "name": "Noodles",
                "options": [
                    {
                        "name": "More noodles",
                        "price": 2
                    },
                    {
                        "name": "Less noodles",
                        "price": 0
                    },
                    {
                        "name": "Regular noodles",
                        "price": 0
                    }
                ]
            },
            {
                "name": "Salt",
                "options": [
                    {
                        "name": "Less salt",
                        "price": 0
                    },
                    {
                        "name": "No salt",
                        "price": 0
                    },
                    {
                        "name": "Regular salt",
                        "price": 0
                    }
                ]
            }
        ]
    },
    {
        "name": "Chicken sushi",
        "price": 4,
        "variables": [
            {
                "name": "Extra",
                "options": [
                    {
                        "name": "Extra roll",
                        "price": 2
                    },
                    {
                        "name": "2 Extra rolls",
                        "price": 4
                    },
                    {
                        "name": "3 Extra rolls",
                        "price": 6
                    },
                    {
                        "name": "4 Extra rolls",
                        "price": 8
                    },
                    {
                        "name": "No extra",
                        "price": 0
                    }
                ]
            },
            {
                "name": "Soy sauce",
                "options": [
                    {
                        "name": "Add soy sauce",
                        "price": 0.50
                    },
                    {
                        "name": "No soy sauce",
                        "price": 0
                    }
                ]
            }
        ]
    },
    {
        "name": "Udon",
        "price": 12,
        "variables": [
            {
                "name": "Noodles",
                "options": [
                    {
                        "name": "More noodles",
                        "price": 2
                    },
                    {
                        "name": "Less noodles",
                        "price": 0
                    },
                    {
                        "name": "Regular noodles",
                        "price": 0
                    }
                ]
            },
            {
                "name": "Salt",
                "options": [
                    {
                        "name": "Less salt",
                        "price": 0
                    },
                    {
                        "name": "No salt",
                        "price": 0
                    },
                    {
                        "name": "Regular salt",
                        "price": 0
                    }
                ]
            }
        ]
    },
    {
        "name": "Katsu curry",
        "price": 8,
        "variables": [
            {
                "name": "Curry",
                "options": [
                    {
                        "name": "More curry",
                        "price": 2.50
                    },
                    {
                        "name": "Regular curry",
                        "price": 0
                    }
                ]
            }
        ]
    },
    {
        "name": "Drink",
        "price": 3.50,
        "variables": [
            {
                "name": "Drink",
                "options": [
                    {
                        "name": "Coke",
                        "price": 0
                    },
                    {
                        "name": "Pepsi",
                        "price": 0
                    },
                    {
                        "name": "Fanta",
                        "price": 0
                    },
                    {
                        "name": "Sprite",
                        "price": 0
                    },
                    {
                        "name": "Water",
                        "price": 0
                    }
                ]
            }
        ]
    }
]

# logic

user_order = []

def print_menu() -> None:
    # get longest item name
    item_longest_name: int = 0
    for menu_item in MENU_ITEMS:
        # if item name is longer than before then overwrite the variable
        if len(menu_item["name"]) > item_longest_name: item_longest_name = len(menu_item["name"])
    
    # for loop iter-ing over array dosent include count
    i: int = 0
    for menu_item in MENU_ITEMS:
        # add 1 to iteration count
        i += 1
        # does not look orange on my machine wtf
        print(Color.orange + "[" + str(i) + "] " + Color.reset, end="")
        print(Color.cyan + menu_item["name"] + " " * (item_longest_name - len(menu_item["name"])), end="")
        print(" " * 5, end="")
        # format currency into correct format
        print(Color.green + "$" + "{:,.2f}".format(menu_item["price"]) + Color.reset)

def print_menu_fancy() -> None:
    # literally just an extra print statement before the actual menu
    print(Color.magenta + AsciiArt.MENU + Color.reset + "\n")
    print_menu()

def select_menu_item(index: int) -> None:
    clear()
    # get the menu item from list
    selected_menu_item = MENU_ITEMS[index]

    user_order_item = [index]

    # show variables
    for variable in selected_menu_item["variables"]:
        clear()
        # fancy shit
        print(Color.magenta + AsciiArt.ORDER + Color.reset + "\n")
        print(Color.magenta + "You need to select your food options!" + Color.reset + "\n")

        print(Color.magenta + variable["name"] + Color.reset)

        longest_option_name: int = 0

        # check longest
        for option in variable["options"]:
            if len(option["name"]) > longest_option_name: longest_option_name = len(option["name"])

        i: int = 0
        for option in variable["options"]:
            i += 1
            # do the actual print
            print(Color.orange + "[" + str(i) + "] " + Color.reset, end="")
            print(Color.cyan + option["name"] + " " * (longest_option_name - len(option["name"])), end="")
            print(" " * 5, end="")
            # format currency into correct format
            print(Color.green + "+ $" + "{:,.2f}".format(option["price"]) + Color.reset)
        
        print(Color.magenta + "What " + variable["name"].lower() + " would you like?" + Color.reset)
        user_input = input("> ")
        try:
            user_input_parsed = int(user_input)
        except:
            clear()
            print(Color.red + "Invalid input!" + Color.reset)
            time.sleep(1)
            return

        if user_input_parsed < 1 or user_input_parsed > len(variable["options"]):
            clear()
            print(Color.red + "Invalid input!" + Color.reset)
            time.sleep(1)
            return
        
        user_input_parsed = user_input_parsed - 1

        user_order_item.append(user_input_parsed)

    user_order.append(user_order_item)
    
def main() -> None:
    # splash screen type thing
    print(Color.magenta + AsciiArt.WELCOME + Color.reset + "\n")
    print("Ready to order? Press " + Color.green + Keyboard.RETURN + Color.reset)
    input()
    # menu part
    while True:
        clear()
        print_menu_fancy()
        print(Color.magenta + "Input number or [q] to finish this order" + Color.reset)
        # retrive user input
        user_input = input("> ")
        if user_input == "q": break
        else:
            # convert to type int
            try:
                user_input_parsed = int(user_input)
            except:
                clear()
                print(Color.red + "Invalid input!" + Color.reset)
                time.sleep(1)
                continue

            # check if in range
            if user_input_parsed < 1 or user_input_parsed > len(MENU_ITEMS):
                clear()
                print(Color.red + "Invalid input!" + Color.reset)
                time.sleep(1)
                continue

            select_menu_item(user_input_parsed - 1)
            
    # receipt time!
    clear()
    print(Color.magenta + AsciiArt.RECEIPT + Color.reset + "\n")
    print(Color.magenta + "Thanks for ordering!" + Color.reset + "\n")

    longest_receipt_name: int = 0

    # check longest
    for item in user_order:
        # get the item's name
        name = MENU_ITEMS[item[0]]["name"]
        variable_names = []

        for variable in MENU_ITEMS[item[0]]["variables"]:
            i: int = -1
            for option in variable["options"]:
                i += 1
                variable_names.append(option["name"])
        
        if longest_receipt_name < len(name): longest_receipt_name = len(name)
        for namel in variable_names:
            if longest_receipt_name < len(namel): longest_receipt_name = len(namel)

    final_price = []
    for item in user_order:
        item_main = MENU_ITEMS[item[0]]
        print(Color.cyan + item_main["name"] + " " * (longest_receipt_name - len(item_main["name"])), end="  ")
        print(Color.green + "$" + "{:,.2f}".format(item_main["price"]) + Color.reset)
        final_price.append(item_main["price"])
        j: int = -1
        for item_extra in item[1:]:
            j += 1
            item_extra = MENU_ITEMS[item[0]]["variables"][j]["options"][item[j+1]]
            print(Color.cyan + item_extra["name"] + " " * (longest_receipt_name - len(item_extra["name"])), end="  ")
            print(Color.green + "$" + "{:,.2f}".format(item_extra["price"]) + Color.reset)
            final_price.append(item_extra["price"])
        print()

    print(Color.cyan + "TOTAL" + " " * (longest_receipt_name - len("TOTAL")), end="  ")
    print(Color.green + "$" + "{:,.2f}".format(sum(final_price)) + Color.reset)

if __name__ == "__main__":
    # clear the screen for my machine
    clear()
    main()
