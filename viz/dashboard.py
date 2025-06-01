import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns


def load_data(filepath):
    return pd.read_csv(filepath)

def get_color(daytime):
    if daytime == 'morning':
        return 'steelblue'
    elif daytime == 'afternoon':
        return 'orange'
    elif daytime == 'evening':
        return 'firebrick'
    elif daytime == 'night':
        return 'midnightblue'

def display_dashboard():
    st.title("User Engagement Dashboard")

    task_selection = st.selectbox("Select a task", ["Task 1: User engagement on weekends", "Task 2: User engagement by time of day"])

    if task_selection == "Task 1: User engagement on weekends":
        st.subheader("Task 1: User engagement on weekends")
        st.write("This dashboard analyzes web usage data for weekends.")

        df_task1 = load_data("data/mart/task1_web_usage_weekend.csv")
        
        st.dataframe(df_task1)

    elif task_selection == "Task 2: User engagement by time of day":
        st.subheader("Task 2: User engagement by time of day")
        st.write("This dashboard analyzes web usage data by time of day.")

        df_task2 = load_data("data/mart/task2_web_usage_daytime.csv")
        
        st.dataframe(df_task2.head())

        colors = df_task2['event_time_of_day'].map(get_color)
        
        fig, ax1 = plt.subplots(figsize=(10, 6))
        ax1.bar(
            df_task2['event_hour'],
            df_task2['total_users'],
            color=colors
        )
        ax1.set_ylabel('Total Users', color='black')
        ax1.set_xlabel('Hour of the Day')
        ax1.set_xticks(range(0, 24))
        ax1.set_title('Total Users by Hour of the Day (colored by time of day)')

        legend_elements = [
            Patch(facecolor='midnightblue', label='Night'),
            Patch(facecolor='steelblue', label='Morning'),
            Patch(facecolor='orange', label='Afternoon'),
            Patch(facecolor='firebrick', label='Evening'),
        ]
        ax1.legend(handles=legend_elements)

        st.pyplot(fig, use_container_width=True)

if __name__ == "__main__":
    display_dashboard()
