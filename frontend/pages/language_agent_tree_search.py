import streamlit as st

def load_page():
    # LANGUAGE AGENT TREE SEARCH UNIFIES REASONING ACTING AND PLANNING IN LANGUAGE MODELS
    st.header("LANGUAGE AGENT TREE SEARCH UNIFIES REASONING ACTING AND PLANNING IN LANGUAGE MODELS")

    tab1, tab2  = st.tabs(["Paper", "Github"])

    with tab1:
        st.header("Paper notes")
        st.write("Summary based on the paper: [https://arxiv.org/pdf/2310.04406.pdf](https://arxiv.org/pdf/2310.04406.pdf)")
        st.subheader("Abstract")
        st.write("""
        While large language models (LLMs) have demonstrated impressive performance
        on a range of decision-making tasks, they rely on simple acting processes and
        fall short of broad deployment as autonomous agents. We introduce LATS 
        (Language Agent Tree Search), a general framework that synergizes the capabilities
        of LLMs in planning, acting, and reasoning. Drawing inspiration from Monte
        Carlo tree search commonly used in model-based reinforcement learning, LATS
        employs LLMs as agents, value functions, and optimizers, repurposing their latent
        strengths for enhanced decision-making. What is crucial in this method is
        the use of an environment for external feedback, which offers a more deliberate
        and adaptive problem-solving mechanism that moves beyond the limitations of
        existing techniques. Our experimental evaluation across diverse domains, such as
        programming, HotPotQA, and WebShop, illustrates the applicability of LATS for
        decision-making while maintaining competitive reasoning performance. In particular, 
        LATS achieves 94.4% for programming on HumanEval with GPT-4 and an
        average score of 75.9 for web browsing on WebShop with GPT-3.5, demonstrating
        the effectiveness and generality of our method.
        """)
      
        st.image("frontend/pages/lats_1.png", caption=None) 
      
        st.markdown("""
        ### Introduction
        - Autonomous Agents: The long-standing goal in AI is to create agents capable of reasoning and decision-making in various environments.
        - LLMs as a New Paradigm: Large language models (LLMs) offer a new approach, showing strong reasoning and adaptability across diverse tasks, including complex environments requiring knowledge and reasoning.
        - Limitations of Current Methods: Existing LLM methods, even with external feedback, are reflexive and lack the deliberate planning of humans. Search-guided methods enable planning but don't incorporate external feedback.
        - LATS Solution: LATS (Language Agent Tree Search) is proposed to address these issues, unifying LLM planning, acting, and reasoning through a search over possible actions, inspired by Monte Carlo tree search.
        - Key Features of LATS:
            - Uses text as an interface between components, leveraging LLM's language understanding and in-context learning.
            - Adapts planning to the environment without additional training.
            - Combines reasoning, acting, and planning to enhance LLMs.
        - LATS Achievements:
            - Doubles GPT-3.5 performance on HotPotQA compared to ReAct.
            - Improves average score by 22.1 on WebShop.
            - Achieves 94.4% Pass@1 rate on HumanEval with GPT-4, setting a new state of the art.
        - Contributions:
            - Introduces an LM-based Monte Carlo tree search variant for more flexible problem-solving.
            - Integrates external feedback and self-reflection to enhance model sensibility.
            - Demonstrates versatility across diverse domains for autonomous reasoning and decision-making.
        """)
       
        st.markdown("""
        ### RELATED WORK
        - LLMs for Reasoning:
            - Chain-of-Thought (CoT) prompting and its variants decompose complex inputs into sequential steps but suffer from error propagation.
            - Advancements like Self-Consistency and multi-step decomposition aim to mitigate this issue.
            - Search algorithms (ToT, RAP) improve CoT by sampling trajectories more effectively but rely solely on LM's internal knowledge.
        - LLMs for Acting:
            - LLMs used as policy models in interactive environments, especially text-based ones.
            - ReAct prompting technique, similar to CoT, is limited by its simplicity and inability to adapt to environment conditions.
            - Extensions like Self-refine, Reflexion, and AdaPlanner address this by incorporating feedback but focus on refining individual plans, not exploring alternatives.
            - External feedback is crucial as LLMs cannot self-correct internal reasoning.
            - Reasoning and practical abilities enhanced by access to external tools, but these methods haven't been improved with planning.
        - Tree-based Search:
            - Widely used in planning and reinforcement learning for exploration-exploitation trade-off.
            - Requires an environment model in RL, but not for LM tasks due to easy backup to any state.
            - LATS leverages the tree-based framework and MCTS to fully utilize LLM potential without training a separate value function.
        - Overall:
            - Existing methods for LLM reasoning and acting have limitations in error propagation, adapting to feedback, and exploring alternatives.
            - LATS aims to overcome these limitations by combining the strengths of tree-based search, external feedback, and LLM capabilities.
            - LATS avoids the need for extra training by utilizing the in-context learning abilities of LLMs.
        
        ### PRELIMINARIES
        - Problem Setting and Prompting:
            - Goal: Generate a final output (answer or task completion) from a natural language input using a pretrained language model.
            - Method: Utilize prompts (instructions or examples) to guide the LM.
                - Chain-of-Thought (CoT) Prompting: Decompose complex inputs into sequential intermediate thoughts to facilitate reasoning.
                - Tree-of-Thought (ToT) Prompting: Extend CoT by exploring multiple reasoning paths using search algorithms.
                - Reasoning via Planning (RAP): Similar to ToT but uses Monte Carlo Tree Search (MCTS) for planning.
                - ReAct: Adapt LLMs to tasks requiring interaction with an external environment, incorporating observations to improve reasoning and acting.
            - Shortcomings of Existing Methods: Lack of flexibility, reliance on internal representations, limited adaptability, and inability to leverage environmental feedback effectively.
        - Monte Carlo Tree Search (MCTS):
          - Heuristic search algorithm used for decision-making.
          - Builds a decision tree where nodes represent states and edges represent actions.
          - Iteratively expands the tree through exploration (sampling actions) and selection (choosing the most promising child node).
          - Uses Upper Confidence bounds applied to Trees (UCT) to balance exploration and exploitation.
          - Backpropagation updates the value function based on the outcome of each episode.
          - Advantage for LMs: No need for an environment model to undo steps, making MCTS suitable for LM tasks.

        The UCT (Upper Confidence bounds applied to Trees) of a child state s is calculated as 
        """)
    
        st.latex("""
        UCT(s) = V(s) + \omega \sqrt(\frac{\ln N(p)}{N(s)})
        """)

        st.markdown("""
        where *N(s)* is the number of visits to a node *s*, *V(s)* is the value function (expected return) from
        the subtree of *s*, *w* is the exploration weight, and *p* is the parent node of *s*. The child node with
        the highest *UCT* value is selected for expansion in the next iteration. When the end of an episode
        is reached, a backpropagation is carried out. 

        ### UNIFYING PLANNING, REASONING, AND ACTING
        - LM Agent:
            - LATS leverages the ReAct framework for sequential decision-making tasks.
            - Agent takes actions based on observations and policy, initialized with a pretrained LM as the base decision-maker.
            - Action space includes both permissible actions and reasoning traces.
            - Samples multiple actions from LM at each step to explore various trajectories.
            - Employs a search algorithm to construct the best trajectory from sampled actions.
        - LATS:
            - Uses a variant of Monte Carlo Tree Search (MCTS) to control the problem-solving process.
            - Each node in the tree represents a state (input, actions, observations).
            - Repurposes the LM as an agent, state evaluator, and feedback generator.
            - Consists of six operations:
                - Selection: Identifies the most promising node for expansion using UCT.
                - Expansion: Samples multiple actions from LM and gets observations from the environment.
                - Evaluation: Assigns a scalar value to each child node using the LM as a value function.
                - Simulation: Expands the selected node until a terminal state is reached.
                - Backpropagation: Updates the values of the tree based on simulation outcome.
                - Reflection: Generates self-reflection for unsuccessful trajectories and uses it as additional context in future iterations.
            - Advantages of LATS:
                - Generality: Supports both reasoning and decision-making tasks.
                - Deliberate: Uses MCTS and LM value function for principled search.
                - Adaptability: Leverages external feedback through observations and self-reflection.
                - Flexibility: Accommodates different scenarios and environments.
                - Modularity: Components can be independently modified and adapted.
        """)

        st.image("frontend/pages/lats_2.png", caption=None) 
      
        st.markdown("""
        ### EXPERIMENTS
        - Goal: Demonstrate LATS's general applicability across various decision-making domains requiring reasoning and acting.
        - Domains:
            - HotPotQA (multi-hop question-answering)
            - Programming (Humaneval, MBPP)
            - WebShop (online shopping environment)
        1. HotPotQA:
            - Action space includes LM thoughts and API calls for search and lookup.
            - Compared LATS with reasoning-based methods (CoT, CoT-SC, ToT, RAP) and acting-based methods (ReAct, Reflexion).
            - Results: LATS outperformed ReAct even with the same number of sampled trajectories, and combining internal and external reasoning in LATS led to the highest performance.
        2. Programming:
            - Used individual solutions as the action space and test suite/compiler feedback as observations.
            - Skipped the simulation step in LATS and used the percentage of passed tests as the reward.
            - Results: LATS achieved the highest performance on both datasets, demonstrating the importance of external feedback.
        3. WebShop:
            - Used search and click commands as actions, browser feedback and reflections as observations.
            - Results: LATS showed a noticeable improvement over ReAct and Reflexion, indicating more effective exploration.
        - Additional Observations:
            - Self-reflection in LATS provided a small performance gain.
            - MCTS was more effective than DFS and A* search algorithms.
            - Adapting search algorithms to decision-making scenarios is non-trivial.
        - Overall:
            - LATS demonstrated strong performance across diverse domains, outperforming or being competitive with existing methods.
            - The experiments highlighted the importance of external feedback, self-reflection, and principled search in enhancing LLM decision-making.
        """)
    
        
    with tab2:
        st.markdown("""
        ## Language Agent Tree Search (LATS) Agent
        - https://llamahub.ai/l/agent/llama-index-agent-lats?from=agent
        - Full cookbook on using the LATS agent: [https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/agent/lats_agent.ipynb](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/agent/lats_agent.ipynb).
        """)
        
if __name__ == "__main__":
    load_page()
