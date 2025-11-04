#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva
eleccion = input("Pizza vegetariana si o no: ")
if eleccion == "si":
    print("Ingredientes vegetarianos: Pimiento y tofu.")
else:
    print("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")

eleccion2 = input("Elige solo un ingrediente más: ").lower()
if eleccion2 == "pimiento":
    print ("Pizza de mozarella,tomate y pimiento")
if eleccion2 == "tofu":
    print ("Pizza de mozarella,tomate y tofu")
if eleccion2 == "peperoni":
    print ("Pizza de mozarella,tomate y peperoni")
if eleccion2 == "jamón":
    print ("Pizza de mozarella,tomate y jamón")
if eleccion2 == "salmon":
    print ("Pizza de mozarella,tomate y salmón")