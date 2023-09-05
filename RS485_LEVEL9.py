# # ######################################RS485_LEVEL8######################################
# # ######################################初始化#############################################
# import json
# import pymysql
# import time
# from datetime import datetime
#
# db = pymysql.connect(
#     host="127.0.0.1", port=3306,#192.168.137.1為本機IP，3306為MySQL用
#     user="PLC", password="123123123",
#     db="graphiccontrol"
# )
# db.autocommit = True
# Int_TimeStamp = int(time.time())
# systime = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
# #讀取SQL`v_words`
# with db.cursor() as cursor:
#     print("Running...", systime)
#     command = "SELECT * FROM `v_words`"
#     cursor.execute(command)
#     db.commit()
#     vals_1 = cursor.fetchall()
#     TmpAddress1 = {}
#     ListAddress1 = []
#     for i in vals_1:
#         TmpAddress1 = {"Name" : str(i[1]), "Address" : str(i[2])}
#         ListAddress1.append(TmpAddress1)
#     print(ListAddress1)
# ##讀取SQL`chart_collects`
#     TmpAddress2 = {}
#     ListAddress2 = []
#     command = "SELECT * FROM `chart_collects`"
#     cursor.execute(command)
#     db.commit()
#     vals_2 = cursor.fetchall()
#     for j in vals_2:
#         for k in j[1].split(","):
#             print(k)
#             TmpAddress2[str(k)] = {
#                 "Name" : TmpAddress1[k]["Name"],
#                 "Address" : TmpAddress1[k]["Address"],
#                 "Value" : 0,
#             }
#         if not TmpAddress1.get(k) is None:
#             TmpAddress2[k] = {
#                 "Name" : TmpAddress1[k]["Name"],
#                 "Address" : TmpAddress1[k]["Address"],
#                 "Value" : TmpAddress1[k]["Value"],
#             }
# print(TmpAddress1)

##########################################老師版本##################################################
import os
import json
import time
import pymysql
import uuid
import math
import minimalmodbus
import requests
from datetime import datetime

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

message = MIMEMultipart()

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


TmpRS485 = RS485(port="COM5", SlaveAddress=1)
while con.open:
    ChartValue = {}
    with con.cursor() as cursor:
        command = "SELECT * FROM `v_words`"
        cursor.execute(command)
        con.commit()
        vals = cursor.fetchall()
        for n in vals:
            TmpNotifyCollect = json.loads(n[8])
            TmpRegisterValue = TmpRS485.Read_Register(TmpAddress=n[2])
            ChartValue[n[2]] = {
                'Guid': n[0], 'Name': n[1], 'Address': n[3],
                'Value': int(TmpRegisterValue), 'Type': 'Word'
            }

        command = "SELECT * FROM `chart_collects`"
        cursor.execute(command)
        con.commit()
        for key1, value1 in enumerate(cursor.fetchall()):
            TmpOccurTimeStamp = int(time.time())
            TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
            TmpGuid = value1[0]
            TmpAddress = value1[1]

            NewChartValue = {}
            for key2, value2 in enumerate(TmpAddress.split(',')):
                NewChartValue[value2] = {
                    'Name': ChartValue[value2]['Name'],
                    'Address': ChartValue[value2]['Address'],
                    'Value': 0,
                }
                if not ChartValue.get(value2) is None:
                    NewChartValue[value2] = {
                        'Name': ChartValue[value2]['Name'],
                        'Address': ChartValue[value2]['Address'],
                        'Value': ChartValue[value2]['Value'],
                    }
            command = "INSERT INTO `chart_values`(`Guid`, `ChartCollectsGuid`, `TimeStamp`, `Collect`, `created_at`, `updated_at`)VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(command, (str(uuid.uuid4()), TmpGuid, TmpOccurTimeStamp, json.dumps(NewChartValue), TmpOccurDate, TmpOccurDate))
            con.commit()
    print('Running... {}'.format(TmpOccurDate))
exit(0)