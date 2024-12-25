import streamlit as st

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(
    api_key=api_key,
)

@st.cache_resource
def load_RAG():

    # import any embedding model on HF hub (https://huggingface.co/spaces/mteb/leaderboard)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    # Settings.embed_model = HuggingFaceEmbedding(model_name="thenlper/gte-large") # alternative model

    Settings.llm = None
    Settings.chunk_size = 256
    Settings.chunk_overlap = 25

    documents = SimpleDirectoryReader("Downloaded_Books").load_data()
    index = VectorStoreIndex.from_documents(documents)

    # set number of docs to retreive
    top_k = 5

    # configure retriever
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=top_k,
    )

    # assemble query engine
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.5)],
    )

    return query_engine

query_engine = load_RAG()

col1,col2 = st.columns([4,1])

with col1:
    st.title("GIKI Digital Library")
with col2:
    st.write("")
    st.write("")
    if st.button("New Chat"):
        st.session_state.messages = []

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter your question here"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = query_engine.query(prompt)
    # reformat response
    context = "Context:\n"
    for i in range(len(response.source_nodes)):
        context = context + response.source_nodes[i].text + "\n\n"

    final_prompt = f"""[INST]
    {context}
    Please respond to the following comment. Use the context above if it is helpful.
    {prompt}
    [/INST]
    """

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        model="llama3-8b-8192",
    )

    answer = chat_completion.choices[0].message.content

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(answer)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})
