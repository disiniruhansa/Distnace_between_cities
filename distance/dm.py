#Import necessary modules
from datetime import date, datetime
import random
import function as f  #Import a custom module names 'function' as 'f'
import sys

# DropMe price chart for traveling
price_chart = {
    'alvin': {'alvin': 0, 'jamz': 20, 'razi': 40, 'mali': 40, 'zuhar': 20},
    'jamz': {'alvin': 20, 'jamz': 0, 'razi': 20, 'mali': 40, 'zuhar': 40},
    'razi': {'alvin': 40, 'jamz': 20, 'razi': 0, 'mali': 20, 'zuhar': 40},
    'mali': {'alvin': 40, 'jamz': 40, 'razi': 20, 'mali': 0, 'zuhar': 20},
    'zuhar': {'alvin': 20, 'jamz': 40, 'razi': 40, 'mali': 20, 'zuhar': 0}
    }

#Promo codes and their corresponding discounts
promo_code = {
    "/pro1" : 1,
    "/pro2" : 2,
    "/pro3" : 3,
    "/pro4" : 4,
    "/pro5" : 5,
    "/pro6" : 6,
    "/pro7" : 7,
    "/pro8" : 8,
    "/pro9" : 9,
    "/pro10" : 10,
    "/pro11" : 11,
    "/pro12" : 12,
    "/pro13" : 13,
    "/pro14" : 14,
    "/pro15" : 15
}

#Vehicle types and their corresponding costs
vehicle = {
    "/c": 2,
    "/v": 3
}

#Print DropMe title
print("****Drop-Me****")
try:
    # If the user runs the program with the argument '/?', show available commands
    if len(sys.argv) == 2 and sys.argv[1] == '/?':
        print("* Keep a space between every command")
        print("* /price to show the price chart")
        print("* vehicle: </c> for car    </v> for van")
        print("* promo code: </pro2> 2KDM, <pro5> 5KDM, <pro10> 10KDM")
        print("* <city_name> <space> <city_name> To get the ride with a Trishaw")
        print("* <city_name> <space> <city_name> <space> </c> To get the ride with a chosen vehicle")
        print("* <city_name> <space> <city_name> <space> </v> To get the ride with a chosen vehicle")
        print("* <city_name> <space> <city_name> <space> </v> <space> <promo_code> to add a promo code")
        print("* <city_name> <space> <city_name> <space> <promo_code> <space> </vehicle_letter> to add a promo code")
        print("* Do not use <> brackets in commands")

    #If the user runs the program with the argument '/price', display the price chart
    elif len(sys.argv) == 2 and sys.argv[1] == '/price':
        #Print the price chart for traveling via Trishaw
        print("Price Chart for Traveling (Trishaw):\n")
        cities = list(price_chart.keys())
        header_row = ["Cities"] + cities

        print("\t".join(header_row))

        for city in cities:
            row = [city] + [str(price_chart[city][dest]) for dest in cities]
            print("\t".join(row))

        #Print the price chart for traveling via Car
        print("Price Chart for Traveling (Car):\n")
        cities = list(price_chart.keys())
        header_row = ["Cities"] + cities

        print("\t".join(header_row))

        for city in cities:
            row = [city] + [str(price_chart[city][dest]*2) for dest in cities]
            print("\t".join(row))

        #Print the price chart for traveling via Van
        print("Price Chart for Traveling (Van):\n")
        cities = list(price_chart.keys())
        header_row = ["Cities"] + cities

        print("\t".join(header_row))

        for city in cities:
            row = [city] + [str(price_chart[city][dest]*3) for dest in cities]
            print("\t".join(row))

    #If the user provides two city names as arguments, calculate the ride cost via Trishaw        
    elif len(sys.argv) == 3 and sys.argv[1].lower() in price_chart and sys.argv[2].lower() in price_chart:
        start = sys.argv[1].lower()
        end = sys.argv[2].lower()
        print(f.invoice(start,end))

    #If the user provides three arguments with a vehicle type or promo code, calculate the ride cost accordingly    
    elif len(sys.argv) == 4 and sys.argv[1].lower() in price_chart and sys.argv[2].lower() in price_chart:
        if sys.argv[3].lower() in vehicle:
            start = sys.argv[1].lower()
            end = sys.argv[2].lower()
            vehi = sys.argv[3].lower()
            print(f.invoice(start,end,vehi))
        elif sys.argv[3] in promo_code:
            start = sys.argv[1].lower()
            end = sys.argv[2].lower()
            vehi = ""
            promoc = sys.argv[3].lower()
            print(f.invoice(start,end,promoc))

    #If the user provides four arguments with a combination of vehicle type and promo code, calculate the cost        
    elif len(sys.argv) == 5 and sys.argv[1].lower() in price_chart and sys.argv[2].lower() in price_chart:
        if sys.argv[3].lower() in vehicle and sys.argv[4].lower() in promo_code:
            start = sys.argv[1].lower()
            end = sys.argv[2].lower()
            vehi = sys.argv[3].lower()
            promoc = sys.argv[4].lower()
            print(f.invoice(start,end,promoc,vehi))
        elif sys.argv[4].lower() in vehicle and sys.argv[3].lower() in promo_code:
            start = sys.argv[1].lower()
            end = sys.argv[2].lower()
            vehi = sys.argv[4].lower()
            promoc = sys.argv[3].lower()
            print(f.invoice(start,end,promoc,vehi))
    
    else:
        # If the user doesn't provide valid arguments, show the help message
        print("* Enter /? To show all the commands")
        
except :
    # If any error occurs during the execution, show the help message
    print("* Enter /? To show all the commands")
    
finally :
    # Print the DropMe title at the end
    print("****Drop-Me****")
