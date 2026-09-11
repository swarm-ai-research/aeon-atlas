'use client'

import { useEffect, useMemo, useRef, useState } from 'react'
import type { Skill, Run } from '../../lib/types'
import type { TopicFile, IssueSummary } from '../../lib/memory'

/**
 * CrystalCore.OS — a themed view onto the real aeon-atlas fleet.
 *
 * Every number and line on this page comes from the same API routes the
 * main HQ dashboard uses (/api/skills, /api/runs, /api/memory/*). There is
 * no separate backend, no fictional data, and nothing here can trigger a
 * skill run or change config — it's read-only telemetry wearing a themed
 * boot-sequence / terminal skin.
 */

type Phase = 'boot' | 'desktop'
type ModuleId = 'fleet' | 'memory' | 'signal' | 'terminal'

interface FleetData {
  skills: Skill[]
  runs: Run[]
  topics: TopicFile[]
  issues: IssueSummary[]
  repo: string
}

function timeAgo(iso: string | null | undefined): string {
  if (!iso) return 'never'
  const ms = Date.now() - new Date(iso).getTime()
  if (!Number.isFinite(ms) || ms < 0) return 'just now'
  const mins = Math.floor(ms / 60000)
  if (mins < 1) return 'just now'
  if (mins < 60) return `${mins}m ago`
  const hrs = Math.floor(mins / 60)
  if (hrs < 24) return `${hrs}h ago`
  return `${Math.floor(hrs / 24)}d ago`
}

function useClock() {
  const [now, setNow] = useState(() => new Date())
  useEffect(() => {
    const id = setInterval(() => setNow(new Date()), 1000)
    return () => clearInterval(id)
  }, [])
  return now
}

async function fetchFleetData(): Promise<FleetData> {
  const [skillsRes, runsRes, topicsRes, issuesRes] = await Promise.allSettled([
    fetch('/api/skills').then((r) => r.json()),
    fetch('/api/runs').then((r) => r.json()),
    fetch('/api/memory/topics').then((r) => r.json()),
    fetch('/api/memory/issues').then((r) => r.json()),
  ])
  return {
    skills: skillsRes.status === 'fulfilled' ? skillsRes.value.skills ?? [] : [],
    runs: runsRes.status === 'fulfilled' ? runsRes.value.runs ?? [] : [],
    topics: topicsRes.status === 'fulfilled' ? topicsRes.value.topics ?? [] : [],
    issues: issuesRes.status === 'fulfilled' ? issuesRes.value.issues ?? [] : [],
    repo: skillsRes.status === 'fulfilled' ? skillsRes.value.repo ?? '' : '',
  }
}

function buildBootLog(data: FleetData): string[] {
  const enabled = data.skills.filter((s) => s.enabled)
  const lastRun = data.runs[0]
  const lines = [
    `Reading aeon.yml — ${data.skills.length} skills registered`,
    `${enabled.length} skill${enabled.length === 1 ? '' : 's'} on duty, ${data.skills.length - enabled.length} standing by`,
    `Memory archive mounted — ${data.topics.length} topic file${data.topics.length === 1 ? '' : 's'}`,
    data.issues.length > 0
      ? `${data.issues.length} open issue${data.issues.length === 1 ? '' : 's'} flagged`
      : 'No open issues',
    lastRun
      ? `Last run: ${lastRun.workflow} — ${lastRun.conclusion ?? lastRun.status} (${timeAgo(lastRun.created_at)})`
      : 'No run history yet',
    'System ready.',
  ]
  return lines
}

export default function CrystalCorePage() {
  const [phase, setPhase] = useState<Phase>('boot')
  const [bootIndex, setBootIndex] = useState(0)
  const [data, setData] = useState<FleetData | null>(null)
  const [activeModule, setActiveModule] = useState<ModuleId | null>(null)
  const now = useClock()

  useEffect(() => {
    fetchFleetData().then(setData)
  }, [])

  const bootLines = useMemo(() => (data ? buildBootLog(data) : []), [data])

  useEffect(() => {
    if (!data || phase !== 'boot') return
    if (bootIndex >= bootLines.length) {
      const t = setTimeout(() => setPhase('desktop'), 500)
      return () => clearTimeout(t)
    }
    const t = setTimeout(() => setBootIndex((i) => i + 1), 320)
    return () => clearTimeout(t)
  }, [data, phase, bootIndex, bootLines.length])

  const enabledCount = data?.skills.filter((s) => s.enabled).length ?? 0
  const totalCount = data?.skills.length ?? 0

  return (
    <div className="relative min-h-screen w-full overflow-hidden bg-[#06080f] text-white">
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap');
        .cc { font-family: 'IBM Plex Mono', monospace; }
        @keyframes cc-blink { 0%, 50% { opacity: 1 } 51%, 100% { opacity: 0 } }
      `}</style>
      <div className="cc absolute inset-0 -z-10 bg-[radial-gradient(120%_120%_at_50%_0%,#1a1040_0%,#0a0e1a_45%,#05070a_85%)]" />

      {phase === 'boot' && (
        <div className="cc relative z-10 flex min-h-screen flex-col items-center justify-center px-6">
          <div className="w-full max-w-[640px]">
            <div className="mb-8 flex items-center gap-3">
              <div className="h-[2px] w-8 bg-[#5fe6ff] shadow-[0_0_10px_#5fe6ff]" />
              <p className="text-[11px] tracking-[0.24em] text-white/50">
                {data?.repo ? data.repo.toUpperCase() : 'AEON FLEET'}
              </p>
            </div>
            <h1 className="mb-8 text-2xl font-semibold tracking-tight md:text-3xl">
              CrystalCore<span className="text-white/40">.OS</span>
              <span className="ml-1 inline-block h-[1em] w-2 translate-y-[3px] bg-[#5fe6ff] [animation:cc-blink_1s_steps(1)_infinite]" />
            </h1>
            <div className="space-y-2 border-l border-white/10 pl-5 text-[13px]">
              {!data && <div className="text-white/40">Connecting to fleet…</div>}
              {bootLines.slice(0, bootIndex).map((line, i) => (
                <div key={i} className="flex gap-3">
                  <span className="text-[#5fe6ff]">[OK]</span>
                  <span className="text-white/80">{line}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {phase === 'desktop' && data && (
        <div className="cc relative z-10 flex min-h-screen flex-col">
          <header className="flex h-12 items-center justify-between border-b border-white/[0.08] px-5">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-[#5fe6ff] shadow-[0_0_8px_#5fe6ff]" />
              <span className="text-[13px] font-semibold">CrystalCore.OS</span>
              <span className="text-[10px] text-white/30">{data.repo || 'aeon fleet'}</span>
            </div>
            <div className="flex items-center gap-4 text-[11px] text-white/50">
              <span>{enabledCount}/{totalCount} on duty</span>
              <span className="tabular-nums">{now.toISOString().slice(11, 19)} UTC</span>
            </div>
          </header>

          <main className="flex flex-1 flex-col items-center px-4 pb-16 pt-10">
            <div className="mb-10 text-center">
              <div className="mx-auto mb-4 h-16 w-16 rotate-45 border-2 border-[#5fe6ff] shadow-[0_0_24px_rgba(95,230,255,0.5)]" />
              <div className="text-[11px] tracking-[0.2em] text-white/40">
                {enabledCount} SKILL{enabledCount === 1 ? '' : 'S'} ACTIVE
              </div>
            </div>

            <div className="grid w-full max-w-[820px] grid-cols-2 gap-3 md:grid-cols-4">
              {(
                [
                  { id: 'fleet', label: 'FLEET', sub: `${totalCount} skills`, accent: '#5fe6ff' },
                  { id: 'memory', label: 'MEMORY CORE', sub: `${data.topics.length} topics`, accent: '#b48bff' },
                  { id: 'signal', label: 'SIGNAL LOG', sub: `${data.runs.length} recent runs`, accent: '#d9a94e' },
                  { id: 'terminal', label: 'TERMINAL', sub: 'crystal@core', accent: '#ffffff' },
                ] as { id: ModuleId; label: string; sub: string; accent: string }[]
              ).map((m) => (
                <button
                  key={m.id}
                  onClick={() => setActiveModule(m.id)}
                  className="rounded-lg border border-white/10 bg-white/[0.03] p-4 text-left transition hover:border-white/25 hover:bg-white/[0.06]"
                >
                  <div className="mb-2 h-[6px] w-[6px] rounded-full" style={{ background: m.accent, boxShadow: `0 0 8px ${m.accent}` }} />
                  <div className="text-[12px] font-semibold">{m.label}</div>
                  <div className="mt-1 text-[10px] text-white/40">{m.sub}</div>
                </button>
              ))}
            </div>
          </main>

          {activeModule && (
            <ModulePanel
              moduleId={activeModule}
              data={data}
              onClose={() => setActiveModule(null)}
            />
          )}
        </div>
      )}
    </div>
  )
}

function ModulePanel({ moduleId, data, onClose }: { moduleId: ModuleId; data: FleetData; onClose: () => void }) {
  return (
    <div className="fixed inset-0 z-30 flex items-end justify-center bg-black/60 p-3 backdrop-blur-md md:items-center">
      <div className="w-full max-w-[640px] overflow-hidden rounded-xl border border-white/10 bg-[#0b1120]">
        <div className="flex items-center justify-between border-b border-white/10 px-5 py-3">
          <span className="text-[12px] font-semibold uppercase tracking-wide">{moduleId}</span>
          <button onClick={onClose} className="text-white/50 hover:text-white">✕</button>
        </div>
        <div className="max-h-[60vh] overflow-y-auto p-5">
          {moduleId === 'fleet' && <FleetList skills={data.skills} />}
          {moduleId === 'memory' && <TopicList topics={data.topics} />}
          {moduleId === 'signal' && <RunList runs={data.runs} />}
          {moduleId === 'terminal' && <Terminal data={data} />}
        </div>
      </div>
    </div>
  )
}

function FleetList({ skills }: { skills: Skill[] }) {
  if (skills.length === 0) return <p className="text-[12px] text-white/40">No skills found.</p>
  return (
    <div className="space-y-1.5">
      {skills.slice(0, 40).map((s) => (
        <div key={s.name} className="flex items-center justify-between border-b border-white/5 py-1.5 text-[12px]">
          <span className="text-white/80">{s.name}</span>
          <span className={s.enabled ? 'text-[#5be3a5]' : 'text-white/30'}>{s.enabled ? 'ON DUTY' : 'off'}</span>
        </div>
      ))}
      {skills.length > 40 && <p className="pt-2 text-[11px] text-white/30">+{skills.length - 40} more</p>}
    </div>
  )
}

function TopicList({ topics }: { topics: TopicFile[] }) {
  if (topics.length === 0) return <p className="text-[12px] text-white/40">No memory topics yet.</p>
  return (
    <div className="space-y-1.5">
      {topics.map((t) => (
        <div key={t.slug} className="flex items-center justify-between border-b border-white/5 py-1.5 text-[12px]">
          <span className="text-white/80">{t.slug}</span>
          <span className="text-white/30">{timeAgo(t.updatedAt)}</span>
        </div>
      ))}
    </div>
  )
}

function RunList({ runs }: { runs: Run[] }) {
  if (runs.length === 0) return <p className="text-[12px] text-white/40">No run history yet.</p>
  return (
    <div className="space-y-1.5">
      {runs.slice(0, 20).map((r) => (
        <div key={r.id} className="flex items-center justify-between border-b border-white/5 py-1.5 text-[12px]">
          <span className="text-white/80">{r.workflow}</span>
          <span className={r.conclusion === 'success' ? 'text-[#5be3a5]' : r.conclusion === 'failure' ? 'text-[#ff6a6a]' : 'text-white/40'}>
            {r.conclusion ?? r.status} · {timeAgo(r.created_at)}
          </span>
        </div>
      ))}
    </div>
  )
}

function Terminal({ data }: { data: FleetData }) {
  const [lines, setLines] = useState<string[]>([
    'CrystalCore.OS shell — read-only view onto the real fleet.',
    "Type 'help' for commands.",
    '',
  ])
  const [input, setInput] = useState('')
  const endRef = useRef<HTMLDivElement>(null)

  useEffect(() => { endRef.current?.scrollIntoView({ behavior: 'smooth' }) }, [lines])

  const run = (raw: string) => {
    const cmd = raw.trim().toLowerCase()
    const out: string[] = [`crystal@core:~$ ${raw}`]
    switch (cmd) {
      case 'help':
        out.push('help, status, skills, issues, topics, whoami, clear')
        break
      case 'status': {
        const enabled = data.skills.filter((s) => s.enabled).length
        out.push(
          `${enabled}/${data.skills.length} skills on duty`,
          `${data.issues.length} open issue(s)`,
          `${data.runs.length} recent run(s) tracked`,
        )
        break
      }
      case 'skills':
        out.push(...data.skills.filter((s) => s.enabled).map((s) => `  ${s.name}`))
        if (out.length === 1) out.push('  (none enabled)')
        break
      case 'issues':
        out.push(...(data.issues.length ? data.issues.map((i) => `  ${i.id}`) : ['  no open issues']))
        break
      case 'topics':
        out.push(...(data.topics.length ? data.topics.map((t) => `  ${t.slug}`) : ['  no topics yet']))
        break
      case 'whoami':
        out.push(`Node: ${data.repo || 'unknown repo'}`, 'This terminal is read-only — no commands are executed on the real system.')
        break
      case 'clear':
        setLines([])
        setInput('')
        return
      default:
        out.push(`command not found: ${raw}`)
    }
    setLines((l) => [...l, ...out, ''])
    setInput('')
  }

  return (
    <div className="flex h-[360px] flex-col rounded-md border border-white/10 bg-black/40">
      <div className="flex-1 overflow-y-auto p-4 text-[12px] leading-relaxed text-white/70">
        {lines.map((l, i) => <div key={i} className="whitespace-pre-wrap">{l || ' '}</div>)}
        <div ref={endRef} />
      </div>
      <div className="flex items-center gap-2 border-t border-white/10 px-4 py-2">
        <span className="text-[11px] text-[#5fe6ff]">crystal@core:~$</span>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter' && input.trim()) run(input) }}
          className="flex-1 bg-transparent text-[12px] text-white outline-none"
          placeholder="help"
          autoFocus
        />
      </div>
    </div>
  )
}
