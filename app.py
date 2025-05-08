from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import gradio as gr
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. Load and prepare documents
def load_docs():
    docs = []
    # Load code examples
    try:
        with open("data/sample_code.py", "r") as f:
            code = f.read()
            docs.append(code)
    except FileNotFoundError:
        print("Warning: data/sample_code.py not found")
    
    # Load documentation
    try:
        with open("data/docs.txt", "r") as f:
            text = f.read()
            docs.append(text)
    except FileNotFoundError:
        print("Warning: data/docs.txt not found")
    
    if not docs:
        raise ValueError("No documents found to process")
    
    # Split into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    return text_splitter.split_text("\n\n".join(docs))

# 2. Create vector database
def setup_vectordb():
    documents = load_docs()
    # Using HuggingFace embeddings as a reliable alternative
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma.from_texts(documents, embeddings)

# 3. Initialize LLM
llm = Ollama(model="mistral")

# 4. Create RAG chain
db = setup_vectordb()
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=db.as_retriever(search_kwargs={"k": 2}),
    chain_type="stuff"
)

# 5. Gradio interface
def explain_code(code_snippet):
    if not code_snippet.strip():
        return "Please enter some code to explain."
    
    response = qa_chain.invoke({
        "query": f"Explain this code: {code_snippet}. Include time complexity and common use cases."
    })
    return response["result"]

interface = gr.Interface(
    fn=explain_code,
    inputs=gr.Textbox(lines=5, placeholder="Paste code here..."),
    outputs="text",
    title="AI Code Explainer",
    description="Enter code to get an explanation of how it works, its time complexity, and common use cases."
)

if __name__ == "__main__":
    interface.launch()
