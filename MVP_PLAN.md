# CyberShield AZ — MVP Planı

## Mərhələ Strategiyası

MVP-nin məqsədi: ABB Innovation demo günü üçün işlək prototip + ölçülə bilən nəticə.

**MVP skopuna daxil:** Modul 1 — Phishing Simulasiya + Təlim
**MVP-dən kənar (sonrakı mərhələlər):** Modul 2, 3, 4

---

## MVP — Modul 1: Phishing Simulasiya + Təlim

### Necə işləyir (istifadəçi axını)

```
Admin panel → Kampaniya yarat → Fake phishing email göndər →
Əməkdaş linkə basar (və ya basmaz) → Nəticə izlənir →
Basan əməkdaşa avtomatik mikro-təlim göndərilir →
Admin dashboardda statistika görünür
```

### Əsas xüsusiyyətlər (MVP scope)

| # | Xüsusiyyət | Prioritet |
|---|---|---|
| 1 | Admin: kampaniya yarat (email şablonu seç, hədəf siyahısı yüklə) | P0 |
| 2 | Fake phishing email göndər (Azərbaycan dilində lokal ssenarilər) | P0 |
| 3 | Link klikini izlə (kim basdı, nə vaxt, harada) | P0 |
| 4 | Avtomatik təlim emaili göndər (basan əməkdaşa) | P0 |
| 5 | Admin dashboard: klik faizi, risk altındakı əməkdaşlar | P0 |
| 6 | 5 hazır phishing şablonu (Azərbaycan banklarına uyğun) | P0 |
| 7 | Hesabat export (PDF/Excel) | P1 |
| 8 | Əməkdaş profil tarixçəsi | P1 |

### Phishing Şablonları (MVP üçün 5 ssenairi)

1. **"Şifrəni yenilə"** — IT departamentindən gələn saxta email
2. **"Hesabınız bloklandı"** — Mühasibat/HR adından
3. **"Sənədi imzala"** — DocuSign/Əmr forması simulasiyası
4. **"Mükafat bildirişi"** — HR adından saxta bonus emaili
5. **"VPN giriş problemi"** — IT support adından

---

## Texniki Stack

### Backend
- **Python + FastAPI** — REST API
- **PostgreSQL** — istifadəçilər, kampaniyalar, klik nəticələri
- **Redis** — sessiya, cache
- **SMTP (SendGrid free tier)** — email göndərmə

### Frontend
- **React + Tailwind CSS** — admin panel
- **Chart.js** — dashboard qrafiklər

### Deploy (MVP üçün)
- **Railway.app** və ya **Render.com** — pulsuz tier, demo üçün kifayət

### Tracking mexanizmi
- Hər əməkdaşa unikal tracking URL (UUID-based)
- 1x1 tracking pixel (email açıldımı)
- Hər klik: timestamp, IP (hash), user-agent

---

## Verilənlər Bazası Sxemi (sadələşdirilmiş)

```
campaigns          users (employees)     clicks
----------         -----------------     ------
id                 id                    id
name               campaign_id           user_id
template_id        email                 campaign_id
org_id             name                  clicked_at
created_at         department            ip_hash
status             clicked (bool)        trained (bool)
                   trained (bool)
```

---

## İnkişaf Mərhələləri

### Mərhələ 0 — Hazırlıq (1 həftə)
- [ ] Repo qur (GitHub)
- [ ] DB sxemini yaz
- [ ] FastAPI skeleton
- [ ] SendGrid hesabı aç (pulsuz: 100 email/gün)

### Mərhələ 1 — Core (3 həftə)
- [ ] İstifadəçi/kampaniya CRUD (API)
- [ ] Email göndərmə (template engine)
- [ ] Tracking URL + klik qeydiyyatı
- [ ] Avtomatik təlim emaili (klik baş verdikdə trigger)

### Mərhələ 2 — Admin Panel (2 həftə)
- [ ] Login / auth (JWT)
- [ ] Kampaniya yaratma UI
- [ ] CSV ilə əməkdaş yükləmə
- [ ] Dashboard: statistika, qrafiklər

### Mərhələ 3 — Demo hazırlığı (1 həftə)
- [ ] 5 phishing şablonu tamamla (Azərbaycan dilindəki ssenarilər)
- [ ] Demo data yüklə
- [ ] Deploy et (Railway/Render)
- [ ] Video demo (2-3 dəq) çək

**Ümumi: ~7 həftə**

---

## Uğur Meyarları (Demo Gününə Qədər)

| Metrik | Hədəf |
|---|---|
| Demo kampaniyasında klik faizi | >30% (realizmı sübut edir) |
| Email çatdırılma dərəcəsi | >95% |
| Dashboard yükləmə sürəti | <2 saniyə |
| Phishing şablonları | 5 hazır, Azərbaycan dilində |
| Pilot marağı | 1 bank/şirkətdən "bəli" |

---

## Resurslar

| Ehtiyac | Həll | Qiymət |
|---|---|---|
| Email göndərmə | SendGrid free | $0 |
| Hosting | Railway/Render free tier | $0 |
| DB | Supabase free | $0 |
| Domain | `.az` domain | ~30 AZN/il |
| **Cəmi MVP xərci** | | **~30 AZN** |

---

## Növbəti Mərhələlər (Post-MVP)

- **Modul 2:** Müştəri Bildiriş Sistemi (mobil/web form)
- **Modul 3:** Risk Skorinq Dashboard (ML-based)
- **Modul 4:** Incident Response Avtomatlaşdırma
- **B2B satış:** Pilot müqavilə (1-2 bank)
- **ABB Innovation müraciəti:** Demo + traction ilə

---

## Status

- [ ] Mərhələ 0 — Hazırlıq
- [ ] Mərhələ 1 — Core
- [ ] Mərhələ 2 — Admin Panel
- [ ] Mərhələ 3 — Demo hazırlığı
