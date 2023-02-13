# Natural-Language-Processing

## READING PAPER NLP

### Paper 1: Analyzing Wrap-Up Effects through an Information-Theoretic Lens
Link paper: https://aclanthology.org/2022.acl-short.3 \
Date: 31/01/2023
| Topic        |                 Analyzing Wrap-Up Effects through an Information-Theoretic Lens                                             |
|--------------|--------------------------------------------------------------------------------------------------------|
| Question Reserch    | - Data measured on words at the end of a sentence is often omitted. Consequently, the understanding of the cognitive processes that might be involved in these wrap-up effects is limited. <br /> - Are word and context surprisals that matter in real time (RT) data analysis? |
| Related Work | - Studies analyzing reading times have been employed to explore a number of psycholinguistic theories.<br /> - The existence of wrap-up effects is well-known the cognitive processes giving rise to them are still not fully understood.<br /> - Most studies of online processing omit data from these words to explicitly control for the confounding factors wrap-up effects introduce.<br /> - The few studies on wrap-up effects rely on smalldatasets, none of which analyze naturalistic text.<br /> - The long line of work that has connected information-theoretic measures and psychometric data employing similar methods to build models of sentence- and clause-final RTs. |
| Solution     | The author attempts to learn more about these processes by examining the relationship between enveloping effects and information theory quantities, such as word and context surprisals. |
| Method       | - Exploring the relationship between clause-final RTs and information-theoretic attributes of text.<br /> - Use surprise estimates from modern language models to look for associations between ending effects and informational content in a sentence.<br /> - Wrap-up effects.<br /> - Information-theoretic|
| Result       | - The author find that operationalizations of the information contained in preceding context lead to better predictions of these RTs, while not adding significant predictive power for sentence-medial RTs.<br /> - Provide evidence (either in support or against) about several theories of the nature of wrap-up processes. |

### Paper 2: On the probability–quality paradox in language generation
Link paper: https://aclanthology.org/2022.acl-short.5 \
Date: 13/02/2023
| Topic        |                 On the probability–quality paradox in language generation                                            |
|--------------|--------------------------------------------------------------------------------------------------------|
| Question Reserch    | |
| Related Work |  - In the domain of machine translation, the most probable string under the model is often the empty string. <br /> - In the domain of openended generation, mode-seeking methods produce dull and generic text. <br /> - The set of stringshas an intuitive relationship to the typical set, an information theoretic concept defined for stationary ergodic stochastic processes. |
| Solution     | - The author offer an explanation by analyzing language generation through an information-theoretic lens. <br /> - Provide preliminary empirical evidence in favor of this hypothesis. <br /> - Quality ratings of both human and machine-generated text-covering multiple tasks and common decoding strategies  |
| Method       | - An analysis comparing human and model-generated text, investigating multiple common decoding strategies and NLG tasks.<br /> - Analysis focuses exclusively on English text. <br /> -The author take these observations as empirical support for hypothesis, helping to explain the probability–quality.|
| Result       | - Quality text has an information content significantly closer to the entropy than expect by chance. <br /> - The author provide empirical evidence in support of our hypothesis in an analysis of both human and machine-generated text, demonstrating that, overwhelmingly, high-quality text indeed has information content in the proposed region. |
