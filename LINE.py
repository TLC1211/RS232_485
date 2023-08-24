import json
import requests

Message = "XD"
LineToken = "wxA1etOMjdiFAjoKLpUuwqYKZTYnpAPh9BRoZ8QWMxi"
TmpX = requests.post(
    "https://notify-api.line.me/api/notify",
    params={"message": Message},
    headers={
        "Authorization": "Bearer " + LineToken,
        "Content-Type": "application/x-www-urlencoded"
    }

)
print(TmpX.text)
print(type(TmpX.text))
print(json.loads(TmpX.text))
print(type(json.loads(TmpX.text)))
print(json.loads(TmpX.text)["status"])