import os
import json
from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader, CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def get_file_state(root_folder):
    file_state = {}
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                modified_time = os.path.getmtime(filepath)
                file_state[filepath] = modified_time
            except Exception as e:
                print(f"Error reading file time for {filepath}: {e}")
    return file_state

def has_file_changes(root_folder, state_file=".file_state.json"):
    current_state = get_file_state(root_folder)
    if os.path.exists(state_file):
        with open(state_file, "r") as f:
            previous_state = json.load(f)
        if current_state != previous_state:
            with open(state_file, "w") as f:
                json.dump(current_state, f)
            return True
        return False
    else:
        with open(state_file, "w") as f:
            json.dump(current_state, f)
        return True

def base_context_creation_and_retrieval_vector_db(root_folder, persist_directory="rag_db", forceRewriteVectorDB=False):
    all_docs = []
    vector_db = None
    state_file = os.path.join(persist_directory, ".file_state.json")

    should_rewrite = forceRewriteVectorDB or not os.path.exists(os.path.join(persist_directory, "chroma.sqlite3")) or has_file_changes(root_folder, state_file)

    if should_rewrite:
        print("🔄 Rebuilding vector DB due to changes or force flag.")
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                filepath = os.path.join(root, file)
                ext = os.path.splitext(filepath)[1].lower()

                if ext == ".txt":
                    loader = TextLoader(filepath)
                elif ext == ".pdf":
                    loader = PyPDFLoader(filepath)
                elif ext == ".docx":
                    loader = Docx2txtLoader(filepath)
                elif ext == ".csv":
                    loader = CSVLoader(filepath)
                else:
                    print(f"Unsupported file type: {filepath}")
                    continue

                try:
                    docs = loader.load()
                    all_docs.extend(docs)
                except Exception as e:
                    print(f"Failed to load {filepath}: {e}")

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = splitter.split_documents(all_docs)

        embedding = OpenAIEmbeddings(openai_api_key=api_key)
        vector_db = Chroma.from_documents(split_docs, embedding, persist_directory=persist_directory)
        vector_db.persist()
        print(f"✅ Vector DB updated at '{persist_directory}'")
    else:
        print("✅ Vector DB unchanged. Using existing.")
        embedding = OpenAIEmbeddings(openai_api_key=api_key)
        vector_db = Chroma(persist_directory=persist_directory, embedding_function=embedding)

    return vector_db.as_retriever(search_kwargs={"k": 50})