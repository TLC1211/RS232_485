#初始化
import json
import pymysql
import uuid
import time
from datetime import  datetime

db = pymysql.connect(
    host="127.0.0.1", port=3306,#192.168.137.1為本機IP，3306為MySQL用
    user="PLC", password="123123123",
    db="graphiccontrol"
)
db.autocommit = True
#PLC通訊參數設定
import minimalmodbus
import time
c = minimalmodbus.Instrument(port="COM5", slaveaddress=1)
c.serial.baudrate = 9600
c.serial.bytesize = 7
c.serial.parity = "E"
c.serial.stopbits = 1
c.serial.timeout = 1
c.mode = minimalmodbus.MODE_ASCII
# c.mode = minimalmodbus.MODE_RTU
c.clear_buffers_before_each_transaction = True
c.close_port_after_each_call = True

#讀回hand_trigger、hand_triggervlaue
Int_TimeStamp = int(time.time())
systime = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
with db.cursor() as cursor:
    command = "SELECT * FROM `bit_cells`"
    cursor.execute(command)
    db.commit()
    vals = cursor.fetchall()
    for n in vals:
        if n[4] == 1:
            if n[5] != 99:
                c.write_bit(
                    registeraddress=int(n[2], 16),
                    value=int(n[5]),
                    functioncode=5
                )
            with db.cursor() as cursor:
                command = "UPDATE `bit_cells` SET `HandTrigger` = '99' where `Guid`=%s;"
                cursor.execute(command, n[0])
                command = "UPDATE `bit_cells` SET `HandTriggerValue` = '99' where `Guid`=%s;"
                cursor.execute(command, n[0])
                db.commit()
                command = "UPDATE `bit_cells` SET `updated_at` = %s where `Guid`=%s;"
                cursor.execute(command, systime, n[0])
                db.commit()
    db.close()

