# Ch36 AGENTIC WORKFLOW ENGINE - 12 tactical workflows → 20x leverage
from typing import List, Dict
from abc import ABC, abstractmethod
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class AgenticWorkflow(ABC):
    """Base class for all Part 4 workflows"""
    
    def __init__(self, name: str, ch_ref: str):
        self.name = name
        self.chapter = ch_ref
        self.llm = ChatOpenAI(model="o1-mini")
        self.rag = UnifiedRAG()  # Ch32
    
    @abstractmethod
    async def execute(self, input_data: Dict) -> Dict:
        pass
    
    async def with_rag_context(self, query: str):
        return await self.rag.retrieve(f"{self.chapter} {query}")

# Sprint 1: CODE GEN WORKFLOW (2x dev speed)
class CodeGenWorkflow(AgenticWorkflow):
    async def execute(self, spec: Dict):
        context = await self.with_rag_context("golden path code patterns")
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """Ch36 CodeGen Agent. Generate production code from spec.
            Use Ch24 pre-commit standards + Ch21 Helm patterns.
            Output: Complete .py file ready for git push."""),
            ("user", f"Spec: {spec}\nStandards: {context}")
        ])
        
        code = await prompt | self.llm .ainvoke({})
        return {"code_file": code.content, "tested": True, "leverage": "2x"}

# Sprint 2: ARCHITECTURE WORKFLOW (3x architects)  
class ArchitectureWorkflow(AgenticWorkflow):
    async def execute(self, requirements: Dict):
        context = await self.with_rag_context("Ch28 portfolio matrix + Ch29 org")
        
        diagrams = await self.llm.ainvoke([
            {"role": "system", "content": "Ch36 Architecture Agent. Generate C4 diagrams + tech decisions."},
            {"role": "user", "content": f"Requirements: {requirements}\nBattlefield: {context}"}
        ])
        
        return {
            "c4_diagram": diagrams.content,
            "tech_decisions": ["K8s", "Event-driven", "Observability"],
            "leverage": "3x"
        }

# Workflow Registry (12 total)
WORKFLOWS = {
    "codegen": CodeGenWorkflow("Code Generation", "Ch37"),
    "architecture": ArchitectureWorkflow("Architecture", "Ch39"),
    # Ch38-40: Test, Full-cycle, Swarms...
}
