import datetime
import os
import sqlite3
import discord.ext.commands
from discord.ext import commands, tasks
from dotenv import load_dotenv


class GroupFlight(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.group_flight_notifier.start()
        self.controller_notifier.start()

    def gf_unload(self):
        self.group_flight_notifier.cancel()
        self.controller_notifier.cancel()

    @tasks.loop(seconds=60.0)
    async def controller_notifier(self):
        print("executing controller notifier")
        con = sqlite3.connect('flights.db')
        cur = con.cursor()
        cur.execute("select callsign, controller_name, controller_cid from controllers;")
        controllers = cur.fetchall()
        cur.execute("select prefix, suffix, pos_name from positions;")
        positions = cur.fetchall()

        for position in positions:
            prefix = position[0]
            suffix = position[1]
            pos_name = position[2]
            for controller in controllers:
                callsign = controller[0]
                controller_name = controller[1]
                controller_cid = controller[2]
                if (callsign[:len(prefix)] == prefix) and (callsign[-len(suffix):] == suffix):
                    cur.execute("SELECT COUNT(*) FROM position_activity WHERE callsign = '{0}' and cid = '{1}' and status = 'A'".format(callsign, controller_cid))
                    record_count = cur.fetchone()
                    print(record_count[0])
                    if record_count[0] == 0:
                        cur.execute("DELETE FROM position_activity WHERE callsign = '{0}' and cid = '{1}'".format(callsign, controller_cid))
                        cur.execute("INSERT INTO position_activity VALUES ('{0}', '{1}', '{2}', 'A', '{3}')".format(callsign, controller_cid, controller_name, pos_name))
                        con.commit()
                        notice = "***Well, hello there!***  {0} (CID {1}) just signed on to {2} ({3}).".format(controller_name, controller_cid, pos_name, callsign)
                        channel = self.bot.get_channel(698739830611378249)
                        await channel.send(notice)

        sql = "select position_activity.callsign, position_activity.controller_name, position_activity.cid, position_activity.pos_name, coalesce(controllers.callsign, 'OFFLINE') is_active from position_activity left join controllers on position_activity.callsign = controllers.callsign and position_activity.cid = controllers.controller_cid where position_activity.status = 'A';"
        cur.execute(sql)
        onlines = cur.fetchall()

        for online in onlines:
            if online[4] == "OFFLINE":
                cur.execute("DELETE FROM position_activity WHERE callsign = '{0}' and cid = '{1}'".format(online[0], online[2]))
                con.commit()
                notice = "***Byyyeeeeeeeee.***  {0} (CID {1}) just signed off of {2} ({3}).".format(online[1], online[2], online[3], online[0])
                channel = self.bot.get_channel(698739830611378249)
                await channel.send(notice)

        cur.close()
        con.close()

    @tasks.loop(seconds=60.0)
    async def group_flight_notifier(self):
        print(self.index)
        con = sqlite3.connect('flights.db')
        cur = con.cursor()
        cur.execute("select origin, destination, count(*) from flights where origin IN (select icao from airports) OR destination IN (select icao from airports) group by origin, destination having count(*) > 5;")
        rows = cur.fetchall()
        cur.close()

        for row in rows:
            cur2 = con.cursor()
            cur2.execute("SELECT count(*) FROM history WHERE origin = '{0}' AND destination = '{1}' and cast((JulianDay('now') - JulianDay(notification_time)) * 24 * 60 As Integer) < 60".format(row[0], row[1]))
            previous_notifications = cur2.fetchone();
            if previous_notifications[0] == 0:
                notice = "***Sheeeesh!***  Group flight check... there are {0} aircraft filed from {1} to {2}.".format(row[2], row[0], row[1])
                channel = self.bot.get_channel(698739830611378249)
                await channel.send(notice)
                cur2.execute("INSERT INTO history VALUES ('{0}','{1}',datetime('now'))".format(row[0], row[1]))
                con.commit()
            self.index += 1
            cur2.close()

    @group_flight_notifier.before_loop
    async def before_group_flight_notifier(self):
        print('waiting to start group flight notifier...')
        await self.bot.wait_until_ready()

    @controller_notifier.before_loop
    async def before_controller_notifier(self):
        print('waiting to start controller notifier...')
        await self.bot.wait_until_ready()


load_dotenv()
DISCORD_KEY = os.environ.get("DISCORD_KEY")
my_bot = discord.ext.commands.Bot("!")
GroupFlight(my_bot)
my_bot.run(DISCORD_KEY)
