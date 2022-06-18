import requests
import json

def LoadMemes():
    with open('data.json') as json_file:
        return json.load(json_file)

def SaveMemes(items):
    with open('data.json', 'w') as f:
        json.dump(items, f)
        
def GetMemes():
    requestUrl = 'https://api.vk.com/method/photos.get'
    params = {
        'access_token' : '5f5c7f525f5c7f525f5c7f52775f216b4955f5c5f5c7f523df1cccfcf21aeb029daceaa',
        'owner_id' : -197700721,
        'album_id' : 284717200,
        'extended' : 1,
        'v' : 5.131
    }

    response = requests.post(requestUrl, params=params)
    items = response.json()['response']['items']
    SaveMemes(items)
    return items

def GetLotsOfMemes():
    memes = GetMemes()

    requestUrl = 'https://api.vk.com/method/photos.get'

    for i in range(1, 6):
        params = {
            'access_token' : '5f5c7f525f5c7f525f5c7f52775f216b4955f5c5f5c7f523df1cccfcf21aeb029daceaa',
            'owner_id' : -205359325,
            'album_id' : "wall",
            'extended' : 1,
            'count' : 100 * i,
            'offset': 100 * (i - 1),
            'v' : 5.131
        }

        response = requests.post(requestUrl, params=params)

        memes += response.json()['response']['items']

    SaveMemes(memes)


def WatchMemes():
    memes = LoadMemes()

    print(f'Всего мемов: {len(memes)}\n\n')

    action = input('All: skip/like/...: ')    

    if action == 'skip':
        SaveMemes(memes)
        return

    if action == 'likes':
        for i in range(len(memes)):
            memes[i]['likes']['count'] += 1
        SaveMemes(memes)
        return

    for i in range(len(memes)):
        print(f'Дата: {memes[i]["date"]}; Автор: {memes[i]["user_id"]}; Лайки: {memes[i]["likes"]["count"]}')
        print(f'{memes[i]["sizes"][-1]["url"]}\n')

        action = input('like/...: ',)

        if action == 'like':
            memes[i]['likes']['count'] += 1
            print(f'\tЛайки: {memes[i]["likes"]["count"]}')
            SaveMemes(memes)


'''
    Во время первого запуска нужно использовать следующую функцию: GetMemes()
    Для просмотра мемов использовать: WatchMemes() - во время выполнения доступны следующие команды:
    1) skipAll - пропустить все мемы
    2) likeAll - лайкнуть все мемы
    3) skip - пропустить мем
    4) like - лайкнуть мем
    ВНИМАНИЕ!!! любое действие не из перечня - ничего не делает

    Все записи можно найти в "data.json"
'''
# GetMemes() # Задание 1 (10 баллов)
# GetLotsOfMemes() Задание 4 (40 баллов)
WatchMemes() # Задание 2 (20 баллов)