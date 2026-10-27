import networkx as nx
import matplotlib.pyplot as plt

metro_cdmx = nx.Graph()

# Definir función para agregar líneas
def agregar_linea(grafo, lista_estaciones, nombre_linea):
    for i in range(len(lista_estaciones) - 1):
        grafo.add_edge(lista_estaciones[i], lista_estaciones[i + 1], linea=nombre_linea)

# Definición de todas las líneas
linea1_rosa = ["Observatorio", "Tacubaya", "Balderas", "Pino Suarez", "Candelaria", "San Lazaro", "Pantitlan"]
linea2_azul = ["Cuatro Caminos", "Tacubaya", "Hidalgo", "Bellas Artes", "Pino Suarez", "Chabacano", "Tasqueña"]
linea3_verde = ["Indios Verdes", "La Raza", "Hidalgo", "Balderas", "Centro Médico", "Zapata", "Universidad"]

linea4_amarilla = [
    "Martín Carrera", "Talismán", "Consulado", "Canal del Norte",
    "Morelos", "Candelaria", "Fray Servando", "Jamaica", "Santa Anita"
]

linea5_amarilla_claro = [
    "Politécnico", "Instituto del Petróleo", "Autobuses del Norte",
    "La Raza", "Misterios", "Valle Gómez", "Consulado", "Terminal Aérea",
    "Hangares", "Pantitlán"
]

linea6_roja = [
    "El Rosario", "Tezozómoc", "UAM-Azcapotzalco", "Ferrería/Arena Ciudad de México",
    "Norte 45", "Vallejo", "Instituto del Petróleo", "Lindavista",
    "Deportivo 18 de Marzo", "Martín Carrera"
]

linea7_naranja = [
    "El Rosario", "Aquiles Serdán", "Camarones", "Tacuba", "San Joaquín",
    "Polanco", "Auditorio", "Constituyentes", "Tacubaya", "San Pedro de los Pinos",
    "San Antonio", "Mixcoac", "Barranca del Muerto"
]

linea8_verde_claro = [
    "Garibaldi/Lagunilla", "Bellas Artes", "San Juan de Letrán", "Salto del Agua",
    "Doctores", "Obrera", "Chabacano", "La Viga", "Santa Anita",
    "Coyuya", "Iztacalco", "Apatlaco", "Aculco", "Escuadrón 201",
    "Atlalilco", "Iztapalapa", "Cerro de la Estrella", "UAM-I", "Constitución de 1917"
]

linea9_cafe = [
    "Tacubaya", "Patriotismo", "Chilpancingo", "Centro Médico",
    "Lázaro Cárdenas", "Chabacano", "Jamaica", "Mixiuhca",
    "Velódromo", "Ciudad Deportiva", "Puebla", "Pantitlán"
]

lineaA_morada = [
    "Pantitlán", "Agrícola Oriental", "Canal de San Juan", "Tepalcates",
    "Guelatao", "Peñón Viejo", "Acatitla", "Santa Marta", "Los Reyes", "La Paz"
]

lineaB_gris = [
    "Buenavista", "Guerrero", "Garibaldi/Lagunilla", "Lagunilla",
    "Tepito", "Morelos", "San Lázaro", "Ricardo Flores Magón",
    "Romero Rubio", "Oceanía", "Deportivo Oceanía", "Bosque de Aragón",
    "Villa de Aragón", "Nezahualcóyotl", "Impulsora", "Río de los Remedios",
    "Múzquiz", "Ecatepec", "Olímpica", "Plaza Aragón", "Ciudad Azteca"
]

linea12_dorada = [
    "Mixcoac", "Insurgentes Sur", "Hospital 20 de Noviembre", "Zapata",
    "Parque de los Venados", "Eje Central", "Ermita", "Mexicaltzingo",
    "Atlalilco", "Culhuacán", "San Andrés Tomatlán", "Lomas de Estrella",
    "Calle 11", "Periférico Oriente", "Tezonco", "Olivos",
    "Nopalera", "Zapotitlán", "Tlaltenco", "Tláhuac"
]

# Agregar líneas al grafo
agregar_linea(metro_cdmx, linea1_rosa, "Rosa")
agregar_linea(metro_cdmx, linea2_azul, "Azul")
agregar_linea(metro_cdmx, linea3_verde, "Verde")
agregar_linea(metro_cdmx, linea4_amarilla, "Amarilla")
agregar_linea(metro_cdmx, linea5_amarilla_claro, "Amarillo Claro")
agregar_linea(metro_cdmx, linea6_roja, "Roja")
agregar_linea(metro_cdmx, linea7_naranja, "Naranja")
agregar_linea(metro_cdmx, linea8_verde_claro, "Verde Claro")
agregar_linea(metro_cdmx, linea9_cafe, "Café")
agregar_linea(metro_cdmx, lineaA_morada, "Morada")
agregar_linea(metro_cdmx, lineaB_gris, "Gris-Verde")
agregar_linea(metro_cdmx, linea12_dorada, "Dorada")

# Configurar figura y visualización
plt.figure(figsize=(22, 22))
pos_completo = nx.kamada_kawai_layout(metro_cdmx)

nx.draw_networkx_nodes(metro_cdmx, pos_completo, node_color="skyblue", node_size=250, alpha=0.9)
nx.draw_networkx_edges(metro_cdmx, pos_completo, alpha=0.4, edge_color="gray", width=1.5)
nx.draw_networkx_labels(metro_cdmx, pos_completo, font_size=7, font_family="sans-serif", verticalalignment="bottom")

plt.title("Mapa de Red del Metro de la Ciudad de México (Grafo Completo)", fontsize=18, fontweight='bold')
plt.axis('off')
plt.show()
EOF
