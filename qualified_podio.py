def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    # Implemente aqui a lógica da função
    if tempo_chegada1 < tempo_chegada2 < tempo_chegada3:
      menorTempo = tempo_chegada1
      segundo = tempo_chegada2
      maiorTempo = tempo_chegada3
    elif tempo_chegada1 < tempo_chegada3 < tempo_chegada2:
      menorTempo = tempo_chegada1
      segundo = tempo_chegada3
      maiorTempo = tempo_chegada2
    elif tempo_chegada2 < tempo_chegada1 < tempo_chegada3:
      menorTempo = tempo_chegada2
      segundo = tempo_chegada1
      maiorTempo = tempo_chegada3
    elif tempo_chegada2 < tempo_chegada3 < tempo_chegada1:
      menorTempo = tempo_chegada2
      segundo = tempo_chegada3
      maiorTempo = tempo_chegada1
    elif tempo_chegada3 < tempo_chegada2 < tempo_chegada1:
      menorTempo = tempo_chegada3
      segundo = tempo_chegada2
      maiorTempo = tempo_chegada1
    else:
      menorTempo = tempo_chegada3
      segundo = tempo_chegada1
      maiorTempo = tempo_chegada2
    
    podio = '1 - ' + str(menorTempo) + ' minutos\n2 - ' + str(segundo) + ' minutos\n3 - ' + str(maiorTempo) + ' minutos'
    
    return podio
  
tempo1 = 120
tempo2 = 90
tempo3 = 110
print(podio_olimpico(tempo1, tempo2, tempo3))