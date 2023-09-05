# ######################################RS485_LEVEL8######################################
# ######################################初始化#############################################
# import json
#
# import pymysql
# import time
# from datetime import datetime
#
#
# db = pymysql.connect(
#     host="127.0.0.1", port=3306,#192.168.137.1為本機IP，3306為MySQL用
#     user="PLC", password="123123123",
#     db="graphiccontrol"
# )
# db.autocommit = True
# ########################################################################################
# ######################################PLC通訊參數設定#####################################
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
# Int_TimeStamp = int(time.time())
# systime = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
#
#
#
#
# with db.cursor() as cursor:
#     print("Running...", systime)
#     command = "SELECT * FROM `bit_cells`"
#     cursor.execute(command)
#     db.commit()
#     vals = cursor.fetchall()
#     #讀取資料表
#     for n in vals:
#         notifydata = json.loads(n[8])
#         NotifyData_SMS = {}
#         NotifyData_Gmail = {}
#         NotifyData_LINE = {}
#         TmpX = c.read_bit(
#             registeraddress=int(n[2], 16),
#             functioncode=2
#         )
#         # if TmpX != notifydata["NotifyType"]:
#         #     continue
#         if n[7] != 1:
#             continue
#         if notifydata["NotifyTimeStamp"] > 60 or notifydata["NotifyTimeStamp"] <= 0:
#             print("continue")
#             continue
#         if notifydata["NotifyType"] == 0:#SMS
#             NotifyData_SMS = {"Name" : n[0], "Address" : n[2], "Type" : 0}
#         if notifydata["NotifyType"] == 1:#Gmail
#             NotifyData_Gmail = {"Name" : n[0], "Address" : n[2], "Type" : 0}
#         if notifydata["NotifyType"] == 2:#LINE
#             NotifyData_LINE = {"Name" : n[0], "Address" : n[2], "Type" : 0}
#         notifydata["NotifyTimeStamp"] = Int_TimeStamp
#         notifydata["NotifyDateTime"] = systime
#         UpdataPHP = json.dumps(notifydata)
#         command = "UPDATE `bit_cells` SET `NotifyCollectData` = %s WHERE `bit_cells`.`Guid` = %s;"
#         cursor.execute(command, (UpdataPHP, n[0]))
#         db.commit()
#     print(NotifyData_SMS)
#     print(NotifyData_LINE)
#     print(NotifyData_Gmail)




######################################老師版本######################################
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


def Send_LINE(Message):
    LineToken = 'wxA1etOMjdiFAjoKLpUuwqYKZTYnpAPh9BRoZ8QWMxi'
    requests.post('https://notify-api.line.me/api/notify',
                  params={"message": Message},
                  headers={
                      "Authorization": "Bearer " + LineToken,
                      "Content-Type": "application/x-www-form-urlencoded"}
                  )


def Send_SMS(Messge):
    Url = 'https://{DoMain}/API21/HTTP/SendSMS.ashx'.format(DoMain='api.e8d.tw')
    requests.post(Url, data={
        'UID': '0972153032',
        'PWD': '1qaz@WSX',
        'SB': '',
        'MSG': Messge.encode('utf-8'),
        'DEST': '0972153032',
        'ST': '',
        'RETRYTIME': 1440
    }, headers={}, timeout=5)


def Send_Email(Temp):
    message["Subject"] = Header('Subject', 'utf-8')  # 撰寫郵件標題
    message["From"] = Header('FromName', 'utf-8')  # 寄件者(名稱或是別名)
    message["To"] = Header('ToName', 'utf-8')  # 收件者(名稱或是別名)
    message["Cc"] = 't10830b609@ntut.org.tw,nexstar1436@gmail.com'  # 副本收件人1, 副本收件人2

    Html = '<!DOCTYPE html><html><body>' \
           '<h2 style="display: flex; justify-content: center; align-items: center;">警示 通知列表</h2>' \
           '<table style="font-family: arial, sans-serif;border-collapse: collapse;width: 100%;">' \
           '<thead><tr><th>元件名稱</th><th>元件地址</th></tr></thead>' + Temp + '</table></body></html>'

    # 文字呈現
    message.attach(MIMEText(Html, "html", "utf-8"))
    msg = message.as_string()  # 將msg將text轉成str
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('nexstar1436@gmail.com', 'pzhuiybsqjrbbdgk')
    from_addr = 'nexstar1436@gmail.com'
    to_addr = ['nexstar1436@gmail.com']
    status = smtp.sendmail(from_addr, (to_addr + ['t10830b609@ntut.org.tw', 'nexstar1436@gmail.com']),
                           msg)  # 加密文件，避免私密信息被截取
    DoneStatus = False
    if status == {}:
        DoneStatus = True
    smtp.quit()
    print(DoneStatus)


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
# while con.open:
NotifyArray = {"SMS": [], "Email": [], "Line": []}
with con.cursor() as cursor:
    command = "SELECT * FROM `bit_cells`"
    cursor.execute(command)
    con.commit()
    vals = cursor.fetchall()
    TmpOccurTimeStamp = int(time.time())
    TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
    for n in vals:
        TmpNotifyCollect = json.loads(n[8])
        TmpBitStatus = TmpRS485.Read_Bit(TmpAddress=n[2])
        if int(n[7]) != 1:  # 需被警示
            continue
        if int(TmpBitStatus) == int(TmpNotifyCollect['NotifyType']) and \
                TmpOccurTimeStamp - int(TmpNotifyCollect['NotifyTimeStamp']) > 60:
            TmpNotifyArray = {
                "BitCell_GUID": n[0],  # 唯一碼
                "Name": n[1],  # 元件名稱
                "Address": n[2],  # 元件地址
                "NotifyType": TmpNotifyCollect['NotifyType'],  # 警示類型
                "NotifyPlatFrom": TmpNotifyCollect['NotifyPlatFrom'],  # 發送平台
                "NowStatus": n[3],  # 當下狀態
                "OccurTimeStamp": TmpOccurTimeStamp,  # 當下秒數
                "OccurDate": TmpOccurDate  # 當下時間
            }
            if int(TmpNotifyCollect['NotifyPlatFrom']) == 0:  # SMS
                NotifyArray['SMS'].append(TmpNotifyArray)
            if int(TmpNotifyCollect['NotifyPlatFrom']) == 1:  # Email
                NotifyArray['Email'].append(TmpNotifyArray)
            if int(TmpNotifyCollect['NotifyPlatFrom']) == 2:  # Line
                NotifyArray['Line'].append(TmpNotifyArray)

    if len(NotifyArray['Line']) >= 1:
        TmpJson_NotifyCollectData = {'NotifyType': '', 'NotifyPlatFrom': '', 'NotifyTimeStamp': '',
                                     'NotifyDateTime': ''}
        StrMessage = '\n ----- 提醒 ----- \n'
        for key2, value2 in enumerate(NotifyArray['Line']):
            TmpJson_NotifyCollectData['NotifyType'] = int(value2['NotifyType'])
            TmpJson_NotifyCollectData['NotifyPlatFrom'] = int(value2['NotifyPlatFrom'])
            TmpJson_NotifyCollectData['NotifyTimeStamp'] = value2['OccurTimeStamp']
            TmpJson_NotifyCollectData['NotifyDateTime'] = value2['OccurDate']
            command = "UPDATE `bit_cells` SET `NotifyCollectData` = %s, `updated_at` = %s WHERE `Guid` = %s"
            cursor.execute(command,
                           (json.dumps(TmpJson_NotifyCollectData), value2['OccurDate'], value2['BitCell_GUID']))
            con.commit()
            StrMessage += '元件名稱: {} \n'.format(value2['Name'])
            StrMessage += '元件地址: {}'.format(value2['Address'])
        Send_LINE(StrMessage)

    if len(NotifyArray['Email']) >= 1:
        TmpJson_NotifyCollectData = {'NotifyType': '', 'NotifyPlatFrom': '', 'NotifyTimeStamp': '',
                                     'NotifyDateTime': ''}
        TrMessage = ''
        for key2, value2 in enumerate(NotifyArray['Email']):
            TmpJson_NotifyCollectData['NotifyType'] = int(value2['NotifyType'])
            TmpJson_NotifyCollectData['NotifyPlatFrom'] = int(value2['NotifyPlatFrom'])
            TmpJson_NotifyCollectData['NotifyTimeStamp'] = value2['OccurTimeStamp']
            TmpJson_NotifyCollectData['NotifyDateTime'] = value2['OccurDate']
            command = "UPDATE `bit_cells` SET `NotifyCollectData` = %s, `updated_at` = %s WHERE `Guid` = %s"
            cursor.execute(command,
                           (json.dumps(TmpJson_NotifyCollectData), value2['OccurDate'], value2['BitCell_GUID']))
            con.commit()
            TrMessage += '<tr>'
            TrMessage += '<th style="border: 1px solid #dddddd;text-align: center;padding: 8px;">' + value2[
                'Name'] + '</th>'
            TrMessage += '<th style="border: 1px solid #dddddd;text-align: center;padding: 8px;">' + value2[
                'Address'] + '</th>'
            TrMessage += '</tr>'
        Send_Email(TrMessage)

    # if len(NotifyArray['SMS']) >= 1:
    #     TmpJson_NotifyCollectData = {'NotifyType': '', 'NotifyPlatFrom': '', 'NotifyTimeStamp': '', 'NotifyDateTime': ''}
    #     StrMessage = '-- 提醒 -- '
    #     for key2, value2 in enumerate(NotifyArray['SMS']):
    #         TmpJson_NotifyCollectData['NotifyType'] = int(value2['NotifyType'])
    #         TmpJson_NotifyCollectData['NotifyPlatFrom'] = int(value2['NotifyPlatFrom'])
    #         TmpJson_NotifyCollectData['NotifyTimeStamp'] = value2['OccurTimeStamp']
    #         TmpJson_NotifyCollectData['NotifyDateTime'] = value2['OccurDate']
    #         command = "UPDATE `bit_cells` SET `NotifyCollectData` = %s, `updated_at` = %s WHERE `Guid` = %s"
    #         cursor.execute(command, (json.dumps(TmpJson_NotifyCollectData), value2['OccurDate'], value2['BitCell_GUID']))
    #         con.commit()
    #         StrMessage += '元件名稱: {}, 元件地址: {}'.format(value2['Name'], value2['Address'])
    #     Send_SMS(StrMessage)
print('Running... {}'.format(TmpOccurDate))
exit(0)
