import random
import pyqrcode
import png

detalleCompras = ([],[],[],[],[],[])

def menuOpciones():
  print("¿Qué acción desea realizar?")
  print("1. Registrar pedidos")
  print("2. Mostrar pedidos")
  print("3. Mostrar detalle de un pedido")
  print("4. Eliminar pedido")
  print("5. Salir del sistema")
  return int(input("Ingrese una opción: "))



def ingresarPedido():
  print("Ingrese los datos del cliente")
  nombre = input("Nombre: ")
  apellido = input("Apellido: ")
  telefono = input("Teléfono: ")
  direccion = input("Dirección: ")
  detalleCompras[0].append(nombre)
  detalleCompras[1].append(apellido)
  detalleCompras[2].append(telefono)
  detalleCompras[3].append(direccion)
  detalleCompras[4].append(random.randrange(1000,9999))
  
  print("Seleccione el paquete ofimático a contratar")
  print("1. Opción 1: PC + Monitor = $500")
  print("2. Opción 2: PC + Monitor 4K = $2000")
  print("3. Opción 3: Laptop UltraProIA = $1500")
  print("4. Opcion 4: Workstation servidor = $3000")
  opcion = int(input("Seleccione una opción: "))
  if opcion == 1:
    detalleCompras[5].append(500+(500*0.15))
  elif opcion == 2:
    detalleCompras[5].append(2000+(2000*0.15))
  elif opcion == 3:
    detalleCompras[5].append(1500+(1500*0.15))
  elif opcion == 4:
    detalleCompras[5].append(3000+(3000*0.15))
  print("Pedido registrado exitosamente")
  


def mostrarPedido(i):
  print("Datos del cliente")
  print(f"* Nombre: {detalleCompras[0][i]}")
  print(f"* Apellido: {detalleCompras[1][i]}")
  print(f"* Teléfono: {detalleCompras[2][i]}")
  print(f"* Dirección: {detalleCompras[3][i]}")
  print(f"* Código del pedido: {detalleCompras[4][i]}")
  print(f"* Total a pagar con IVA: ${detalleCompras[5][i]}")
  


def mostrarPedidos():
  if len(detalleCompras[0]) == 0:
    print("No existen pedidos registrados")
    return
  else:
    #Mostrar pedidos
    print("Lista de pedidos registrados")
    for c in range(len(detalleCompras[0])):
      mostrarPedido(c)



def mostrarDetallePedido():
  if len(detalleCompras[0]) == 0:
    print("No existen pedidos registrados")
    return
  else:
    codigo = int(input("Ingrese el código del pedido: "))
    if codigo in detalleCompras[4]:
      codigoIndex = detalleCompras[4].index(codigo)
      mostrarPedido(codigoIndex)
      pagoQRPichincha(codigoIndex)
    else:
      print("El código ingresado no existe")



def eliminarPedido():
  if len(detalleCompras[0]) == 0:
    print("No existen pedidos registrados")
    return
  else:  
    codigo = int(input("Ingrese el código del pedido: "))
    if codigo in detalleCompras[4]:
      codigoIndex = detalleCompras[4].index(codigo)
      for f in range(len(detalleCompras)):
       detalleCompras[f].pop(codigoIndex)
      print("Pedido eliminado exitosamente")
    else:
      print("El código ingresado no existe")



def pagoQRPichincha(i):
  textoPago = f"Datos del pago\n * Código del pedido: {detalleCompras[4][i]}\n * Pago final: ${detalleCompras[5][i]}\n"
  
  codigoQr = pyqrcode.create(textoPago)
  nombreArchivo = "CódigoQr.png"
  codigoQr.png(nombreArchivo, scale=8)
  print("Código QR generado exitosamente")



def main():
  print("Bienvenido a TechWorld S.A.")
  opcion = menuOpciones()
  while opcion != 5:
    if opcion == 1:
      ingresarPedido()
    elif opcion == 2:
      mostrarPedidos()
    elif opcion == 3:
      mostrarDetallePedido()
    elif opcion == 4:
      eliminarPedido()
    opcion = menuOpciones()    
  print("Gracias por usar el sistema") 


main()
