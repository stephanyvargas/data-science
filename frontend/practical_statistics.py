# practical_statistics.py
import streamlit as st

def load_page():
    st.markdown(
        """
        ## Practical Statistics for Data Scientists

        Personal notes and study using the book Practical Statistics for Data Scientists from O'Reilly publisher.

        - **Main GitHub Repository**: [Practical Statistics for Data Scientists](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/master)

        ### Chapter 1: Exploratory Data Analysis

        - [Jupyter Notebook for Chapter 1](https://github.com/gedeck/practical-statistics-for-data-scientists/blob/master/python/notebooks/Chapter%201%20-%20Exploratory%20Data%20Analysis.ipynb)

        #### Key Concepts

        - **Inference**: Making conclusions from data.
        - **Types of Data**:
          - Numerical (continuous and discrete)
          - Categorical (set values, binary, ordinal, etc)
        - **Pandas Variable Types**: [Documentation](https://pandas.pydata.org/docs/user_guide/basics.html#dtypes)

        #### Estimates of Data: Metrics

        - **Central Tendency**: Understanding the "typical value."
        - Metrics include:
          - **Mean**: $ \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i $
          - **Weighted Mean**: $ \bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i} $
          - **Median**: The middle value.
          - **Percentile**: Value below which a given percentage falls.
          - **Weighted Median**: Median considering weights.
          - **Trimmed Mean**: Mean after removing extreme values.
          - **Robust Metrics**: Metrics less sensitive to outliers.
          - **Outlier Detection**: Identifying extreme values.

        #### When to Use Trimmed and Weighted Mean

        - **Trimmed Mean**: Useful for handling extreme values.
        - **Weighted Mean**: Useful when:
          1. Some values are more variable than others.
          2. Data collected does not equally represent different groups.
        """
    )
