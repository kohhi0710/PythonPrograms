
import python_bitbankcc

class BitBankPubAPI:

    def __init__(self):
        self.pub = python_bitbankcc.public()

    def get_ticker(self, pair):
        try:
            value = self.pub.get_ticker(pair)
            return value
        except Exception as e:
            print(e)
            return None

class BitBankPrvAPI:

    def __init__(self):
        API_KEY = 'BITBANK_API_KEY'
        API_SECRET = 'BITBANK_API_SECRET'
        self.prv = python_bitbankcc.private(API_KEY, API_SECRET)

    def get_asset(self):
        try:
            value = self.prv.get_asset()
            return value
        except Exception as e:
            print(e)
            return None

def main():
    pub_set = BitBankPubAPI()
    prv_set = BitBankPrvAPI()

    ticker = pub_set.get_ticker('btc_jpy')
    print(ticker['last'])

    asset_dict = prv_set.get_asset()
    print(asset_dict['assets'])

if __name__ == '__main__':
    main()
