import os, pandas

def is_consolidating(df, percentage=2):
    recent_candlesticks = df[-15:]
    print(recent_candlesticks)

    max_close = recent_candlesticks['close'].max()
    min_close = recent_candlesticks['close'].min()

    threshold = 1 - (percentage / 100)

    if min_close > (max_close * threshold):
        return True

    return False

def is_breakingout(df, percentage=2.5):
    last_close = df[-1:]['close'].values()

    if is_consolidating(df[:-1]):
        recent_close = df[-16:-1]

        if last_close > recent_close['close'].max():
            return True

    return False


for filename in os.listdir('datasets/daily'):
    df = pandas.read_csv('datasets/daily/{}'.format(filename))


    if is_consolidating(df):
        print("{} is consolidating".format(filename))