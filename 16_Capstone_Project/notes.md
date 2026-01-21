# What are AI agents ?

- AI agents are software programs that can interact with users in natural language, perform tasks, and provide information based on user input.
- They can be used in a wide range of applications, including chatbots, virtual assistants, and autonomous vehicles.
- Agents are built with LLM with tools.

## Characterstics of AI Agent :-

- Goal-driven : Tell agent what to do
- Autonomous plan : Agent breaks down the problem and sequence tasks on it own
- Tool-Using :- Agent calls APIs, calculator, search tools and etc
- Context-aware :- Maintains memory across steps to inform future actions
- Adaptive :- Rethinks plan when things change(Ex: API fails)

## How do AI agents work with an example ?

- Let I have a AI agent for makemytrip website. In makemytrip there are many options like booking hotel, train or flight or cab and many more.
- If i have an agent that is capable to do all the things by query of a user.
- Ex:- Book a roundticket of a flight from Bhubaneswar to Lucknow (1st April to 10 April). Cab from lucknow airport to nearest railway station. Then a train for lucknow to mathura. then a hotel in mathura. Plan preference is budget friendly.

### 1. Understanding user intent:-

- The agent interanally interprets
  - 1st (FLIGHT)
    - From - BBSR, Odisha
    - Flight Destination - Lucknow, UP
  - 2nd (cab)
    - From - Lucknow airport
    - To - Railway station, Lucknow
  - 3rd (train)
    - From - Lucknow railway station
    - To - Mathura junction
  - 4th (hotel)
    - Hotel in mathura

  - last (Flight)
    - From - Lucknow, UP
    - To - BBSR, Odisha

### 2. Research Transport Prices

### 3. Search for affordable stay

### 4. Local transport option

### 5. Visit plan for all day

### 6. Return

### Summary of expenses

> Total expenses with Yes, confirm option and if card access of user then book confirmed, sent receipt via mail, add to your google calender, daily reminders
