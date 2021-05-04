import PySimpleGUI as sg
import os
import json
import csv

def get_file_one():
    #https://www.kaggle.com/abcsds/pokemon
    return "Pokemon.csv"

def get_file_two():
    # https://www.kaggle.com/umutalpaydn/nba-20202021-season-player-stats
    return "nba2021_advanced.csv"

def build_player_json(item):
    return {"name":item[0],"team":item[3],"age":item[2]}

def build_pokemon_json(item):
    return {"name":item[1],"type":item[2],"attack":item[6],"legendary":item[12]}

def process_file(filter_function, source_file, result_file, map_function):
    with open(os.path.join(os.getcwd(), source_file),"r") as some_file:
        csvreader=csv.reader(some_file, delimiter=',')
        #saco el encabezado
        next(csvreader)
        filtered_items=list(filter(filter_function, csvreader))[:20]
    data = []
    with open(result_file, 'w') as file_result:
        for item in filtered_items:
            new_item = map_function(item)
            data.append(new_item)
        json.dump(data, file_result)
        

layout = [
        [sg.Text("Qué datos analizamos?",size=(30,0),font="Arial 12 bold",justification='center')],
        [sg.Button('Pokemon',font="Arial 12 bold", size=(20, 2), key="-UNO-")],
        [sg.Button('Jugadores NBA',font="Arial 12 bold", size=(20, 2), key="-DOS-")],
        [sg.Button('Salir',font="Arial 12 bold", size=(20, 2), key="-EXIT-")]
]

window = sg.Window('Actividad x Python Plus - TEORIA -', layout, element_justification="center", disable_close=True, size=(400,300))

while True:
    event, values = window.read()
    if event == '-EXIT-':
        break
    elif event == '-UNO-':
        # 20 Pokemon de fuego cuyo poder de ataque > 75
        process_file(lambda x: x[2]=="Fire" and int(x[6]) > 75, get_file_one(), "pokemon.json", build_pokemon_json)
        sg.popup("Archivo pokemon.json creado.")
    else:
        # 20 Jugadores de NBA entre 25 y 35 años que juegan en la posición PG
        process_file(lambda x: x[1]=="PG" and int(x[2]) > 25 and int(x[2]) < 35, get_file_two(), "players.json", build_player_json)
        sg.popup("Archivo players.json creado.")

window.close()
