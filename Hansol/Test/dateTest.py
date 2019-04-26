import calendar

for mon in range(1, 13):
    strMon = ""
    strDay = ""
    if (len(str(mon)) == 1):
        strMon = "0" + str(mon)
    else:
        strMon = str(mon)

    endDay = calendar.monthrange(2018, mon)[1]
    print("------------------------------------------")
    print(strMon + "월의 마지막 날: " + str(endDay))
    print("------------------------------------------")
    for day in range(1, endDay + 1):
        if (len(str(day)) == 1):
            strDay = "0" + str(day)
        else:
            strDay = str(day)
        print("2018" + strMon + strDay)