#Courtesy of Coingecko
def btc24hourcandleseveryhalfhour():
    yield 41706.94
    yield 41475.03
    yield 41325.59
    yield 41348.51
    yield 41903.98
    yield 41779.55
    yield 40897.02
    yield 40935.16
    yield 40859.31
    yield 39870.85
    yield 40896.52
    yield 40892.65
    yield 41043.50
    yield 41511.57
    yield 41632
    yield 41895.44
    yield 42032.78
    yield 41907.31
    yield 41972.60
    yield 41845.50
    yield 41942.18
    yield 42089.72
    yield 42039.88
    yield 41981.79
    yield 41944.17
    yield 42040.80
    yield 42244.23
    yield 42409.44
b = btc24hourcandleseveryhalfhour()
for i in b:
    print(i)

def btcmonthlycandles():
    yield 43216.46
    yield 47387.21
    yield 47303.56
    yield 56208.27
    yield 61661.36
    yield 61837.26
    yield 54711.87
    yield 47777.76
    yield 44802.61
    yield 49338.78
    yield 42802.14
    yield 41936.26
    yield 33704.54
    yield 33950.79
    yield 36903.30
    yield 35834.47
    yield 56507.76
    yield 56600.75
    yield 59979.39
    yield 59060.03
    yield 49019.37
    yield 48532.24
    yield 39279.41
    yield 34199.52
    yield 38397.90
g = btcmonthlycandles()
thismonthvalue = next(g)
print(thismonthvalue)

btc_recent_history_by_percentage = {'Last hour':1, '24 hours':-1.6, '7 days':-12, '14 days':-18, '30 days':-11.39, '1 year':3.5}

def btc_dec31price_since_2011():
    yield 48023
    yield 28956
    yield 7182
    yield 3741
    yield 968
    yield 430
    yield 320
    yield 757
    yield 14
    yield 5
p = btc_dec31price_since_2011()
for i in p:
    print(i)
