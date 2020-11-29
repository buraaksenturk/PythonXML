########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#           2019-2020 Sezonu Futbolcu Bilgisi          #
#                XML uzantılı bir dosyada              #
#                    saklama programı                  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################
#~~~~~~~~~~~~~~~~~~YAZAN:BURAK ŞENTÜRK~~~~~~~~~~~~~~~~~#

# Kullanılacak Olan Kütüphaneler #
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree
from xml.dom.minidom import parseString
import sys
import defusedxml.ElementTree as dET
import time

# Kullanıcıyı Karşılama Kısmı
print("""
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #               Merhaba Sayın Kullanıcı,               #
        #                yapmak istediği işlem                 #
        #                Kayıt Ekleme ise => 1                 #
        #             Kayıt Kontrol etme ise => 2              #
        #          uygulamadan çıkmak için ise => 3            #
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        """)
deger = int(input("Yapmak istediğiniz işlemi yazınız => "))

# Kayıt Ekleme Kısmı #
if deger == 1:
    print("""
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #                   Kayıt Ekleme Alanı                 #
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        """)
    time.sleep(1)

    # Kayıt adeti sorgulama (Döngü istenilen adet kadar dönecek!)
    kayitAdet = int(input("Kaç kayıt ekleyeceksiniz? "))

    # Uyarı Alanı#
    print("Sorulacak soruları futbolcunun bilgilerine göre doldurunuz!")

    for futbolcu in range(kayitAdet):
        # Değişken Atamaları #
        ad_soyad = input("Adını ve soyadını giriniz: ")
        yas = int(input("Yaşını giriniz: "))
        ulke = input("Hangi ülkenin vatandaşı olduğunu giriniz: ")
        mevkii = input("Mevkisini giriniz: ")
        takim = input("Oynadığı takımın adını giriniz: ")
        takimtd = input("Oynadığı takımın teknik direktörünün adını giriniz: ")
        lig = input("Oynadığı ligin adını giriniz: ")
        ilk_11_oynama = int(input("İlk 11 oynadığı maç sayısını giriniz: "))
        gol_sayisi = int(input("Toplam gol sayısını giriniz: "))
        asist_sayisi = int(input("Toplam asist sayısını giriniz: "))
        kirmizi_kart_sayisi = int(
            input("Toplam kırmızı kart sayısını giriniz: "))
        sari_kart_sarisi = int(input("Toplam sarı kart sayısını giriniz: "))
        kiralik_mi = input("Oyuncu takıma kiralık mı geldi? ")

        def futbolcu_bilgileri(ad_soyad, yas, ulke, mevkii, takim, takimtd, lig, ilk_11_oynama, gol_sayisi, asist_sayisi, kirmizi_kart_sayisi, sari_kart_sayisi, kiralik_mi):
            futbolcu = Element('futbolcu')
            futbolcu.set('adsoyad', ad_soyad)
            yas_alani = ET.SubElement(futbolcu, 'yas')
            yas_alani.text = str(yas)
            ulke_alani = ET.SubElement(futbolcu, 'ulke')
            ulke_alani.text = str(ulke)
            mevkii_alani = ET.SubElement(futbolcu, 'mevkii')
            mevkii_alani.text = str(mevkii)
            takim_alani = ET.SubElement(futbolcu, 'takim')
            takim_alani.text = str(takim)
            takimtd_alani = ET.SubElement(futbolcu, 'takimteknikdirektoru')
            takimtd_alani.text = str(takimtd)
            lig_alani = ET.SubElement(futbolcu, 'lig')
            lig_alani.text = str(lig)
            ilk_11_oynama_alani = ET.SubElement(futbolcu, 'ilk_11_oynama')
            ilk_11_oynama_alani.text = str(ilk_11_oynama)
            gol_sayisi_alani = ET.SubElement(futbolcu, 'gol_sayisi')
            gol_sayisi_alani.text = str(gol_sayisi)
            asist_sayisi_alani = ET.SubElement(futbolcu, 'asist_sayisi')
            asist_sayisi_alani.text = str(asist_sayisi)
            kirmizi_kart_sayisi_alani = ET.SubElement(
                futbolcu, 'kirmizi_kart_sayisi')
            kirmizi_kart_sayisi_alani.text = str(kirmizi_kart_sayisi)
            sari_kart_sayisi_alani = ET.SubElement(
                futbolcu, 'sari_kart_sayisi')
            sari_kart_sayisi_alani.text = str(sari_kart_sayisi)
            kiralik_mi_alani = ET.SubElement(futbolcu, 'kiralik_mi')
            kiralik_mi_alani.text = str(kiralik_mi)

            return futbolcu

    futbolcular = [
        {
            "ad_soyad": ad_soyad,
            "yas": yas,
            "ulke": ulke,
            "mevkii": mevkii,
            "takim": takim,
            "takimtd": takimtd,
            "lig": lig,
            "ilk_11_oynama": ilk_11_oynama,
            "gol_sayisi": gol_sayisi,
            "asist_sayisi": asist_sayisi,
            "kirmizi_kart_sayisi": kirmizi_kart_sayisi,
            "sari_kart_sayisi": sari_kart_sarisi,
            "kiralik_mi": kiralik_mi
        }
    ]

    root = Element('futbolcular')

    for futbolcu in futbolcular:
        futbolcu_alani = futbolcu_bilgileri(**futbolcu)
        root.append(futbolcu_alani)

    # Futbolcu Çıktısı Oluşturma
    tree = ElementTree(element=root)
    tree.write("futbolcular_ciktisi.xml",
               encoding="UTF-8", xml_declaration=True)

    # Futbolcu Çıktısı XML - Başlangıcı
    xml_duzenleme = ET.tostring(root)
    dom = parseString(xml_duzenleme)

    duzenlenmis_xml = dom.toprettyxml(encoding="UTF-8")
    with open("duzenlenmis_cikti.xml", "ab") as f:
        f.write(duzenlenmis_xml)

# Kayıt Kontrol Kısmı #
elif deger == 2:
    print("""
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #                   Kayıt Kontrol Alanı                #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    """)
    time.sleep(1)
    kontrol = input(
        "Kontrol etmek istediğiniz kaydın ad soyadını giriniz: ")

    file_name = "duzenlenmis_cikti.xml"

    try:
        data = dET.parse(file_name)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        sys.exit(1)
    root = data.getroot()
    print("""
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #                Yaşını öğrenmek için => 1               #
    #    Hangi ülke vatandaşı olduğunu öğrenmek için => 2    #
    #               Mevkisini öğrenmek için => 3             #
    #           Oynadığı takımı öğrenmek için => 4           #
    # Oynadığı takımın teknik direktörünü öğrenmek için => 5 #
    #            Oynadığı ligi öğrenmek için => 6            #
    #       İlk 11 oynama sayısını öğrenmek için => 7        #
    #        Toplam gol sayısını öğrenmek için => 8          #
    #       Toplam asist sayısını öğrenmek için => 9         #
    #    Toplam kırmızı kart sayısını öğrenmek için => 10    #
    #      Toplam sarı kart sayısını öğrenmek için => 11     #
    #         Kiralık mı olduğunu öğrenmek için => 12        #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    """)

    # Sergilenmek  istenen kısmın seçildiği alan#
    alanf = input(
        "Bu futbolcuya ait hangi bilgiyi kontrol etmek istersiniz?")

    # Yaş Kontrol Kısmı #
    if alanf == "1":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/yas')
        print(kontrol_model)

    # Ülke Kontrol Kısmı #
    elif alanf == "2":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/ulke')
        print(kontrol_model)

    # Mevkii Kontrol Kısmı #
    elif alanf == "3":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/mevkii')
        print(kontrol_model)

    # Takım Kontrol Kısmı #
    elif alanf == "4":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/takim')
        print(kontrol_model)

    # Takım Teknik Direktör Kontrol Kısmı #
    elif alanf == "5":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/takimtd')
        print(kontrol_model)

    # Lig Kontrol Kısmı #
    elif alanf == "6":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/lig')
        print(kontrol_model)

    # İlk 11 Oynama Kontrol Kısmı #
    elif alanf == "7":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/ilk_11_oynama')
        print(kontrol_model)

    # Gol Sayısı Kontrol Kısmı #
    elif alanf == "8":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/gol_sayisi')
        print(kontrol_model)

    # Asist Sayısı Kontrol Kısmı #
    elif alanf == "9":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/asist_sayisi')
        print(kontrol_model)

    # Kırmızı Kart Sayısı Kontrol Kısmı #
    elif alanf == "10":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/kirmizi_kart_sayisi')
        print(kontrol_model)

    # Sarı Kart Sayısı Kontrol Kısmı #
    elif alanf == "11":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/sari_kart_sayisi')
        print(kontrol_model)

    # Kiralık Mı Kontrol Kısmı #
    elif alanf == "12":
        kontrol_model = root.findtext(
            f'./futbolcu[@adsoyad="{kontrol}"]/kiralik_mi')
        print(kontrol_model)

    # Değerlerin Sağlanmadığı Kısım #
    else:
        print("""
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Yanlış Bir Tuşlama Yaptınız.Çıkış Yapılıyor Lüfen Bekleyiniz.. #
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        """)
        time.sleep(1)

# Çıkış Kısmı #
else:
    print("""
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #           Çıkış Yapılıyor Lüfen Bekleyiniz           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    """)
    time.sleep(1)
