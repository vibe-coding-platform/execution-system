# Human 👍👎 → KG updates → 95%→99%
class FeedbackFlywheel:
    async def update_kg(self, query: str, human_feedback: str, success: bool):
        # Update confidence scores
        cypher = """
        MERGE (q:Query {text: $query})
        MERGE (c:Chapter {id: $chapter_id})
        MERGE (q)-[:IMPROVES_WITH {success: $success, feedback: $feedback}]->(c)
        """
        self.graph.query(cypher, {
            "query": query,
            "chapter_id": "Ch21",  # Example
            "success": success,
            "feedback": human_feedback
        })
