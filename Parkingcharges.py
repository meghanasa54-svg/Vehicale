RATES = {"two-wheeler": 20, "four-wheeler": 50, "heavy": 100}

def parking_fee(vehicle, hours):
    return RATES[vehicle.lower()] * hours

vehicle = input("Vehicle type (two-wheeler/four-wheeler/heavy): ")
number = input("vechicale number:")
hours = float(input("Parking duration (hours): "))
print("Vehicle type:", vehicle)
print("Duration:", hours, "hours")
print("Total fee: Rs.", parking_fee(vehicle, hours))