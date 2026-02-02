# Ch36A WORKFLOW ORCHESTRATION ENGINE - 12 workflows → 20x leverage (Prefect + Ch33 Supervisor Integration)
from prefect import flow, task, get_run_logger
from prefect.deployments import Deployment
from typing import Dict, List
from decision_agent import Supervisor  # Ch33
from agentic_workflows import WORKFLOWS  # Ch36

@task
def route_to_agent(trigger: str) -> str:
    """Ch33 supervisor routing → Workflow agent"""
    supervisor = Supervisor()
    agent_name = supervisor.classify_trigger(trigger)
    return agent_name

@task  
def execute_workflow(agent_name: str, input_data: Dict) -> Dict:
    """Execute agentic workflow with Ch32 RAG context"""
    workflow = WORKFLOWS.get(agent_name)
    if workflow:
        result = workflow.execute(input_data)
        return {"status": "automated", "leverage": workflow.leverage}
    return {"status": "human_review"}

@flow(name="Ch36A.AgenticWorkflow")
async def agentic_workflow(trigger: str, input_data: Dict):
    """Orchestrates 5→12 agentic workflows → 20x leverage"""
    logger = get_run_logger()
    
    # 1. Ch33 Supervisor routes
    agent_name = await route_to_agent(trigger)
    logger.info(f"Routed to: {agent_name}")
    
    # 2. Execute workflow
    result = await execute_workflow(agent_name, input_data)
    
    # 3. Ch34 Intelligence logging
    await log_intelligence(result)
    
    return result

# 5 PRIORITY WORKFLOWS (Sprint 1)
PRIORITY_WORKFLOWS = Deployment.build_from_flow(
    flow=agentic_workflow,
    name="priority-workflows",
    parameters={"trigger": "codegen", "input_data": {}},
    schedule={"cron": "0 * * * *"}  # Hourly
)
