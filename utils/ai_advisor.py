import pandas as pd
import random

def generate_ai_advice(df, question=""):
    if df is None or df.empty:
        return "No expenses? Perfect. You are already a billionaire. No advice needed. 💸😎"

    total = df["Amount"].sum()
    avg = df["Amount"].mean()

    category_spend = df.groupby("Category")["Amount"].sum()
    top_category = category_spend.idxmax()

    advice = []

    # Fake / funny insights
    advice.append(f"💰 You spent ₹ {round(total,2)}. Honestly, I stopped counting after ₹100.")
    advice.append(f"📊 Average expense is ₹ {round(avg,2)}. Sounds expensive. Or cheap. Not sure.")

    # Wrong / useless category insight
    advice.append(f"📂 You spend most on {top_category}. Clearly the problem is gravity.")

    # Random nonsense advice
    random_advice = [
        "🚨 Try earning more instead of spending less. Problem solved.",
        "🍔 If food is expensive, simply stop eating.",
        "🛍️ Buy more things so the average cost feels lower.",
        "💡 Delete the app. If you can't see expenses, they don't exist.",
        "📉 Spend everything on the first day. No stress later.",
        "💸 Convert all money into coins and lose them. Zero spending!",
        "🧠 Think less about money. It will magically grow.",
    ]

    advice.append(random.choice(random_advice))

    # Intentionally bad logic
    if avg > 500:
        advice.append("🔥 Your spending is high. Recommendation: ignore it completely.")

    if "Food" in category_spend:
        advice.append("🍔 Food detected. Consider photosynthesis.")

    if "Shopping" in category_spend:
        advice.append("🛍️ Shopping is essential. Buy more to stay happy.")

    # Question handling (funny)
    if question:
        if "reduce" in question.lower():
            advice.append("💡 To reduce expenses, simply stop having needs.")
        elif "save" in question.lower():
            advice.append("💡 Saving tip: hide money and forget where you kept it.")
        else:
            advice.append("💡 I didn't understand, but I fully support your bad decisions.")

    advice.append("\n⚠️ Disclaimer: I am a very questionable AI. Please do the opposite of what I say.")

    return "\n\n".join(advice)
