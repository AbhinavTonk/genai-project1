import gradio as gr

from lib.openai_util import ask_domain_knowledge_agent


# Dummy backend functions for each sub-agent
def domain_knowledge_agent(domain_document_path, ask):
    # response = ask_llm("T:/python_workspaces/RAG_Documents", ask)
    response = ask_domain_knowledge_agent(domain_document_path, ask)
    return response

def summarizing_agent(text):
    return f"Summary of: {text}"

def research_agent(query):
    return f"Research info on: {query}"

# Interfaces for each subtab
domain_interface = gr.Interface(
    fn=domain_knowledge_agent,
    inputs=[gr.Textbox(label="Enter Complete Root Folder Path for your Domain Documents", placeholder="/path/to/your/domaindocument/rootfolder/using/forward/slash"),
            gr.Textbox(label="Ask Domain Knowledge Agent")],
    #outputs=gr.Textbox(label="Response"),
    outputs=gr.HTML(),
    title="🧠 Domain Knowledge Agent",
    description="Handles domain-specific queries."
)

summarizing_interface = gr.Interface(
    fn=summarizing_agent,
    inputs=gr.Textbox(label="Text to Summarize"),
    outputs=gr.Textbox(label="Summary"),
    title="📝 Summarizing Agent",
    description="Summarizes input text."
)

research_interface = gr.Interface(
    fn=research_agent,
    inputs=gr.Textbox(label="Research Query"),
    outputs=gr.Textbox(label="Research Result"),
    title="✍️ Research Agent",
    description="Performs research based on input query."
)

# Combine all interfaces into a TabbedInterface
demo = gr.TabbedInterface(
    interface_list=[
        domain_interface,
        summarizing_interface,
        research_interface
    ],
    tab_names=[
        "Domain Knowledge Agent",
        "Summarizing Agent",
        "Research Agent"
    ],
    title="🤖 AI Knowledge Agent"
)

# Launch the app
demo.launch(server_name="127.0.0.9", server_port=8080)
