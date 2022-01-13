import client
import client_test
import server_test


## need to delete this:



if __name__ == '__main__':
    locator = client.client_locator()

    while True:
        locator.find_someone_or_exit()



