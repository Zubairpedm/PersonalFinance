import streamlit as st
import matplotlib.pyplot as plt

# Title of the app
st.title("💰 Personal Finance Calculator")

# Description
st.markdown("Enter your income and expenses to calculate your monthly savings and see a visual breakdown.")

# User input
income = st.number_input("Enter your monthly income (₹)", min_value=0)
expenses = st.number_input("Enter your monthly expenses (₹)", min_value=0)

# Calculate savings
savings = income - expenses

# Display result
st.subheader("📊 Financial Summary")
st.write(f"**Monthly Income:** ₹{income}")
st.write(f"**Monthly Expenses:** ₹{expenses}")
st.write(f"**Monthly Savings:** ₹{savings}")

# Visual representation using pie chart
if income > 0:
    labels = ['Expenses', 'Savings']
    values = [expenses, savings if savings > 0 else 0]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

    st.pyplot(fig)
else:
    st.info("Enter your income to see the pie chart.")

# Footer
st.markdown("---")
st.caption("🛠️ Built by Zubair Uddin using Streamlit")
