#Import necessary modules
import random
from datetime import date, datetime
import os

#Price chart for traveling between
price_chart = {
    'alvin': {'alvin': 0, 'jamz': 20, 'razi': 40, 'mali': 40, 'zuhar': 20},
    'jamz': {'alvin': 20, 'jamz': 0, 'razi': 20, 'mali': 40, 'zuhar': 40},
    'razi': {'alvin': 40, 'jamz': 20, 'razi': 0, 'mali': 20, 'zuhar': 40},
    'mali': {'alvin': 40, 'jamz': 40, 'razi': 20, 'mali': 0, 'zuhar': 20},
    'zuhar': {'alvin': 20, 'jamz': 40, 'razi': 40, 'mali': 20, 'zuhar': 0}
    }

# Promo codes and their corresponding discounts
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

#Function to save the invoice details to a text file
def save(start,end,first_price,promo,random_reduct,price):
    fn = date.today()
    if not os.path.exists("invoices"):
        os.makedirs("invoices")
    filename = datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f") + ".txt"
    file_path = os.path.join("invoices", filename)

    with open(file_path, "w") as f:
        f.write("Date               : " + str(date.today()) + "\n")
        f.write("Time               : " + datetime.now().strftime("%H:%M:%S") + "\n")
        f.write("Start              : " + start + "\n")
        f.write("End                : " + end + "\n")
        f.write("Amount             : " + str(first_price) +" KMD" + "\n")
        f.write("Promo              : " + str(promo) +" KMD" + "\n")
        f.write("Random Reduction   : " + str(random_reduct) +" KMD" + "\n")
        f.write("Final Payment      : " + str(price) +" KMD" + "\n")
        f.write("\n")
        f.close()
    pass


#Function to calculate the invoice details based on start and end cities, promo code, and vehicle type
def invoice_cal(start, end, promoc=None, vehi=None):
    amount = price_chart[start][end] * vehicle[vehi] if vehi in vehicle else price_chart[start][end]
    prom = promo_code[promoc] if promoc in promo_code else 0
    ran = random.choice([5, 0]) if not prom else 0
    famount = amount - prom - ran
    return amount, prom, ran, famount


#Function to generate the invoice and save it to a file
def invoice(start, end, promoc=None, vehi=None):
    amount, prom, ran, famount = invoice_cal(start, end, promoc, vehi)
    save(start,end,amount,prom,ran,famount)
    print("Start            : ", start)
    print("End              : ", end)
    print("Amount           : ", amount, " KMD")
    print("Promo            : ", prom, " KMD")
    print("Random Reduct    : ", ran, " KMD")
    print("Final Amount     : ", famount, " KMD")
    return
