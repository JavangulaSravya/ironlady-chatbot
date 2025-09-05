# Iron Lady Leadership Chatbot (Rules-Based)

faq = {
    "programs": "Iron Lady offers unique women’s leadership programs focused on courage, confidence, and career growth. These include personal transformation journeys, career acceleration tracks, and leadership workshops.",
    "duration": "Programs vary in duration. Some workshops last a few weeks, while signature journeys can last several months.",
    "format": "Iron Lady programs are mainly online for accessibility, with some offline or hybrid events.",
    "certificate": "Yes! Participants receive completion certificates recognizing their leadership journey with Iron Lady.",
    "mentors": "Experienced mentors, coaches, and leaders guide participants, specializing in women’s leadership and career growth."
}

print("💬 Welcome to Iron Lady’s Leadership Chatbot! (Type 'exit' to quit)\n")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Bot: Thanks for chatting with Iron Lady 💜 Stay courageous!")
        break

    if "program" in user_question.lower():
        response = faq["programs"]
    elif "duration" in user_question.lower():
        response = faq["duration"]
    elif "online" in user_question.lower() or "offline" in user_question.lower() or "format" in user_question.lower():
        response = faq["format"]
    elif "certificate" in user_question.lower():
        response = faq["certificate"]
    elif "mentor" in user_question.lower() or "coach" in user_question.lower():
        response = faq["mentors"]
    else:
        response = "I’d love to help! You can ask me about programs, duration, format, certificates, or mentors."

    print("💜 Iron Lady Bot:", response)
