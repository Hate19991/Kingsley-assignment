print("which bus-top are you highlighting\nIkeja - 200\negbeda - 300\nIpaja - 400")

Stop = input("input text here (your location)>>  ")
Ikeja = 200
Egbeda = 300
Ipaja = 400

if Stop == 'egbeda' or Stop == "1":
    print(f"{Stop} highlighted get ready to drop")
    print("how much money do you have")
    balance = int(input("amount here >>  "))
    if balance >= Egbeda:
        print("okay you may board now")
        total = balance - Egbeda
        print(f"Your change is {total}")
        exit()
    elif balance > 1000:
        print("not enough spare change")
        exit()
    elif balance < Egbeda:
        print("you may not board the bus")
        exit()
    else:
        print("get Lost")
        exit()
        
if Stop == 'ipaja' or Stop == "3":
    print(f"{Stop} highlighted get ready to drop")
    print("how much money do you have")
    balance = int(input("amount here >>  "))
    if balance >= Ipaja:
        print("okay you may board now")
        total = balance - Ipaja
        print(f"Your change is {total}")
        exit()
    elif balance > 1000:
        print("not enough spare change")
        exit()
    elif balance < Ipaja:
        print("you may not board the bus")
        exit()
    else:
        print("get Lost")
        exit()
        
if Stop == 'ikeja' or Stop == "2":
    print(f"{Stop} highlighted get ready to drop")
    print("how much money do you have")
    balance = int(input("amount here >>  "))
    if balance >= Ikeja:
        print("okay you may board now")
        total = balance - Ikeja
        print(f"Your change is {total}")
        exit()
    elif balance > 1000:
        print("not enough spare change")
        exit()
    elif balance < Ikeja:
        print("you may not board the bus")
        exit()
    else:
        print("get Lost")
        exit()
    


