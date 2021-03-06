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

cur.execute("INSERT INTO positions VALUES('MIA', 'CTR', 'Miami Center')")
cur.execute("INSERT INTO positions VALUES('ZMO', 'CTR', 'Miami Oceanic')")
cur.execute("INSERT INTO positions VALUES('MIA', 'APP', 'Miami Approach')")
cur.execute("INSERT INTO positions VALUES('MIA', 'DEP', 'Miami Departure')")
cur.execute("INSERT INTO positions VALUES('TPA', 'APP', 'Tampa Approach')")
cur.execute("INSERT INTO positions VALUES('TPA', 'DEP', 'Tampa Departure')")
cur.execute("INSERT INTO positions VALUES('RSW', 'APP', 'Fort Myers Approach')")
cur.execute("INSERT INTO positions VALUES('RSW', 'DEP', 'Fort Myers Departure')")
cur.execute("INSERT INTO positions VALUES('PBI', 'APP', 'Palm Beach Approach')")
cur.execute("INSERT INTO positions VALUES('PBI', 'DEP', 'Palm Beach Departure')")
cur.execute("INSERT INTO positions VALUES('NQX', 'APP', 'Key West Approach')")
cur.execute("INSERT INTO positions VALUES('MIA', 'TWR', 'Miami Tower')")
cur.execute("INSERT INTO positions VALUES('MIA', 'GND', 'Miami Ground')")
cur.execute("INSERT INTO positions VALUES('MIA', 'DEL', 'Miami Delivery')")
cur.execute("INSERT INTO positions VALUES('FLL', 'TWR', 'Fort Lauderdale Tower')")
cur.execute("INSERT INTO positions VALUES('FLL', 'GND', 'Fort Lauderdale Ground')")
cur.execute("INSERT INTO positions VALUES('FLL', 'DEL', 'Fort Lauderdale Delivery')")
cur.execute("INSERT INTO positions VALUES('TMB', 'TWR', 'Tamiami Tower')")
cur.execute("INSERT INTO positions VALUES('TMB', 'GND', 'Tamiami Ground')")
cur.execute("INSERT INTO positions VALUES('TMB', 'DEL', 'Tamiami Delivery')")
cur.execute("INSERT INTO positions VALUES('OPF', 'TWR', 'Opa-Locka Tower')")
cur.execute("INSERT INTO positions VALUES('OPF', 'GND', 'Opa-Locka Ground')")
cur.execute("INSERT INTO positions VALUES('OPF', 'DEL', 'Opa-Locka Delivery')")
cur.execute("INSERT INTO positions VALUES('EYW', 'TWR', 'Key West Tower')")
cur.execute("INSERT INTO positions VALUES('EYW', 'GND', 'Key West Ground')")
cur.execute("INSERT INTO positions VALUES('PBI', 'TWR', 'Palm Beach Tower')")
cur.execute("INSERT INTO positions VALUES('PBI', 'GND', 'Palm Beach Ground')")
cur.execute("INSERT INTO positions VALUES('PBI', 'DEL', 'Palm Beach Delivery')")
cur.execute("INSERT INTO positions VALUES('TPA', 'TWR', 'Tampa Tower')")
cur.execute("INSERT INTO positions VALUES('TPA', 'GND', 'Tampa Ground')")
cur.execute("INSERT INTO positions VALUES('TPA', 'DEL', 'Tampa Delivery')")
cur.execute("INSERT INTO positions VALUES('SRQ', 'TWR', 'Sarasota Tower')")
cur.execute("INSERT INTO positions VALUES('SRQ', 'GND', 'Sarasota Ground')")
cur.execute("INSERT INTO positions VALUES('SRQ', 'DEL', 'Sarasota Delivery')")
cur.execute("INSERT INTO positions VALUES('RSW', 'TWR', 'Fort Myers Tower')")
cur.execute("INSERT INTO positions VALUES('RSW', 'GND', 'Fort Myers Ground')")
cur.execute("INSERT INTO positions VALUES('RSW', 'DEL', 'Fort Myers Delivery')")
cur.execute("INSERT INTO positions VALUES('RSW', 'TWR', 'Fort Myers Tower')")
cur.execute("INSERT INTO positions VALUES('RSW', 'GND', 'Fort Myers Ground')")
cur.execute("INSERT INTO positions VALUES('6FA', 'TWR', 'Gwinn Tower')")
cur.execute("INSERT INTO positions VALUES('6FA', 'GND', 'Gwinn Ground')")
cur.execute("INSERT INTO positions VALUES('APF', 'TWR', 'Naples Tower')")
cur.execute("INSERT INTO positions VALUES('APF', 'GND', 'Naples Ground')")
cur.execute("INSERT INTO positions VALUES('BCT', 'TWR', 'Boca Raton Tower')")
cur.execute("INSERT INTO positions VALUES('BCT', 'GND', 'Boca Raton Ground')")
cur.execute("INSERT INTO positions VALUES('BKV', 'TWR', 'Brooksville Tower')")
cur.execute("INSERT INTO positions VALUES('BOW', 'TWR', 'Bartow Tower')")
cur.execute("INSERT INTO positions VALUES('BOW', 'GND', 'Bartow Ground')")
cur.execute("INSERT INTO positions VALUES('FMY', 'TWR', 'Page Tower')")
cur.execute("INSERT INTO positions VALUES('FMY', 'GND', 'Page Ground')")
cur.execute("INSERT INTO positions VALUES('FPR', 'TWR', 'Fort Pierce Tower')")
cur.execute("INSERT INTO positions VALUES('FPR', 'GND', 'Fort Pierce Ground')")
cur.execute("INSERT INTO positions VALUES('FXE', 'TWR', 'Executive Tower')")
cur.execute("INSERT INTO positions VALUES('FXE', 'GND', 'Executive Ground')")
cur.execute("INSERT INTO positions VALUES('FXE', 'DEL', 'Executive Delivery')")
cur.execute("INSERT INTO positions VALUES('HST', 'TWR', 'Homestead Tower')")
cur.execute("INSERT INTO positions VALUES('HST', 'GND', 'Homestead Ground')")
cur.execute("INSERT INTO positions VALUES('LAL', 'TWR', 'Lakeland Tower')")
cur.execute("INSERT INTO positions VALUES('LAL', 'GND', 'Lakeland Ground')")
cur.execute("INSERT INTO positions VALUES('MCF', 'TWR', 'MacDill Tower')")
cur.execute("INSERT INTO positions VALUES('MCF', 'GND', 'MacDill Ground')")
cur.execute("INSERT INTO positions VALUES('PIE', 'TWR', 'St. Petersburg Tower')")
cur.execute("INSERT INTO positions VALUES('PIE', 'GND', 'St. Petersburg Ground')")
cur.execute("INSERT INTO positions VALUES('PIE', 'DEL', 'St. Petersburg Delivery')")
cur.execute("INSERT INTO positions VALUES('PGD', 'TWR', 'Punta Gorda Tower')")
cur.execute("INSERT INTO positions VALUES('PGD', 'GND', 'Punta Gorda Ground')")
cur.execute("INSERT INTO positions VALUES('PMP', 'TWR', 'Pompano Tower')")
cur.execute("INSERT INTO positions VALUES('PMP', 'GND', 'Pompano Ground')")
cur.execute("INSERT INTO positions VALUES('SPG', 'TWR', 'Whitted Tower')")
cur.execute("INSERT INTO positions VALUES('SPG', 'GND', 'Whitted Ground')")
cur.execute("INSERT INTO positions VALUES('SUA', 'TWR', 'Stuart Tower')")
cur.execute("INSERT INTO positions VALUES('SUA', 'GND', 'Stuart Ground')")
cur.execute("INSERT INTO positions VALUES('SUA', 'DEL', 'Stuart Delivery')")


# create message history table

cur.execute('''DROP TABLE history''')
cur.execute('''CREATE TABLE history (origin text, destination text, notification_time timestamp)''')



# create position activity table
cur.execute('''DROP TABLE position_activity''')
cur.execute('''CREATE TABLE position_activity (callsign text, cid text, controller_name text, status text, pos_name text)''')


# clean-up
con.commit()
con.close()
