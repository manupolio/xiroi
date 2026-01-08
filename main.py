import qrcode

i = 0
with open('texts.txt', 'r', encoding="utf-8") as fitxer:
    for linia in fitxer:
        qr = qrcode.make(linia.strip())
        qr.save(f"qr{str(i)}.png")
        i += 1