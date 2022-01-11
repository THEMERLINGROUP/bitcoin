from itertools import groupby, accumulate
#liquidity stats
def liquidity():
    return "Selling asset for cash OR REKT"
liquidity()
rekt_inmillions = [{'Time':'1 hour', 'Price':3.99}, {'Time':'4 hour', 'Price':5.81}, {'Time':'12 hour', 'Price':35.55}, {'Time':'24 hours', 'Price':122.69}]
rekt = groupby(rekt_inmillions, key=lambda x:x['Time'])
for key, value in rekt:
    print(key, list(value))
highest_long_in_millions_total = [54.84, 494.58, 438.35, 169.93, 82.32, 85.8, 112.13, 141.63] #1.58 billion
acc = accumulate(highest_long_in_millions_total)
print(list(acc))
longs_btc_in_millions_this_year = [{'Date':'1/9/22', 'Long':249.99}, {'Date':'1/8/22', 'Long':'45.41'}, {'Date':'1/7/22', 'Long':217.28}, {'Date':'1/6/22', 'Long':416.02}, {'Date':'1/5/22', 'Long':186.99}, {'Date':'1/4/22', 'Long':637.68}, {'Date':'1/3/22', 'Long':116.5}, {'Date':'1/2/22', 'Long':98.06}, {'Date':'1/1/22', 'Long':39.34}]
longs = groupby(longs_btc_in_millions_this_year, key=lambda x:x['Long'])
for key, value in longs:
    print(key, list(value))
highest_longs = [{'Date':'12/3/21', 'Price':'$1.58 billion'}, {'Date':'11/15/21', 'Price':'$792.78 million'}, {'Date':'1/4/22', 'Price':'637.68 million'}, {'Date':'11/25/21', 'Price':'661.41 million'}, {"Date":'11/9/21', 'Price':'613.37 million'}, {'Date':'10/26/21', 'Price':'764.81 million'}]
high = groupby(highest_longs, key=lambda x:x['Price'])
for key, value in high:
    print(key, list(value))
highest_shorts_in_millions = [{'Date':'12/22/21', 'Short':162.55}, {"Date":"12/5/21", 'Short':'214.18 million'}, {'Date':'12/3/21', 'Short':437.26}, {'Date':'11/7/21', 'Short':248.91}, {'Date':'11/1/21', 'Short':185.38}, {'Date':'10/19/21', 'Short':221.16}]
short = groupby(highest_shorts_in_millions, key=lambda x:x['Short'])
for key, value in short:
    print(key, list(value))
    