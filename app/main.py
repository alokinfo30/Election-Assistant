# app/main.py
from flask import Blueprint, render_template, request, jsonify, current_app
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
import json
import uuid
from datetime import datetime

load_dotenv()
logger = logging.getLogger(__name__)

main_bp = Blueprint('main', __name__)

# Import crew
try:
    from app.crew import ElectionAssistantCrew
    CREW_AVAILABLE = True
    logger.info("✅ ElectionAssistantCrew imported successfully")
except ImportError as e:
    logger.warning(f"⚠️ Crew not available: {e}")
    CREW_AVAILABLE = False

# Service mapping
SERVICES = {
    "process": {
        "name": "Election Process",
        "icon": "📚",
        "description": "Learn how elections work"
    },
    "timeline": {
        "name": "Election Timeline",
        "icon": "📅",
        "description": "See important dates and deadlines"
    },
    "step_guide": {
        "name": "Step-by-Step Guide",
        "icon": "📋",
        "description": "Follow each step of the process"
    },
    "faq": {
        "name": "FAQ",
        "icon": "❓",
        "description": "Get answers to common questions"
    },
    "accessibility": {
        "name": "Accessibility",
        "icon": "♿",
        "description": "Information for all voters"
    }
}

SUPPORTED_LANGUAGES = os.getenv('SUPPORTED_LANGUAGES', 'en,hi,es,fr,ar,zh,pt,ru').split(',')
DEFAULT_COUNTRY = os.getenv('DEFAULT_ELECTION_COUNTRY', 'India')

@main_bp.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', 
                         services=SERVICES, 
                         languages=SUPPORTED_LANGUAGES,
                         default_country=DEFAULT_COUNTRY)

@main_bp.route('/api/service', methods=['POST'])
def handle_service():
    """Handle a service request"""
    try:
        data = request.json
        service_type = data.get('service_type')
        
        if not service_type:
            return jsonify({
                'error': 'Missing service type',
                'status': 'error'
            }), 400
        
        if service_type not in SERVICES:
            return jsonify({
                'error': f'Invalid service type: {service_type}',
                'status': 'error'
            }), 400
        
        if not CREW_AVAILABLE:
            return jsonify({
                'error': 'CrewAI not available. Please check installation.',
                'status': 'error'
            }), 500
        
        country = data.get('country', DEFAULT_COUNTRY)
        language = data.get('language', 'en')
        crew = ElectionAssistantCrew()
        
        # Route to appropriate handler
        if service_type == 'process':
            result = crew.explain_process(country, language)
        elif service_type == 'timeline':
            result = crew.create_timeline(country, language)
        elif service_type == 'step_guide':
            result = crew.create_step_guide(country, language)
        elif service_type == 'faq':
            question = data.get('question', '')
            if not question:
                return jsonify({
                    'error': 'Missing question for FAQ',
                    'status': 'error'
                }), 400
            result = crew.answer_faq(question, country, language)
        elif service_type == 'accessibility':
            result = crew.get_accessibility_info(country, language)
        else:
            return jsonify({
                'error': f'Unhandled service type: {service_type}',
                'status': 'error'
            }), 400
        
        if result['status'] == 'error':
            return jsonify({
                'error': result.get('error', 'Unknown error'),
                'status': 'error'
            }), 500
        
        return jsonify({
            'status': 'success',
            'service': service_type,
            'result': result,
            'timestamp': datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error handling service: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@main_bp.route('/api/services', methods=['GET'])
def get_services():
    """Get all available services"""
    return jsonify({
        'status': 'success',
        'services': SERVICES,
        'languages': SUPPORTED_LANGUAGES,
        'default_country': DEFAULT_COUNTRY
    })

@main_bp.route('/api/models', methods=['GET'])
def get_models():
    """Get available models"""
    try:
        from app.model_manager import model_manager
        results = model_manager.test_providers()
        available = [m for m, v in results.items() if v]
        
        return jsonify({
            'status': 'success',
            'models': {
                'primary': os.getenv('OPENROUTER_PRIMARY_MODEL', 'openai/gpt-4o-mini'),
                'fallbacks': os.getenv('OPENROUTER_FALLBACK_MODELS', '').split(','),
                'available': available,
                'all_tested': results
            }
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@main_bp.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'crew_available': CREW_AVAILABLE,
        'version': '1.0.0',
        'features': list(SERVICES.keys()),
        'languages_supported': len(SUPPORTED_LANGUAGES)
    })