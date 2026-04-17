async function runAgent(forcedPrompt = null) {
    const input = document.getElementById('userPrompt');
    const prompt = forcedPrompt || input.value;
    const outputPanel = document.getElementById('decisionOutput');
    const jsonDisplay = document.getElementById('jsonOutput');
    const statusLabel = document.getElementById('agentStatus');

    if (!prompt) return;

    // UI Reset
    outputPanel.classList.remove('hidden');
    jsonDisplay.textContent = "Processing logic...";
    statusLabel.textContent = "AGENT THINKING...";
    statusLabel.style.color = "#c9d1d9";

    try {
        const response = await fetch('/process', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: prompt })
        });

        const data = await response.json();
        
        // Render stylized JSON
        jsonDisplay.textContent = JSON.stringify(data, null, 2);
        
        // Update Status based on decision
        if (data.status === 'success') {
            statusLabel.textContent = "DECISION: FULFILLMENT SECURED";
            statusLabel.style.color = "#22c55e";
        } else if (data.status === 'out_of_stock') {
            statusLabel.textContent = "DECISION: AUTONOMOUS RECOVERY TRIGGERED";
            statusLabel.style.color = "#f59e0b";
        } else {
            statusLabel.textContent = "DECISION: EXCEPTION DETECTED";
            statusLabel.style.color = "#ef4444";
        }
    } catch (err) {
        jsonDisplay.textContent = "Error connecting to Agent Engine.";
        statusLabel.textContent = "DECISION: SYSTEM ERROR";
        statusLabel.style.color = "#ef4444";
    }
}

// Add enter key support
document.getElementById('userPrompt').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        runAgent();
    }
});