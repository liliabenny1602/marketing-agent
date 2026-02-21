import streamlit as st
from main import run


# ---------- CACHED EXECUTION ----------
@st.cache_data(show_spinner=False)
def run_cached():
    return run()


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Agent Control Panel",
    layout="wide"
)

st.title("Autonomous Marketing Agent System")

# optional cache reset
if st.button("Clear Cache"):
    st.cache_data.clear()


# ---------- HEADER ----------
run_button = st.button("Run Campaign", type="primary")


# ---------- PLACEHOLDERS ----------
status_area = st.container()
metrics_area = st.container()
main_area = st.container()


# ---------- EXECUTION ----------
if run_button:

    with st.spinner("Agents running..."):
        result = run_cached()

    # ===============================
    # STATUS PANEL
    # ===============================
    with status_area:

        st.subheader("Execution Timeline")

        timeline = [
            "Analyst",
            "Memory",
            "Strategist",
            "Copywriter",
            "Optimizer"
        ]

        cols = st.columns(len(timeline))

        for col, step in zip(cols, timeline):
            col.write(f"✔ {step}")


    # ===============================
    # METRICS PANEL
    # ===============================
    with metrics_area:

        st.subheader("Campaign Metrics")

        metrics = result["metrics"]

        cols = st.columns(5)

        keys = ["ctr", "cpc", "roas", "impressions", "conversions"]

        for col, key in zip(cols, keys):
            col.metric(key.upper(), metrics.get(key))


    # ===============================
    # MAIN GRID
    # ===============================
    with main_area:

        left, right = st.columns([1, 1])

        # -------- LEFT --------
        with left:

            st.subheader("Analysis")
            st.write(result["analysis"])

            st.subheader("Memory Retrieval")

            for m in result["memories"]:
                st.info(m)


        # -------- RIGHT --------
        with right:

            st.subheader("Strategy Plan")
            st.write(result["strategy"])

            st.subheader("Execution Decision")
            st.success(result["execution"])


    # ===============================
    # COPY OUTPUT
    # ===============================
    st.subheader("Generated Ad Variants")
    st.write(result["copy"])


    # ===============================
    # RAW STATE DEBUGGER
    # ===============================
    with st.expander("Full Agent State (Debug)"):
        st.json(result)