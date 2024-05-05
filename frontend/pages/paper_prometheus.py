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
    st.markdown("""
    ## Prometheus
    Prometheus🔥 is a family of open-source language models specialized in evaluating other language models. By effectively simulating human judgments and proprietary LM-based evaluations, we aim to resolve the following issues:
    - Fairness: Not relying on closed-source models for evaluations!
    - Controllability: You don’t have to worry about GPT version updates or sending your private data to OpenAI by constructing internal evaluation pipelines
    - Affordability: If you already have GPUs, it is free to use!
    """)
    
    st.markdown("""
    ### Introduction
    - Existing methods for evaluating large language models (LLMs) are not sufficient due to the complexity of LLM outputs.
    - Language model-based evaluation is a promising solution, where LMs assess other LMs' outputs. 
    - This approach can be done in two ways: 
            - direct assessment (giving a quality score) or 
            - pairwise ranking (determining which of two outputs is better).
    - Proprietary LMs are often used for evaluation, but they lack transparency and can be expensive.
    - Recent work focuses on open-source evaluator LMs, but they struggle to match human evaluation or proprietary LMs.
    - This paper proposes a new method that combines evaluator LMs trained on both direct assessment and pairwise ranking tasks.
    - PROMETHEUS 2, achieves high correlations with human evaluators and outperforms other open-source LMs. 
    - To train PROMETHEUS 2, a new dataset called PREFERENCE COLLECTION is introduced, which includes more diverse evaluation criteria.

    ### Related Work
    - LM-based evaluation is a promising alternative to traditional metrics (Rouge, BLEU, BERTScore) that struggle to capture quality beyond similarity to a reference answer.
    - Weight merging has been shown to improve performance in various NLP tasks, and this work applies it to enhance evaluator LMs.

    ### Methodology
    - **Direct Assessment** and **Pairwise Ranking** 
        - Direct assessment: Takes an instruction, response, and optionally a reference answer and evaluation criteria as input, and outputs a score (1-5 Likert scale).
    """)

    st.latex("""
    f_{\rm direct} : (i, r) \rightarrow s \quad {\rm where } \quad s \in \mathbb(R)
    """)
    st.markdown("""
    Pairwise ranking: Takes an instruction, two responses, optionally a reference answer and evaluation criteria, and outputs which response is better.
    3.3 The Preference Collection: Describes a new dataset created for training evaluator LMs on pairwise ranking with fine-grained evaluation criteria. Key points:
    Based on the FEEDBACK COLLECTION dataset used for direct assessment.
    Includes 1,000 custom evaluation criteria beyond general ones like helpfulness.
    Created by pairing responses from the FEEDBACK COLLECTION and generating new verbal feedback comparing them using GPT-4.
    3.4 Employing Evaluator Language Models: Explains four methods for training evaluator LMs. Key points:
    Prompting: Using an LM to make judgements without training.
    Single-Format Training: Training on data for either direct assessment or pairwise ranking.
    Joint Training: Training on data for both direct assessment and pairwise ranking.
    Weight Merging: Training separate LMs for each task and then combining their weights (focusing on this method).
    Linear merging with a coefficient of 0.5 is found to work best with Mistral-7B base model.
    Other merging techniques (Task Arithmetic, TIES, DARE) are also explored.
    """)
        
if __name__ == "__main__":
    load_page()
