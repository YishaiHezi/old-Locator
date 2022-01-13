import socket
import threading


#########################################################################
import time

missions = []
results = ['1']


def start_threads():
    x1 = threading.Thread(target=run_server_listener, daemon=True)
    x1.start()

    x = threading.Thread(target=run_server_sender, daemon=True)
    x.start()

    while True:
        time.sleep(1)


def run_server_listener():
    s = socket.socket()
    print('listen socket was created')
    s.bind(('localhost', 9998))
    s.listen(3)
    print('server is listening..')

    while True:
        c, addr = s.accept()
        print(f'connected to address: {addr}')

        what_to_do = c.recv(1024).decode()

        while what_to_do != '0':
            print(f"The client send me this: {what_to_do}.\n"
                  "adding it to missions..\n")
            missions.append(what_to_do)
            print(f"missions: {missions}\n")
            time.sleep(1)
            results.append(what_to_do)
            what_to_do = c.recv(1024).decode()

        print(f'exiting...')
        c.close()
        return




def run_server_sender():
    # global results
    s = socket.socket()
    print('sender socket was created')
    s.bind(('localhost', 9999))
    s.listen(3)

    while True:
        c, addr = s.accept()
        print(f'connected to address: {addr}')

        while True:
            while len(results) <= 1:
                time.sleep(2)
            c.send(bytes(f'result of: {results[-1]}', 'utf-8'))
            del results[-1]

        c.close()

#########################################################################


def run_server_test():
    s = socket.socket()
    print('socket was created')
    s.bind(('localhost', 9999))
    s.listen(3)
    print('server is listening..')

    while True:
        c, addr = s.accept()
        print(f'connected to address: {addr}')

        name = c.recv(1024).decode()
        c.send(bytes(f'Hi, this is the server. Welcome {name}!', 'utf-8'))

        what_to_do = c.recv(1024).decode()

        print(f"The client send me this: {what_to_do}")
        print(what_to_do[0])
        print(what_to_do[1])

        if what_to_do[1] == '*':
            if what_to_do[0] == '1':
                print('updating the user mac address in the DB..')

            elif what_to_do[0] == '2':
                print(f'getting {what_to_do[2:]}\'s location from the DB..')

        c.close()



#########################################################################3

# run_server_test()

start_threads()

