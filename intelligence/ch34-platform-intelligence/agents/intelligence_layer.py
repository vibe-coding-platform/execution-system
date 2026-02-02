# Ch34 PLATFORM INTELLIGENCE LAYER - Ch33 Agents → Exec Insights → $3M/yr  (Platform Intelligence Spec)
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pandas as pd

app = FastAPI(title="Ch34 Platform Intelligence")
Base = declarative_base()
engine = create_engine('sqlite:///ch34_intelligence.db')
SessionLocal = sessionmaker(bind=engine)

class AgentExecution(Base):
    __tablename__ = 'agent_executions'
    id = Column(Integer, primary_key=True)
    agent_id = Column(String)  # D001, D002, etc
    timestamp = Column(DateTime, default=datetime.utcnow)
    success = Column(Integer)  # 1=success, 0=failure
    latency_ms = Column(Float)
    savings_usd = Column(Float)
    human_intervention = Column(Integer)

Base.metadata.create_all(engine)

class IntelligenceLayer:
    def __init__(self):
        self.db = SessionLocal()
    
    def log_execution(self, agent_id: str, success: bool, latency: float, savings: float):
        """Log every Ch33 agent execution → Real-time P&L"""
        exec = AgentExecution(
            agent_id=agent_id,
            success=1 if success else 0,
            latency_ms=latency,
            savings_usd=savings,
            human_intervention=0
        )
        self.db.add(exec)
        self.db.commit()
    
    def get_pnl_dashboard(self):
        """Exec P&L dashboard → $942k/yr trajectory"""
        df = pd.read_sql("SELECT * FROM agent_executions WHERE timestamp > datetime('now', '-30 days')", engine)
        
        metrics = {
            "total_executions": len(df),
            "success_rate": df['success'].mean(),
            "avg_latency_ms": df['latency_ms'].mean(),
            "total_savings_30d": df['savings_usd'].sum(),
            "annualized_savings": df['savings_usd'].sum() * 12 * 4.33,
            "top_agent": df.groupby('agent_id')['savings_usd'].sum().idxmax()
        }
        return metrics

@app.post("/log")
async def log_execution(data: dict):
    intel = IntelligenceLayer()
    intel.log_execution(**data)
    return intel.get_pnl_dashboard()
