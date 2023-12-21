# practical_statistics.py
import streamlit as st

def load_page():
    st.markdown(
        """
        ## Dive into Data Science: Practical Statistics for Data Scientists

        Welcome to an interactive journey through the fascinating world of statistics! Here, I share my personal notes and insights gained from the acclaimed book, "Practical Statistics for Data Scientists" published by O'Reilly.

        **Discover More**: Explore the [Official GitHub Repository](https://github.com/gedeck/practical-statistics-for-data-scientists/tree/master) for comprehensive resources and examples.

        ### Chapter 1: Unraveling Exploratory Data Analysis

        Get hands-on with data: Access the [Interactive Jupyter Notebook for Chapter 1](https://github.com/gedeck/practical-statistics-for-data-scientists/blob/master/python/notebooks/Chapter%201%20-%20Exploratory%20Data%20Analysis.ipynb).

        #### Core Concepts Decoded

        - **Inference**: The art of drawing insightful conclusions from complex data.
        - **Types of Data**:
          - Numerical (continuous and discrete): The backbone of quantitative analysis.
          - Categorical (from binary to ordinal): Unlocking the patterns in qualitative data.
        - **Pandas Variable Types**: Dive deeper with the [Pandas Documentation](https://pandas.pydata.org/docs/user_guide/basics.html#dtypes).

        #### Data Metrics: The Heart of Analysis

        - **Central Tendency**: Unveiling the 'heart' of your data. Discussion on various measures of location [here](https://en.wikipedia.org/wiki/Central_tendency)
        - Key Metrics:
          - **Mean**: 
            - Description: The mean, or average, is the sum of all values divided by their count.
            - Equation: 
              st.latex(r"\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i")
          - **Weighted Mean**: 
            - Equation:
              st.latex(r"\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i})
          - **Median**: The point where your data splits in half.
          - **Weighted Median**: A tailored median giving more weight to certain values.
          - **Percentile**: Benchmarking values in a percentage scale.
          - **Trimmed Mean**: Averaging by removing data extremes.
          - **Robust Metrics**: Metrics resistant to outliers' impact.
          - **Outlier Detection**: Spotting the anomalies that can sway your insights.

        ##### Tailoring Averages: Trimmed and Weighted Mean

        - **Trimmed Mean**: Ideal for mitigating the effect of outliers. Often involves excluding the top and bottom 10%.
        - **Weighted Mean**: Essential when:
          1. Variability matters in your values.
          2. Achieving representation across diverse groups.

        #### Estimates of Variability

        *Variability*, also referred to as *dispersion*, measures whether the data values are tightly clustered or spread out.

        - **Mean Absolute Deviation (MAD)**:
          - Description: The average distance between each data point and the mean.
          - Equation:
            st.latex(r"MAD = \frac{1}{n} \sum_{i=1}^{n} |x_i - \bar{x}|)
        - **Variance**:
          - Description: The average of the squared differences from the Mean.
          - Equation:
            st.latex(r"\sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2)
        - **Standard Deviation**:
          - Description: The square root of the variance, providing a measure of the spread of a distribution.
          - Equation:
            st.latex(r"\sigma = \sqrt{\sigma^2})
        - **Median Absolute Deviation from the Median (MAD Median)**:
          - Description: Median of the absolute deviations from the median of the dataset.
          - Equation:
            st.latex(r"MAD_{\text{Median}} = \text{Median}(|x_i - \text{Median}(x)|))
        - **Percentiles**:
          - Description: The value below which a given percentage of observations in a group of observations fall.
        - **Interquartile Range (IQR)**:
          - Description: Measures the spread of the middle 50% of the data.
          - Equation:
            st.latex(r"IQR = Q_3 - Q_1)
        """
    )

if __name__ == "__main__":
    load_page()
