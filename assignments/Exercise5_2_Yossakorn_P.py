Distance = float(input("ระยะทาง : "))
DisUnit = int(input("หน่วยเระยะทาง: '1.เมตร' '2.กิโลเมตร' : "))
Time = float(input("เวลา : "))
TimeUnit = int(input("หน่วยเวลา '1.วินาที' '2.ชั่วโมง' : "))

if DisUnit == 1 and TimeUnit == 1:
    result = Distance / Time
    print("อัตราเร็ว = ", result , "m/s")

if DisUnit == 1 and TimeUnit == 2:
    Time *= 3600
    result = Distance / Time
    print(print("อัตราเร็ว = ", result , "m/s"))

if DisUnit == 2 and TimeUnit == 2:
    result = Distance / Time
    print("อัตราเร็ว = ", result, "km/h")

if DisUnit == 2 and TimeUnit == 1:
    Time /= 3600
    result = Distance / Time
    print("อัตราเร็ว = ", result, "km/h")