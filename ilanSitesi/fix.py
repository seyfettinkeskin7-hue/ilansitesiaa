f = open('ilanlar/views.py', 'r')
content = f.read()
f.close()

# Cift hesaplama sil
idx = content.rfind('def hesaplama')
first = content.find('def hesaplama')
if idx != first:
    content = content[:first] + content[idx:]

f = open('ilanlar/views.py', 'w')
f.write(content)
f.close()
print('views.py OK')

f = open('ilanSitesi/urls.py', 'r')
u = f.read()
f.close()
if 'hesaplama' not in u:
    u = u.replace("path('hutbeler/', views.hutbeler, name='hutbeler'),",
        "path('hutbeler/', views.hutbeler, name='hutbeler'),\n    path('hesaplama/', views.hesaplama, name='hesaplama'),")
    f = open('ilanSitesi/urls.py', 'w')
    f.write(u)
    f.close()
print('urls.py OK')

f = open('ilanlar/templates/akademi.html', 'r')
h = f.read()
f.close()
h = h.replace('/hesaplama.html', '/hesaplama/')
f = open('ilanlar/templates/akademi.html', 'w')
f.write(h)
f.close()
print('akademi.html OK')
