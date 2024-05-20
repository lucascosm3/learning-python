# IMC Calculation with f'strings

name = 'Lucas Cosme'
height = 1.71
weight = 98.0
imc = (weight // (height * 2))

f_strings = f'Name: {name} \nHeight: {height:.2f} \nWeighs {weight} kilos \nIMC: {imc}'
print(f_strings)
