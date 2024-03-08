# Sincronização de Relógios Físicos
Implementação do Algoritmo de Berkeley para sincronizar relógios em uma rede local usando gRPC.

# Dupla
- Francisco Racklyn Sotero dos Santos (21110615)
- Jucyelle Barros do Nascimento (21110438)

# Instruções
1. Execute os seguintes comandos em terminais separados para configurar cada slave:
- python slave.py 5001 10
- python slave.py 5002 -5
- python slave.py 5003 20

Aqui, as portas (5001, 5002, 5003) representam os diferentes slaves, e os números finais (10, -5, 20) são os deslocamentos de tempo em segundos para cada slave, garantindo que cada um tenha um horário único (é possível utilizar outros números para teste).

2. Execute o master:

- python master.py

O script master.py será responsável por coordenar a sincronização dos relógios dos slaves, levando em consideração os deslocamentos de tempo configurados.
