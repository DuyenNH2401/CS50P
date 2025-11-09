months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
while True:
    try:
        date = input("Dated: ")
        m, d, y = date.split("/")
        m, d, y = int(m), int(d), int(y)
        if  1 <= d <= 31 and 1 <= m <= 12:
            print(f"{y}-{m:02}-{d:02}")
            break
    except:
        try:
            m2, d2, y2 = date.split(" ")
            if d2[-1] == ",":
                d2 = d2.replace(",", "")
                if m2 in months and 1 <= int(d2) <= 31:
                    print(f"{int(y2)}-{months[m2]:02}-{int(d2):02}")
                    break
            pass
        except:
            pass