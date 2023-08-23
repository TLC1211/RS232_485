from pyModbusTCP.client import ModbusClient
import time
c = ModbusClient(
    host="192.168.1.5",
    port=502,
    auto_open=True,
    unit_id=1,
    timeout=1,
    debug=False
)
start_time = time.time()
#寫入單筆Bit
#-----------------------------
# s = c.write_single_coil(
#     bit_addr=int("500", 16),
#     bit_value=False
# )
# print(s)
#寫入多筆Bits
#-----------------------------
# bits_value=[True, False, True]
# s = c.write_multiple_coils(
#     bits_addr=int("800", 16),
#     bits_value=bits_value
# )
#讀出多筆Bits
#-----------------------------
# s = c.read_coils(
#     bit_addr=int("800", 16),
#     bit_nb=3
# )
# print(s)
#寫入單筆數值
#-----------------------------
# s = c.write_single_register(
#     reg_addr=int("17D0",16),
#     reg_value=18489
# )
# print(s)
#寫多筆數值
#-----------------------------
# OriginalArray = ["AB", "CD", "EF", "GH", "IJ",
#                  "KL", "MN", "OP", "QR", "ST",
#                  "UV", "WX", "YZ","ab", "cd",
#                  "ef", "gh", "ij", "kl", "mn",
#                  "op", "qr", "st", "uv", "wx",
#                  "yz", "01", "23", "45", "67",
#                  "89", "~@", "#$", "%^", "&*",
#                  "()", "_+", "<>", "?/"
#                  ]
# TmpArray = []
# MaxIndex = len(OriginalArray)
#
# for index1, value1 in enumerate(OriginalArray):
#     Tmp2 = int(value1.encode("utf-8").hex(),16)
#     TmpArray.append(Tmp2)
#
# s = c.write_multiple_registers(
#     regs_addr=int("17D0", 16),
#     regs_value=TmpArray
# )
#
# s = c.read_holding_registers(
#     reg_addr=int("17D0", 16),
#     reg_nb=100
# )
# end_time = time.time()
# print(f'寫入時間為 : {(end_time - start_time)}')
#寫入讀取練習
Tmp = []
i = 15
for n in range(0,100):
    i +=1
    Tmp.append(i)
c.write_multiple_registers(
    regs_addr=int("17D0", 16),
    regs_value=Tmp
)
s = c.read_holding_registers(
    reg_addr=int("17D0", 16),
    reg_nb=100
)

TmpArray = []
for index, value in enumerate(s):
    if value != 0:
        Tmp1 = hex(value)[2:]
        TmpArray.append(bytes.fromhex(Tmp1).decode("utf-8"))
    else:
        TmpArray.append(value)
print(TmpArray)
end_time = time.time()
print(Tmp)
print(f'寫入以及讀取的時間為 : {(end_time - start_time)}')