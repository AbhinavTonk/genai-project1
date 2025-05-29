import gradio

def dev_ai_agent():
    pass

def qa_ai_agent():
     pass


# Main
if __name__ == '__main__':
    dev_ai_agent_interface = gradio.Interface(fn=dev_ai_agent,
                            title="🤖 Dev AI Agent",
                            description="©Abhinav Tonk",
                            inputs=[
                                gradio.Textbox(label="Ask Dev AI Agent"),
                                gradio.Dropdown(choices=["8qdrilldown", "testcases"], label="Genai Usecase"),
                                gradio.File(file_types=[".txt"], type="filepath", label="Context Document"),
                                gradio.File(file_types=[".txt"], type="filepath", label="Examples")
                            ],
                            submit_btn="Send", #default = "Submit"
                            clear_btn="Reset", #default = "Clear"
                            outputs=gradio.Textbox(label="Generated Prompt"))

    qa_ai_agent_interface = gradio.Interface(fn=qa_ai_agent,
                     title="🤖 QA AI Agent",
                     description="©Abhinav Tonk",
                     inputs=[
                         gradio.Textbox(label="Ask QA AI Agent"),
                         gradio.Dropdown(choices=["8qdrilldown", "testcases"], label="Genai Usecase"),
                         gradio.File(file_types=[".txt"], type="filepath", label="Context Document"),
                         gradio.File(file_types=[".txt"], type="filepath", label="Examples")
                     ],
                     submit_btn="Send",  # default = "Submit"
                     clear_btn="Reset",  # default = "Clear"
                     outputs=gradio.Textbox(label="Generated Prompt"))

    demo = gradio.TabbedInterface([dev_ai_agent_interface, qa_ai_agent_interface],["Dev AI Agent", "QA AI Agent"])
    demo.launch(server_name="127.0.0.9", server_port=8080)