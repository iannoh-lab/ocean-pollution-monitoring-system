# Setup Guide

## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iannoh-lab/ocean-pollution-monitoring-system.git
   cd ocean-pollution-monitoring-system
   ```

2. **Install dependencies**:
   Make sure you have [Python](https://www.python.org/downloads/) installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Set environment variables**:
   Create a `.env` file in the root directory and add necessary configuration:
   ```bash
   POLLUTION_MONITORING_API_KEY=your_api_key
   POLLUTION_MONITORING_ENDPOINT=https://api.yourservice.com
   ```

## Quick Start Guide

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Access the application**:
   Open your web browser and go to `http://localhost:5000`.

3. **Monitor data**:
   Follow on-screen instructions to view pollution data and analytics.