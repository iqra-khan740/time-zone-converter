async function convertLogs() {
    const logs = document.getElementById("logInput").value;
    const tz = document.getElementById("timezone").value;
    const output = document.getElementById("output");

    if (!logs.trim()) {
        output.textContent = "⚠️ Please paste some logs first.";
        return;
    }

    try {
        const response = await fetch("/convert", {   // ✅ Relative URL
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ logs: logs, tz: tz })
        });

        const data = await response.json();
        if (data.converted_logs) {
            output.textContent = data.converted_logs.join("\n");
        } else {
            output.textContent = "❌ Error: " + (data.error || "Unknown error");
        }
    } catch (err) {
        output.textContent = "🚨 Could not connect to backend. Is Flask running?";
    }
}