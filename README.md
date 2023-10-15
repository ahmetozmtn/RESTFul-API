<h1 id="tr" style="text-align:center">
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
python main.py
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
    -   Uyarı!!! ; PUT istediği atarken güncellemek istediğiniz verilerin JSON formatında isteğin Body kısmına ekleminiz gerekiyor
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

## Veritabanı

Projede SQLAlchemy kullanılarak bir SQLite veritabanı kullanılmaktadır. Veritabanı şeması ve tablo yapısı için `models.py` dosyasına bakabilirsiniz.

## Katkılar

Eğer projeye katkıda bulunmak isterseniz, lütfen bir Pull Requets oluşturun. Katkılarınızı bekliyoruz!

## Lisans

Bu proje [MIT lisansı](LICENSE) altında lisanslanmıştır.

<br>

<h1 id="eng" style="text-align:center">
RESTful API Example
</h1>

### This project is a simple example of a RESTful API developed using Flask and SQLAlchemy.

## Installation and Running

<br>

**Clone the project**

```shell
git clone CLONE_URL
```

**Navigate to the project folder**

```shell
cd RESTFul-API
```

**Install the required dependencies**

```shell
pip install -r requirements.txt
```

**Run the project**

-   Linux & Mac OS X

```shell
python3 main.py
```

-   Windows

```shell
python main.py
```

<br>

## Usage

The project provides the following endpoints:

-   `api/addData`: Make a POST request to add a new record to the database.

    -   Example usage: `api/addData/1`
    -   Warning!!! ; When sending a POST request, you need to add the data you want to add in JSON format to the Body of the request.

        -   Example;

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

-   `api/deleteData/<int:id>`: Make a DELETE request to delete a record with the specified ID.
    -   Example usage : `api/deleteData/1`

<br>

-   `api/getData`: Make a GET request to retrieve all records.

<br>

-   `api/allDelete`: Make a DELETE request to delete all records.

<br>

-   `api/updateData/<int:id>`: Make a PUT request to update a record with the specified ID.

    -   Example usage: `api/updateData/1`
    -   Warning!!! ; When sending a PUT request, you need to add the data you want to update in JSON format to the Body of the request

        -   Example;

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

## Database

In the project, SQLAlchemy is used to use an SQLite database. You can refer to the `models.py` file for the database schema and table structure.

## Contributions

If you would like to contribute to the project, please create a Pull Request. We welcome your contributions!

## License

This project is licensed under the [MIT license](LICENSE).
