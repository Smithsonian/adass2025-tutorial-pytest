#  --- Exercise ---
#  See test_temperature_ex.py for instructions
def classify_temperature(temp_c):
    if temp_c < 0:
        return "freezing"
    elif temp_c < 20:
        return "cold"
    elif temp_c < 30:
        return "warm"
    else:
        return "hot"
