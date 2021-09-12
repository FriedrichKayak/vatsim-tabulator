import sqlite3

# create (or open) the database and connect to it
con = sqlite3.connect('flights.db')
cur = con.cursor()

# create flights table
cur.execute('''DROP TABLE flights''')
cur.execute('''CREATE TABLE flights (callsign text, origin text, destination text, prefile text)''')

# create controller table
cur.execute('''DROP TABLE controllers''')
cur.execute('''CREATE TABLE controllers (callsign text, logon_date text, controller_name text, controller_cid text)''')

# create airports of interest table
cur.execute('''DROP TABLE airports''')
cur.execute('''CREATE TABLE airports (icao text)''')

cur.execute("INSERT INTO airports VALUES ('X06')")
cur.execute("INSERT INTO airports VALUES ('07FA')")
cur.execute("INSERT INTO airports VALUES ('06FA')")
cur.execute("INSERT INTO airports VALUES ('KAVO')")
cur.execute("INSERT INTO airports VALUES ('KAGR')")
cur.execute("INSERT INTO airports VALUES ('KBOW')")
cur.execute("INSERT INTO airports VALUES ('X10')")
cur.execute("INSERT INTO airports VALUES ('KBCT')")
cur.execute("INSERT INTO airports VALUES ('KBKV')")
cur.execute("INSERT INTO airports VALUES ('X05')")
cur.execute("INSERT INTO airports VALUES ('KCLW')")
cur.execute("INSERT INTO airports VALUES ('2IS')")
cur.execute("INSERT INTO airports VALUES ('X36')")
cur.execute("INSERT INTO airports VALUES ('X01')")
cur.execute("INSERT INTO airports VALUES ('KFLL')")
cur.execute("INSERT INTO airports VALUES ('FXE')")
cur.execute("INSERT INTO airports VALUES ('KFMY')")
cur.execute("INSERT INTO airports VALUES ('KRSW')")
cur.execute("INSERT INTO airports VALUES ('KFPR')")
cur.execute("INSERT INTO airports VALUES ('KHWO')")
cur.execute("INSERT INTO airports VALUES ('KHST')")
cur.execute("INSERT INTO airports VALUES ('X51')")
cur.execute("INSERT INTO airports VALUES ('KIMM')")
cur.execute("INSERT INTO airports VALUES ('KEYW')")
cur.execute("INSERT INTO airports VALUES ('KNQX')")
cur.execute("INSERT INTO airports VALUES ('X14')")
cur.execute("INSERT INTO airports VALUES ('X49')")
cur.execute("INSERT INTO airports VALUES ('KLAL')")
cur.execute("INSERT INTO airports VALUES ('X07')")
cur.execute("INSERT INTO airports VALUES ('X25')")
cur.execute("INSERT INTO airports VALUES ('KMTH')")
cur.execute("INSERT INTO airports VALUES ('KMKY')")
cur.execute("INSERT INTO airports VALUES ('KTMB')")
cur.execute("INSERT INTO airports VALUES ('KTNT')")
cur.execute("INSERT INTO airports VALUES ('KMIA')")
cur.execute("INSERT INTO airports VALUES ('KOPF')")
cur.execute("INSERT INTO airports VALUES ('KAPF')")
cur.execute("INSERT INTO airports VALUES ('KOBE')")
cur.execute("INSERT INTO airports VALUES ('KPHK')")
cur.execute("INSERT INTO airports VALUES ('KPCM')")
cur.execute("INSERT INTO airports VALUES ('KPMP')")
cur.execute("INSERT INTO airports VALUES ('KSPG')")
cur.execute("INSERT INTO airports VALUES ('KPIE')")
cur.execute("INSERT INTO airports VALUES ('KSRQ')")
cur.execute("INSERT INTO airports VALUES ('X26')")
cur.execute("INSERT INTO airports VALUES ('KSEF')")
cur.execute("INSERT INTO airports VALUES ('KSUA')")
cur.execute("INSERT INTO airports VALUES ('KTPA')")
cur.execute("INSERT INTO airports VALUES ('KVDF')")
cur.execute("INSERT INTO airports VALUES ('KMCF')")
cur.execute("INSERT INTO airports VALUES ('X39')")
cur.execute("INSERT INTO airports VALUES ('KTPF')")
cur.execute("INSERT INTO airports VALUES ('KVNC')")
cur.execute("INSERT INTO airports VALUES ('X52')")
cur.execute("INSERT INTO airports VALUES ('KVRB')")
cur.execute("INSERT INTO airports VALUES ('KCHN')")
cur.execute("INSERT INTO airports VALUES ('F45')")
cur.execute("INSERT INTO airports VALUES ('KPBI')")
cur.execute("INSERT INTO airports VALUES ('KLNA')")
cur.execute("INSERT INTO airports VALUES ('KGIF')")
cur.execute("INSERT INTO airports VALUES ('KZPH')")

# create positions of interest table
cur.execute('''DROP TABLE positions''')
cur.execute('''CREATE TABLE positions (prefix text, suffix text, pos_name text)''')

cur.execute("INSERT INTO positions VALUES ('MIA', 'APP', 'Miami Approach')")
cur.execute("INSERT INTO positions VALUES ('JAX', 'CTR', 'Jacksonville Center')")
cur.execute("INSERT INTO positions VALUES ('MIA', 'CTR', 'Miami Center')")
cur.execute("INSERT INTO positions VALUES ('BCT', 'GND', 'Boca Raton Ground')")


# create message history table

cur.execute('''DROP TABLE history''')
cur.execute('''CREATE TABLE history (origin text, destination text, notification_time timestamp)''')


# create position activity table
cur.execute('''DROP TABLE position_activity''')
cur.execute('''CREATE TABLE position_activity (callsign text, cid text, controller_name text, status text, pos_name text)''')


# clean-up
con.commit()
con.close()
