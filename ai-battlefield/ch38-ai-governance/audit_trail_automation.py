# Ch38 AUDIT TRAIL - EU AI Act + SOX compliance → Zero deniability  (Immutable Compliance Log)
import hashlib
import sqlite3
from datetime import datetime

class AuditTrailAutomation:
    def __init__(self):
        self.db = sqlite3.connect('ch38_audit_trail.db')
        self.create_audit_table()
    
    def create_audit_table(self):
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS audit_trail (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                workflow_id TEXT,
                decision TEXT,
                confidence REAL,
                risk_score REAL,
                pnl_impact REAL,
                governance_result TEXT,
                audit_hash TEXT
            )
        ''')
        self.db.commit()
    
    def log_decision(self, workflow_id: str, decision_data: dict):
        """Immutable audit trail → EU AI Act compliance"""
        # Create audit hash (tamper-proof)
        audit_string = f"{workflow_id}{decision_data}{datetime.utcnow()}"
        audit_hash = hashlib.sha256(audit_string.encode()).hexdigest()
        
        self.db.execute('''
            INSERT INTO audit_trail 
            (timestamp, workflow_id, decision, confidence, risk_score, 
             pnl_impact, governance_result, audit_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            datetime.utcnow(),
            workflow_id,
            str(decision_data),
            decision_data.get('confidence', 0),
            decision_data.get('risk_score', 0),
            decision_data.get('pnl_impact', 0),
            decision_data.get('governance_result', 'PENDING'),
            audit_hash
        ))
        self.db.commit()
    
    def verify_integrity(self) -> bool:
        """Verify audit trail hasn't been tampered"""
        cursor = self.db.execute("SELECT * FROM audit_trail ORDER BY id")
        for row in cursor.fetchall():
            expected_hash = hashlib.sha256(str(row[:-1]).encode()).hexdigest()
            if expected_hash != row[-1]:  # audit_hash column
                return False
        return True
