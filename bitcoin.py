from itertools import product, accumulate, groupby
 
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

class Bitcoin:
    def __init__(self):
        self.name=("Bitcoin price for 1/10 Morning")
        self.price =41735.30
        self.time=("11:34amEST")
        self.date=("January 10, 2022")
        pass
b1=Bitcoin()
b2=Bitcoin()
b3=Bitcoin()
b4=Bitcoin()
print(b1.name)
print(b2.price)
print(b3.time)
print(b4.date)

#numbers in millions
continents = [28, 24, 38, 160, 1, 32, 24]
global_crypto_adoption_2021 = accumulate(continents)
print(list(global_crypto_adoption_2021))
#stats presented by 1ml.com/statistics For 1/10/22 2:45EST
class Lightning():
    def __init__(self):
        self.nodes = 32610
        self.nodeswactivechannels = 19239
        self.nodeswpublicIP = 14459
        self.avergenodecapacity = 0.173 #BTC
        self.avgnodeageindays = 411.7
        self.channels = 84966
        self.newnodes = 72
        self.updatednodes = 10700
        self.avgchannelcapacity = 0.039 #BTC
        self.avgchanncelageindays = 277.7
        self.TorOnionservicenodes = 11399
        self.networkcapacity = 3334.43 #BTC
        self.newchannels = 312
        self.updatedchannels = 76669
        self.Layer1CapacityRatio = 0.015878
        self.avgchannelspernode = 8.83
        self.medianbasefee = 1.0000000 #sat
        self.nodecountdown = 967390
        self.channelcountdown = 915034
        self.capacitycountdown = 996666
        self.medianfeerate = 0.000038 #sat
        pass
l1 = Lightning()
l2 = Lightning()
l3 = Lightning()
l4 = Lightning()
l5 = Lightning()
l6 = Lightning()
l7 = Lightning()
l8 = Lightning()
l9 = Lightning()
l10 = Lightning()
l11 = Lightning()
l12 = Lightning()
l13 = Lightning()
l14 = Lightning()
l15 = Lightning()
l16 = Lightning()
l17 = Lightning()
l18 = Lightning()
l19 = Lightning()
l20 = Lightning()
l21 = Lightning()
print(l1.nodes)
print(l2.nodeswactivechannels)
print(l3.nodeswpublicIP)
print(l4.avergenodecapacity)
print(l5.avgnodeageindays)
print(l6.channels)
print(l7.newnodes)
print(l8.updatednodes)
print(l9.avgchannelcapacity)
print(l10.avgchanncelageindays)
print(l11.TorOnionservicenodes)
print(l12.networkcapacity)
print(l13.newchannels)
print(l14.updatedchannels)
print(l15.Layer1CapacityRatio)
print(l16.avgchannelspernode)
print(l17.medianbasefee)
print(l18.nodecountdown)
print(l19.channelcountdown)
print(l20.capacitycountdown)
print(l21.medianfeerate)
node_capacity_Jan_8th = [{'Average':'price in sats', 'Price': 34537467}, {'90th percentile':'price in sats','Price':26857215}, {'50th percentile':'price in sats', 'Price':470000}, {'10th percentile':'price in sats', 'Price':50000}]
sat_price = groupby(node_capacity_Jan_8th, key= lambda x:x['Price'])
for key, value in sat_price:
    print(key, list(value))
#https://dcabtc.com/
weekly_Dca_btc_5years = [{'$1 every week for 5 years':848, 'ROI percentage':440.35},{'$10 every week for 5 years':8483, 'ROI percentage':440.35}, {'$100 every week for 5 years':84835, 'ROI percentage':440.35}]
week_grp = groupby(weekly_Dca_btc_5years, key= lambda x:x['ROI percentage'])
for key, value in week_grp:
    print(key, list(value))
HUNDRED_every_two_weeks_dca_btc = [{'6 months':2935, 'ROI percentage':125.84},{'1 year':3315, 'ROI percentage':22.81},{'2 years':26624, 'ROI percentage':402.34},{'3 years':42376, 'ROI percentage':436.41}]
every_two_weeks_grp = groupby(HUNDRED_every_two_weeks_dca_btc, key= lambda x:x['ROI percentage'])
for key, value in every_two_weeks_grp:
    print(key, list(value))
monthly_dca1 = [{'Amount invested':100, '6 months':965, 'ROI percentage':60.94}, {'Amount invested':100, '1 year':1384, 'ROI percentage':15.39}, {'Amount invested':100, '2 years':5740, 'ROI percentage':139.20}, {'Amount invested':100, '3 years':19688, 'ROI percentage':446.90}]
grp = groupby(monthly_dca1, key= lambda x:x['Amount invested'])
for key, value in grp:
    print(key, list(value))
monthly_dca2 = [{'Amount':500, '6 months':4828, 'ROI':60.94}, {'Amount':500, '1 year':6923, 'ROI':15.39}, {'Amount':500, '2 years':28703, 'ROI':139.20}, {'Amount':500, '3 years':98441, 'ROI':446.90}]
grp2 = groupby(monthly_dca2, key= lambda x:x['Amount'])
for key, value in grp2:
    print(key, list(value))
monthly_dca3 = [{'Amount':1000, '6 months':9656, 'ROI':60.94}, {'Amount':1000, '1 year':13846, 'ROI':15.39}, {'Amount':1000, '2 years':57407, 'ROI':139.20}, {'Amount':1000, '3 years':196882, 'ROI':446.90}]
grp3 = groupby(monthly_dca3, key= lambda x:x['Amount'])
for key, value in grp3:
    print(key, list(value))

class btc_metrics():
    def __init__(self) -> None:
        self.price = 41794.50
        self.marketcap = 788789702379
        self.marketcapdominance = 38.77
        self.tradingvolume = 27785329725
        self.volumemarketcap = 0.0351
        self.todaylow = 39692.03 #also known as 24h
        self.todayhigh = 42893.60
        self.weeklow = 40655.25
        self.weekhigh = 47507.69
        self.marketcaprank = 1
        self.alltimehigh = 69044.77 #November 10,2021
        self.alltimelow = 67.81 #July 6,2013
        pass
m1 = btc_metrics()
m2 = btc_metrics()
m3 = btc_metrics()
m4 = btc_metrics()
m5 = btc_metrics()
m6 = btc_metrics()
m7 = btc_metrics()
m8 = btc_metrics()
m9 = btc_metrics()
m10 = btc_metrics()
m11 = btc_metrics()
m12 = btc_metrics()
print(m1.price)
print(m2.marketcap)
print(m3.marketcapdominance)
print(m4.tradingvolume)
print(m5.volumemarketcap)
print(m6.todaylow)
print(m7.todayhigh)
print(m8.weeklow)
print(m9.weekhigh)
print(m10.marketcaprank)
print(m11.alltimehigh)
print(m12.alltimelow)

