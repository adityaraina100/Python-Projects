import requests

def check_server_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return True
    except requests.RequestException:
        return False

if __name__ == '__main__':
    server_url = 'https://example.com/'  
    #use website like 'https://77example.com/' to check the other response(server is down)
    server_status = check_server_status(server_url)

    if server_status:
        print('The server is up and running.')
    else:
        print('The server is down.')
