from itertools import product
 
def btcvseth(eth, btc):
 
    return list(product(eth, btc))
   
# BTC vs ETH since Dec. 31st 2017(descending from 2021-2017)
#Based on yearly closes, using Yahoo Finance
if __name__ == "__main__":
    eth = [3682.63, 737.80, 129.61,133.37, 756.73]
    btc = [48023, 28956, 7182, 3741, 13860]
    print(btcvseth(eth, btc))
Bitcoin_Birthday = "Genesis block was mined January 3,2009"
if(Bitcoin_Birthday == "Genesis block was mined January 3,2009"):
    print("HAPPY BIRTHDAY BITCOIN") #today is January 4, 

