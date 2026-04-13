import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import Layout from '../components/Layout'
import api from '../api/client'

export default function CampaignStats() {
  const { id } = useParams()
  const [stats, setStats] = useState(null)

  useEffect(() => {
    api.get(`/api/campaigns/${id}/stats`).then((r) => setStats(r.data))
  }, [id])

  if (!stats) return <Layout><p className="text-gray-400">Yüklənir...</p></Layout>

  return (
    <Layout>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <Link to="/campaigns" className="text-sm text-gray-400 hover:text-gray-600">← Kampaniyalar</Link>
          <h2 className="text-2xl font-bold text-gray-900 mt-1">{stats.campaign_name}</h2>
          <p className="text-gray-500 text-sm">Kampaniya Hesabatı</p>
        </div>
      </div>

      {/* Ümumi statistika */}
      <div className="grid grid-cols-4 gap-4 mb-8">
        <div className="bg-white rounded-xl border border-gray-100 shadow-sm p-5">
          <p className="text-sm text-gray-500 mb-1">Cəmi hədəf</p>
          <p className="text-3xl font-bold text-gray-900">{stats.total_targets}</p>
        </div>
        <div className="bg-white rounded-xl border border-gray-100 shadow-sm p-5">
          <p className="text-sm text-gray-500 mb-1">Klik sayı</p>
          <p className="text-3xl font-bold text-red-600">{stats.clicked}</p>
        </div>
        <div className="bg-white rounded-xl border border-gray-100 shadow-sm p-5">
          <p className="text-sm text-gray-500 mb-1">Klik faizi</p>
          <p className="text-3xl font-bold text-orange-500">{stats.click_rate}%</p>
        </div>
        <div className="bg-white rounded-xl border border-gray-100 shadow-sm p-5">
          <p className="text-sm text-gray-500 mb-1">Təlim aldı</p>
          <p className="text-3xl font-bold text-green-600">{stats.trained}</p>
        </div>
      </div>

      {/* Əməkdaş cədvəli */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-100">
          <h3 className="font-semibold text-gray-800">Əməkdaş detalları</h3>
        </div>
        <table className="w-full text-sm">
          <thead className="bg-gray-50 border-b border-gray-100">
            <tr>
              <th className="text-left px-6 py-3 text-gray-500 font-medium">Ad</th>
              <th className="text-left px-6 py-3 text-gray-500 font-medium">Email</th>
              <th className="text-left px-6 py-3 text-gray-500 font-medium">Departament</th>
              <th className="text-left px-6 py-3 text-gray-500 font-medium">Status</th>
              <th className="text-left px-6 py-3 text-gray-500 font-medium">Vaxt</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-50">
            {stats.targets.map((t, i) => (
              <tr key={i} className="hover:bg-gray-50">
                <td className="px-6 py-4 font-medium text-gray-900">{t.name}</td>
                <td className="px-6 py-4 text-gray-500">{t.email}</td>
                <td className="px-6 py-4">
                  <span className="bg-indigo-50 text-indigo-700 text-xs font-medium px-2.5 py-1 rounded-full">
                    {t.department || '—'}
                  </span>
                </td>
                <td className="px-6 py-4">
                  {t.clicked ? (
                    <span className="bg-red-50 text-red-600 text-xs font-semibold px-2.5 py-1 rounded-full">
                      Kliklədi
                    </span>
                  ) : (
                    <span className="bg-green-50 text-green-600 text-xs font-semibold px-2.5 py-1 rounded-full">
                      Keçdi
                    </span>
                  )}
                </td>
                <td className="px-6 py-4 text-gray-400 text-xs">
                  {t.clicked_at ? new Date(t.clicked_at).toLocaleString('az-AZ') : '—'}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Layout>
  )
}
