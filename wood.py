import requests
import random

url = 'https://woodwood.us4.list-manage.com/subscribe?u=2e511c179057ba062952a96e8&id=a54d6bfae0'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def wood_wood_raffle():
    for number in range(1,10000):
        info = {
            'MERGE0': 'email+{}@gmail.com'.format(random.randint(1,10000)),  # email, don't change end
            'MERGE1': 'Joe',  # first name
            'MERGE2': 'Shmoe',  # last name
            'MERGE4': '6062892345',  # phone number
            'MERGE3': '03.5 UK / 36 EU',  # 3 digits for UK size and 2 for EU
            'MERGE6': 'woodwood.com',  # don't change
            'MERGE5': 'United States of America',  # country fully typed out
            'gdpr[469]': "Y"  # don't change
        }

        req = requests.post(url, data=info, headers=headers, timeout=8)

        if req.status_code == 200:
            print('Raffle Entry Successful:' + str(number))
        else:
            print('Raffle Entry Unsuccessful')


if __name__ == '__main__':
    wood_wood_raffle()
