import { Link } from 'react-router-dom'

const stats = [
  { value: '22M+', label: 'AZN — 2024-cü ildə bank fırıldaqçılığından zərər' },
  { value: '70%', label: 'kiberhücumların phishing ilə başlayır' },
  { value: '95%', label: 'uğurlu hücum insan səhvindən qaynaqlanır' },
]

const modules = [
  {
    icon: '🎣',
    title: 'Phishing Simulasiya',
    desc: 'Əməkdaşlarınıza Azərbaycan dilində real ssenarilər üzrə fake hücum göndərin.',
  },
  {
    icon: '📊',
    title: 'Risk Skorinq',
    desc: 'Hansı əməkdaşın risk altında olduğunu görün, prioritet verin.',
  },
  {
    icon: '🎓',
    title: 'Avtomatik Təlim',
    desc: 'Hücuma düşən əməkdaşa dərhal fərdi təlim göndərilir.',
  },
  {
    icon: '🔔',
    title: 'Bildiriş Sistemi',
    desc: 'Müştərilər şübhəli zəng/mesaj aldıqda bankı xəbərdar etsin.',
  },
]

const steps = [
  { n: '1', title: 'Qeydiyyat', desc: 'Şirkət adı və email ilə 1 dəqiqədə hesab açın.' },
  { n: '2', title: 'CSV Yüklə', desc: 'Əməkdaş siyahısını HR sisteminizdən export edib yükləyin.' },
  { n: '3', title: 'Kampaniya Başlat', desc: 'Şablon seçin, göndərin — nəticəni real vaxtda izləyin.' },
]

const plans = [
  {
    name: 'Başlanğıc',
    price: '299',
    features: ['50 əməkdaşa qədər', '3 phishing şablonu', 'Dashboard', 'Email dəstək'],
    cta: 'Başla',
    highlight: false,
  },
  {
    name: 'Biznes',
    price: '699',
    features: ['250 əməkdaşa qədər', 'Bütün şablonlar', 'Risk Skorinq', 'Hesabat (PDF)', 'Prioritet dəstək'],
    cta: 'Başla',
    highlight: true,
  },
  {
    name: 'Korporativ',
    price: 'Fərdi',
    features: ['Limitsiz əməkdaş', 'Fərdi ssenarilər', 'API inteqrasiya', 'Dedicated dəstək'],
    cta: 'Əlaqə saxla',
    highlight: false,
  },
]

export default function Landing() {
  return (
    <div className="min-h-screen bg-white font-sans">

      {/* Navbar */}
      <nav className="flex items-center justify-between px-8 py-5 border-b border-gray-100 max-w-6xl mx-auto">
        <span className="text-xl font-bold text-gray-900">LionSafe</span>
        <div className="flex gap-4">
          <Link to="/login" className="text-sm text-gray-600 hover:text-gray-900 font-medium px-4 py-2">
            Giriş
          </Link>
          <Link to="/register" className="text-sm bg-red-600 hover:bg-red-700 text-white font-semibold px-4 py-2 rounded-lg transition">
            Pulsuz Başla
          </Link>
        </div>
      </nav>

      {/* Hero */}
      <section className="max-w-4xl mx-auto text-center px-6 py-24">
        <span className="bg-red-50 text-red-600 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wide">
          Azərbaycan bankları üçün
        </span>
        <h1 className="text-5xl font-bold text-gray-900 mt-6 mb-6 leading-tight">
          Əməkdaşlarınızı<br />phishing-dən qoruyun
        </h1>
        <p className="text-xl text-gray-500 mb-10 max-w-2xl mx-auto">
          LionSafe Azərbaycan dilində phishing simulasiya platformasıdır.
          Real ssenarilər, avtomatik təlim, anlıq statistika.
        </p>
        <div className="flex gap-4 justify-center">
          <Link to="/register" className="bg-red-600 hover:bg-red-700 text-white font-semibold px-8 py-3.5 rounded-xl transition text-base">
            Pulsuz Sınayın
          </Link>
          <a href="#how" className="border border-gray-300 hover:border-gray-400 text-gray-700 font-semibold px-8 py-3.5 rounded-xl transition text-base">
            Necə işləyir?
          </a>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-gray-900 py-16">
        <div className="max-w-4xl mx-auto px-6 grid grid-cols-3 gap-8 text-center">
          {stats.map((s) => (
            <div key={s.value}>
              <p className="text-4xl font-bold text-red-500 mb-2">{s.value}</p>
              <p className="text-gray-400 text-sm">{s.label}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Modules */}
      <section className="max-w-5xl mx-auto px-6 py-24">
        <h2 className="text-3xl font-bold text-gray-900 text-center mb-4">Nə təklif edirik?</h2>
        <p className="text-gray-500 text-center mb-12">Bir platformada — 4 modul</p>
        <div className="grid grid-cols-2 gap-6">
          {modules.map((m) => (
            <div key={m.title} className="border border-gray-100 rounded-2xl p-6 hover:shadow-md transition">
              <span className="text-3xl">{m.icon}</span>
              <h3 className="text-lg font-semibold text-gray-900 mt-3 mb-2">{m.title}</h3>
              <p className="text-gray-500 text-sm">{m.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* How it works */}
      <section id="how" className="bg-gray-50 py-24">
        <div className="max-w-4xl mx-auto px-6">
          <h2 className="text-3xl font-bold text-gray-900 text-center mb-4">Necə işləyir?</h2>
          <p className="text-gray-500 text-center mb-12">3 addımda başlayın</p>
          <div className="grid grid-cols-3 gap-8">
            {steps.map((s) => (
              <div key={s.n} className="text-center">
                <div className="w-12 h-12 bg-red-600 text-white rounded-full flex items-center justify-center text-xl font-bold mx-auto mb-4">
                  {s.n}
                </div>
                <h3 className="font-semibold text-gray-900 mb-2">{s.title}</h3>
                <p className="text-gray-500 text-sm">{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section className="max-w-5xl mx-auto px-6 py-24">
        <h2 className="text-3xl font-bold text-gray-900 text-center mb-4">Qiymətlər</h2>
        <p className="text-gray-500 text-center mb-12">Aylıq ödəniş — AZN</p>
        <div className="grid grid-cols-3 gap-6">
          {plans.map((p) => (
            <div
              key={p.name}
              className={`rounded-2xl p-8 border ${
                p.highlight
                  ? 'border-red-600 bg-red-600 text-white shadow-xl'
                  : 'border-gray-200 text-gray-900'
              }`}
            >
              <p className={`text-sm font-semibold mb-2 ${p.highlight ? 'text-red-100' : 'text-gray-500'}`}>
                {p.name}
              </p>
              <p className="text-4xl font-bold mb-1">
                {p.price === 'Fərdi' ? p.price : `₼${p.price}`}
              </p>
              {p.price !== 'Fərdi' && (
                <p className={`text-sm mb-6 ${p.highlight ? 'text-red-100' : 'text-gray-400'}`}>/ ay</p>
              )}
              <ul className="space-y-2 mb-8 mt-4">
                {p.features.map((f) => (
                  <li key={f} className={`text-sm flex gap-2 ${p.highlight ? 'text-red-50' : 'text-gray-600'}`}>
                    <span>✓</span> {f}
                  </li>
                ))}
              </ul>
              <Link
                to="/register"
                className={`block text-center text-sm font-semibold py-2.5 rounded-xl transition ${
                  p.highlight
                    ? 'bg-white text-red-600 hover:bg-red-50'
                    : 'bg-red-600 text-white hover:bg-red-700'
                }`}
              >
                {p.cta}
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="bg-gray-900 py-20 text-center">
        <h2 className="text-3xl font-bold text-white mb-4">Bankınızı qorumağa başlayın</h2>
        <p className="text-gray-400 mb-8">Qeydiyyat pulsuzdur. Kredit kartı tələb edilmir.</p>
        <Link
          to="/register"
          className="bg-red-600 hover:bg-red-700 text-white font-semibold px-8 py-3.5 rounded-xl transition"
        >
          Pulsuz Başla
        </Link>
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-100 py-8 text-center text-gray-400 text-sm">
        © 2026 LionSafe. Bütün hüquqlar qorunur.
      </footer>
    </div>
  )
}
