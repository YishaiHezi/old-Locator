import socket
import threading



######################################################################
import time

client_results = []


def start_threads():
    x1 = threading.Thread(target=run_client_listener, daemon=True)
    x1.start()

    x = threading.Thread(target=run_client_sender, daemon=True)
    x.start()

    while True:
        time.sleep(1)



def run_client_sender():
    c = socket.socket()
    c.connect(('localhost', 9998))
    print('client sender is connected!')

    what_to_do = 1

    while what_to_do:
        time.sleep(1)
        what_to_do = input('What do you want to do? enter a mission, or 0 to exit: ')
        c.send(bytes(what_to_do, 'utf-8'))
        if what_to_do == '0':
            print('exiting!...')
            return


def run_client_listener():
    c = socket.socket()
    c.connect(('localhost', 9999))
    print('client listener is connected!')

    result = c.recv(1024).decode()

    while True:
        time.sleep(1)
        print(f'I have a result! : {result}')
        print(f'adding: {result} to client_results..\n')
        client_results.append(result)
        result = c.recv(1024).decode()


###########################################################################


def run_client_test():
    my_mac = '2.2.2.2'


    c = socket.socket()
    c.connect(('localhost', 9999))
    print('socket is connected!')


    name = input('Hi, please put your name: ')
    c.send(bytes(name, 'utf-8'))


    print(c.recv(1024).decode())

    what_to_do = input('What do you want to do? enter 1 for telling the server '
                       'your mac, or 2 to ask the server for a user: ')



    if what_to_do == '1':
        p = what_to_do + '*' + my_mac
    else:
        user_name = input('Enter the name of the user you want to find: ')
        p = what_to_do + '*' + user_name

    c.send(bytes(p, 'utf-8'))


# run_client_test()


start_threads()

