"""
DB-yə test məlumatı yüklə.
İstifadə: python seed.py
"""
from app.services.database import SessionLocal
from app.services.auth import hash_password
from app.models import Organization, User, Template

db = SessionLocal()

# --- Təşkilat ---
org = Organization(name="Demo Bank ASC", domain="demobank.az")
db.add(org)
db.flush()

# --- Admin istifadəçi ---
admin = User(
    org_id=org.id,
    email="admin@demobank.az",
    name="Admin",
    is_admin=True,
    hashed_password=hash_password("Admin1234!"),
)
db.add(admin)

# --- Phishing şablonları (5 ssenairi, Azərbaycan dilində) ---

templates = [
    Template(
        name="IT: Şifrəni yenilə",
        subject="[IT Dəstək] Hesabınızın şifrəsi müddəti bitib — dərhal yeniləyin",
        category="it_support",
        body_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:1px solid #ddd;padding:30px">
  <img src="https://via.placeholder.com/200x50?text=DemoBank+IT" alt="IT Dəstək" style="margin-bottom:20px"><br>
  <p>Hörmətli əməkdaş,</p>
  <p>Sistemimiz sizin hesabınızın şifrəsinin <strong>bu gün saat 18:00-da</strong> müddətinin bitəcəyini aşkar etmişdir.</p>
  <p>Hesabınıza giriş itirməmək üçün aşağıdakı düyməyə klikləyin:</p>
  <a href="{{TRACKING_URL}}" style="background:#c0392b;color:#fff;padding:12px 24px;text-decoration:none;border-radius:4px;display:inline-block;margin:16px 0">Şifrəmi Yenilə</a>
  <p style="color:#888;font-size:12px">Bu link 2 saat ərzində etibarlıdır. Əgər bu sorğunu siz etməmisinizsə, IT dəstəyə müraciət edin.</p>
  <p>Hörmətlə,<br>IT Dəstək Qrupu | DemoBank</p>
</div>
""",
        training_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:4px solid #e74c3c;padding:30px;text-align:center">
  <h2 style="color:#e74c3c">⚠️ Bu bir phishing simulasiyası idi!</h2>
  <p>Hörmətli <strong>{{NAME}}</strong>,</p>
  <p>Siz bu dəfə saxta bir IT emailinə kliklədiniz. Real hücumda bu, hesabınızın oğurlanmasına səbəb ola bilərdi.</p>
  <h3>Necə tanımalı idiniz?</h3>
  <ul style="text-align:left">
    <li>IT heç vaxt email vasitəsilə şifrə dəyişdirməyi tələb etmir</li>
    <li>Linkdən əvvəl domenə baxın — demobank.az olmalıdır</li>
    <li>Tələsik dil ("dərhal", "2 saat") — phishing əlamətidir</li>
  </ul>
  <p>Bu vəziyyətdə: emaili IT departamentinə bildirin, linki açmayın.</p>
</div>
""",
    ),
    Template(
        name="HR: Bonus bildirişi",
        subject="HR: 2026-cı il I rüb mükafatı haqqında məlumat",
        category="hr",
        body_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:1px solid #ddd;padding:30px">
  <p>Hörmətli əməkdaş,</p>
  <p>2026-cı ilin I rübü üzrə fəaliyyət göstəriciləriniz əsasında <strong>mükafat siyahısına</strong> daxil edildiniz.</p>
  <p>Mükafat məbləğinizi və detalları görmək üçün aşağıdakı linkə daxil olun:</p>
  <a href="{{TRACKING_URL}}" style="background:#27ae60;color:#fff;padding:12px 24px;text-decoration:none;border-radius:4px;display:inline-block;margin:16px 0">Mükafatımı Gör</a>
  <p style="color:#888;font-size:12px">Korporativ hesabınızla daxil olun.</p>
  <p>Hörmətlə,<br>İnsan Resursları Departamenti | DemoBank</p>
</div>
""",
        training_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:4px solid #e74c3c;padding:30px;text-align:center">
  <h2 style="color:#e74c3c">⚠️ Bu bir phishing simulasiyası idi!</h2>
  <p>Hörmətli <strong>{{NAME}}</strong>,</p>
  <p>Bonus və mükafat vədi — ən çox istifadə edilən phishing üsullarından biridir.</p>
  <h3>Necə tanımalı idiniz?</h3>
  <ul style="text-align:left">
    <li>HR mükafatları email linki ilə deyil, daxili sistem vasitəsilə elan edilir</li>
    <li>Gözlənilməz "xoş xəbər" emaillərinə şübhə ilə yanaşın</li>
    <li>HR-a birbaşa zəng edib soruşun</li>
  </ul>
</div>
""",
    ),
    Template(
        name="Mühasibat: Sənədi imzala",
        subject="Təcili: Müqavilə sənədini imzalamaq tələb olunur",
        category="finance",
        body_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:1px solid #ddd;padding:30px">
  <p>Hörmətli əməkdaş,</p>
  <p>Mühasibatlıq departamenti sizinlə bağlı <strong>müqavilə sənədini</strong> imzalanmaq üçün göndərmişdir.</p>
  <p>İş günü sonuna qədər imzalanmasa, proses gecikəcəkdir:</p>
  <a href="{{TRACKING_URL}}" style="background:#2980b9;color:#fff;padding:12px 24px;text-decoration:none;border-radius:4px;display:inline-block;margin:16px 0">Sənədə Bax və İmzala</a>
  <p>Hörmətlə,<br>Mühasibatlıq | DemoBank</p>
</div>
""",
        training_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:4px solid #e74c3c;padding:30px;text-align:center">
  <h2 style="color:#e74c3c">⚠️ Bu bir phishing simulasiyası idi!</h2>
  <p>Hörmətli <strong>{{NAME}}</strong>,</p>
  <p>Saxta "sənəd imzalama" sorğuları korporativ phishing-in ən yaygın növüdür.</p>
  <h3>Necə tanımalı idiniz?</h3>
  <ul style="text-align:left">
    <li>Müqavilə sənədləri heç vaxt xarici link vasitəsilə göndərilmir</li>
    <li>"İş günü sonu" kimi müddət təzyiqi — manipulyasiya əlamətidir</li>
    <li>Mühasibatlığa birbaşa zəng edib sənədi tələb edin</li>
  </ul>
</div>
""",
    ),
    Template(
        name="IT: VPN problemi",
        subject="[Təcili] VPN girişinizdə problem aşkar edildi",
        category="it_support",
        body_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:1px solid #ddd;padding:30px">
  <p>Hörmətli əməkdaş,</p>
  <p>Sizin VPN hesabınızda <strong>şübhəli giriş cəhdi</strong> aşkar edilmişdir. Hesabınız müvəqqəti olaraq məhdudlaşdırılmışdır.</p>
  <p>Hesabınızı bərpa etmək üçün kimliyinizi təsdiq edin:</p>
  <a href="{{TRACKING_URL}}" style="background:#8e44ad;color:#fff;padding:12px 24px;text-decoration:none;border-radius:4px;display:inline-block;margin:16px 0">Kimliyimi Təsdiq Et</a>
  <p style="color:#888;font-size:12px">Təsdiq edilməsə, hesabınız 24 saat bloklanacaq.</p>
  <p>Hörmətlə,<br>Kibertəhlükəsizlik Qrupu | DemoBank</p>
</div>
""",
        training_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:4px solid #e74c3c;padding:30px;text-align:center">
  <h2 style="color:#e74c3c">⚠️ Bu bir phishing simulasiyası idi!</h2>
  <p>Hörmətli <strong>{{NAME}}</strong>,</p>
  <p>"Hesabın bloklanması" hədəsi — istifadəçini tələsdirməyin klassik üsuludur.</p>
  <h3>Necə tanımalı idiniz?</h3>
  <ul style="text-align:left">
    <li>IT heç vaxt email vasitəsilə kimlik təsdiqləməyi tələb etmir</li>
    <li>"24 saat blok" kimi hədə dili — phishing əlamətidir</li>
    <li>IT dəstəyə birbaşa zəng edin</li>
  </ul>
</div>
""",
    ),
    Template(
        name="Rəhbərlik: Təcili köçürmə",
        subject="Rəhbərlikdən: Təcili ödəniş tapşırığı",
        category="executive",
        body_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:1px solid #ddd;padding:30px">
  <p>Salam,</p>
  <p>Mən hal-hazırda görüşdəyəm və telefonuma baxmaq mümkün deyil. Aşağıdakı linkdən <strong>təcili ödəniş formasını</strong> doldurun — bu gün tamamlanmalıdır.</p>
  <a href="{{TRACKING_URL}}" style="background:#e67e22;color:#fff;padding:12px 24px;text-decoration:none;border-radius:4px;display:inline-block;margin:16px 0">Ödəniş Forması</a>
  <p>Təşəkkür edirəm.</p>
</div>
""",
        training_html="""
<div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;border:4px solid #e74c3c;padding:30px;text-align:center">
  <h2 style="color:#e74c3c">⚠️ Bu bir phishing simulasiyası idi!</h2>
  <p>Hörmətli <strong>{{NAME}}</strong>,</p>
  <p>Bu "CEO fraud" və ya "BEC" (Business Email Compromise) adlanır — dünyada ən böyük maliyyə itkisinə səbəb olan hücum növüdür.</p>
  <h3>Necə tanımalı idiniz?</h3>
  <ul style="text-align:left">
    <li>Rəhbərlik heç vaxt email vasitəsilə ödəniş tapşırmır</li>
    <li>Göndərənin email domenini yoxlayın</li>
    <li>Belə hallarda rəhbərlə telefon əlaqəsi qurun</li>
  </ul>
</div>
""",
    ),
]

for t in templates:
    db.add(t)

# --- Test əməkdaşlar ---
employees = [
    User(org_id=org.id, email="leyla.mammadova@demobank.az", name="Leyla Məmmədova", department="Mühasibatlıq"),
    User(org_id=org.id, email="tural.hasanov@demobank.az", name="Tural Həsənov", department="IT"),
    User(org_id=org.id, email="nigar.aliyeva@demobank.az", name="Nigar Əliyeva", department="HR"),
    User(org_id=org.id, email="rashad.guliyev@demobank.az", name="Rəşad Quliyev", department="Kredit"),
    User(org_id=org.id, email="aysel.ibrahimova@demobank.az", name="Aysel İbrahimova", department="Mühasibatlıq"),
]

for e in employees:
    db.add(e)

db.commit()
print("✓ Təşkilat:", org.name)
print("✓ Admin:", admin.email, "/ şifrə: Admin1234!")
print(f"✓ {len(templates)} şablon əlavə edildi")
print(f"✓ {len(employees)} test əməkdaş əlavə edildi")
