import os, requests, time
def pause():
    print()
    if os.name == 'nt':
        os.system('pause')
    else:
        input('Press enter to continue...')
def check_server():
    print('############################\n# C&C:Online Server Status #\n############################')
    try:
        for game,data in requests.get('https://info.server.cnc-online.net/').json().items():
            try:
                user_count = len(data['users'])
                if user_count:
                    print('{}{}{:0>3} online'.format(game, (2 - (len(game) // 8)) * '\t', user_count))
            except:
                pass
    except:
        print('SERVER OFFLINE')
    pause()
if __name__ == '__main__':
    check_server()