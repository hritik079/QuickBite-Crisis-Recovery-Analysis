import streamlit as st
import pandas as pd
from PIL import Image

# 1. Page Configuration
st.set_page_config(page_title="QuickBite Recovery", page_icon="🍔", layout="wide")

st.title("🍔 QuickBite Express: Crisis Impact & Recovery Dashboard")
st.markdown("This dashboard tracks the impact of the June 2025 food safety and delivery crisis.")

# 2. Key Performance Indicators (KPIs) - BULLETPROOF VERSION
st.subheader("🔴 Immediate Crisis Impact (June - Sept 2025)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Estimated Revenue Loss")
    st.markdown("# ₹ -4.78M")
    st.markdown("**📉 -63.6% Drop**")

with col2:
    st.markdown("### SLA Compliance")
    st.markdown("# 12.2%")
    st.markdown("**📉 -31.4% Drop**")

with col3:
    st.markdown("### Average Rating")
    st.markdown("# 2.4 / 5.0")
    st.markdown("**📉 -2.1 Stars**")

st.divider()

# 3. Visualizations 
st.subheader("📊 Visualizing the Decline")
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("**1. Order Volume Collapse**")
    try:
        img1 = Image.open('order_volume_trend.png')
        st.image(img1, use_container_width=True)
    except FileNotFoundError:
        st.warning("Please run Step 5 in Colab to generate 'order_volume_trend.png'")

with col_chart2:
    st.markdown("**2. Customer Trust Decay**")
    try:
        img2 = Image.open('ratings_trend.png')
        st.image(img2, use_container_width=True)
    except FileNotFoundError:
        st.warning("Please run Step 5 in Colab to generate 'ratings_trend.png'")

st.divider()

# 4. Actionable Insights
st.subheader("💡 Strategic Recommendations for Leadership")
st.markdown("""
* **Targeted Win-Back Campaigns:** Focus recovery budgets heavily on **Chennai, Kolkata, and Bengaluru**, as these regions saw the highest percentage drop (>61%) in order volume.
* **Delivery Infrastructure Audit:** The drop to 12.2% SLA compliance indicates the monsoon outage broke the logistics chain. Implement dynamic delivery ETAs.
* **Sentiment Reversal:** Reviews highlighted 'Food', 'Quality', and 'Packaging' as major pain points. Roll out a visible "Safety Certified" badge for partner restaurants that pass the new audits.
""")

st.caption("Developed by Abhinav Basu | Data Analyst, QuickBite Express")
