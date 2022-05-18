candles = int(input())

heights_candle = list(map(int, input().split()))

print(heights_candle.count(max(heights_candle)))