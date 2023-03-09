import pywhatkit

numero = input("A que numero quieres enviar el mensaje?  ")
mensaje = input("Que mensaje quieres enviar?  ")

pywhatkit.sendwhatmsg_instantly(numero, mensaje)
