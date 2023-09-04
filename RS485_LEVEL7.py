#RS485_LEVEL7
#初始化
import pymysql
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

while True:
    Int_TimeStamp = int(time.time())
    systime = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
    with db.cursor() as cursor:
        command = "SELECT * FROM `v_words`"
        cursor.execute(command)
        db.commit()
        vals = cursor.fetchall()
        for n in vals:
            wordd = c.read_register(
                        registeraddress=int(n[2], 16),
                        number_of_decimals=2,
                        functioncode=3,
                        signed=True
                    )
            ddin = int(wordd * 100)
            print(ddin)
            command = "UPDATE `v_words` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
            cursor.execute(command, (ddin, systime, n[0]))
            db.commit()