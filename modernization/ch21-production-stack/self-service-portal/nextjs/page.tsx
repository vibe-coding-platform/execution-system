// Ch21 Self-Service Portal - Deploy your service in 90s
export default function SelfServicePortal() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="max-w-4xl mx-auto p-8">
        <h1 className="text-5xl font-black bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent mb-12">
          Service Self-Service
        </h1>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Deploy New Service */}
          <div className="bg-white/10 backdrop-blur-xl p-8 rounded-3xl border border-white/20">
            <h2 className="text-2xl font-bold text-white mb-6">Deploy Service</h2>
            <div className="space-y-4">
              <input placeholder="GitHub repo (e.g. platform-starter fork)" className="w-full p-4 bg-white/10 rounded-2xl border border-white/20 text-white placeholder-white/60" />
              <div className="grid grid-cols-2 gap-4">
                <button className="bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-4 px-6 rounded-2xl transition-all duration-200">
                  🚀 Staging
                </button>
                <button className="bg-purple-600 hover:bg-purple-700 text-white font-bold py-4 px-6 rounded-2xl transition-all duration-200">
                  ⛩️ Production
                </button>
              </div>
            </div>
          </div>

          {/* Compliance Dashboard */}
          <div className="bg-white/10 backdrop-blur-xl p-8 rounded-3xl border border-white/20">
            <h2 className="text-2xl font-bold text-white mb-6">Compliance</h2>
            <div className="grid grid-cols-2 gap-4 text-center">
              <div>
                <div className="text-3xl font-black text-emerald-400">98%</div>
                <div className="text-slate-300">Pattern Compliance</div>
              </div>
              <div>
                <div className="text-3xl font-black text-amber-400">47/50</div>
                <div className="text-slate-300">Services Golden Path</div>
              </div>
              <div>
                <div className="text-3xl font-black text-sky-400">3.2min</div>
                <div className="text-slate-300">Deploy → Prod</div>
              </div>
              <div>
                <div className="text-3xl font-black text-rose-400">0.8%</div>
                <div className="text-slate-300">Error Rate</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
