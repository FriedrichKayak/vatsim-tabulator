import urllib.request
import json
import sqlite3

with urllib.request.urlopen("https://status.vatsim.net/status.json") as status:
    data = json.loads(status.read().decode())
    v3url = data['data']['v3'][0]

with urllib.request.urlopen(v3url) as connections:
    vatsim = json.loads(connections.read().decode())


# create (or open) the database and connect to it
con = sqlite3.connect('flights.db')
cur = con.cursor()

# create flights table
cur.execute('''DELETE FROM flights;''')
# create controller table
cur.execute('''DELETE FROM controllers;''')

# insert records from VATSIM
for flight in vatsim['pilots']:
    if not flight['flight_plan'] is None:
        sql = "INSERT INTO flights VALUES ('{0}', '{1}', '{2}', '{3}');".format(flight['callsign'],
                                                                                 flight['flight_plan']['departure'],
                                                                                 flight['flight_plan']['arrival'], 'N')
        print(sql)
        cur.execute(sql)

for prefile in vatsim['prefiles']:
    if not prefile['flight_plan'] is None:
        sql = "INSERT INTO flights VALUES ('{0}', '{1}', '{2}', '{3}');".format(prefile['callsign'],
                                                                                 prefile['flight_plan']['departure'],
                                                                                 prefile['flight_plan']['arrival'], 'Y')
        print(sql)
        cur.execute(sql)

for controller in vatsim['controllers']:
    sql = "INSERT INTO controllers VALUES ('{0}', '{1}', '{2}', '{3}');".format(controller['callsign'],
                                                                             controller['logon_time'],
                                                                             controller['name'],
                                                                             controller['cid'])
    print(sql)
    cur.execute(sql)

# clean-up
con.commit()
con.close()



