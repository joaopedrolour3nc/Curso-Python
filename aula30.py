"""
CONSTANTE = "VARIAVEIS" que não vão mudar
Muitas condições no mesmo if(ruim)
    <-- Contagem de Complexidade (ruim)
"""

velocidade = 61 # Velocidade do carro
local_do_carro = 100 # local em que o carro está na estrada 
RADAR_1 = 60 # A Velocidade do Radar 1
LOCAL_1 = 100 # Local onde está o radar 1
RADAR_RANGE = 1 # A Distância que o radar 1 pega

velocidade_do_carro_passou_radar_1 = velocidade > RADAR_1

carro_passou_por_radar_1 = local_do_carro >= (LOCAL_1 - RADAR_RANGE) and \
 local_do_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_por_radar_1 and velocidade_do_carro_passou_radar_1

if velocidade_do_carro_passou_radar_1:
    print('Você passou da Velocidade do Radar')

if carro_passou_por_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em Radar 1')