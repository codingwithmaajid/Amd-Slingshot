# 🚀 Retail Pilot 

Retail Pilot AI is an Autonomous, Context-aware decision system designed to revolutionize retail operations. By bridging the gap between customer demand and inventory management, it acts as an intelligent agent that parses intent, fulfills orders seamlessly, and triggers autonomous recovery protocols when supply chain gaps are detected.

# 🧠 Problem Statement

Modern retail environments face significant operational hurdles that lead to lost revenue and customer dissatisfaction:
- **Inventory Mismanagement**: Manual tracking often leads to stockouts or overstocking.
- **Delayed Response**: Human intervention is required to handle out-of-stock scenarios and supplier notifications.
- **Operational Inefficiency**: Lack of real-time visibility into the decision-making process for fulfillment and recovery.

# 💡 Solution

Retail Pilot AI solves these challenges by deploying a deterministic, rule-based decision engine that operates autonomously:
- **Autonomous Intent Parsing**: Automatically identifies products and customer needs from natural language or direct inputs.
- **Intelligent Fulfillment**: Executes instant fulfillment logic when stock is available.
- **Self-Healing Recovery**: Independently triggers supplier restock notifications and suggests inventory substitutes without human oversight.

# ⚙️ How It Works

1.  **Input**: The system accepts structured SKU IDs or natural language requests (e.g., "I'd like some espresso beans").
2.  **Processing**: The AI Decision Engine validates the request against real-time inventory data, assesses stock levels, and branches into fulfillment or recovery logic.
3.  **Output**: Generates a structured JSON decision output, updates operational logs, and provides immediate feedback through the dashboard.

# 🧠 AI Decision Engine

The engine is built for reliability, speed, and transparency:
- **Autonomous Mode**: Operates end-to-end without manual approval for standard operational procedures.
- **Context-Aware Decision Making**: Uses keyword-based parsing to understand the "what" and "why" behind a request.
- **Real-Time Analysis**: Processes state changes instantly to ensure inventory accuracy.
- **Explainability**: Every decision is logged with a clear rationale, ensuring owners can audit the "Agent Thinking" process.

# 📡 Monitoring Dashboard

The system features a dual-interface approach for complete operational control:
- **Status Monitoring**: Real-time "ONLINE" status and system health indicators.
- **Autonomous Mode**: Visual confirmation that the AI Agent is in control of decision-making.
- **Activity Feed**: A live stream of Agent logs, documenting every fulfillment secured and every autonomous recovery triggered.

# 🌐 Live Demo

Experience the autonomous engine live:
[https://retail-pilot-ai-767319399090.asia-south1.run.app/](https://retail-pilot-ai-767319399090.asia-south1.run.app/)

# 🛠️ Tech Stack

- **Frontend**: Vanilla JavaScript / HTML5 / CSS3 (Optimized for performance and accessibility).
- **Backend**: Python / Flask (Lightweight REST API architecture).
- **Containerization**: Docker.
- **Deployment**: Google Cloud Run (Serverless execution).
- **CI/CD**: Google Cloud Build.
- **Registry**: Google Container Registry (GCR).

# ☁️ Google Cloud Integration

- **Google Cloud Run**: Hosts the application in a fully managed, serverless environment, ensuring zero-maintenance scaling.
- **Google Cloud Build**: Automates the build and deployment pipeline directly from the source.
- **Google Container Registry**: Securely stores and manages Docker images for reliable deployments.

# 🔐 Security

- **IAM Roles**: Implements principle of least privilege for service accounts.
- **Secure API Handling**: Sanitized input processing to prevent injection or logic bypass.
- **Environment Variables**: Sensitive configurations like ports and operational thresholds are managed through environment variables.

# ⚡ Efficiency

- **Optimized Processing**: The rule-based engine eliminates the latency of heavy LLM calls for deterministic retail logic.
- **Serverless Scaling**: Automatically scales to zero when not in use and spins up instantly to handle demand spikes.

# 🧪 Testing

- **Workflow Validation**: Rigorous testing of In-Stock, Out-of-Stock, and Unknown SKU scenarios.
- **Stable Deployment**: Containerized environment ensures "it works on my machine" translates perfectly to production.

# ♿ Accessibility

- **Clean UI**: Minimalist design focused on high contrast and readable typography.
- **Easy Usability**: Intuitive search and one-click fulfillment buttons.
- **Real-Time Feedback**: Instant toast notifications and status updates for all user actions.

# 📂 Project Structure

```text
retailpilot-ai/
├── app.py              # Flask Entry Point & REST API
├── engine.py           # AI Decision Engine Logic
├── Dockerfile          # Container Configuration
├── data/
│   └── sample.json     # Mock Inventory Database
├── static/
│   ├── app.js          # Frontend Logic & API Integration
│   └── style.css       # Unified Professional Styling
├── templates/
│   ├── index.html      # Customer Storefront
│   └── admin.html      # Owner Command Center
├── DOC.md              # System Documentation
└── README.md           # Project Overview
```

# 🚀 Setup Instructions

1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/codingwithmaajid/Amd-Slingshot.git
    cd retailpilot-ai
    ```
2.  **Install Dependencies**:
    ```bash
    pip install flask
    ```
3.  **Run Locally**:
    ```bash
    python app.py
    ```
4.  **Docker Build (Optional)**:
    ```bash
    docker build -t retail-pilot-ai .
    docker run -p 5000:5000 retail-pilot-ai
    ```

# 🎯 Future Improvements

- **Predictive Analytics**: Integrate machine learning to forecast demand before stockouts occur.
- **Personalization**: Suggest substitutes based on individual customer purchase history.
- **Real-Time Data Integration**: Connect directly to live ERP and Supplier APIs for actual inventory sync.
- **Multi-Agent Coordination**: Deploy specialized agents for logistics, pricing, and procurement.