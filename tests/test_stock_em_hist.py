import akshare as ak


def test_stock_a_code():
    df_a_hist = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date="20170301", end_date='20211124',adjust="qfq")
    print(df_a_hist)


if __name__ == "__main__":
    test_stock_a_code()
