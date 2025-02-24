# Ctrl Shift Intelligence

The repository showcases our solutions in the domains of education, content creation and business for ctrl shift intelligence. The app can be accessed at https://ctrl-shift-intelligence.streamlit.app/

## Overview
A Streamlit-based web application offering AI-powered solutions across education, content creation, and business domains. Features include topic explanations, question generation, creative writing, and customer support assistance.

## Features
- **Education Tools**
  - Topic Explainer: Detailed explanations of academic subjects
  
  Example: Put *Chemistry* as subject and *Alkenes* as topic. The AI will explain the topic in brief. You can further prompt more queries to it
  
  - Question Maker: Customizable question generation
  
  Example: Put *Maths* as subject and *Bellman Equations* as topic. The field for number of questions and difficulty can be left with the default values or be changed as required. The AI will generate the number of questions asked, at the difficulty level specified for the given subject and topic

- **Content Creation**
  - Shakespeare Says: AI-generated creative writing
  
  Example: Ask the AI to generate prose or poems in the style of Shakespeare or in the style of whicever English writer you wish. Just specify the theme of the content (and optionally writer)

- **Business Solutions**
  - Customer Support: Product-specific troubleshooting
  
  Example: Enter the bill id `BILL-99001`, name of product as *Wireless Mouse* and any issue you're facing. The chatbot will guide you through. Entering the bill ID and issue is compulsory, and either the product name, or the product ID must be entered. All the value bill IDs can be found in `data.jon`

**IMPORTANT**: After the *running* symbol dissapears from the top right, just press the key `r` to show the response from the AI. 

*Note: In all of these tools, you can further prompt the AI to modify the queries or get further assistance on the matter*

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


