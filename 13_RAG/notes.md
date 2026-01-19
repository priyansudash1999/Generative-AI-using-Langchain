# RAG in Langchain

## What is RAG ?

- As we know LLMs are giant transformer based nuerological archiotecture and LLMs are trained with billions of data.
- So, LLMs have nearly all knowldege about the world and LLMs are stored the data in parameters as numbers. so this knowledge known as parametric knowledge.
- Let we have a LLM which has many data in its parameter, then how can we access the data from it.. ---> Using Prompting.

  ![RAG](./assets/rag.png)

- There are certain situation where the flow does not work, where we can not generate good response from LLM using Prompting.
- Situations Example:-
  1. Where I ask LLM about my private data(from my private website). Any LLM has not trained about our private data, so it can not answer
  2. When we ask about recent or today's news to LLM because LLM has knowledge cutoff(When LLM was trained last). so, LLM can not respond us.
  3. Halucination:- Sometimes LLM can give incorrect response with confidently.
  - **So, what is the correct way to handle LLM. This is known as fine-tuning.**

### Fine tuning :

- We take a pretrained LLM and train it using some outsource data.

  > #### Analogy:- A student got a it job in his college last year. Student is LLM here and the college syallbus is pretraining and when he got a job and got training in company that training is fine-tuning

- Types of fine-tuning.
  - Supervised fine tuning
  - Continued pre training (unsupervised fine tuning)

#### Supervised Fine Tuning :-

- Steps:
  - Step 1:- **Collect Data** - A few hundred-few hundred thousand carefully curated examples
  - Step 2:- **Choose a method** - Full Parameter Fine tuning, LoRA\QLoRA or parameter-efficient adapters.
  - Step 3:- **Train for a few epochs** - You keep the base weights frozen or partially frozen and update only a small subset(LoRA) or all weights(full Fine Tuning).
  - Step 4:- **Evaluate & Safety test** - Measure exact match, factuality, and hallucination rate against held-out data; red-team for safety.

##### **How fine tuning solve our problems situations ?**

- **Private data** : When we train LLM with our private data then model can save it in its parameter and then it can able to answer the questions.
- **Recent Data** : We can fine tune our new data repeatedly to update LLM about our data.
- **Hallucianation** : We can add examples of tricky prompts(where LLM was confused ) to make LLM understand the tricky part, so it can answer about `I don't know`.

  > There are some major problems in fine tuning.

- Problems:-
  - Expensive:- When we fine tune a large model it is very costly.
  - Technical Expertize :- Need AL Engineers and Data scientists.
  - Fine tune need after update any data in our website.
