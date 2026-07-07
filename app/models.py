# app/models.py
from pydantic import BaseModel, Field
from typing import Dict, Optional, List, Any
from datetime import datetime
from enum import Enum

class ElectionStep(BaseModel):
    """Model for an election step"""
    step_number: int = Field(..., description="Step number")
    title: str = Field(..., description="Step title")
    description: str = Field(..., description="Detailed description")
    tips: List[str] = Field(default_factory=list, description="Useful tips")
    common_mistakes: List[str] = Field(default_factory=list, description="Common mistakes to avoid")
    resources: List[str] = Field(default_factory=list, description="Helpful resources")

class TimelineEvent(BaseModel):
    """Model for a timeline event"""
    date: str = Field(..., description="Event date")
    title: str = Field(..., description="Event title")
    description: str = Field(..., description="Event description")
    category: str = Field(..., description="Category: pre-election, election-day, post-election")

class ElectionFAQ(BaseModel):
    """Model for an election FAQ"""
    question: str = Field(..., description="FAQ question")
    answer: str = Field(..., description="FAQ answer")
    category: str = Field(..., description="FAQ category")
    related_links: List[str] = Field(default_factory=list, description="Related resources")

class AccessibilityInfo(BaseModel):
    """Model for accessibility information"""
    category: str = Field(..., description="Category: physical, visual, hearing, cognitive, language")
    title: str = Field(..., description="Title")
    description: str = Field(..., description="Description")
    available_services: List[str] = Field(..., description="Available services")
    contact_info: str = Field(..., description="Contact information for assistance")

class ElectionGuide(BaseModel):
    """Complete election guide model"""
    country: str = Field(..., description="Country name")
    language: str = Field("en", description="Language code")
    process_explanation: str = Field(..., description="Detailed process explanation")
    timeline: List[TimelineEvent] = Field(..., description="Election timeline")
    steps: List[ElectionStep] = Field(..., description="Step-by-step guide")
    faqs: List[ElectionFAQ] = Field(..., description="Frequently asked questions")
    accessibility_info: List[AccessibilityInfo] = Field(..., description="Accessibility information")
    key_dates: Dict[str, str] = Field(..., description="Key dates summary")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

class QueryRequest(BaseModel):
    """User query request"""
    query: str = Field(..., description="User query")
    country: str = Field("India", description="Country context")
    language: str = Field("en", description="Language preference")
    query_type: str = Field("general", description="Query type: process, timeline, step, faq, accessibility")