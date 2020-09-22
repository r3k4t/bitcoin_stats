
#!/usr/bin/python
#Author : Rahat Khan Tusar(RKT)
#Github : https://github.com/r3k4t
#Now start coding
import os
import sys
import blockchain
import time
from blockchain import  statistics

# get the stats object

stats = statistics.get()
os.system("clear")
print ("             SssssssssssssssssssssssS")
print ("               Bitcoin  Statistics")
print ("             SssssssssssssssssssssssS")
print
time.sleep(5)
print
time.sleep(1)

#get and print Bitcoin trade volume

print ("Bitcoin Trade Volume :%s\n"% stats.trade_volume_btc)
time.sleep(1)

# get and print Bitcoin mined

print ("Bitcoin mined: %s\n" % stats.btc_mined)
time.sleep(1)
print ("Bitcoin market price: %s\n" % stats.market_price_usd)
time.sleep(1)

# get and print Bitcoin market price in usd

print ("Author : Rahat Khan Tusar(RKT)")
print ("Github : https://github.com/r3k4t")

