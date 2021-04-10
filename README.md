# Email ile veri gönderme.
 
 Bu proje bir veritabanı sorgusu ile elde edilen verilerin bir dosya formatına(örn. Excel) çevrilip mail atılmasını sağlar. Bu projeye 1 tane mail servisi ve 1 tane veritabanını destekler. Daha fazla bilgi için [katkıda bulunmak için](#katkıda-bulunmak-için) kısmını okuyun.

# Motivasyon

 Bu projenin var olma amacı belirli alışkanlıklar kazanmak. Bu anlışkanlıklar; Unittest, docstring, projeye başlanmadan önce planlama yapma ve projeyi belirli adımları takip ederek yapma.

# Kurulum
 
 ```
    sudo apt-get install libpq-dev # psycopg2 modülü için.
    pip install -r req.txt
 ```

# Nasıl kullanılır
 Projenin root dizinindeki `main.py` dosyanın içindeki `Assign this variables` bölümünü doldurmanız gerekmektedir. Bu bölüm aşağıdaki gibidir;

 ```python

    db_type = DBEnum.PostgreSQL # Kullandığınız veritabanı. Veritabanı ile ilgili 
    # giriş bilgileri db klasörünün  altındaki gerekli veritabanı dosyanın içinde 
    # hazır olarak gelmektedir. Elle değiştirmeniz gerekir. Parametre olarak verilmez.
    data_query = 'SELECT * FROM temp' # Kullanacağınız sorgu.

    # attach_file_name = '' # Maile eklemek istediğiniz dosyanın adı. 
    # Default olarak Data ismiyle eklenir. Farklı bir isim istiyorsanız yorum satırını kaldırın.
    attach_file_type = FileTypeEnum.Excel # Maile ekleyeceğiniz dosyanın Tipi.

    mail_service = MailEnum.Hotmail # Kendinizin kullandığı mail servisi
    auth = {
        'user': '', # Mail adresiniz
        'password': '' # Mail şifreniz
    }
    mailTo = '' # Mail göndermek istediğiniz adres.
    mailSubject = '' # Mailin konusu
    mailMessage = '' # Mailin mesajı.

 ```

# Katkıda bulunmak için

## Veritabanı eklemek için
Bu projenin desteklediği veritabanı sadece `PostgreSQL`' dir. `MySQL` postgres' nin kopyasıdır.

Bu projeye veritabanı eklemek istiyorsanız; 

`db` klasörü altına eklemek istediğiniz veritabanının adı ile başlayan ve `IDB` sınıfını kalıtım olan bir sınıf oluşturarak yapabilirsiniz. 

Oluşturacağınız sınıf 3 fonksiyondan oluşmalıdır. Bunlar; `connect`, `fetch`, `disconnect`. 

`connect` fonksiyonu veritabanı ile bağlantıyı sağlar.<br/>
`fetch` fonksiyonu belirtilen sorguyu gerçekleştirir ve gelen veriyi DataFrame' e dönüştürür.<br/>
`disconnect` ise veritabanı bağlantısını kapatır.

Eklediğiniz veritabanını `db` klasörünün altındaki `DBEnum` dosyasına ekleyin.

Son olarakta root dizinindeki `DBFactory` dosyasındaki `if` şartına ekleyin.

## Mail eklemek için
Bu projenin desteklediği mail servisi sadece `Hotmail`' dir.

Bu projeye mail servisi eklemek istiyorsanız; 

`Mail` klasörünün altındaki `MailEnum` dosyanına eklemeniz gerekir. 

Eklemek istediğiniz servisin, `STMP` bağlantı bilgilerini bir `dict` şeklinde eklemeniz gerekir. 

`smtplib` modülünün `SMTP` sınıfının kabul ettiği bütün parametreleri yazabilirsiniz.

## Dosya Tipi eklemek için
Bu projenin desteklediği dosya tipleri `CSV` ve `Excel` dir.

Bu projeye dosya tipi eklemek istiyorsanız; 

`writer` klasörü altına eklemek istediğiniz dosya tipi adı ile başlayan ve `IWriter` sınıfını kalıtım alan bir sınıf oluşturarak yapabilirsiniz. 

Oluşturacağınız sınıf tek fonksiyondan oluşmalı: `generate`

`generate` fonksiyonu eklediğiniz dosya formatında dosya oluşturmaya yarar.

Eklediğiniz veritabanını `db` klasörünün altındaki `DBEnum` dosyasına ekleyin.

Son olarakta eklediğiniz veritabanını `writer` klasörünün altındaki `FileTypeEnum` dosyasına ekleyin.

Son olarakta root dizinindeki `WriterFactory` dosyasındaki `if` şartına ekleyin.