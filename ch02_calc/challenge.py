#executar a instalação do modulo "scipy" atraves do power shell
#executar a instação do mudolo "numpy" atraves do power shell
import numpy as np
from scipy.optimize import minimize

# Solicitar ao usuário as distâncias entre os locais
D = np.zeros((4, 4))
for i in range(4):
    for j in range(i+1, 4):
        distance = float(input("Insira a distância entre o local {} e o local {}: ".format(i+1, j+1)))
        D[i, j] = distance
        D[j, i] = distance

# Solicitar ao usuário o coeficiente de consumo de combustível
k = float(input("Insira o coeficiente de consumo de combustível (em litros por quilômetro): "))

# Solicitar ao usuário o preço do combustível
fuel_price = float(input("Insira o preço do combustível (em reais por litro): "))

# Função objetivo
def objective(x):
    distance_cost = np.sum(D * x)
    fuel_cost = k * np.sum(np.square(x))
    total_cost = distance_cost + fuel_cost
    return total_cost

# Restrição: todos os locais devem ser visitados exatamente uma vez
def constraint(x):
    return np.sum(x) - 1

# Vetor de suposições iniciais
x0 = np.array([0, 0, 0, 0])

# Definindo os limites de cada variável
bounds = [(0, 1)] * len(x0)

# Definindo a restrição
constraint_eq = {'type': 'eq', 'fun': constraint}

# Resolvendo o problema de otimização
result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraint_eq)

# Obtendo a sequência de visitas ótima
sequence = np.argsort(result.x)

# Cálculo do custo total em reais
distance_cost = np.sum(D * result.x)
fuel_cost = k * np.sum(np.square(result.x))
total_cost = distance_cost + fuel_cost
total_cost_in_reais = total_cost * fuel_price

# Exibindo os resultados
print("Sequência de visitas ótima: ", sequence)
print("Custo total mínimo: R$ {:.2f}".format(total_cost_in_reais))