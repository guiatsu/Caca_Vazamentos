from models import *

def get_time_series():

    #Se possivel, fazer serie temporal para analisar consumo.
    
    return


def is_alerta(leitura):

    if len(Alerta_Sensor.select().where(Alerta_Sensor.fk_leitura == leitura)) > 0 :
        return True
    
    return False


def main():

    sensors = [s for s in Sensor.select()]
    sensors = [sensors[0]]

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

                if (leituras[i].consumo >= 1.2* comparacao.consumo):
                    
                    descricao = "SENSOR " + str(s+1) + " AVISOU POSSIVEL VAZAMENTO\n" +\
                                "CONSUMO DE " + str(leituras[i].consumo) + " m3\n" +\
                                "LEITURA FEITA NA DATA " + str(leituras[i].data_leitura) +\
                                " \nCOMPARADO COM CONSUMO DE " + str(comparacao.consumo)+"\n"

                    if( not is_alerta(leituras[i]) ):
                        Alerta_Sensor.create(fk_leitura=leituras[i])

                    print(descricao)