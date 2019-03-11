'''
https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6
'''
from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime

local_time = lambda counter: "LAMPORT_TIME={0}, LOCAL_TIME={1}".format(counter, datetime.now())

calc_max_timestamp = lambda received_ts, counter: max(received_ts, counter) + 1

'''
Funcao que representa um evento num sistema distribuido
'''


def event(pid, time):
    time += 1
    print("Event: {0}, LOCAL_TIME: {1}".format(pid, local_time(time)))
    return time


'''
O evento de enviar uma mensagem recebe como argumento o ID do process
a hora da ocorrencia (timestamp) e um Objeto PIPE

Pipe eh um objeto da biblioteca de  de multiprocessamento que representa uma conexao
de 2 vias entre 2 processos. Todo pype consiste de 2objetos conecatos

'''


def send_message(pid, time, pipe):
    time += 1
    pipe.send(('Data', time))
    print('(SEND) PID: {0}, {1}'.format(pid, local_time(time)))
    return time


def receive_message(pid, time, pipe):
    message, timestamp_sended_msg = pipe.recv()
    time = calc_max_timestamp(timestamp_sended_msg, time)
    print('(RECEIVE) PID: {0}, {1}'.format(pid, local_time(time)))
    return time


def get_pair_pipes():
    a, b = Pipe()
    return a, b


'''
    Processo 1 executara trocas de mensagens pelo Pipe ab/ba
    cada processo tem o seu proprio ID
    
    Abaixo segue o link do diagrama de processos, eventos de trocas
    de mensagens que inspirou os metodos abaixo
    https://cdn-images-1.medium.com/max/1000/1*zEQ5D0f5lPUJcTBO50u-TA.png
'''


def process_1(pipe_ab):
    pid = getpid()
    time = event(pid, 0)  # time comeca com 0    ->
    time = send_message(pid, time, pipe_ab)
    time = event(pid, time)
    time = receive_message(pid, time, pipe_ab)
    time = event(pid, time)

'''
    pipe_ba representa o pipe ou a outra ponta (volta) do canal de troca de mensagens
    entre o processo a -> b
    pipe_bc represetna o pipe (ida) de troca de mensagens entre o process
    b -> c
'''
def process_2(pipe_ba, pipe_bc):
    pid = getpid()
    time = receive_message(pid, 0, pipe_ba)
    time = send_message(pid, time, pipe_ba)
    time = send_message(pid, time, pipe_bc)
    time = receive_message(pid, time, pipe_bc)

'''
    pipe_cv reresemta p camal  (volta) de trica de mensagens
    entre o process b -> c
'''
def process_3(pipe_cb):
    pid = getpid()
    time = receive_message(pid, 0, pipe_cb)
    time = send_message(pid, time, pipe_cb)


if __name__ == '__main__':
    ab, ba = get_pair_pipes()
    bc, cb = get_pair_pipes()
    p1 = Process(target=process_1, args=(ab,))
    p2 = Process(target=process_2, args=(ba, bc))
    p3 = Process(target=process_3, args=(cb,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()