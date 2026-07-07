# app/agents.py
import os
import logging
from crewai import Agent
from app.model_manager import model_manager

logger = logging.getLogger(__name__)

try:
    from crewai_tools import SerperDevTool, ScrapeWebsiteTool
    TOOLS_AVAILABLE = True
except ImportError:
    logger.warning("⚠️ crewai_tools not available. Using fallback.")
    TOOLS_AVAILABLE = False
    
    class SerperDevTool:
        def __init__(self):
            self.name = "SerperDevTool"
            self.description = "Search tool (fallback)"
        def run(self, query):
            return f"Search results for: {query} (fallback)"
    
    class ScrapeWebsiteTool:
        def __init__(self):
            self.name = "ScrapeWebsiteTool"
            self.description = "Web scraping tool (fallback)"
        def run(self, url):
            return f"Scraped content from: {url} (fallback)"

def create_process_explainer():
    """Create the process explainer agent"""
    config = model_manager.get_model_config('process_explainer')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.3))
    
    return Agent(
        role="Election Process Expert",
        goal="Explain the election process in simple, clear terms",
        backstory=(
            "You are a senior election official with decades of experience in conducting "
            "elections. You have deep knowledge of electoral processes, voter registration, "
            "polling procedures, and result tabulation. You excel at explaining complex "
            "processes in simple, easy-to-understand language."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

def create_timeline_agent():
    """Create the timeline agent"""
    config = model_manager.get_model_config('timeline_agent')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.2))
    
    return Agent(
        role="Election Timeline Specialist",
        goal="Provide clear and accurate election timelines",
        backstory=(
            "You are an election timeline expert who has managed schedules for numerous "
            "elections. You understand the sequence of events from voter registration "
            "to result declaration. You provide clear, step-by-step timelines with "
            "important dates and deadlines."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

def create_step_guide_agent():
    """Create the step guide agent"""
    config = model_manager.get_model_config('step_guide_agent')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.4))
    
    return Agent(
        role="Election Step-by-Step Guide Expert",
        goal="Create comprehensive guides for each step of the election process",
        backstory=(
            "You are a voter education specialist who creates easy-to-follow guides. "
            "You break down complex procedures into simple steps, making them accessible "
            "to all voters regardless of their background or experience."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

def create_faq_agent():
    """Create the FAQ agent"""
    config = model_manager.get_model_config('faq_agent')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.3))
    
    return Agent(
        role="Election FAQ Specialist",
        goal="Answer common questions about elections",
        backstory=(
            "You are a voter helpdesk specialist who has answered thousands of election "
            "questions. You understand the concerns and confusions voters have and "
            "provide clear, accurate, and helpful answers."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

def create_accessibility_agent():
    """Create the accessibility agent"""
    config = model_manager.get_model_config('accessibility_agent')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.4))
    
    return Agent(
        role="Election Accessibility Specialist",
        goal="Ensure election information is accessible to all voters",
        backstory=(
            "You are an accessibility expert who ensures that election information and "
            "processes are accessible to all voters, including those with disabilities, "
            "elderly voters, and first-time voters. You provide information in multiple "
            "formats and languages."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )