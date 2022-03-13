from models import *

def get_past_avg(dataUntilToday):

    if(len(dataUntilToday) == 0): return 0

    if(len(dataUntilToday) == 1): return 0
    print("----------------media de numero {}------------------".format(len(dataUntilToday)))
    sum = 0

    for i in range(len(dataUntilToday)-1):
        sum += dataUntilToday[i].consumo

    sum /= len(dataUntilToday)-1
    # print("---------------resultado: {}-----------------------".format(sum))
    print("---------------mes atual:{}------------------------".format(dataUntilToday[-1].consumo))

    return sum


def get_time_series():

    #Se possivel, fazer serie temporal para analisar consumo.

    return

def compare_with_before():

    # leituras = Leitura.select().where((Leitura.fk_sensor == 1) & (Leitura.data_leitura < Leitura.select(Leitura.data_leitura).max()))
    

    # calcula media dos meses anteriores 
    # consumo atual > 20% ?
    # se sim = Alerta
    # senao, fodase
    # Nz+nx= nz   Ny > Nz + (nz*0,2)
    # nz 


    return
    

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
                
                    is_alerta = len(Alerta_Sensor.select().where(Alerta_Sensor.fk_leitura == comparacao)) > 0
                    
                    if(is_alerta):
                        j-=1
                        comparacao = leituras[j]

                        if(j == 0):
                            is_alerta = False
                        

                    else: break

                if (not is_alerta) and (leituras[i].consumo >= 1.2* comparacao.consumo):
                    
                    descricao = "SENSOR " + str(s+1) + " AVISOU POSSIVEL VAZAMENTO\n" +\
                                "CONSUMO DE " + str(leituras[i].consumo) + " m3\n" +\
                                "LEITURA FEITA NA DATA " + str(leituras[i].data_leitura) +\
                                " \nCOMPARADO COM CONSUMO DE " + str(comparacao.consumo)

                    if(len(Alerta_Sensor.select().where(Alerta_Sensor.fk_leitura == leituras[i]))) == 0:
                        Alerta_Sensor.create(fk_leitura=leituras[i])

                    print(descricao)
                    print()

        for a in Alerta_Sensor.select():
            print(a.fk_leitura.consumo)


    # print("NO MES  " + str(i) + "  DEU MERDA")