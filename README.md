# genai-project1 (AI Knowledge Agent)

# 1- Pull the project in your local
git clone <projectRepoUrl>

# 2- Create Python Virtual Environment (First time only)
a) Navigate to the root directory of your project
b) python -m venv venv

# 3- Activate Virtual Environment (From root directory where venv folder is created)
    a) Windows: venv\Scripts\activate.bat
    b) Unix: source venv/bin/activate

# 4- Install Dependencies (from root folder of project where requirements.txt is present)
pip install -r requirements.txt

# 5- Setup openai api key
set OPENAI_API_KEY=<Your openai api key>

# 6- Running the python script from root directory
python -m bin.app
