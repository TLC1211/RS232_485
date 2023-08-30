import pymysql
import uuid
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
#     	`Price` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT'郵遞區號',
#     	`Weight` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT'手機號碼',
#     	PRIMARY KEY (`Guid`(40)),
#     	INDEX (`Name`(40)),
#     	INDEX (`Price`(40)),
#     	INDEX (`Weight`(40))
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

#利用for迴圈寫入資料表
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
with db.cursor() as cursor:
    SQL = """
        CREATE TABLE `graphiccontrol`.`ITOrder` (
        `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
        `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '姓名',
        `Price` INT UNSIGNED NOT NULL COMMENT '價錢',
        `weight` INT UNSIGNED NOT NULL COMMENT '重量',
        PRIMARY KEY (`Guid`),
        INDEX (`Name`),
        INDEX (`Price`),
        INDEX (`weight`)
    ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
    """
    cursor.execute(SQL)

tmp = []
TmpI = 5
for n in range(20):
    tmp.append([str(uuid.uuid4()), 'A{}'.format(n), n * 5 + 1, n * 5 + 2])
    TmpI += 1

with db.cursor() as cursor:
    SQL = "INSERT INTO `ITOrder` (`Guid`, `Name`,`Price`,`weight`) values (%s, %s , %s, %s)"
    for n in tmp:
        cursor.execute(SQL, (n[0], n[1], int(n[2]), int(n[3])))
        db.commit()

with db.cursor() as cursor:
    SQL = "select * from `ITOrder` order by Price desc"
    # SQL = "select * from `ITOrder` where Price < 46"
    # SQL = "select * from `ITOrder` where `Price` < 46 order by `Price` desc"
    # SQL = "select * from `ITOrder` where (`Price` < 46) and (`weight` > 17)"
    # SQL = "select * from `ITOrder` where (`Price` < 46) and (`weight` > 17) order by `Price` desc"
    cursor.execute(SQL)
    TmpX = cursor.fetchall()
    print('(`Guid`, `Name`,`Price`,`weight`)')
    for n in TmpX:
        print(n)
exit(0)