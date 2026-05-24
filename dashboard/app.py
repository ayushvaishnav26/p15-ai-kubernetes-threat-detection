import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
from streamlit_autorefresh import st_autorefresh
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulator.k8s_monitor import get_pod_status

LOG_FILE = "logs/generated_logs.txt"

# Auto Refresh
st_autorefresh(interval=2000, key="refresh")

# Page Config
st.set_page_config(
    page_title="AI Threat Detection Dashboard",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00FFAA;
}

[data-testid="metric-container"] {
    background-color: #111827;
    border: 1px solid #00FFAA;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,255,170,0.3);
}

.stAlert {
    border-radius: 15px;
}

.threat-box {
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    font-weight: bold;
}

.low {
    background-color: #1E3A1E;
    color: #00FF00;
}

.medium {
    background-color: #3A3000;
    color: #FFD700;
}

.high {
    background-color: #3A1E00;
    color: #FF9900;
}

.critical {
    background-color: #3A0000;
    color: #FF0000;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🛡 AI Kubernetes Threat Detection Center")

try:

    # Read logs
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    logs = [log.strip() for log in logs]

    df = pd.DataFrame(logs, columns=["Logs"])

    # Threat Detection
    failed_logs = [log for log in logs if "LOGIN_FAILED" in log]

    total_logs = len(logs)

    threat_count = len(failed_logs)

    safe_count = total_logs - threat_count

    # Extract IPs
    ips = [log.split(" - ")[0] for log in failed_logs]

    ip_counts = Counter(ips)

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("📄 Total Logs", total_logs)

    col2.metric("🚨 Threat Events", threat_count)

    col3.metric("✅ Safe Events", safe_count)

    st.divider()

    # Threat Status
    if threat_count > 15:

        st.error("🚨 CRITICAL THREAT LEVEL")

    elif threat_count > 5:

        st.warning("⚠ Suspicious Activity Detected")

    else:

        st.success("✅ SYSTEM SECURE")

    st.divider()

    # Top Attackers
    st.subheader("🌐 Top Attacking IPs")

    ip_df = pd.DataFrame(
        ip_counts.items(),
        columns=["IP Address", "Failed Attempts"]
    )

    st.dataframe(
        ip_df,
        use_container_width=True
    )

    st.divider()

    # Threat Feed
    st.subheader("🚨 Live Threat Feed")

    for log in failed_logs[-10:]:

        st.markdown(
            f"""
            <div class="threat-box critical">
            🚨 {log}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # Live Logs
    st.subheader("📡 Live Security Logs")

    st.dataframe(
        df.tail(20),
        use_container_width=True,
        height=400
    )

    st.divider()

    # Charts
    st.subheader("📊 Threat Analytics")

    chart_data = pd.DataFrame({
        "Category": ["Safe", "Threats"],
        "Count": [safe_count, threat_count]
    })

    st.bar_chart(
        chart_data.set_index("Category")
    )

    st.divider()

    # Live Threat Timeline
    st.subheader("📈 Live Threat Timeline")

    timeline_data = pd.DataFrame({
        "Threat Events": list(range(threat_count))
    })

    st.line_chart(timeline_data)

    st.divider()

    # CPU & Memory Monitoring
    st.subheader("🖥 System Metrics")

    import psutil

    cpu = psutil.cpu_percent()

    memory = psutil.virtual_memory().percent

    metric1, metric2 = st.columns(2)

    metric1.metric("CPU Usage", f"{cpu}%")

    metric2.metric("Memory Usage", f"{memory}%")

    st.progress(int(cpu))

    st.progress(int(memory))
    st.divider()

    st.divider()

    # Kubernetes Monitoring
    st.subheader("☸ Kubernetes Pod Monitoring")

    pod_data = get_pod_status()

    if pod_data:

        pod_df = pd.DataFrame(pod_data)

        st.dataframe(
            pod_df,
            use_container_width=True
        )

    else:

        st.warning("No Kubernetes Pods Found")

    # Pie Chart
    st.subheader("🥧 Threat Distribution")

    pie_data = pd.DataFrame({
        "Category": ["Safe Activities", "Threat Activities"],
        "Count": [safe_count, threat_count]
    })

    fig = px.pie(
        pie_data,
        names="Category",
        values="Count",
        hole=0.4
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except FileNotFoundError:

    st.warning("No logs found yet.")