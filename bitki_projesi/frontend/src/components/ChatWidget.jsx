import { useState, useRef, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { sendChatMessage } from '../services/api'

// Sağ altta açılır-kapanır sohbet balonu.
// diseaseContext: o an tespit edilen hastalık (opsiyonel) - asistan bağlamı bilsin diye.
function ChatWidget({ diseaseContext = '' }) {
  const [acik, setAcik] = useState(false)          // Pencere açık mı?
  const [mesajlar, setMesajlar] = useState([        // Sohbet geçmişi
    { rol: 'asistan', metin: 'Merhaba! 🌿 Bitki hastalıkları, tedavi ve bakım konusunda sorularını yanıtlayabilirim. Nasıl yardımcı olabilirim?' }
  ])
  const [girdi, setGirdi] = useState('')            // Kullanıcının yazdığı metin
  const [yukleniyor, setYukleniyor] = useState(false)
  const mesajSonuRef = useRef(null)

  // Yeni mesaj gelince sohbet kutusunu en alta kaydır (sayfayı etkilemeden)
  useEffect(() => {
    const kutu = mesajSonuRef.current?.parentElement
    if (kutu) {
      kutu.scrollTop = kutu.scrollHeight
    }
  }, [mesajlar, yukleniyor])

  const gonder = async () => {
    const soru = girdi.trim()
    if (!soru || yukleniyor) return

    // Kullanıcı mesajını ekle
    setMesajlar(prev => [...prev, { rol: 'kullanici', metin: soru }])
    setGirdi('')
    setYukleniyor(true)

    try {
      const veri = await sendChatMessage(soru, diseaseContext)
      const cevap = veri.reply || veri.error || 'Bir cevap alınamadı.'
      setMesajlar(prev => [...prev, { rol: 'asistan', metin: cevap }])
    } catch (err) {
      setMesajlar(prev => [...prev, { rol: 'asistan', metin: 'Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.' }])
    } finally {
      setYukleniyor(false)
    }
  }

  const tusaBas = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      gonder()
    }
  }

  return (
    <>
      {/* Açma/kapama butonu (sağ alt) */}
      <motion.button
        onClick={() => setAcik(!acik)}
        whileHover={{ scale: 1.08, rotate: acik ? 0 : 8 }}
        whileTap={{ scale: 0.95 }}
        animate={acik ? {} : { scale: [1, 1.08, 1] }}
        transition={acik ? {} : { duration: 2, repeat: Infinity, ease: 'easeInOut' }}
        style={{
          position: 'fixed', bottom: '24px', right: '24px', zIndex: 1000,
          width: '58px', height: '58px', borderRadius: '50%',
          border: '2px solid #16a34a',
          cursor: 'pointer', fontSize: '1.7rem',
          background: acik ? 'linear-gradient(135deg, #16a34a, #22c55e)' : '#ffffff',
          color: acik ? 'white' : '#16a34a',
          boxShadow: '0 8px 24px rgba(22,163,74,0.35)',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}
        aria-label="Sohbet asistanı"
      >
        {acik ? '✕' : '🍃'}
      </motion.button>

      {/* Sohbet penceresi */}
      <AnimatePresence>
        {acik && (
          <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 20, scale: 0.95 }}
            transition={{ duration: 0.25 }}
            style={{
              position: 'fixed', bottom: '92px', right: '24px', zIndex: 1000,
              width: 'min(370px, calc(100vw - 48px))', height: '480px',
              background: 'var(--surface, #ffffff)', borderRadius: '18px',
              boxShadow: '0 12px 40px rgba(0,0,0,0.18)',
              display: 'flex', flexDirection: 'column', overflow: 'hidden',
              border: '1px solid rgba(0,0,0,0.06)',
            }}
          >
            {/* Başlık */}
            <div style={{
              padding: '14px 18px', background: 'linear-gradient(135deg, #16a34a, #22c55e)',
              color: 'white', fontWeight: 600, fontSize: '0.95rem',
              display: 'flex', alignItems: 'center', gap: '8px',
            }}>
              🌿 LeafScan Asistanı
            </div>

            {/* Mesajlar */}
            <div style={{ flex: 1, overflowY: 'auto', overscrollBehavior: 'contain', padding: '14px', display: 'flex', flexDirection: 'column', gap: '10px', background: 'var(--slate-50, #f8fafc)' }}>
              {mesajlar.map((m, i) => (
                <div key={i} style={{
                  alignSelf: m.rol === 'kullanici' ? 'flex-end' : 'flex-start',
                  maxWidth: '85%',
                  padding: '9px 13px', borderRadius: '14px', fontSize: '0.88rem', lineHeight: 1.5,
                  whiteSpace: 'pre-wrap',
                  background: m.rol === 'kullanici' ? 'linear-gradient(135deg, #16a34a, #22c55e)' : '#ffffff',
                  color: m.rol === 'kullanici' ? 'white' : 'var(--text-primary, #1e293b)',
                  border: m.rol === 'kullanici' ? 'none' : '1px solid rgba(0,0,0,0.06)',
                  boxShadow: m.rol === 'asistan' ? '0 1px 3px rgba(0,0,0,0.05)' : 'none',
                }}>
                  {m.metin}
                </div>
              ))}
              {yukleniyor && (
                <div style={{ alignSelf: 'flex-start', padding: '9px 13px', borderRadius: '14px', fontSize: '0.88rem', background: '#ffffff', border: '1px solid rgba(0,0,0,0.06)', color: 'var(--text-secondary, #64748b)' }}>
                  Yazıyor...
                </div>
              )}
              <div ref={mesajSonuRef} />
            </div>

            {/* Girdi alanı */}
            <div style={{ padding: '12px', borderTop: '1px solid rgba(0,0,0,0.06)', display: 'flex', gap: '8px', background: 'var(--surface, #ffffff)' }}>
              <input
                type="text"
                value={girdi}
                onChange={(e) => setGirdi(e.target.value)}
                onKeyDown={tusaBas}
                placeholder="Bir soru yazın..."
                disabled={yukleniyor}
                style={{
                  flex: 1, padding: '10px 12px', borderRadius: '10px',
                  border: '1px solid rgba(0,0,0,0.12)', fontSize: '0.88rem',
                  fontFamily: 'inherit', outline: 'none',
                }}
              />
              <button
                onClick={gonder}
                disabled={yukleniyor || !girdi.trim()}
                style={{
                  padding: '0 16px', borderRadius: '10px', border: 'none',
                  cursor: (yukleniyor || !girdi.trim()) ? 'default' : 'pointer',
                  background: (yukleniyor || !girdi.trim()) ? '#cbd5e1' : 'linear-gradient(135deg, #16a34a, #22c55e)',
                  color: 'white', fontWeight: 600, fontSize: '0.88rem', fontFamily: 'inherit',
                }}
              >
                Gönder
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}

export default ChatWidget