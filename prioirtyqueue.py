prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

print prices['IBM']

price_item = zip(prices.values(),prices.keys())

price_item.sort(reverse=True)
for i in xrange(2):
    print price_item[i][1]


x= "world"
cnt = 0
for i in x :
    cnt += 1
print cnt