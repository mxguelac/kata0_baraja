import barajas

print(barajas.crear_baraja(['As', '2', '3', '4', '5', '6', '7','S', 'C', 'R'], ('O', 'C', 'E', 'B')))


b = barajas.crear_baraja('A234567SCR', 'oceb')
print(b)
barajas.barajar_for(b)

mi_baraja = barajas.Baraja('A234567SCR', 'oceb')
print(mi_baraja.naipes)