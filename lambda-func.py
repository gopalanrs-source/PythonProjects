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

num = 2

def funcbuilder(x):
    return lambda num: num+x

add_10 = funcbuilder(10)
add_20 = funcbuilder(20)

print(add_10(5))
print(add_20(5))

number = [3,7,12,18, 20,21]

squared_numbers = list(map(lambda x: x**2, number))
print(squared_numbers)


odd_num = list(filter(lambda n:n%2 !=0,number))
print(odd_num)

from functools import reduce
from statistics import mean


#cbse results calculation
scores = sorted([96,88,90,99,85,99])
print(scores)
total = reduce(lambda acc, curr: acc+curr, scores[1:]) # for top 5 marks
print(total)
average_score = mean(scores)         
# print(total)
print(average_score)


names = ["Alice Wonderland", "Bob Marley", "Charlieze Theron", "David E Kelly", "Eve"]

char_count = reduce(lambda acc, name: acc+len(name), names,0)
print(char_count)