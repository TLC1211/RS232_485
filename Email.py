import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

start_time = time.time()
message = MIMEMultipart()

def UploadFileToByte(Path, Name):
    with open("{}/{}".format(Path, Name), "rb") as file:
        part = MIMEApplication(file.read(), Name=Name)
        part["Contect-Disposition"] = "attachment; filename={name}".format(name=Name)
    return part

message["Subject"] = Header("Subject", "utf-8")#撰寫郵件標題
message["From"] = Header("Chiu", "utf-8")#寄件者(名稱或是副檔名)
message["To"] = Header("ToChiu", "utf-8")#收件者(名稱或是副檔名)
message["Cc"] = "nexstar1436@gmail.com,finnick37@gmail.com"#副本收件人1,副本收件人2

#文字呈現
# message.attach(MIMEText("txt send", "plain", "utf-8"))#("資料來源"，"資料來源類型"，"格式")

#網頁呈現
TestHtml = """"
<!DOCTYPE html>
<html>
<body>

<h2>HTML Table</h2>

<h2>Absolute URLs</h2>
<p><a href="https://www.w3.org/">W3C</a></p>
<p><a href="https://www.google.com/">Google</a></p>

<h2>Relative URLs</h2>
<p><a href="html_images.asp">HTML Images</a></p>
<p><a href="/css/default.asp">CSS Tutorial</a></p>

<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
  Sorry, your browser does not support inline SVG.
</svg>

<p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
For 50 years, WWF has been protecting the future of nature. The world's leading conservation organization, WWF works in 100 countries and is supported by 1.2 million members in the United States and close to 5 million globally.
</blockquote>


<table style="font-family: arial, sans-serif;border-collapse: collapse;width: 100%;">
  <tr>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Company</th>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Contact</th>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Country</th>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Alfreds Futterkiste</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;"><span style="font-size:100px">🐰🤞🤖👽🕜🕝🀄🔞</span></td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Germany</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Centro comercial Moctezuma</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Francisco Chang</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Mexico</td>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Ernst Handel</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Roland Mendel</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Austria</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Island Trading</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Helen Bennett</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">UK</td>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Laughing Bacchus Winecellars</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Yoshi Tannamuri</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Canada</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Magazzini Alimentari Riuniti</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;"><img src="https://www.w3schools.com/html/img_girl.jpg" alt="Girl in a jacket" style="width:100%;height:500px;"></td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Italy</td>
  </tr>
</table>

</body>
</html>
"""

message.attach(MIMEText(TestHtml, "html", "utf-8"))

#附件檔案
Tmp = [[".", "AA.txt"], [".", "BB.txt"], [".", "CC.txt"], [".", "DD.txt"], [".", "EE.txt"], [".", "FF.txt"], [".", "GG.txt"], [".", "HH.txt"], [".", "preheat.rar"]]
for n in range(0, len(Tmp)):
    message.attach(UploadFileToByte(Tmp[n][0], Tmp[n][1]))

msg = message.as_string()#將msg將text轉成str
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("t10830b609@ntut.org.tw", "ghisinfsxaprwuco")
from_addr = "t10830b609@ntut.org.tw"
to_addr = "m10803126@gapps.ntust.edu.tw"
status = smtp.sendmail(from_addr, to_addr, msg)
#加密文件，密免私密信息被截取
DoneStatus = False
if status == {}:
    DoneStatus = True
smtp.quit()

end_time = time.time()
print(DoneStatus)
print(f"發送時長為 : {end_time - start_time}")