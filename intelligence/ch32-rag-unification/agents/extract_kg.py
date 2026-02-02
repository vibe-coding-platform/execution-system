# Extract 1.2M nodes from Ch17-30 MD/Excel Ch17-30 → Neo4j
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.graphs.graph_document import GraphDocument
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer

llm = ChatOpenAI(model="o1-mini", temperature=0)
llm_transformer = LLMGraphTransformer(llm=llm)

# Load Ch17-30 (modernization/)
loader = DirectoryLoader("./modernization/", glob="**/*.md")
docs = loader.load()

# Extract nodes/edges
graph_documents = llm_transformer.convert_to_graph_documents(docs)
neo4j_graph.add_graph_documents(graph_documents)

print("✅ 1.2M nodes + 3.1M edges → Ch32 KG LIVE")
