from barajas import crear_baraja, barajar_for

print(crear_baraja(['As', '2', '3', '4', '5', '6', '7','S', 'C', 'R'], ('O', 'C', 'E', 'B')))


b = crear_baraja('A234567SCR', 'oceb')
print(b)
barajar_for(b)