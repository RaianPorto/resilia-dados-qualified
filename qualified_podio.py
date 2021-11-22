# def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
#     # Implemente aqui a lógica da função
#     if tempo_chegada1 < tempo_chegada2 < tempo_chegada3:
#       menorTempo = tempo_chegada1
#       segundo = tempo_chegada2
#       maiorTempo = tempo_chegada3
#     elif tempo_chegada1 < tempo_chegada3 < tempo_chegada2:
#       menorTempo = tempo_chegada1
#       segundo = tempo_chegada3
#       maiorTempo = tempo_chegada2
#     elif tempo_chegada2 < tempo_chegada1 < tempo_chegada3:
#       menorTempo = tempo_chegada2
#       segundo = tempo_chegada1
#       maiorTempo = tempo_chegada3
#     elif tempo_chegada2 < tempo_chegada3 < tempo_chegada1:
#       menorTempo = tempo_chegada2
#       segundo = tempo_chegada3
#       maiorTempo = tempo_chegada1
#     elif tempo_chegada3 < tempo_chegada2 < tempo_chegada1:
#       menorTempo = tempo_chegada3
#       segundo = tempo_chegada2
#       maiorTempo = tempo_chegada1
#     else:
#       menorTempo = tempo_chegada3
#       segundo = tempo_chegada1
#       maiorTempo = tempo_chegada2
    
#     podio = '1 - ' + str(menorTempo) + ' minutos\n2 - ' + str(segundo) + ' minutos\n3 - ' + str(maiorTempo) + ' minutos'
    
#     return podio
  
# tempo1 = 120
# tempo2 = 90
# tempo3 = 110
# print(podio_olimpico(tempo1, tempo2, tempo3))

def podio_olimpico(tempo_chegada1, tempo_chegada2,tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    # Implemente aqui a lógica da função
    
    if tempo_chegada1 < tempo_chegada2 < tempo_chegada3:
      primeiro = nome_corredor1
      segundo = nome_corredor2
      terceiro = nome_corredor3
      tempo1 = str(tempo_chegada1)
      tempo2 = str(tempo_chegada2)
      tempo3 = str(tempo_chegada3)
    elif tempo_chegada3 < tempo_chegada2 < tempo_chegada1:
      primeiro = nome_corredor3
      segundo = nome_corredor2
      terceiro = nome_corredor1
      tempo1 = str(tempo_chegada3)
      tempo2 = str(tempo_chegada2)
      tempo3 = str(tempo_chegada1)
    elif tempo_chegada1 < tempo_chegada3 < tempo_chegada2:
      primeiro = nome_corredor1
      segundo = nome_corredor3
      terceiro = nome_corredor2
      tempo1 = str(tempo_chegada1)
      tempo2 = str(tempo_chegada3)
      tempo3 = str(tempo_chegada2)
    elif tempo_chegada2 < tempo_chegada3 < tempo_chegada1:
      primeiro = nome_corredor2
      segundo = nome_corredor3
      terceiro = nome_corredor1
      tempo1 = str(tempo_chegada2)
      tempo2 = str(tempo_chegada3)
      tempo3 = str(tempo_chegada1)
    elif tempo_chegada3 < tempo_chegada1 < tempo_chegada2:
      primeiro = nome_corredor3
      segundo = nome_corredor1
      terceiro = nome_corredor2
      tempo1 = str(tempo_chegada3)
      tempo2 = str(tempo_chegada1)
      tempo3 = str(tempo_chegada2)
    else:
      primeiro = nome_corredor2
      segundo = nome_corredor1
      terceiro = nome_corredor3
      tempo1 = str(tempo_chegada2)
      tempo2 = str(tempo_chegada1)
      tempo3 = str(tempo_chegada3)
    
    podio = '1 - ' + primeiro + ' - ' + tempo1 + ' minutos\n2 - ' + segundo + ' - ' + tempo2 + ' minutos\n3 - ' + terceiro + ' - ' + tempo3 + ' minutos'

    return podio

tempo1 = 320
tempo2 = 180
tempo3 = 120
corredor1 = "Ronaldo"
corredor2 = "Wanderlei Cordeiro de Lima"
corredor3 = "Eliud Kipchoge"

print(podio_olimpico(tempo1, tempo2, tempo3, corredor1, corredor2, corredor3))