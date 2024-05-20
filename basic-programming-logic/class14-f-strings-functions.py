a = 'Orange'
b = 'Pineapple'
c = 1.50

string = 'a={fruit1} b={fruit2} c={number:.2f}'
format_string = string.format(fruit1=a, fruit2=b, number=c)

print(format_string)
