import csv, json
from collections import OrderedDict

def save(data):
    with open('delitos.json', "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def read():

    stats = {}
    with open('delitos.csv', newline='', encoding='utf-8') as csvfile:
        # Crea un objeto lector CSV
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        # Itera sobre cada fila en el archivo CSV
        for row in csvreader:
            # Accede a los valores de cada columna por su nombre
            id_mapa = row['id-mapa']
            anio = row['anio']
            mes = row['mes']
            dia = row['dia']
            fecha = row['fecha']
            franja = row['franja']
            tipo = row['tipo']
            subtipo = row['subtipo']
            armado = row['uso_arma'] == 'SI'
            motorizado = row['uso_moto'] == 'SI'
            barrio = row['barrio']
            comuna = row['comuna']
            latitud = row['latitud']
            longitud = row['longitud']
            cantidad = int(row['cantidad'])
            
            # Tipo de Robo por Barrio
            if 'general' not in stats:
                stats['general'] = {}
            
            if tipo not in stats['general']:
                stats['general'][tipo] = cantidad
            else:
                stats['general'][tipo] += cantidad
                
            # Tipo de Robo por Barrio
            if 'barrio' not in stats:
                stats['barrio'] = {}
                
            if barrio not in stats['barrio']:
                stats['barrio'][barrio] = {}   
                
            if tipo not in stats['barrio'][barrio]:
                stats['barrio'][barrio][tipo] = cantidad
            else:
                stats['barrio'][barrio][tipo] += cantidad
          
          
            # Tipo de Robo por Mes
            if 'mes' not in stats:
                stats['mes'] = {}
            
            if mes not in stats['mes']:
                stats['mes'][mes] = {}
            
            if tipo not in stats['mes'][mes]:
                stats['mes'][mes][tipo] = cantidad
            else:
                stats['mes'][mes][tipo] += cantidad
            
            # Tipo de Robo por Dia
            if 'dia' not in stats:
                stats['dia'] = {}
            
            if dia not in stats['dia']:
                stats['dia'][dia] = {}
            
            if tipo not in stats['dia'][dia]:
                stats['dia'][dia][tipo] = cantidad
            else:
                stats['dia'][dia][tipo] += cantidad
                
            # Tipo de Robo por Por dia Por Mes
            if 'mes_dia' not in stats:
                stats['mes_dia'] = {}
            
            if mes not in stats['mes_dia']:
                stats['mes_dia'][mes] = {}
            
            if dia not in stats['mes_dia'][mes]:
                stats['mes_dia'][mes][dia] = {}
            
            if tipo not in stats['mes_dia'][mes][dia]:
                stats['mes_dia'][mes][dia][tipo] = cantidad
            else:
                stats['mes_dia'][mes][dia][tipo] += cantidad
                
            # Modo de robo
            if 'modo' not in stats:
                stats['modo'] = { 'armado': 0, 'motorizado': 0, 'ambos': 0, 'ninguno': 0 }
            
            if armado and motorizado :
                stats['modo']['ambos'] +=cantidad
            elif armado or motorizado:
                if armado:
                    stats['modo']['armado'] +=cantidad
                    
                if motorizado:
                    stats['modo']['motorizado'] +=cantidad
            else: 
                stats['modo']['ninguno'] +=cantidad
                
            # Tipo de delito segun dia del mes
            if 'fecha' not in stats:
                stats['fecha'] = {}
            
            day = fecha.split('-')[2]
            
            if day not in stats['fecha']:
                stats['fecha'][day] = {}
                
            if tipo not in stats['fecha'][day]:
                stats['fecha'][day][tipo] = cantidad
            else:
                stats['fecha'][day][tipo] += cantidad
                
    return stats




if __name__ == '__main__':
    print('started')
    delitos = read()

    save(delitos)