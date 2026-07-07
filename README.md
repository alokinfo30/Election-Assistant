# Election-Assistant
 AI-powered Election Assistant that helps users understand the election process, timelines, and steps in an interactive way.


 ElectionAssistant/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model_manager.py
│   ├── agents.py
│   ├── tasks.py
│   ├── crew.py
│   ├── models.py
│   └── utils.py
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── data/
│   └── .gitkeep
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md






# 🗳️ AI-Powered Election Assistant

An intelligent assistant that helps users understand the election process, timelines, and steps in an interactive and easy-to-follow way.

## Features

- 📚 **Process Explanation**: Understand how elections work
- 📅 **Election Timeline**: See important dates and deadlines
- 📋 **Step-by-Step Guide**: Follow each step of the voting process
- ❓ **FAQ**: Get answers to common election questions
- ♿ **Accessibility**: Information for all voters
- 🌍 **Multi-Language Support**: 8+ languages available

## Architecture

### AI Agents

1. **Process Explainer**: Explains the election process in simple terms
2. **Timeline Agent**: Provides accurate election timelines
3. **Step Guide Agent**: Creates comprehensive step-by-step guides
4. **FAQ Agent**: Answers common election questions
5. **Accessibility Agent**: Ensures information is accessible to all

### Technology Stack

- **CrewAI** - Multi-agent orchestration
- **OpenRouter** - Multi-model support with auto-fallback
- **Flask** - Web framework
- **Pydantic** - Data validation
- **HTML/CSS/JS** - Responsive frontend

### Models Used

| Model | Provider | Use Case |
|-------|----------|----------|
| `openai/gpt-4o-mini` | OpenAI | Process Explanation, Accessibility |
| `mistralai/mixtral-8x22b-instruct` | Mistral | Timelines |
| `meta-llama/llama-3.1-8b-instruct` | Meta | Step Guides |
| `deepseek/deepseek-chat` | DeepSeek | FAQ |

## Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd ElectionAssistant

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with your OpenRouter API key
# (see .env.example for template)

# 5. Run the application
python run.py




Configuration
Environment Variables
Variable	Description
OPENROUTER_API_KEY	Your OpenRouter API key
OPENROUTER_PRIMARY_MODEL	Primary model to use
OPENROUTER_FALLBACK_MODELS	Fallback models
DEFAULT_ELECTION_COUNTRY	Default country for election info
SUPPORTED_LANGUAGES	Comma-separated language codes
API Endpoints
Endpoint	Method	Description
/	GET	Web interface
/api/service	POST	Handle service request
/api/services	GET	List all services
/api/models	GET	List available models
/api/health	GET	Health check
Service Types
process - Explanation of election process

timeline - Election timeline

step_guide - Step-by-step voting guide

faq - Answers to election questions

accessibility - Accessibility information





## Step 20: Final Commands

```powershell
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenRouter API key to .env

# 5. Run the application
python run.py

# 6. Open browser
# http://localhost:5000


✅ Features:

5 Specialized AI Agents for different election services

8+ Languages support for diverse users

Interactive Interface for easy understanding

Auto-Fallback between 4 different models

Responsive Design for mobile and desktop

Export and Copy functionality

Real-time Status Updates during processing

✅ Services:
📚 Process Explanation - Understand how elections work

📅 Timeline - Important dates and deadlines

📋 Step-by-Step Guide - Follow the voting process

❓ FAQ - Get answers to common questions

♿ Accessibility - Information for all voters

✅ Technology Stack:
CrewAI for multi-agent orchestration

OpenRouter for multi-model support

Flask for web interface

Pydantic for data validation

