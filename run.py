# run.py
import os
import sys

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    
    print("=" * 70)
    print("🗳️ AI-Powered Election Assistant")
    print("=" * 70)
    print(f"🚀 Server running at: http://localhost:{port}")
    print(f"📱 Open in your browser")
    print("=" * 70)
    print("🤖 AI Agents:")
    print("  1. 📚 Process Explainer - Explains the election process")
    print("  2. 📅 Timeline Agent - Provides election timelines")
    print("  3. 📋 Step Guide Agent - Creates step-by-step guides")
    print("  4. ❓ FAQ Agent - Answers common questions")
    print("  5. ♿ Accessibility Agent - Ensures inclusive access")
    print("=" * 70)
    print("🌍 Supported Languages:")
    print("  English, Hindi, Spanish, French, Arabic, Chinese, Portuguese, Russian")
    print("=" * 70)
    print("🗳️ Empowering Voters with Knowledge")
    print("=" * 70)
    
    app.run(host='0.0.0.0', port=port, debug=debug)