distance=float(input())
def calculate_taxi_fare(distance: float):
    if distance <=0:
        return float(0)
    elif distance <=1:
        return float(10000)
    elif distance <=10:
        return float(10000 + (distance-1)*14000)
    else:
        return float(10000 + 9*14000 + (distance-10)*12000)

print(calculate_taxi_fare(distance))