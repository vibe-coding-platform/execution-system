// Ch24 - Governance view in self-service portal (React/Next.js page or component)
export default function GovernanceView() {
  return (
    <div className="bg-slate-950 min-h-screen text-slate-50 p-8">
      <h1 className="text-4xl font-black mb-6">Smart Governance</h1>

      <div className="grid md:grid-cols-3 gap-6 mb-10">
        <Metric value="92%" label="Pre-commit coverage" />
        <Metric value="88%" label="Policy-compliant pipelines" />
        <Metric value="0" label="Direct prod changes (30d)" />
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        <Card title="Pre-commit Status">
          <ul className="space-y-2 text-sm text-slate-200">
            <li>✔ .pre-commit-config.yaml in 47/50 repos</li>
            <li>✔ Vibe snowflake policy installed in 43/50 repos</li>
            <li>⚠ 3 repos still allow direct pushes to main</li>
          </ul>
        </Card>

        <Card title="Policy-as-Code Checks">
          <ul className="space-y-2 text-sm text-slate-200">
            <li>✔ K8s: No :latest images</li>
            <li>✔ Terraform: No public S3 buckets</li>
            <li>⚠ 2 pipelines missing OPA step</li>
          </ul>
        </Card>
      </div>
    </div>
  );
}

function Metric({ value, label }: { value: string; label: string }) {
  return (
    <div className="bg-slate-900 border border-slate-700 rounded-2xl p-6 text-center">
      <div className="text-3xl font-bold text-emerald-400">{value}</div>
      <div className="text-slate-400 text-sm mt-1">{label}</div>
    </div>
  );
}

function Card({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="bg-slate-900 border border-slate-700 rounded-2xl p-6">
      <h2 className="text-lg font-semibold mb-3">{title}</h2>
      {children}
    </div>
  );
}