# Ctrl Shift Intelligence

The repository showcases our solutions in the domains of education, content creation and business for ctrl shift intelligence. The app can be accessed at https://ctrl-shift-intelligence.streamlit.app/

## Overview
A Streamlit-based web application offering AI-powered solutions across education, content creation, and business domains. Features include topic explanations, question generation, creative writing, and customer support assistance.

## Features
- **Education Tools**
  - Topic Explainer: Detailed explanations of academic subjects
  - Question Maker: Customizable question generation
- **Content Creation**
  - Shakespeare Says: AI-generated creative writing
- **Business Solutions**
  - Customer Support: Product-specific troubleshooting


# Project Structure
```
├── data.json                      # Product database for customer support
└── website/
    ├── landing_page.py            # Main entry point
    ├── styling.py                 # UI styling configurations
    ├── classes.py                 # API interactions
    ├── prompts.py                 # AI prompt templates
    ├── requirements.txt           # Dependency list
    └── pages/
        ├── Topic_Explainer.py     # Topic explanation module
        ├── Question_Maker.py      # Question generation module
        ├── ShakeSpear_Says.py     # Creative writing module
        └── Customer_Support.py    # Support ticket system
```



# Installation and Setup

1. Go to [Openrouter](https://openrouter.ai/) and register
2. Navigate to its [settings](https://openrouter.ai/settings/keys) and create a new API key


3. Clone the respository

```
git clone https://github.com/AMOGHA1140/ctrl_shift_intelligence.git
```

4. Navigate into the cloned respository and install necessary packages

```
cd ctrl_shift_intelligence
pip install -r requirements.txt
```

5. Open `classes.py` and change the value of `API_KEY` to the new api key which you just created on Openrouter

6. Run the website

```
streamlit run /website/landing_page.py
```
