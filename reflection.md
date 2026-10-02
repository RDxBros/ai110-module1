# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game didn't work as intended and was full of bugs. The main bug I noticed is that the hints are reserved so when the guess is too high, it says go higher instead of go lower. The show hint checkbox doesn't change anything.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|             Input             | Expected Behavior  | Actual Behavior     | Console Output / Error           |
|-------------------------------|--------------------|---------------------|----------------------------------|
|Secret is 50, guess is 80      |Hint says "Go LOWER"|Hint says "Go HIGHER"|Returned opposite                 |
|Secret is 10, guess is 9       |Outcome is "Too Low"|Outcome is "Too High"|Returned opposite                 |
|Win/lose then click "New Game" |A fresh game starts |Says "Game Over"     |Status is never reset to "playing"|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Claude Code for this project. It correctly told me the secret number was being turned into a string on even attempts, and I checked that by reading the code and seeing the `str()` call on those turns. It said the info text is hardcoded but that was irrelevant so I didn't address it.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed if it acted correctly every time I played where I tried different techniques to test functionality. One example is checking that guessing a number larger than secret made the game tell me to go lower. AI helped me understand certain edge cases to test that I missed. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you click a button or type something, Streamlit runs the whole file again from the top. Normal variables get wiped on each run, so the secret number would change every time. Session state is to save things like the secret, score and attempts so they stay the same between runs.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is writing a small test for each bug before fixing it, so I know the fix actually worked. Next time I would read and test the AI's code earlier instead of trusting it at first. This project showed me that AI code can look finished and still be full of bugs, so I have to verify it myself.
