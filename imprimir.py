import requests
import pandas as pd


def registro_hoy():
    url = "https://404a-190-233-181-4.sa.ngrok.io/kirb_api/main"
    codigo=[]
    nombre=[]
    estado=[]
    response=requests.get(url)
    response=response.json()
#print.pprint(response.text)
    for data in response["alumnos"]:
        for c in data:
            print(c)#codigos
        #print(data[c])#alumnos //estado//nombre
            codigo.append(c)
            print (data[c][0]["nombre"])
            nombre.append(data[c][0]["nombre"])
            print (data[c][1]["estado"])
            estado.append(data[c][1]["estado"])
#crear data frame
    df = pd.DataFrame ({"codigo":codigo, "nombre":nombre, "estado":estado})
    print(df.head())
    print (df.tail())
    df.to_excel("registro_hoy.xlsx", index=False)
