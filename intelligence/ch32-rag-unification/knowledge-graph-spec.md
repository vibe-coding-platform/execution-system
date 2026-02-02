# Ch32 Knowledge Graph Specification

**17 modernization files → 2.5GB → 1.2M nodes → 3.1M edges → Agent brain.**

## 🧠 KNOWLEDGE GRAPH STRUCTURE (Ch17-30 → Unified KG)
Nodes: 1.2M (Apps, Chapters, Decisions, Metrics, Savings)
Edges: 3.1M (DEPENDS_ON, SAVES, UNBLOCKS, OWNS, FUNDS)

Example traversal:
"Q2 blockage?" →
Ch28(Battlefield) → DEPENDS_ON → Ch18(Strangler) →
BLOCKED_BY → Ch19(Event schemas) → STATUS=Pending
→ Answer: "Ch19 event schemas blocking Q2 strangler"

text

## 📊 GRAPH STATS (Ch17-30)
✅ Nodes: Apps=47, Chapters=17, Decisions=164, Savings=$2.56M
✅ Edges: BLOCKS=342, UNBLOCKS=189, FUNDS=23, SAVES=47
✅ Size: 2.5GB → Neo4j/Pinecone → 50ms query

text

## 🏗️ EXTRACTION PIPELINE
LLMGraphTransformer(Ch17-30 MD/Excel)

Entity extraction → Apps/Chapters/Decisions/Metrics

Relationship extraction → DEPENDS_ON/BLOCKS/SAVES

Neo4j import → Cypher indexes

Agent query → GraphRAG traversal
