# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Streamlit Data Analytics App")

# Upload dataset
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read the dataset
    data = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the dataset
    st.write("### Data Preview")
    st.write(data.head())
    
    # Display summary of the dataset
    st.write("### Data Summary")
    st.write(data.describe())
    
    # Plotting
    st.write("### Data Visualization")
    
    # Select type of graph
    graph_type = st.selectbox("Choose a graph type", ["Line Plot", "Bar Plot", "Histogram", "Box Plot", "Scatter Plot"])
    
    # Check if user wants to select only categorical variables for x-axis
    if st.checkbox("Select only categorical variables for x-axis"):
        # Assuming categorical columns have fewer unique values, we filter based on that
        categorical_columns = [col for col in data.columns if data[col].nunique() < 10]
    else:
        categorical_columns = data.columns
    
    # Select columns based on graph type
    if graph_type in ["Line Plot", "Bar Plot", "Histogram"]:
        selected_column = st.selectbox("Select a column", categorical_columns)
    elif graph_type in ["Box Plot", "Scatter Plot"]:
        x_axis = st.selectbox("Select x-axis", categorical_columns)
        y_axis = st.selectbox("Select y-axis", data.columns)
    
    # Plot based on user's choice
    if st.button("Plot"):
        st.write(f"### {graph_type} for selected column(s)")
        fig, ax = plt.subplots()
        
        if graph_type == "Line Plot":
            data[selected_column].plot(kind="line", ax=ax)
            plt.ylabel(selected_column)
        elif graph_type == "Bar Plot":
            data[selected_column].value_counts().plot(kind="bar", ax=ax)
            plt.ylabel("Count")
        elif graph_type == "Histogram":
            data[selected_column].plot(kind="hist", ax=ax)
            plt.xlabel(selected_column)
            plt.ylabel("Count")
        elif graph_type == "Box Plot":
            data[[x_axis, y_axis]].boxplot(by=x_axis, ax=ax)
            plt.ylabel(y_axis)
        elif graph_type == "Scatter Plot":
            data.plot(kind="scatter", x=x_axis, y=y_axis, ax=ax)
        
        st.pyplot(fig)
