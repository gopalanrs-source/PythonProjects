squared = lambda x: x**2
print(squared(5))


add_next_100_strike = lambda x : x+100
print(add_next_100_strike(21500))

CE_strikes = []
PE_strikes = []


def get_CE_PE_strike(spot_price):
    print(f"Spot price is {spot_price}")
    strike_level = round(spot_price / 100) * 100
    # global CE_strikes, PE_strikes
    global CE_strikes, PE_strikes
    CE_strikes = [strike_level-100, strike_level, strike_level+100, strike_level+200] # deep itm, itm, otm1, otm2
    PE_strikes = [strike_level+100, strike_level, strike_level-100, strike_level-200] # deep itm, itm, otm1, otm2
    print(f"CE strikes are {CE_strikes}")
    print(f"PE strikes are {PE_strikes}")
    return CE_strikes, PE_strikes


print(get_CE_PE_strike(21551))

