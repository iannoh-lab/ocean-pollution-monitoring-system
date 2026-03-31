import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')

# Import routes and modules
from src.spectrophotometry import (
    calibrate_wavelengths,
    calculate_chlorophyll_a,
    calculate_nutrient_concentration,
    analyze_dissolved_organic_matter,
    extract_water_quality_parameters
)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'ocean-pollution-monitoring-system',
        'environment': os.getenv('FLASK_ENV', 'unknown')
    }), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    """Application metrics endpoint"""
    return jsonify({
        'service': 'ocean-pollution-monitoring-system',
        'version': '1.0.0',
        'status': 'running'
    }), 200

@app.route('/', methods=['GET'])
def index():
    """Welcome endpoint"""
    return jsonify({
        'message': 'Welcome to Ocean Pollution Monitoring System',
        'description': 'An open-source system for monitoring ocean pollutants at Mombasa port',
        'version': '1.0.0',
        'endpoints': {
            'health': '/health',
            'metrics': '/metrics',
            'api': '/api/v1'
        }
    }), 200

@app.route('/api/v1/spectrophotometry', methods=['POST'])
def spectrophotometry_analysis():
    """Spectrophotometry analysis endpoint"""
    try:
        return jsonify({
            'status': 'success',
            'message': 'Spectrophotometry analysis module available',
            'functions': [
                'calibrate_wavelengths',
                'calculate_chlorophyll_a',
                'calculate_nutrient_concentration',
                'analyze_dissolved_organic_matter',
                'extract_water_quality_parameters'
            ]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'status': 'error', 'message': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 5000))
    host = os.getenv('APP_HOST', '0.0.0.0')
    debug = os.getenv('FLASK_ENV') == 'development'
    
    app.run(host=host, port=port, debug=debug)