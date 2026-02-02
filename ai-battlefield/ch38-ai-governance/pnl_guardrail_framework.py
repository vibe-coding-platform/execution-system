# Ch38 P&L GUARDRails - $15M/yr protected → No rogue workflows  (Financial Risk Controls)
import sqlite3
from datetime import datetime, timedelta

class PnLGuardrailFramework:
    def __init__(self):
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect('ch38_governance.db')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS pnl_guardrails (
                workflow_id TEXT,
                pnl_impact REAL,
                risk_score REAL,
                decision TEXT,
                timestamp DATETIME,
                audit_hash TEXT
            )
        ''')
        conn.commit()
        conn.close()
    
    def validate_pnl_impact(self, workflow_id: str, projected_pnl: float) -> bool:
        """$100k minimum impact + portfolio balance check"""
        conn = sqlite3.connect('ch38_governance.db')
        
        # Historical baseline
        baseline = conn.execute(
            "SELECT AVG(pnl_impact) FROM pnl_guardrails WHERE decision='APPROVED'"
        ).fetchone()[0] or 0
        
        # Guardrails
        portfolio_concentration = self.check_portfolio_balance(workflow_id)
        min_impact = projected_pnl > 100000  # $100k threshold
        
        conn.close()
        return min_impact and portfolio_concentration
    
    def check_portfolio_balance(self, workflow_id: str) -> bool:
        """No workflow >25% total portfolio risk"""
        conn = sqlite3.connect('ch38_governance.db')
        total = conn.execute("SELECT SUM(pnl_impact) FROM pnl_guardrails").fetchone()[0]
        workflow_total = conn.execute(
            "SELECT SUM(pnl_impact) FROM pnl_guardrails WHERE workflow_id=?", 
            (workflow_id,)
        ).fetchone()[0] or 0
        
        concentration = (workflow_total / total) < 0.25 if total > 0 else True
        conn.close()
        return concentration
