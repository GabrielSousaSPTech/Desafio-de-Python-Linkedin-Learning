
from datetime import datetime
import time
import sched
class Agendamento():
    def agendarFuncao(self, tempoAgendamento, funcao, parametroFuncao):
        print(f'{funcao.__name__}() agendado para {time.asctime(time.localtime(tempoAgendamento))}')
        while(True):
            if(datetime.now() >= datetime.fromtimestamp(tempoAgendamento)):
                funcao(parametroFuncao)
                break
            time.sleep(0.5)




# ==============================================================================================
                                # Solução realizada no video                 




    def agendamento(self, horario_do_evento, funcao, *args):
        s = sched.scheduler(time.time, time.sleep)
        s.enterabs(horario_do_evento, 1, funcao, argument=args)
        t = time.asctime(time.localtime(horario_do_evento))
        print(f'{funcao.__name__}() agendado para {t}')

        s.run()

a = Agendamento()
a.agendarFuncao(time.time() +10, print, 'Olá!!')

a.agendamento(time.time() +3, print, 'Olá do Linkedin Learning!!')