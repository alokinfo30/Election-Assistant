# app/crew.py
from crewai import Crew
import os
import logging
from typing import Dict, List, Optional
from app.model_manager import model_manager

logger = logging.getLogger(__name__)

class ElectionAssistantCrew:
    """Orchestrate the election assistant services"""
    
    def __init__(self):
        try:
            from app.agents import (
                create_process_explainer,
                create_timeline_agent,
                create_step_guide_agent,
                create_faq_agent,
                create_accessibility_agent
            )
            from app.tasks import (
                create_process_explanation_task,
                create_timeline_task,
                create_step_guide_task,
                create_faq_task,
                create_accessibility_task
            )
            
            self.create_process_explainer = create_process_explainer
            self.create_timeline_agent = create_timeline_agent
            self.create_step_guide_agent = create_step_guide_agent
            self.create_faq_agent = create_faq_agent
            self.create_accessibility_agent = create_accessibility_agent
            
            self.create_process_explanation_task = create_process_explanation_task
            self.create_timeline_task = create_timeline_task
            self.create_step_guide_task = create_step_guide_task
            self.create_faq_task = create_faq_task
            self.create_accessibility_task = create_accessibility_task
            
            self.verbose = os.getenv('DEBUG', 'False').lower() == 'true'
            self.model_manager = model_manager
            
            logger.info("✅ ElectionAssistantCrew initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize ElectionAssistantCrew: {str(e)}")
            raise
    
    def explain_process(self, country: str, language: str = "en") -> Dict:
        """Explain the election process"""
        try:
            logger.info(f"📚 Explaining election process for {country}")
            
            agent = self.create_process_explainer()
            task = self.create_process_explanation_task(agent, country, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "country": country,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "process_explanation",
                "country": country,
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Process explanation failed: {str(e)}")
            return {
                "status": "error",
                "service": "process_explanation",
                "error": str(e)
            }
    
    def create_timeline(self, country: str, language: str = "en") -> Dict:
        """Create election timeline"""
        try:
            logger.info(f"📅 Creating election timeline for {country}")
            
            agent = self.create_timeline_agent()
            task = self.create_timeline_task(agent, country, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "country": country,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "timeline",
                "country": country,
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Timeline creation failed: {str(e)}")
            return {
                "status": "error",
                "service": "timeline",
                "error": str(e)
            }
    
    def create_step_guide(self, country: str, language: str = "en") -> Dict:
        """Create step-by-step guide"""
        try:
            logger.info(f"📋 Creating step guide for {country}")
            
            agent = self.create_step_guide_agent()
            task = self.create_step_guide_task(agent, country, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "country": country,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "step_guide",
                "country": country,
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Step guide creation failed: {str(e)}")
            return {
                "status": "error",
                "service": "step_guide",
                "error": str(e)
            }
    
    def answer_faq(self, question: str, country: str, language: str = "en") -> Dict:
        """Answer election FAQ"""
        try:
            logger.info(f"❓ Answering FAQ: {question[:50]}...")
            
            agent = self.create_faq_agent()
            task = self.create_faq_task(agent, question, country, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "question": question,
                "country": country,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "faq",
                "country": country,
                "language": language,
                "question": question,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"FAQ answering failed: {str(e)}")
            return {
                "status": "error",
                "service": "faq",
                "error": str(e)
            }
    
    def get_accessibility_info(self, country: str, language: str = "en") -> Dict:
        """Get accessibility information"""
        try:
            logger.info(f"♿ Getting accessibility info for {country}")
            
            agent = self.create_accessibility_agent()
            task = self.create_accessibility_task(agent, country, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "country": country,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "accessibility",
                "country": country,
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Accessibility info failed: {str(e)}")
            return {
                "status": "error",
                "service": "accessibility",
                "error": str(e)
            }