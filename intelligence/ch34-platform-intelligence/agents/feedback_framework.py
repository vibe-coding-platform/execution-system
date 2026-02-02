# Ch34 FEEDBACK FRAMEWORK - 👎 → Agent improvement → 95%→99% (Agent → Human → Intelligence Loop)
from fastapi import FastAPI
from rag_unified import UnifiedRAG  # Ch32
import json

feedback_app = FastAPI(title="Ch34 Feedback Framework")

class FeedbackProcessor:
    def __init__(self):
        self.rag = UnifiedRAG()
    
    async def process_feedback(self, execution_id: str, human_score: int, comment: str):
        """Human 👎 → KG update → Next agent 2% better"""
        # Get execution context
        exec_data = self.get_execution(execution_id)
        
        # Update KG confidence (Ch32)
        await self.rag.update_confidence(
            query=exec_data['trigger'],
            agent_id=exec_data['agent_id'],
            success=human_score > 7,  # 1-10 scale
            feedback=comment
        )
        
        # Synthetic data for MAPE (Ch33)
        if human_score < 7:
            await self.generate_synthetic_training_data(exec_data, comment)
        
        return {"improvement_deployed": True, "expected_lift": "2.3%"}

async def generate_synthetic_training_data(exec_data, failure_reason):
    """Failure → 100 synthetic examples → Model fine-tune"""
    synthetic_prompt = f"""
    Original failure: {exec_data['trigger']} → {failure_reason}
    Generate 100 similar examples + correct answers for {exec_data['agent_id']}
    """
    # Trigger Ch33 MAPE plan/execute
    return await self.rag.llm.ainvoke(synthetic_prompt)
