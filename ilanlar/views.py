<!DOCTYPE html>
<html>
<head>
    <title>Giriş Yap</title>
    <style>
        body { font-family: Arial; margin: 0; background: #f5f5f5; }
        .header { background: #FF6000; padding: 15px; color: white; }
        .header h1 { margin: 0; font-size: 24px; }
        .form-kart { max-width: 400px; margin: 40px auto; background: white; padding: 30px; border-radius: 8px; }
        .form-kart h2 { color: #FF6000; margin-top: 0; }
        label { font-size: 13px; color: #555; font-weight: bold; }
        input { width: 100%; padding: 10px; margin: 5px 0 15px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background: #FF6000; color: white; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; }
        a { color: #FF6000; }
        .hata { background: #fee; color: #c00; padding: 10px; border-radius: 6px; margin-bottom: 15px; font-size: 14px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🕌 Dingönüllüleri</h1>
    </div>
    <div class="form-kart">
        <h2>Giriş Yap</h2>
        {% if hata %}
        <div class="hata">{{ hata }}</div>
        {% endif %}
        <form method="post">
            {% csrf_token %}
            <label>Kullanıcı Adı</label>
            <input type="text" name="username" placeholder="Kullanıcı adınız">
            <label>Şifre</label>
            <input type="password" name="password" placeholder="Şifreniz">
            <button type="submit">Giriş Yap</button>
        </form>
        <p style="margin-top:15px;">Hesabın yok mu? <a href="/kayit/">Kayıt ol</a></p>
    </div>
</body>
</html>