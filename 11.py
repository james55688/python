def get_constellation(month, date):
    dates = [21, 19, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22]
    constellations = ["摩羯座(Capricorn)", "水瓶座(Aquarius)", "雙魚座(Pisces)", "牡羊座(Aries)", "金牛座(Taurus)", "雙子座(Gemini)", "巨蟹座(Cancer)", "獅子座(Leo)", "處女座(Virgo)", "天秤座(Libra)", "天蝎座(Scorpio)", "射手座(Sagittarious)", "摩羯座(Capricorn)"]
    if date < dates[month-1]:
        return constellations[month-1]
    else:
        return constellations[month]

m = int(input("請輸入月份:"))
d = int(input("請輸入日期:"))

print ((get_constellation(m,d)))