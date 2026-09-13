import streamlit as st
from app.orchestrator import orchestrate

st.set_page_config(
    page_title="LIFEOPS",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 LIFEOPS")
st.subheader("Autonomous Personal Operations Agent")
st.caption("Plan → Research → Act → Verify → Recover → Remember → Report")

st.divider()

st.markdown("### 🎯 Mission")
st.info("Give LIFEOPS a real-world objective and watch the workflow progress from planning to verified results.")

objective = st.text_area(
    "What should LIFEOPS accomplish?",
    placeholder="Example: Prepare everything I need to submit my hackathon project."
)

if st.button("🚀 Run LIFEOPS", type="primary"):
    if not objective.strip():
        st.warning("Please enter an objective.")
    else:
        st.session_state["objective"] = objective
        with st.spinner("LIFEOPS is working..."):
            state = orchestrate(objective)
        st.session_state["workflow_state"] = state
        st.success("LIFEOPS workflow completed.")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🧠 Planning", "Ready")

with col2:
    st.metric("🔎 Research", "Ready")

with col3:
    st.metric("✅ Verification", "Ready")

with col4:
    st.metric("🛡️ Safety", "Active")

st.divider()

st.markdown("### 🔄 LIFEOPS Workflow")

st.markdown("""
**🎯 Objective** → **🧠 Plan** → **🎯 Prioritize** → **🔎 Research**
→ **⚙️ Act** → **🛡️ Approval** → **✅ Verify**
→ **🔄 Recover** → **🧠 Remember** → **📊 Report**
""")

st.divider()

st.caption("LIFEOPS • Built for Agents for Humans Hackathon • Everyday Agents")


if "workflow_state" in st.session_state:
    state = st.session_state["workflow_state"]

    st.divider()
    st.markdown("## 📊 LIVE WORKFLOW RESULTS")

    tabs = st.tabs([
        "🧠 Plan",
        "🎯 Priority",
        "🔎 Research",
        "⚙️ Action",
        "✅ Verification",
        "📊 Report"
    ])

    with tabs[0]:
        st.markdown("### 🧠 Planning")
        st.write(state.plan)

    with tabs[1]:
        st.markdown("### 🎯 Prioritized Work")
        st.write(state.priorities)

    with tabs[2]:
        st.markdown("### 🔎 Research & Evidence")
        st.write(state.research)
        if state.evidence:
            st.success(f"Persistent evidence records: {len(state.evidence)}")

    with tabs[3]:
        st.markdown("### ⚙️ Actions")
        st.write(state.action)

    with tabs[4]:
        st.markdown("### ✅ Verification")
        st.write(state.verification)

    with tabs[5]:
        st.markdown("### 📊 Final Readiness Report")
        st.write(state.report)

        if state.errors:
            st.error("Workflow issues detected")
            for error in state.errors:
                st.write(error)
