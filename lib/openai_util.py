import os
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

import lib.text_file_util as text_file_util
import lib.pdf_util as pdf_util
from config.api_key_config import api_key
from lib.rag_util import base_context_creation_and_retrieval_vector_db
from prompt_engineering import role, audience, output_format, tone

# Domain Knowledge Agent
def ask_domain_knowledge_agent(base_context_folder, query):
    # Step 1: Retrieve context documents
    retriever = base_context_creation_and_retrieval_vector_db(base_context_folder)
    docs = retriever.get_relevant_documents(query)
    context_text = "\n".join([doc.page_content for doc in docs])

    # Step 2: Prompt template
    prompt = PromptTemplate(
        input_variables=["context", "role", "tone", "format", "query"],
        template=text_file_util.read_text_file("prompt_engineering/domain_document_prompt.txt")
    )

    # Step 3: Create LLMChain
    llm_chain = LLMChain(
        llm=ChatOpenAI(model_name="gpt-4o", openai_api_key=api_key),
        prompt=prompt
    )

    # Step 4: Inputs for prompt
    inputs = {
        "query": query,
        "context": context_text,
        "role": role.PRODUCT_OWNER,
        "tone": tone.PROFESSIONAL,
        "format": output_format.HTML
    }

    # Step 5: Run LLMChain
    result = llm_chain.invoke(inputs)
    response = result["text"]

    print("Answer:\n", response)

    # Step 6: Save outputs (when using non html formats)
    # text_file_util.write_text_file("outputs/output.txt", response)
    # pdf_util.create_pdf("outputs/output.pdf", response)

    return response

