import { motion, AnimatePresence } from 'framer-motion'
import { useRef, useState } from 'react'
import ConfidenceBar from './ConfidenceBar'
import TopPredictions from './TopPredictions'
import { useLanguage } from '../context/LanguageContext'
import html2canvas from 'html2canvas'
import jsPDF from 'jspdf'
import ChatWidget from '../components/ChatWidget'

function AnalysisResult({ result, loading, previewImage, previewBase64 }) {
  const { t, language } = useLanguage()
  const resultRef = useRef(null)
  // Hangi sekmenin aktif olduğunu tutan state (başlangıçta "belirtiler")
  const [aktifSekme, setAktifSekme] = useState('belirtiler')

  const handleSavePDF = async () => {
    if (!result) return
    try {
      const element = resultRef.current
      const canvas = await html2canvas(element, {
        scale: 2,
        useCORS: true,
        allowTaint: true,
        backgroundColor: '#ffffff',
        logging: false,
        width: element.offsetWidth,
        windowWidth: 1200,
        imageTimeout: 0,
      })

      const imgData = canvas.toDataURL('image/png')
      const pdf = new jsPDF('p', 'mm', [210, 350])
      const pdfWidth = pdf.internal.pageSize.getWidth()
      const pdfHeight = (canvas.height * pdfWidth) / canvas.width

      pdf.setFontSize(16)
      pdf.setTextColor(22, 163, 74)
      pdf.text('LeafScan - Analiz Sonucu', 14, 16)
      pdf.setFontSize(10)
      pdf.setTextColor(100, 116, 139)
      pdf.text(`Tarih: ${new Date().toLocaleString('tr-TR')}`, 14, 24)

      // Base64 görsel varsa ekle
      if (previewBase64) {
        pdf.addImage(previewBase64, 'JPEG', 14, 30, pdfWidth - 28, 60)
        pdf.addImage(imgData, 'PNG', 14, 96, pdfWidth - 28, Math.min(pdfHeight, 220))
      } else {
        pdf.addImage(imgData, 'PNG', 14, 30, pdfWidth - 28, Math.min(pdfHeight, 280))
      }

      pdf.save(`leafscan-analiz-${Date.now()}.pdf`)
    } catch (err) {
      console.error('PDF hatası:', err)
    }
  }

  const handlePrint = () => window.print()

  if (loading) {
    return (
      <div className="result-panel" style={{ minHeight: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '4rem', marginBottom: '16px', animation: 'scan-leaf 1.5s ease-in-out infinite' }}>🍃</div>
          <div className="spinner" style={{ margin: '0 auto 16px' }} />
          <p style={{ color: 'var(--text-secondary)', fontWeight: 500, fontSize: '0.95rem' }}>{t('analyzing_text')}</p>
          <p style={{ color: 'var(--text-tertiary)', fontSize: '0.8rem', marginTop: '8px' }}>Yapay zeka analiz ediyor...</p>
        </div>
      </div>
    )
  }

  if (!result) {
    return (
      <div className="result-panel">
        <div className="instructions">
          <h3 className="instructions-title">🔬 {t('inst_title')}</h3>
          <div className="instructions-steps">
            {[1, 2, 3, 4].map(n => (
              <div key={n} className="instruction-step">
                <div className="step-number">{n}</div>
                <div className="step-content">
                  <h4>{t(`inst_step${n}_title`)}</h4>
                  <p>{t(`inst_step${n}_desc`)}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    )
  }

  // --- Sekme tanımları ---
  // Her sekme: id, etiket (emoji + başlık) ve gösterilecek içerik.
  // Sağlıklı bitkilerde tedavi/önleme boş olacağı için sadece dolu olanları tutuyoruz.
  const sekmeler = [
    { id: 'belirtiler', etiket: '📋 Belirtiler', icerik: result.belirtiler },
    { id: 'organik', etiket: '🌿 Organik', icerik: result.organik_tedavi },
    { id: 'kimyasal', etiket: '🧪 Kimyasal', icerik: result.kimyasal_tedavi },
    { id: 'onleme', etiket: '🛡️ Önleme', icerik: result.onleme },
  ].filter(s => {
    // İçeriği boş olan sekmeleri gösterme
    if (!s.icerik) return false
    // Bitki sağlıklıysa tedavi/önleme sekmelerini gizle, sadece belirtiler kalsın
    if (result.is_healthy && s.id !== 'belirtiler') return false
    return true
  })

  // Aktif sekme mevcut değilse ilk sekmeye düş
  const aktifIcerik = sekmeler.find(s => s.id === aktifSekme) || sekmeler[0]
  const diseaseContext = result && !result.is_healthy
  ? `${result.plant} bitkisinde ${result.disease} hastalığı tespit edildi.`
  : (result && result.is_healthy ? `${result.plant} bitkisi sağlıklı görünüyor.` : '')

  return (
    <AnimatePresence mode="wait">
      <motion.div
        className="result-panel"
        initial={{ opacity: 0, scale: 0.97 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, type: 'spring', stiffness: 120 }}
        style={{ border: result.is_healthy ? '1.5px solid rgba(22,163,74,0.2)' : '1.5px solid rgba(239,68,68,0.2)' }}
      >
        <div ref={resultRef}>
          <motion.div className="result-details" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
            <motion.div initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ type: 'spring', stiffness: 200, delay: 0.1 }}>
              {result.is_healthy ? (
                <div className="result-badge healthy" style={{ fontSize: '1rem', padding: '12px 24px' }}>✅ {t('badge_healthy')}</div>
              ) : (
                <div className="result-badge diseased" style={{ fontSize: '1rem', padding: '12px 24px' }}>⚠️ {t('badge_diseased')}</div>
              )}
            </motion.div>

            <div className="result-detail-row">
              <span className="result-detail-label">{t('plant_label')}</span>
              <span className="result-detail-value">🌱 {language === 'en' ? result.plant_en : result.plant || '—'}</span>
            </div>

            {!result.is_healthy && (
              <motion.div className="result-detail-row" initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.2 }} style={{ background: 'rgba(239,68,68,0.04)', borderLeft: '3px solid #ef4444' }}>
                <span className="result-detail-label">{t('disease_label')}</span>
                <span className="result-detail-value" style={{ color: '#dc2626' }}>🦠 {language === 'en' ? result.disease_en : result.disease || '—'}</span>
              </motion.div>
            )}

            <ConfidenceBar confidence={result.confidence} />

            {result.top_predictions?.length > 0 && <TopPredictions predictions={result.top_predictions} />}

            {/* --- Sekmeli bilgi alanı --- */}
            {sekmeler.length > 0 && (
              <motion.div className="info-card" initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.3 }} style={{ padding: 0, overflow: 'hidden' }}>
                {/* Sekme başlıkları */}
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4px', padding: '8px', borderBottom: '1px solid rgba(0,0,0,0.06)' }}>
                  {sekmeler.map(s => (
                    <button
                      key={s.id}
                      onClick={() => setAktifSekme(s.id)}
                      style={{
                        flex: '1 1 auto',
                        padding: '8px 10px',
                        borderRadius: '8px',
                        border: 'none',
                        cursor: 'pointer',
                        fontSize: '0.82rem',
                        fontWeight: 600,
                        fontFamily: 'inherit',
                        whiteSpace: 'nowrap',
                        transition: 'all 0.2s',
                        background: aktifIcerik.id === s.id ? 'rgba(22,163,74,0.12)' : 'transparent',
                        color: aktifIcerik.id === s.id ? 'var(--green-700)' : 'var(--text-secondary)',
                      }}
                    >
                      {s.etiket}
                    </button>
                  ))}
                </div>
                {/* Aktif sekmenin içeriği (değişince yumuşak geçiş) */}
                <div style={{ padding: '16px' }}>
                  <AnimatePresence mode="wait">
                    <motion.p
                      key={aktifIcerik.id}
                      className="info-card-text"
                      initial={{ opacity: 0, x: 8 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -8 }}
                      transition={{ duration: 0.2 }}
                      style={{ margin: 0 }}
                    >
                      {aktifIcerik.icerik}
                    </motion.p>
                  </AnimatePresence>
                </div>
              </motion.div>
            )}
          </motion.div>
          <ChatWidget diseaseContext={diseaseContext} />
        </div>

        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.5 }} style={{ display: 'flex', gap: '10px', marginTop: '16px' }}>
          <button onClick={handleSavePDF} style={{ flex: 1, padding: '10px', borderRadius: '10px', border: '1px solid rgba(22,163,74,0.2)', background: 'rgba(22,163,74,0.06)', color: 'var(--green-700)', fontWeight: 600, fontSize: '0.85rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px', fontFamily: 'inherit' }}
            onMouseEnter={e => e.currentTarget.style.background = 'rgba(22,163,74,0.12)'}
            onMouseLeave={e => e.currentTarget.style.background = 'rgba(22,163,74,0.06)'}>
            💾 PDF Kaydet
          </button>
          <button onClick={handlePrint} style={{ flex: 1, padding: '10px', borderRadius: '10px', border: '1px solid rgba(0,0,0,0.08)', background: 'var(--slate-50)', color: 'var(--text-secondary)', fontWeight: 600, fontSize: '0.85rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px', fontFamily: 'inherit' }}
            onMouseEnter={e => e.currentTarget.style.background = 'var(--slate-100)'}
            onMouseLeave={e => e.currentTarget.style.background = 'var(--slate-50)'}>
            🖨️ Yazdır
          </button>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  )
}

export default AnalysisResult