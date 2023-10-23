from heyoo import WhatsApp
token = 'EAAN51sZCPbZBkBO4y3Y2nt4bo40WH7aQLpSTZBJ0ygLwZAfS22IBVosc7L4PVRLRcW5CZBqSO5aWFgj1GHNK48D9MqFeHOvfJmnQ0GgRE1qQm2IZB7WuAPMX7uITEbfV0tFZARZBZAdNMFRZBxYvyAoMBElx3z8icZBZCwtZAMRhPeVDZC1jsI76Wq9vSrEuEIHK2bUWvFmm3yO0ooOTMpNHEZD'
idNumeroTelefono='140419589154864'
telefonoEnvia='+573168649514'
mensajeTexto='Hola Soy Vigilant'
urlImagen = 'https://www.movilexito.com/sites/default/files/2023-10/Banner-Desktop.jpg'
miWhastApp = WhatsApp(token, idNumeroTelefono)
miWhastApp.send_image(image=urlImagen,recipient_id=telefonoEnvia,)
miWhastApp.send_message(mensajeTexto, telefonoEnvia)

