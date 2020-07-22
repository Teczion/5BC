'''
Dependiendo del lugar de procedencia de un individuo,
necesitamos gravarlo apropiadamente. Los estados de
CA, MN y NY tienen impuestos del 7,5%, 9,5% y 8,9% 
respectivamente. 

Usar esta información para tomar el monto de una compra
y el estado correspondiente para asegurar que se gravan
con el monto correcto.
'''

state = "NY"
monto_compra = 100

if state == "CA": #Codicional para CA
    valor_impuesto = .075
    total_cost = monto_compra*(1+valor_impuesto)
    result = "Desde que eres de {}, tu total es de {}.".format(state, total_cost)

elif state == "MN": #Condicional para MN
    valor_impuesto = .095
    total_cost = monto_compra*(1+valor_impuesto)
    result = "Desde que eres de {}, tu total es de {}.".format(state, total_cost)

elif state == "NY":  #Condicional para NY
    valor_impuesto = .089
    total_cost = monto_compra*(1+valor_impuesto)
    result = "Desde que eres de {}, tu total es de {}.".format(state, total_cost)

print(result)