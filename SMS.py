import requests
Url = "https://{DoMain}/API21/HTTP/SendSMS.ashx".format(DoMain="api.e8d.tw")
tmp = requests.post(
    Url, data={
        "UID" : "0972153032",
        "PWD" : "~!QAZ2wsx",
        "SB" : "",
        "MSG" : "您的驗證碼為: G-X56XX8".encode("utf-8"),
        "DEST" : "0972153032, 0937950891, 0933916108, 0971816355, 0952717700",
        "ST" : "",
        "RETRYTIME" : 1440
    }, headers={}, timeout=5
)
print(tmp.text)
查詢歷史紀錄
Url = 'https://{DoMain}/API21/HTTP/GetDeliveryStatus.ashx'.format(DoMain='api.e8d.tw')
tmp = requests.post(Url, data={
    'UID': '',
    'PWD': '',
    'BID': '6a8c8ad1-f7c3-42e9-80b1-2f605ff56cc6',
    'PNO': 1,
    'RESPFORMAT': 1
}, headers={}, timeout=5)
print(tmp.text)
查詢餘額
Url = 'https://{DoMain}/API21/HTTP/GetCredit.ashx'.format(DoMain='api.e8d.tw')
tmp = requests.post(Url, data={
    'UID': '0972153032',
    'PWD': '~!QAZ2wsx',
}, headers={}, timeout=5)
print(tmp.text)
