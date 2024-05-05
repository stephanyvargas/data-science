import streamlit as st

def load_page():
    # **PROMETHEUS 2: An Open Source Language Model Specialized in Evaluating Other Language Models**
    st.header("PROMETHEUS 2: An Open Source Language Model Specialized in Evaluating Other Language Models")
    st.write("Summary based on the paper: [https://arxiv.org/pdf/2405.01535](https://arxiv.org/pdf/2405.01535)")
    st.subheader("Abstract")
    st.write("""
    Proprietary LMs such as GPT-4 are often employed to assess the quality of responses from various LMs. However, concerns including 
    transparency, controllability, and affordability strongly motivate the development of opensource LMs specialized in evaluations. On the
    other hand, existing open evaluator LMs exhibit critical shortcomings: 1) they issue scores that significantly diverge from those assigned 
    by humans, and 2) they lack the flexibility to perform both direct assessment and pairwise ranking, the two most prevalent forms of assessment.
    Additionally, they do not possess the ability to evaluate based on custom evaluation criteria, focusing instead on general attributes like
    helpfulness and harmlessness. To address these issues, we introduce Prometheus 2, a more powerful evaluator LM than it’s predecessor that
    closely mirrors human and GPT-4 judgements. Moreover, it is capable of processing both direct assessment and pair-wise ranking formats
    grouped with a user-defined evaluation criteria. On four direct assessment benchmarks and four pairwise ranking benchmarks, PROMETHEUS
    2 scores the highest correlation and agreement with humans and proprietary LM judges among all tested open evaluator LMs. Our models,
    code, and data are all publicly available in [https://github.com/prometheus-eval/prometheus-eval](https://github.com/prometheus-eval/prometheus-eval).
    """)
    
    st.write("**Main points**")
    st.markdown("""
    - language model-based evaluation has emerged as a scalable and cheap paradigm for assessing LM-generated text
    """)
    
    st.code("""
    def logging_decorator(func): 
        # ...
        
    def timer_decorator(func):
        # ... (Code from above)
    """) 
    
if __name__ == "__main__":
    load_page()
