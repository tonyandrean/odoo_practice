# Vendor Authentication with API Key and Rate Limit

## Tools
| Tool       | Version     |
|------------|-------------|
| Postman    | -           |
| Odoo       | 17 CE       |

---

## Generate API Key
1. Pilih user yang ingin digunakan di **Odoo**
2. Generate **API Key** pada user tersebut

---

## Akses API Menggunakan Postman

### 1. Tambahkan Header
| Key      | Value |
|----------|--------------------------|
| API-Key  | (API Key yang digenerate dari user) |

### 2. Kirim Request
- Kirim request **POST, PUT, GET, DELETE**
- Jika **API Key salah / kosong**, akan muncul error:
    ```json
    {
      "error": "API Key is missing"
    }
- Jika **API Key benar** status response **success**

### 3. Rate Limit
- Rate limit di set max **5 request per 60 sec**
- Jika melebihi batas, akan menampilkan message:
    ```json
    {
        "error": "Too many requests. Please try again later."
    }
    ```