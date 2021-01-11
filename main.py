
import requests
from pprint import pprint

TOKEN = '....' # Ваш токен не работаел. сгенерил свой

OAUTH_URL = 'https://api.vk.com/method/'


class User:

    def __init__(self, id, token = TOKEN):
        self.token = token
        self.id = id

    def match_with_me(self):

        friend_id = input('Введите id пользователя: ')

        response = requests.get('https://api.vk.com/method/friends.getMutual',
                                params={
                                'access_token': TOKEN,
                                    'v': 5.122,
                                    'target_uid': friend_id
                                }
                                )

        pprint(response.json()["response"])

    def match_list(self, list):
        response = requests.get('https://api.vk.com/method/friends.getMutual',
                                params={
                                    'access_token': TOKEN,
                                    'v': 5.122,
                                    'target_uids': list
                                }
                                )

        pprint(response.json()["response"][0]['common_friends'])

    def my_friends(self):
        response = requests.get('https://api.vk.com/method/friends.get',
                                params={
                                    'access_token': TOKEN,
                                    'v': 5.122,
                                    'user_id': self.id
                                }
                                )

        pprint(response.json()['response']["items"])


    def print(self):
        print('http://vk.com/id'+str(self.id))

def both_friends(u1, u2):

    response1 = requests.get('https://api.vk.com/method/friends.get',
                            params={
                                'access_token': TOKEN,
                                'v': 5.122,
                                'user_id': u2.id
                            }
                            )

    response2 = requests.get('https://api.vk.com/method/friends.get',
                             params={
                                 'access_token': TOKEN,
                                 'v': 5.122,
                                 'user_id': u1.id
                             }
                             )

    u1_friends = response2.json()['response']["items"]
    u2_friends = response1.json()['response']["items"]

    result_list = list (set(u1_friends) & set(u2_friends))

    print(result_list)

def main():

    list = [182569464, 34362269]


    me = User(7545141, TOKEN)

    me.print()
    print('-----Друзья между мной и кем то по токену----')
    me.match_with_me()
    print('----Не особо понял как работает. ищет общих со списком-----')
    me.match_list(list)
    print('----Мои друзья------')
    me.my_friends()
    print('----------')
    print('----между двумя объектами класса------')

    vlad = User(182569464)
    misha = User(34362269)
    both_friends(vlad, misha)

main()