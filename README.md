# El Algılama Projesi

Bu proje, gerçek zamanlı olarak kamera görüntüsünde el hareketlerini algılayan ve görselleştiren bir Python uygulamasıdır.

## Özellikler

- Gerçek zamanlı el algılama
- El iskeletinin görselleştirilmesi
- Parmak uçlarının mavi noktalarla işaretlenmesi
- Çoklu el desteği (aynı anda 2 el algılayabilme)

## Gereksinimler

- Python 3.10 veya üzeri
- OpenCV (`opencv-python`)
- MediaPipe
- NumPy

## Kurulum

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Programı çalıştırın:
```bash
python3 main.py
```

## Kullanım

- Program çalıştığında kamera görüntüsü açılacaktır
- Ellerinizi kameraya gösterin
- Program otomatik olarak ellerinizi algılayacak ve işaretleyecektir
- Programı kapatmak için 'q' tuşuna basın

## Notlar

- Program en iyi şekilde çalışabilmesi için iyi aydınlatma koşulları gereklidir
- Kamera izinlerinin verilmiş olduğundan emin olun
- Program aynı anda en fazla 2 eli algılayabilir

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. 