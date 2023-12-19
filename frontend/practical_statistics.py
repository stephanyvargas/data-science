# practical_statistics.py
import streamlit as st

def load_page():
    # Title and Description
    st.title("Practical Statistics for Data Scientists")
    st.write("Personal notes and study resources based on the O'Reilly book.")

    # GitHub Repository Link
    st.markdown("**Main GitHub Repository**: [View on GitHub](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/master)")

    # Chapter Details
    st.header("Chapter 1: Exploratory Data Analysis")
    st.markdown("- [Jupyter Notebook for Chapter 1](https://github.com/gedeck/practical-statistics-for-data-scientists/blob/master/python/notebooks/Chapter%201%20-%20Exploratory%20Data%20Analysis.ipynb)")

    # Key Concepts
    st.subheader("Key Concepts")
    st.markdown("""
    - **Inference**: Drawing conclusions from data.
    - **Data Types**: Numerical (continuous/discrete), Categorical (binary, ordinal).
    - **Pandas Variable Types**: [Pandas Documentation](https://pandas.pydata.org/docs/user_guide/basics.html#dtypes)
    """)

    # Estimates of Data
    st.subheader("Estimates of Data: Metrics")
    st.markdown("""
    - Central Tendency: Understanding the 'typical value.'
    - Metrics: Mean, Weighted Mean, Median, Percentile, etc.
    """)

    # Displaying LaTeX Equations
    st.latex(r"\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i")  # Mean
    st.latex(r"\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}")  # Weighted Mean

    # When to Use Trimmed and Weighted Mean
    st.subheader("When to Use Trimmed and Weighted Mean")
    st.markdown("""
    - **Trimmed Mean**: Effective for extreme values.
    - **Weighted Mean**: Best when data points have varying importance or representativeness.
    """)

if __name__ == "__main__":
    load_page()
