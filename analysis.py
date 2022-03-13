from models import *

def get_time_series():

    #Se possivel, fazer serie temporal para analisar consumo.
    
    return


def is_alerta(leitura):

    if len(Alerta_Sensor.select().where(Alerta_Sensor.fk_leitura == leitura)) > 0 :
        return True
    
    return False


def analysis():

    sensors = [s for s in Sensor.select()]

    min_consumo = 50

    for s in range(len(sensors)):
        
        leituras = [l for l in Leitura.select().where(Leitura.fk_sensor == s+1)]

        for i in range(len(leituras)):  

            if i > 1:

                j = i-1

                comparacao = leituras[j]

                while(j >= 1):
                    
                    if(is_alerta(comparacao)):
                        j-=1
                        comparacao = leituras[j]             

                    else: break

                if (leituras[i].consumo >= 1.2* comparacao.consumo ) and (comparacao.consumo > min_consumo):

                    if( not is_alerta(leituras[i]) ):
                        Alerta_Sensor.create(fk_leitura=leituras[i])