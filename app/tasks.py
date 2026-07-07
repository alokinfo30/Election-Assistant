# app/tasks.py
from crewai import Task
import logging

logger = logging.getLogger(__name__)

def create_process_explanation_task(agent, country: str, language: str = "en"):
    """Create the process explanation task"""
    return Task(
        description=f"""
        Explain the election process for {country} in a clear, simple way.
        
        The explanation should cover:
        1. What is an election and why it matters
        2. Who can vote (eligibility criteria)
        3. How to register to vote
        4. How to find your polling station
        5. What happens on election day
        6. How votes are counted
        7. How results are announced
        
        Language: {language}
        
        Make the explanation engaging, easy to understand, and suitable for 
        first-time voters. Use simple language and avoid jargon.
        """,
        expected_output="""
        A comprehensive explanation of the election process in simple, clear language.
        The response should be structured with clear sections and bullet points where appropriate.
        """,
        agent=agent
    )

def create_timeline_task(agent, country: str, language: str = "en"):
    """Create the timeline task"""
    return Task(
        description=f"""
        Create a detailed election timeline for {country}.
        
        Include:
        1. Pre-election activities
           - Voter registration dates
           - Candidate nomination dates
           - Campaign periods
           - Voter education campaigns
        
        2. Election day activities
           - Polling hours
           - Voting procedures
           - Special arrangements
        
        3. Post-election activities
           - Counting dates
           - Result announcement dates
           - Dispute resolution timeline
        
        Format the timeline clearly with dates and descriptions.
        Language: {language}
        """,
        expected_output="""
        A comprehensive election timeline with clear dates and descriptions.
        The timeline should be organized chronologically with clear headings.
        """,
        agent=agent
    )

def create_step_guide_task(agent, country: str, language: str = "en"):
    """Create the step guide task"""
    return Task(
        description=f"""
        Create a step-by-step guide for the election process in {country}.
        
        Steps should cover:
        1. Checking voter eligibility
        2. Voter registration process
        3. Finding your polling station
        4. Understanding the ballot
        5. Voting procedures (in-person, postal, proxy)
        6. Verification of vote
        7. What to do if you face issues
        
        Include tips, common mistakes to avoid, and what to expect at each step.
        Language: {language}
        
        Make each step clear and actionable.
        """,
        expected_output="""
        A detailed step-by-step guide with clear instructions and tips.
        Each step should have a clear title, description, and actionable items.
        """,
        agent=agent
    )

def create_faq_task(agent, question: str, country: str, language: str = "en"):
    """Create the FAQ task"""
    return Task(
        description=f"""
        Answer the following question about elections in {country}:
        
        Question: {question}
        
        Provide a clear, accurate, and helpful answer.
        Include relevant laws, procedures, and practical advice.
        Language: {language}
        
        If the question is specific to a particular region within {country}, 
        please address that regional context.
        """,
        expected_output="""
        A clear, accurate answer to the election question.
        The answer should be comprehensive and easy to understand.
        """,
        agent=agent
    )

def create_accessibility_task(agent, country: str, language: str = "en"):
    """Create the accessibility task"""
    return Task(
        description=f"""
        Provide accessibility information for voters in {country}.
        
        Include:
        1. Special provisions for voters with disabilities
        2. Assistance available at polling stations
        3. Voting options for elderly voters
        4. Support for first-time voters
        5. Language assistance
        6. Transportation assistance
        7. Alternative voting methods
        
        Format the information clearly and make it easy to understand.
        Language: {language}
        """,
        expected_output="""
        Comprehensive accessibility information for all voters.
        The information should be organized by category for easy reference.
        """,
        agent=agent
    )