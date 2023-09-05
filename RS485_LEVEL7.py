# #RS485_LEVEL7
# #初始化
# import pymysql
# from datetime import  datetime
#
# db = pymysql.connect(
#     host="127.0.0.1", port=3306,#192.168.137.1為本機IP，3306為MySQL用
#     user="PLC", password="123123123",
#     db="graphiccontrol"
# )
# db.autocommit = True
#
# #PLC通訊參數設定
# import minimalmodbus
# import time
# c = minimalmodbus.Instrument(port="COM5", slaveaddress=1)
# c.serial.baudrate = 9600
# c.serial.bytesize = 7
# c.serial.parity = "E"
# c.serial.stopbits = 1
# c.serial.timeout = 1
# c.mode = minimalmodbus.MODE_ASCII
# # c.mode = minimalmodbus.MODE_RTU
# c.clear_buffers_before_each_transaction = True
# c.close_port_after_each_call = True
#
# while True:
#     Int_TimeStamp = int(time.time())
#     systime = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#     with db.cursor() as cursor:
#         print("Running...", systime)
#         command = "SELECT * FROM `v_words`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         for n in vals:
#             #Read
#             wordd = c.read_register(
#                         registeraddress=int(n[2], 16),
#                         number_of_decimals=0,
#                         functioncode=3,
#                         signed=True
#                     )
#             command = "UPDATE `v_words` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (wordd, systime, n[0]))
#             db.commit()
#             #Write
#             if n[4] != "1":
#                 continue
#             if n[5] == "99":
#                 continue
#             c.write_register(
#                 registeraddress=int(n[2], 16),
#                 value=n[5],
#                 number_of_decimals=0,
#                 signed=True,
#                 functioncode=6
#             )
#             command = "UPDATE `v_words` SET `HandTrigger` = %s,`HandTriggerValue` = %s, `NowValue` = %s, `updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (99, 99, n[5], systime, n[0]))
#             db.commit()

#########################################老師版本##############################################
import os
import json
import time
import pymysql
import uuid
import math
import minimalmodbus

from datetime import datetime

db_settings = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'PLC',
    "password": '123123123',
    "db": "graphiccontrol",
    "charset": "utf8"
}

con = pymysql.connect(**db_settings)
con.autocommit = True


class RS485:
    def __init__(self, port, SlaveAddress):
        self.minimalmodbus = minimalmodbus.Instrument(port=port, slaveaddress=SlaveAddress)
        self.minimalmodbus.serial.baudrate = 9600
        self.minimalmodbus.serial.bytesize = 7
        self.minimalmodbus.serial.parity = 'E'
        self.minimalmodbus.serial.stopbits = 1
        self.minimalmodbus.serial.timeout = 1
        self.minimalmodbus.mode = minimalmodbus.MODE_ASCII
        self.minimalmodbus.clear_buffers_before_each_transaction = True
        self.minimalmodbus.close_port_after_each_call = True

    def Read_Bit(self, TmpAddress):
        return self.minimalmodbus.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)

    def Write_Bit(self, TmpAddress, TmpBool):
        return self.minimalmodbus.write_bit(registeraddress=int(TmpAddress, 16), value=TmpBool, functioncode=5)

    def Read_Register(self, TmpAddress):
        return self.minimalmodbus.read_register(
            registeraddress=int(TmpAddress, 16),
            number_of_decimals=0,  # 1 2 3 4
            functioncode=3,
            signed=True
        )

    def Write_Register(self, TmpAddress, TmpValue):
        return self.minimalmodbus.write_register(
            registeraddress=int(TmpAddress, 16),
            value=TmpValue,
            number_of_decimals=0,  # 1 2 3 4
            functioncode=16,
            signed=True
        )


def Show(avg1, avg2, avg3):
    print('{} {} {}'.format(avg1, avg2, avg3))


TmpRS485 = RS485('COM5', 1)
while con.open:
    with con.cursor() as cursor:
        command = "SELECT * FROM `v_words`"
        cursor.execute(command)
        con.commit()
        vals = cursor.fetchall()
        TmpOccurTimeStamp = int(time.time())
        TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
        for n in vals:
            # Read
            command = "UPDATE `v_words` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
            cursor.execute(command, (TmpRS485.Read_Register(TmpAddress=n[2]), TmpOccurDate, n[0]))
            con.commit()
            # Write
            if int(n[4]) != 1:
                continue
            if int(n[5]) == 99:
                continue
            TmpRS485.Write_Register(TmpAddress=n[2], TmpValue=int(n[5]))
            command = "UPDATE `v_words` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at` = %s WHERE Guid = %s"
            cursor.execute(command, (99, 99, TmpOccurDate, n[0]))
            con.commit()
    print('Running... {}'.format(TmpOccurDate))
exit(0)
