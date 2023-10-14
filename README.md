<h1 style="text-align:center">
RestFul API Example
</h1>

### Bu proje, Flask ve SQLAlchemy kullanılarak geliştirilmiş basit bir RESTful API örneği'dir.

## Kurulum ve çalıştırma

<br>

**Projeyi klonlama**

```shell
git clone CLONE_URL
```

**Proje klasörne girin**

```shell
cd RESTFul-API
```

**Gerekli bağımlılıkları yüklemek için**

```shell
pip install -r requirements.txt
```

**Projeyi çalıştırma**

-   Linux & Mac OS X

```shell
python3 main.py
```

-   Windows

```shell
python3 main.py
```

<br>

## Kullanım

Proje aşağıdaki endpointleri sağlamaktadır:

-   `api/addData`: Veritabanına yeni bir kayıt eklemek için POST isteği yapılır.
    -   Örnek kullanım: `api/addData/1`
    -   Uyarı!!! ; POST istediği atarken eklemek istediğiniz verilerin JSON formatında, isteğin Body kısmına ekleminiz gerekiyor.
        -   Örnek;
            ```json
            {
                "username": "username",
                "password": "password",
                "email": "example@example.com",
                "phone": "0555555555",
                "address": "example example",
                "city": "City",
                "state": "State",
                "product_name": "Product Name"
            }
            ```

<br>

-   `api/deleteData/<int:id>`: Belirtilen ID'ye sahip kaydı silmek için DELETE isteği yapılır.
    -   Örnek kullanım : `api/deleteData/1`

<br>

-   `api/getData`: Tüm kayıtları getirmek için GET isteği yapılır.

<br>

-   `api/allDelete`: Tüm kayıtları silmek için DELETE isteği yapılır.

<br>

-   `api/updateData/<int:id>`: Belirtilen ID'ye sahip kaydı güncellemek için PUT isteği yapılır.
    -   Örnek kullanım: `api/updateData/1`
    -   Uyarı!!! ; PUT istediği atarken güncellemek istediğiniz verilerin JSON formatında isteğin Body kısmına ekleminiz gerekiyor - Örnek;
        ```json
        {
            "username": "username",
            "password": "password",
            "email": "example@example.com",
            "phone": "0555555555",
            "address": "example example",
            "city": "City",
            "state": "State",
            "product_name": "Product Name"
        }
        ```

## Veritabanı

Projede SQLAlchemy kullanılarak bir SQLite veritabanı kullanılmaktadır. Veritabanı şeması ve tablo yapısı için `models.py` dosyasına bakabilirsiniz.

## Katkılar

Eğer projeye katkıda bulunmak isterseniz, lütfen bir Pull Requets oluşturun. Katkılarınızı bekliyoruz!

## Lisans

Bu proje [MIT lisansı](LICENSE) altında lisanslanmıştır.

---
