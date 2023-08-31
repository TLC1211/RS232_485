import json

import pymysql
import uuid

from datetime import  datetime
import time
print(time.time())#timestamp
Int_TimeStamp = int(time.time())
print(datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S'))
db = pymysql.connect(
    host="127.0.0.1", port=3306,#192.168.137.1為本機IP，3306為MySQL用
    user="PLC", password="123123123",
    db="graphiccontrol"
)
db.autocommit = True

#建立資料庫
# with db.cursor() as cursor:
#     sql = """
#         CREATE TABLE `graphiccontrol`.`test` (
#     	`Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT'唯一碼',
#     	`Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT'姓名',
#     	`PostalCode` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT'郵遞區號',
#     	`Phone` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT'手機號碼',
#     	PRIMARY KEY (`Guid`(40)),
#     	INDEX (`Name`(40)),
#     	INDEX (`PostalCode`(40)),
#     	INDEX (`Phone`(40))
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci
#     """
#     cursor.execute(sql)
#     db.close()

#寫入資料表至資料表
# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `test`(`Guid`,`Name`,`PostalCode`,`Phone`)
#     VALUES('289150e0-5682-4f80-b908-f13fa36186ca','NB', '302', '0912345678');
#     """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print("Error!")
#         db.rollback()
#     db.close()

# #利用for迴圈寫入資料表
# with db.cursor() as cursor:
#     sql = "insert into `test` (`Guid`, `Name`, `PostalCode`, `Phone`) values (%s, %s, %s, %s)"
#     try:
#         for n in [
#             ["5c165c02-f6f7-4a7d-8934-30208e73a28d", "牛", "300", "0912345678"],
#             ["5c165c02-f6f7-4a7d-8934-30208e73a28e", "狗", "301", "0922345678"],
#             ["5c165c02-f6f7-4a7d-8934-30208e73a28f", "貓", "302", "0932345678"],
#             ["5c165c02-f6f7-4a7d-8934-30208e73a28g", "蛇", "303", "0942345678"]
#         ]:
#             cursor.execute(sql, (n[0], n[1], n[2], n[3]))
#             db.commit()
#     except:
#         print("Error!")
#         db.rollback()
#     db.close()

#取回一筆
# with db.cursor() as cursor:
#     command = "SELECT * FROM `test`"
#     cursor.execute(command)
#     db.commit()
#     vals = cursor.fetchone()
#     print(vals)#'5c165c02-f6f7-4a7d-8934-30208e73a28d', '牛', '300', '0912345678'
#     db.close()

#回顛倒再取回一筆
# with db.cursor() as cursor:
#     command = "SELECT * FROM `test` order by Phone desc "
#     cursor.execute(command)
#     db.commit()
#     vals = cursor.fetchone()
#     print(vals)
#     db.close()

#取回所有
# with db.cursor() as cursor:
#     # command = "SELECT * FROM `test` where `PostalCode` <= 303"
#     command = "SELECT * FROM `test` where `PostalCode` <= 303 and `phone` = 0932345678"
#     cursor.execute(command)
#     db.commit()
#     for n in cursor.fetchall():
#         print(n)
#     db.close()

#餵值
# tmp = []
# tmpi = 5
# for n in range(5):
#     tmp.append([str(uuid.uuid4()), tmpi * n, tmpi * n + 1, tmpi * n + 2])
#     tmpi += 1
# with db.cursor() as cursor:
#     sql = "insert into `test` (`Guid`, `Name`, `PostalCode`, `Phone`) VALUES (%s, %s, %s, %s)"
#     try:
#         for n in tmp:
#             cursor.execute(sql, (n[0], n[1], n[2], n[3]))
#             db.commit()
#     except:
#         db.rollback()

#加入序列
# with db.cursor() as cursor:
#     SQL = """
#         CREATE TABLE `graphiccontrol`.`ITOrder` (
#         `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#         `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '姓名',
#         `Price` INT UNSIGNED NOT NULL COMMENT '價錢',
#         `weight` INT UNSIGNED NOT NULL COMMENT '重量',
#         PRIMARY KEY (`Guid`),
#         INDEX (`Name`),
#         INDEX (`Price`),
#         INDEX (`weight`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#     cursor.execute(SQL)
#
# tmp = []
# TmpI = 5
# for n in range(20):
#     tmp.append([str(uuid.uuid4()), 'A{}'.format(n), n * 5 + 1, n * 5 + 2])
#     TmpI += 1
#
# with db.cursor() as cursor:
#     SQL = "INSERT INTO `ITOrder` (`Guid`, `Name`,`Price`,`weight`) values (%s, %s , %s, %s)"
#     for n in tmp:
#         cursor.execute(SQL, (n[0], n[1], int(n[2]), int(n[3])))
#         db.commit()
#
# with db.cursor() as cursor:
#     SQL = "select * from `ITOrder` order by Price desc"
#     # SQL = "select * from `ITOrder` where Price < 46"
#     # SQL = "select * from `ITOrder` where `Price` < 46 order by `Price` desc"
#     # SQL = "select * from `ITOrder` where (`Price` < 46) and (`weight` > 17)"
#     # SQL = "select * from `ITOrder` where (`Price` < 46) and (`weight` > 17) order by `Price` desc"
#     cursor.execute(SQL)
#     TmpX = cursor.fetchall()
#     print('(`Guid`, `Name`,`Price`,`weight`)')
#     for n in TmpX:
#         print(n)
# exit(0)

#更新資料1(修改狗-->DOG)
# with db.cursor() as cursor:
#     command = "UPDATE `test` SET `Name` = 'DOG' where `Guid`='5c165c02-f6f7-4a7d-8934-30208e73a28e';"
#     cursor.execute(command)
#     db.commit()
#     db.close()

#更新資料2(貓-->Cat)
# with db.cursor() as cursor:
#     command = "UPDATE `test` SET `Phone` = '0955555555' where `Guid`=%s;"
#     cursor.execute(command, '5c165c02-f6f7-4a7d-8934-30208e73a28d')
#     db.commit()
#     db.close()

#刪除資料
# with db.cursor() as cursor:
#     command = "delete from `test` where `Guid`=%s;"
#     cursor.execute(command, '5c165c02-f6f7-4a7d-8934-30208e73a28g')
#     db.commit()
#     db.close()

#--------------------------------------------------------------------------------------------
#PLC資料表建立

#1.資料表新增(bit_cells)
# with db.cursor() as cursor:
#     sql = """
#         CREATE TABLE `graphiccontrol`.`bit_cells`(
# `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
# `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
# `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
# `NowValue` TINYINT NOT NULL COMMENT '當下數值',
# `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
# `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
# `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
# `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
# `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
# `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
# `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY (`Guid`(40)),
# INDEX (`Name`(40)),
# INDEX (`Address`(40)),
# INDEX (`NowValue`),
# INDEX (`HandTrigger`),
# INDEX (`HandTriggerValue`)
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#         """
#     cursor.execute(sql)
#     db.close()
#資料寫入
# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `bit_cells`(
# `Guid`,
# `Name`,
# `Address`,
# `NowValue`,
# `HandTrigger`,
# `HandTriggerValue`,
# `CollectData`,
# `NotifyStatus`,
# `NotifyCollectData`,
# `created_at`,
# `updated_at`
# ) VALUES (
# '06fea5f1-5426-4470-b05b-30f3307c0639',
# 'Y0',
# '500',
# 0,
# 99,
# 99,
# '{}',
# 0,
# '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
# '2023-05-16 05:18:26',
# '2023-07-11 16:16:16'
# );"""
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print("Error!")
#         db.rollback()
#     db.close()

#利用for寫入MO~M6,Y1~Y12
# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `bit_cells`(
# `Guid`,
# `Name`,
# `Address`,
# `NowValue`,
# `HandTrigger`,
# `HandTriggerValue`,
# `CollectData`,
# `NotifyStatus`,
# `NotifyCollectData`,
# `created_at`,
# `updated_at`
# )
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
# """
#     try:
#         for n in [
#             ['0ef01a88-bb17-43b5-b1cd-9b4b413b67de', 'M0', '800', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['e7f36000-ae2a-476b-9da5-b0994107506d', 'M1', '801', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['870355d5-2bd2-443f-9725-1900069ba3f9', 'M2', '802', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['ae134e21-605f-4b17-b79c-c6f7d4d81bc0', 'M3', '803', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['1cadd753-097b-48f0-826d-0ee6e9b511a1', 'M4', '804', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['6e8e66d5-1345-4b40-84d6-739d3ce8b3c2', 'M5', '805', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['4644f644-be81-4015-a7bd-122b49de5670', 'M6', '806', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['5dd603d7-a83d-41fa-8ee6-5706315f832e', 'Y1', '501', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['21919f8c-72d3-4ffd-84a4-428279720201', 'Y2', '502', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['16a81116-2e7e-462b-a081-2021f6603a60', 'Y3', '503', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['293d88e5-4401-4250-9c52-91e7982c8cbb', 'Y4', '504', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['05a98649-488c-4124-bcb8-a725b42ca3f0', 'Y5', '505', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['184ecb46-5660-468b-aa64-60e7ec41361b', 'Y6', '506', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['f58b4857-f968-40e0-bc02-05dbe6f0b8d6', 'Y7', '507', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['0ed95206-635d-4854-9859-7a5a00631daa', 'Y10', '508', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['100ce918-6b9c-4f95-8851-cb788f2008d9', 'Y11', '509', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#             ['73cca88c-f042-4379-b2fc-1936fd43b9d1', 'Y12', '50A', '0', '99', '99', '{}', '0',
#              '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#              '2023-05-16 05:18:26',
#              '2023-07-11 16:16:16'
#              ],
#         ]:
#             cursor.execute(sql, (n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8], n[9], n[10]))
#             db.commit()
#     except:
#         print("Error!")
#         db.rollback()
#     db.close()

#建立資料表(chart_collects)
# with db.cursor() as cursor:
#     sql = """
#         CREATE TABLE `graphiccontrol`.`chart_collects`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址集合',
#     `Data` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `Collect` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '參數集合',
#     `Remark` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '備注',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40))
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
# """
#     cursor.execute(sql)
#     db.close()

#寫入資料(chart_collects)
# with db.cursor() as cursor:
#     sql = """
# INSERT INTO `chart_collects` (`Guid`, `Address`, `Data`, `Collect`, `Remark`, `created_at`, `updated_at`) VALUES
# ('576688f3-f773-4d04-98cd-dd113dd87d45','17E8,17E9', '{}', '{}', '折線圖', '2023-05-17 01:47:39', '2023-05-29 03:06:54'),
# ('a5f7af4d-f967-4258-8e6f-3382726aac6a','17E5,17E6,17E7', '{}', '{}', '圓餅圖','2023-05-17 02:27:32', '2023-05-17 02:27:32');"""
#     cursor.execute(sql)
#     db.commit()
#     db.close()

#建立資料表(chart_values)
# with db.cursor() as cursor:
#     sql = """
#         CREATE TABLE `graphiccontrol`.`chart_values`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#     `ChartCollectsGuid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '圖表設定唯一碼',
#     `TimeStamp` INT UNSIGNED NOT NULL COMMENT '當下秒數',
#     `Collect` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)), INDEX (`ChartCollectsGuid`(40)),
#     INDEX (`TimeStamp`)
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
# """
#     cursor.execute(sql)
#     db.close()

# #建立資料表(settings)
# with db.cursor() as cursor:
#     sql = """
#         CREATE TABLE  `graphiccontrol`.`settings` (
#     `Guid` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '全局唯一識別元',
#     `Name` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `CollectData` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)))ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
# """
#     cursor.execute(sql)
#     db.commit()
#     db.close()

#寫入資料表(settings)
# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `settings` (`Guid`, `Name`, `CollectData`, `created_at`, `updated_at`) VALUES
# ('427841f6-a5b5-4658-a4d7-105a5730124c', 'LoopTimes', '{\"ReTry\":3,\"LineNotifyLimitTime\":60}', '2023-05-16 05:28:18', '2023-05-29 04:28:28'),
# ('4605e414-192f-4667-82d1-fcbd2766255f', 'SMS', '{\"OwnPhone\":\"0972153032\",\"OwnPassword\":\"~!QAZ2wsx\",\"Group\":[{\"Phone\":\"0972153032\"}]}', '2023-05-16 05:28:18', '2023-05-31 02:02:10'),
# ('4650c0d7-ae99-40f0-9572-a3375c03e68d', 'Line', '{\"Group\":[{\"Token\":\"1FP4CFtj7O7cCX59jAfdLiu8GCqOu6Xe26Kd2v5ZgYk\"}]}', '2023-05-16 05:28:18', '2023-05-29 04:24:36'),
# ('e972137f-347a-41c7-b662-9a378de35211', 'Email', '{\"OwnEmail\":\"nexstar1436@gmail.com\",\"OwnPassword\":\"pzhuiybsqjrbbdgk\",\"Group\":[{\"ToEmail\":\"nexstar1436@gmail.com\"}]}', '2023-05-16 05:28:18', '2023-05-31 02:05:47');
# """
#     cursor.execute(sql)
#     db.commit()
#     db.close()

#建立資料表(v_strings)
# with db.cursor() as cursor:
#     sql = """
# CREATE TABLE `graphiccontrol`.`v_strings`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#     `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#     `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#     `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#     `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#     `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#     `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`Name`(40)),
#     INDEX (`Address`(40)),
#     INDEX (`NowValue`),
#     INDEX (`HandTrigger`),
#     INDEX (`HandTriggerValue`)
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
# """
#     cursor.execute(sql)
#     db.commit()
#     db.close()

#寫入資料(v_strings)
# with db.cursor() as cursor:
#     SQL = """
#          INSERT INTO `v_strings`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,'0',99,'99',
#             '{\"WordType\":\"String\",\"SignedType\":true,\"NumberOfRegisters\":1,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#             0,'{\"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#             %s,%s
#         )
#     """
#     for n in [
#         ['D2006', '17D6'], ['D2007', '17D7'], ['D2008', '17D8'], ['D2009', '17D9'], ['D2010', '17DA']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], Int_TimeStamp, Int_TimeStamp))
#         db.commit()
#     db.close()

#建立資料表(v_words)
# with db.cursor() as cursor:
#     sql = """
# CREATE TABLE `graphiccontrol`.`v_words`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#     `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#     `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#     `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#     `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#     `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#     `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`Name`(40)),
#     INDEX (`Address`(40)),
#     INDEX (`NowValue`),
#     INDEX (`HandTrigger`),
#     INDEX (`HandTriggerValue`)
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
# """
#     cursor.execute(sql)
#     db.commit()
#     db.close()

#寫入資料(v_words)
# with db.cursor() as cursor:
#     SQL = """
#         INSERT INTO `v_words`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,'0',99,'99',
#             '{\"WordType\":\"Word\",\"SignedType\":true,\"NumberOfDecimals\":0,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#             0,
#             '{\"NotifyPlatFrom\": 2, \"NotifyTimeStamp\": 1685327881, \"NotifyDateTime\": \"2023-05-29 10:38:01\"}',
#             %s,%s
#         )
#     """
#     for n in [
#         ['D2000', '17D0'], ['D2001', '17D1'], ['D2002', '17D2'], ['D2004', '17D4'],
#         ['D2021', '17E5'], ['D2022', '17E6'], ['D2023', '17E7'], ['D2024', '17E8'], ['D2025', '17E9']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], Int_TimeStamp, Int_TimeStamp))
#         db.commit()
#     db.close()

#--------------------------------------------------------------------------------------------
#Python + MySQL

#從bit.cells讀回M5
#數據集合為{"NotifyType": 1, "NotifyPlatFrom": 2, "NotifyTimeStamp": 0, "NotifyDateTime": 0}
with db.cursor() as cursor:
    # command = "SELECT * FROM `test` where `PostalCode` <= 303"
    command = "SELECT * FROM `bit_cells`" #取回graphiccontrrol下bit.cells表格所有資料
    cursor.execute(command)#執行command
    # db.commit() #insert、update、delete才需要使用讀回資料不需要
    for i in cursor.fetchall():
        if i[1] == "M5" and i[7] == 1:
            collecdata = json.loads(i[8])
            NotifyType = int(collecdata["NotifyType"])
            NotifyPlatFrom = int(collecdata["NotifyPlatFrom"])
            if NotifyType == 1 and NotifyPlatFrom == 2:
                print("LINE")
    db.close()