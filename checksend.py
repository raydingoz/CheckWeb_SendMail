from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
import urllib.request
import json
import smtplib
import datetime
import locale
locale.setlocale(locale.LC_ALL)
today = datetime.date.today()

tarih1=""
tarih2=""
tarih3=""
eskitarih1=""
eskitarih2=""
eskitarih3=""

mail_1_alici = ['rafi57gerze@gmail.com','0901130315@ogr.iu.edu.tr']
bir_mesaj_1parca= """\
<html>
  <head></head>
  <body>
    <p>1. Sınıf Ders Programı Değişmiştir<br /><em>G&uuml;ncel Tarih: <span style="color: #ff0000;">
    </html>
"""
bir_mesaj_2parca = """\
<html>
 </span></em></p>
<p>İndirmek i&ccedil;in tıklayınız</p>
<p>(<a href="http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog1.pdf"><strong>pdf</strong></a>) (<a href="http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog1.doc"><strong>word</strong></a>)</p>
<p>&ccedil;alışmazsa: http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog1.doc</p>
<p style="text-align: center;"><strong><em>CerrahApp - raydingoz - 2017</em></strong></p>
<p>takip listesinden &ccedil;ıkmak i&ccedil;in <a href="https://goo.gl/forms/B8vRMOUuhz3dRrOG2">tıklayınız</a></p>
</html>
"""

mail_2_alici = ['rafi57gerze@gmail.com','0901130315@ogr.iu.edu.tr']
iki_mesaj_1parca= """\
<html>
  <head></head>
  <body>
    <p>2. Sınıf Ders Programı Değişmiştir<br /><em>G&uuml;ncel Tarih: <span style="color: #ff0000;">
    </html>
"""
iki_mesaj_2parca = """\
<html>
 </span></em></p>
<p>İndirmek i&ccedil;in tıklayınız</p>
<p>(<a href="http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog2.pdf"><strong>pdf</strong></a>) (<a href="http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog2.doc"><strong>word</strong></a>)</p>
<p>&ccedil;alışmazsa: http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog2.doc</p>
<p style="text-align: center;"><strong><em>CerrahApp - raydingoz - 2017</em></strong></p>
<p>takip listesinden &ccedil;ıkmak i&ccedil;in <a href="https://goo.gl/forms/B8vRMOUuhz3dRrOG2">tıklayınız</a></p>
</html>
"""

mail_3_alici = ['rafi57gerze@gmail.com','0901130315@ogr.iu.edu.tr']
uc_mesaj_1parca= """\
<html>
  <head></head>
  <body>
    <p>3. Sınıf Ders Programı Değişmiştir<br /><em>G&uuml;ncel Tarih: <span style="color: #ff0000;">
    </html>
"""
uc_mesaj_2parca = """\
<html>
 </span></em></p>
<p>İndirmek i&ccedil;in tıklayınız</p>
<p>(<a href="http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog3.pdf"><strong>pdf</strong></a>) (<a href="http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog3.doc"><strong>word</strong></a>)</p>
<p>&ccedil;alışmazsa: http://www.ctf.edu.tr/egitim_ogretim/ders/2017_2018/17_18_dersprog3.doc</p>
<p style="text-align: center;"><strong><em>CerrahApp - raydingoz - 2017</em></strong></p>
<p>takip listesinden &ccedil;ıkmak i&ccedil;in <a href="https://goo.gl/forms/B8vRMOUuhz3dRrOG2">tıklayınız</a></p>
</html>
"""


def website():
    url = "http://www.ctf.edu.tr/egitim_ogretim/dersprog.htm"
    url_oku = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_oku, 'html.parser')
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        sinif = str(tds[1].text)
        sinif = sinif.strip('\t\r\n')

        if (sinif == "1"):
            global tarih1
            tarih1 = str(tds[2].text)
            tarih1 = tarih1.strip('\t\r\n')
            print("web  : 1. sınıf        : " + tarih1)
        elif (sinif == "2"):
            global tarih2
            tarih2 = str(tds[2].text)
            tarih2 = tarih2.strip('\t\r\n')
            print("web  : 2. sınıf        : " + tarih2)
        elif (sinif == "3"):
            global tarih3
            tarih3 = str(tds[2].text)
            tarih3 = tarih3.strip('\t\r\n')
            print("web  : 3. sınıf        : " + tarih3)
def eskial():

    url = "____READ_DATA_API___.php"
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    print("")
    global eskitarih1
    eskitarih1 = data["api"][0]["deger"]
    print("eski : Birinci Sınıf   : "+data["api"][0]["deger"])

    global eskitarih2
    eskitarih2 = data["api"][1]["deger"]
    print("eski : İkinci Sınıf    : "+data["api"][1]["deger"])

    global eskitarih3
    eskitarih3 = data["api"][2]["deger"]
    print("eski : Üçüncü Sınıf    : "+data["api"][2]["deger"])
def yenitarihgir(bir,iki,uc):
    urllib.request.urlopen("____ADD_DATA_API___.php?bir="+bir+"&iki="+iki+"&uc="+uc).read()
def karsilastir():
    if (tarih1!=eskitarih1):
        print("bir eşit değil")
        yenitarihgir(tarih1,tarih2,tarih3)
        mailat(mail_1_alici,"Ders Programı",bir_mesaj_1parca + tarih1 + bir_mesaj_2parca)
    if (tarih2!=eskitarih2):
        print("iki eşit değil")
        yenitarihgir(tarih1,tarih2,tarih3)
        mailat(mail_1_alici,"Ders Programı",iki_mesaj_1parca+ tarih2+iki_mesaj_2parca)
    if (tarih3!=eskitarih3):
        print("üç eşit değil")
        yenitarihgir(tarih1,tarih2,tarih3)
        mailat(mail_1_alici,"Ders Programı",uc_mesaj_1parca+ tarih3+"d"+uc_mesaj_2parca+"tarih: "+today.strftime('%d %b'))
def mailat(alici,baslik, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("____EMAIL___", "___PASSWORD___")
        message = 'Subject: {}\n\n{}'.format(baslik, msg)
        m = MIMEText(msg.encode('utf-8'), 'html', 'utf-8')
        m['Subject'] = Header(baslik, 'utf-8')
        server.sendmail("____EMAIL___", alici, m.as_string())
        server.quit()
        print('mail başarıyla gönderildi')
    except Exception as e:
        print(e)
        print("mail gönderilirken hata")

website()
eskial()
karsilastir()
