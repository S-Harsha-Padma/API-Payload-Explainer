This project contains code for a API payload explainer</br>

Model used: Llama using Groq API</br>
UI: streamlit</br>

# Pre-requisites:
Make sure you have a GROQ_API_KEY and add it in your .env at the project root (It is free)
GROQ_API_KEY=<your_key>

# To Bootrap the APP:
## Create Virtual Environmet
python -m venv .venv (.venv can be any name of your choice)</br>
## Activate the env
source .venv/bin/activate </br>
pip install -r requirements.txt </br>
cd /pathto/your/project </br>
streamlit run app.py </br>
