# RetailPilot AI

Autonomous Retail Decision System built for hackathon demonstration.

## 🚀 Quick Start
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open http://127.0.0.1:5000

## 🧠 System Logic
RetailPilot AI uses a deterministic decision engine to handle retail operations without human intervention:
- **Automatic Fulfillment**: If stock is present, triggers logistics pipelines.
- **Autonomous Recovery**: If out of stock, triggers supplier API restocks and suggests inventory substitutes instantly.

## 🧱 Architecture
- **API Layer**: Flask REST API handling `/process`.
- **Decision Engine**: Rule-based Python logic (`engine.py`).
- **Data Layer**: JSON-based inventory state (`data/sample.json`).
- **Frontend**: Vanilla JS/CSS dashboard for live decision monitoring.