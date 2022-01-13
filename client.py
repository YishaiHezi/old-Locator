import get_default_mac
import threading
import requests
import time


class client_locator:

    def __init__(self):
        self.MAC = None

        response = requests.get('http://192.168.14.39/')
        print(response.text)
        print('')

        self.USER = input('Please enter your name: ')
        self.start_thread()

########################################################################
# This code is related to the thread that checks the mac address all the time:

    def start_thread(self):
        x = threading.Thread(target=self.get_my_mac_and_location, daemon=True)
        x.start()

    def get_my_mac_and_location(self):
        while True:
            if self.USER is not None:
                time.sleep(5)
                self.MAC = get_default_mac.get_router_mac()

                mac_and_name = {'mac': self.MAC, 'name': self.USER}
                res = requests.post('http://192.168.14.39/macs',
                                    json=mac_and_name)
                print(res.text)



########################################################################
# This code ask the user for names to find:

    def find_someone_or_exit(self):
        name = input('Enter someone\'s name if you want '
                     'to know their location, otherwise enter 0: ')

        if name == '0':
            print('Bye :)')
            exit(0)

        else:
            name_dict = {'name': name}
            response = requests.get('http://192.168.14.39/names', json=name_dict)
            location = response.text

            if location != 'Not found':
                print(f'{name} is in {location}\n')

            else:
                print(f'We couldn\'t find {name}\'s location :(\n')


# if __name__ == '__main__':
#     locator = client_locator()

#     while True:
#         locator.find_someone_or_exit()
