#通訊參數設定
import minimalmodbus
import time
c = minimalmodbus.Instrument(port="COM5", slaveaddress=4)
c.serial.baudrate = 9600
c.serial.bytesize = 7
c.serial.parity = "E"
c.serial.stopbits = 1
c.serial.timeout = 1
c.mode = minimalmodbus.MODE_ASCII
#c.mode = minimalmodbus.MODE_RTU
c.clear_buffers_before_each_transaction = True
c.close_port_after_each_call = True
start_time = time.time()
#寫入站存器
# c.write_bit(
#     registeraddress=int("800", 16),
#     value=1,
#     functioncode=5
# )
# #讀取站存器
# TmpX = c.read_bit(
#     registeraddress=int("800", 16),
#     functioncode=2
# )
#print(TmpX)
#寫入多的暫存器
# TmpX_1 = [0, 1, 1, 0, 1, 1, 0, 1, 0]
# TmpX_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
# TmpX_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# c.write_bits(
#     registeraddress=int("800",16),
#     values=TmpX_2
# )
#讀取多個位
# TmpX = c.read_bits(
#     registeraddress=int("0800",16),
#     number_of_bits=9,
#     functioncode=2
# )
# print(TmpX)
# print(type(TmpX))
#練習一

# TmpArray = []
# for index in range(0,30):
#     if index % 2 == 0:
#         TmpArray.append(0)
#     else:
#         TmpArray.append(1)
# c.write_bits(
#     registeraddress=int("800", 16),
#     values=TmpArray
# )
# print(TmpArray)
# print(len(TmpArray))
#寫入16位寄存器
# Tmp2 = 16706
# c.write_register(
#     registeraddress=int("17D0", 16),
#     value=Tmp2,
#     number_of_decimals=0,
#     signed=True,
#     functioncode=6
# )
#讀取16位寄存器
# Tmp = c.read_register(
#     registeraddress=int("17D0",16),
#     number_of_decimals=2,
#     functioncode=3,
#     signed=True
# )
# print(Tmp)
#文字>十六進制>10進制
# for xx in ["&", "~", "&~"]:
#     Tmp2 = int(xx.encode("utf-8").hex(),16)
#     print(Tmp2)
#寫入ASCII字串
# c.write_string(
#     registeraddress=int("17D0", 16),
#     textstring="AB",
#     number_of_registers=1
# )
#讀取ASCII
Tmp = c.read_string(
    registeraddress=int("17D0", 16),
    number_of_registers=1,
    functioncode=3
)
print(Tmp)