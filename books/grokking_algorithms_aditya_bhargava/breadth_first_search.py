from collections import deque


cities = dict()
cities['Moscow'] = ['Khimki', 'Podolsk', 'Lubertsi']
cities['Khimki'] = []
cities['Ramenskoye'] = ['Kolomna', 'Lubertsi', 'Noginsk']
cities['Krasnodar'] = ['Ramenskoye']
cities['Noginsk'] = []
cities['Kolomna'] = []
cities['Lubertsi'] = ['Ramenskoye', 'Noginsk']
cities['Podolsk'] = ['Domodedovo']
cities['Domodedovo'] = ['Ramenskoye', 'Moscow']


def bfs(graph, city_for_search):
    search_queue = deque()
    search_queue += graph['Moscow']
    searched = []
    while search_queue:
        city = search_queue.popleft()
        if city not in searched:
            if city == city_for_search:
                print(f'Yes. Delivery from Moscow to {city_for_search} is available.')
                return True
            else:
                search_queue += graph[city]
                searched.append(city)
    print(f'Not. Delivery from Moscow to {city_for_search} is not available yet.')
    return False


if __name__ == '__main__':
    bfs(cities, 'Kolomna')
    bfs(cities, 'Ramenskoye')
    bfs(cities, 'Krasnodar')
    bfs(cities, input('Input city: '))
