"""
v1 = "POO "
v2 = "Desarrollo"
vc = "Hola "+ v1 + v2+str(200)
print(vc)

nombre = input("Nombre:")
n1 = float(input("Numero 1:"))
n2 = float(input("Numero 2:"))
r = (n1+n2)
print("El total es:",r)
"""
cliente = input("Cliente:")
producto = input("Producto:")
precio = float(input("Precio:"))
cantidad = int(input("Cantidad:"))
subtotal = (precio*cantidad)
iva = (subtotal*0.12)
total = (subtotal+iva)
msg= "Subtotal:"+str(round(subtotal,2))+"\nIva:"+str(round(iva,2))\
     +"\nTotal:"+str(round(total,2))
print(msg)