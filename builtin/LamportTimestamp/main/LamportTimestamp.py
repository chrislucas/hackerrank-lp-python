'''
https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6
'''
from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime


def print_local_time(counter):
    print("LAMPORT_TIME={0}, LOCAL_TIME{1}".format(counter, datetime.now()))

def calc_receiver_timestamp(recv_ts, counter):
    return max(recv_ts, counter) + 1


if __name__ == '__main__':
    pass
