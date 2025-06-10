import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from project_updated import ExpenseManager
import json
from decimal import Decimal
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'username' not in st.session_state:
    st.session_state.username = None
if 'manager' not in st.session_state:
    st.session_state.manager = None

def load_expenses():
    if st.session_state.manager:
        expenses = st.session_state.manager.get_expenses()
        if expenses:
            df = pd.DataFrame(expenses)
            return df
    return pd.DataFrame()

def create_charts(df):
    if not df.empty:
        # Category-wise expense distribution
        fig_pie = px.pie(df, 
                        values='amount', 
                        names='category',
                        title='Expense Distribution by Category',
                        hole=0.3)
        st.plotly_chart(fig_pie)

        # Timeline of expenses
        df['date'] = pd.to_datetime(df['date'])
        df_grouped = df.groupby('date')['amount'].sum().reset_index()
        fig_line = px.line(df_grouped, 
                          x='date', 
                          y='amount',
                          title='Expense Timeline',
                          labels={'amount': 'Total Amount', 'date': 'Date'})
        st.plotly_chart(fig_line)

def main():
    st.title("💰 Expense Tracker")

    # Login Section
    if not st.session_state.username:
        st.markdown("### Welcome! Please enter your name to start")
        username = st.text_input("Your Name")
        if st.button("Start Tracking"):
            if username.strip():
                st.session_state.username = username
                st.session_state.manager = ExpenseManager(username)
                st.experimental_rerun()
            else:
                st.error("Please enter a valid name")
        return

    # Main Interface
    st.sidebar.title(f"Welcome, {st.session_state.username.capitalize()}! 👋")
    
    # Add Expense Section
    with st.sidebar:
        st.markdown("### Add New Expense")
        with st.form("add_expense_form"):
            category = st.text_input("Category").lower()
            amount = st.number_input("Amount (₹)", min_value=0.0, format="%f")
            submit_button = st.form_submit_button("Add Expense")
            
            if submit_button and category and amount > 0:
                try:
                    st.session_state.manager.add_expense(category, amount)
                    st.success(f"Added ₹{amount} expense in {category.capitalize()}")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # Main Content Area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Expense Overview")
        df = load_expenses()
        if not df.empty:
            create_charts(df)
        else:
            st.info("No expenses recorded yet. Add some expenses to see the analysis!")

    with col2:
        st.markdown("### Recent Expenses")
        df = load_expenses()
        if not df.empty:
            df['date'] = pd.to_datetime(df['date'])
            df = df.sort_values('date', ascending=False)
            
            for _, row in df.head(5).iterrows():
                st.markdown(
                    f"""
                    <div style="padding: 10px; border-radius: 5px; margin: 5px 0; background-color: #f0f2f6;">
                        <h4>{row['category'].capitalize()}</h4>
                        <p>₹{row['amount']} - {row['date'].strftime('%Y-%m-%d')}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info("No recent expenses")

if __name__ == "__main__":
    main() 