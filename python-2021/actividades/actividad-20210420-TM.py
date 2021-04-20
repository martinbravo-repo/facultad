import csv

### listar los juegos gratuitos disponibles en idioma español.
# Languages 12
# Price 7
# Name 2
games_file=open("/home/vito/facultad/python-2021/actividades/appstore_games.csv","r")
csvreader=csv.reader(games_file, delimiter=',')
print('*'*20)
print('Ejercicio 1')
print('*'*20)
games_es=filter(lambda x:  "ES" in x[12] and x[7]=="0", csvreader)
for elem in games_es:
    print(elem[2])
games_file.close()


# los íconos (OPCIONAL en formato imagen, sino la url) de los 10 juegos con más calificaciones de usuarios (User Rating Count).
# Icon URL 4
# User Rating Count 6
# Name 2
print('*'*20)
print('Ejercicio 2')
print('*'*20)
games_file=open("/home/vito/facultad/python-2021/actividades/appstore_games.csv","r")
csvreader=csv.reader(games_file, delimiter=',')
#saco el encabezado
next(csvreader)
all_games = [(x[2],x[4],int(x[6])) for x in csvreader if x[6] != '']
sorted_games = sorted(all_games, key=lambda x: x[2], reverse=True)
for index in range(10):
    print(sorted_games[index][1])
games_file.close()

