import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Streamlit App
st.title("Interactive Data Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.write("### Preview of Data:")
    st.write(df.head())

    # Summary statistics
    st.write("### Summary Statistics:")
    st.write(df.describe())

    # Column selection for visualization
    columns = df.select_dtypes(include=['number']).columns
    if len(columns) > 0:
        x_axis = st.selectbox("Choose X-axis:", columns)
        y_axis = st.selectbox("Choose Y-axis:", columns)

        # Scatter plot
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig)

        # Histogram
        selected_column = st.selectbox("Select column for histogram:", columns)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax)
        st.pyplot(fig)

    else:
        st.write("No numerical columns found for visualization.")

    # Pie Chart: Visualize a Categorical Column
    categorical_columns = df.select_dtypes(include=['object']).columns
    if len(categorical_columns) > 0:
        categorical_column = st.selectbox("Select a categorical column for pie chart:", categorical_columns)
        
        # Pie chart with Plotly
        pie_data = df[categorical_column].value_counts()
        fig = px.pie(pie_data, values=pie_data.values, names=pie_data.index, title=f"Distribution of {categorical_column}")
        st.plotly_chart(fig)

        # Optional: Matplotlib Pie Chart
        st.write(f"### Matplotlib Pie Chart for {categorical_column}:")
        fig, ax = plt.subplots()
        ax.pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.pyplot(fig)
