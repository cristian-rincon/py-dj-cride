from os import system

# Success code for linux terminal is equal to 0.
request_install = system("pip install requests")

if not request_install:
    import requests

    circles_url_raw_data = "https://gist.githubusercontent.com/pablotrinidad/93ee462e0ee761bd505f0a2fed3d1c8c/raw/61f02a79080586901d0c9b510d4c4d2fff7f3836/circles.csv"
    response = requests.get(circles_url_raw_data)
    if response.status_code == 200:
        datas_raw = response.text
        datas_list = [data.split(',') for data in datas_raw.split('\n')]
        for data in datas_list:
            Circle.objects.update_or_create(
                name=data[0],
                slug_name=data[1],
                defaults={
                    'is_public': bool(data[2]),
                    'verified': bool(data[3]),
                    'members_limit': int(data[4]) if data[4].isnumeric() else 0,
                },
            )
    else:
        print('ERROR: conexion.')
else:
    print('ERROR: problem on installation "requests" package.')