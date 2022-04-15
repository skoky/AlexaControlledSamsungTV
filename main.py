from samsungctl_ts.remote_websocket import Remote


def main():
    r = Remote({
        'method': 'websocket',
        'port': 8002,
        'timeout': 20,
        'host': '10.0.10.7',
        'mac_address': 'f4:fe:fb:9b:a4:5c',
        'name':'hugo'
    })
    r.control('KEY_MUTE')


if __name__ == '__main__':
    main()
