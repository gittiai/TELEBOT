# TELEBOT(Your Personal Telegram Post Generator)

A GenAI tool that converts JEE-related keywords or questions into engaging Telegram posts, including CTA suggestions, hashtags, multilingual support, and multiple tones like motivational or relatable.

📌 Features :
 ● Input: 1–3 keywords or a full query (e.g., rank vs percentile, how to stay focused as a dropper?)

 ● LLM-Powered generation using Gemini Pro and Groq

 ● Tones supported: Motivational, Relatable, Announcement Style

 ● Language switcher: Convert to Hindi, Tamil, Telugu, Bengali, etc.

 ● 3 unique post variations at once (using different temperatures)

 ● History view with input and outputs

 ● Built using Streamlit + LangChain

## 🛠️ Prompt Design Strategy

The prompt is engineered to **simulate human-written Telegram posts**, especially tailored for JEE/NEET students. Key design elements:
- 70–80 words max to maintain short-form engagement
- Informal yet purposeful tone (avoids generic ChatGPT style)
- Forced line spacing between post, CTA, and hashtags
- Encourages real interaction (like reactions, replies)

## 📷 Example Inputs & Outputs
**Input Query:** `dropper regret`  
**Selected Tone:** Motivational  
**Output 1:**  
Don't let your JEE/NEET drop affect your future

Regret is a heavy burden to carry, but it's never too late to learn from your mistakes. If you've dropped a year, use it to strengthen your concepts and come back stronger. You got this!

Drop a ❤️ if you're determined to come back stronger! Reply with your score to share your story and get support!

#JEERegret #NEETDrop #PaperPhodnaHai

**Input Query:** `rank vs percentile`  
**Selected Tone:** Motivational  
**Output 2:** 
Don't get confused between Rank and Percentile!

Understand the difference and boost your confidence. Rank is the position you hold, while Percentile shows how you performed compared to others. Focus on improving your percentile, and your rank will follow.

Drop a ❤️ if you're feeling motivated to crack JEE/NEET!

Reply with your score if you want to compare and learn from each other!

#JEE #NEET #PercentileMatters #PaperPhodnaHai

**Input Query:** `tough shift`  
**Selected Tone:** Tips  
**Output 3:** 
Tough shift ahead? Don't worry, we've got you covered. Here are some tips to help you tackle the JEE/NEET exam:

Focus on your weak areas and make a study plan. Practice with previous year's papers and mock tests. Stay calm and manage your time effectively during the exam.

Drop a ❤️ if you're feeling motivated!

Reply with your score if you've already appeared for the exam.

#JEEPreparationTips #NEETExamStrategy #PaperPhodnaHai

