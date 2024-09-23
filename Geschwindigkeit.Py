kmh = 1
kmh_to_mph = 0.621371
for kmh in range(0, 101, 5):
    mph = kmh * kmh_to_mph
print(f"{kmh} km/h sind {mph:.2f} mp/h")

