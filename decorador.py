
import requests


def imprimir_mensajes(funcion):
   def wrapper(lista):
       for pagina in lista:
           response = requests.get(pagina)
           if(response.status_code == 200):
               print("La pagina {0} esta online.".format(pagina))
           else:
               print("La pagina {0} esta offline.".format(pagina))
   return wrapper

@imprimir_mensajes
def pagina_online(lista):
    print("Revisaremos la lista de URLS para ver su estado.")
    if not lista:
        print("La lista esta vacia")
