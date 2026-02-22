import streamlit as st
import random
import styles.background as background

# Sets background image
bg = background.Background("https://fun.tgv.com.my/wp-content/themes/tgv-child/assets/spongebob/sea-bg.jpg")
bg.set_page_bg()

# Session variables initialization
if 'q_idx_spongebob' not in st.session_state:
    st.session_state.q_idx_spongebob = 0
if 'user_scores_spongebob' not in st.session_state:
    st.session_state.user_scores_spongebob = [0] * 6

# Quiz  data
# Score Order: [SpongeBob, Patrick, Squidward, Mr. Krabs, Sandy, Plankton]
quiz = [
    {"question": "What is your dream job?", "options": [("Fry Cook at the best restaurant", [1,0,0,0,0,0]), ("Professional Napper", [0,1,0,0,0,0]), ("Famous Clarinet Player", [0,0,1,0,0,0])]},
    {"question": "How do you spend your free time?", "options": [("Jellyfishing with friends", [1,1,0,0,0,0]), ("Counting your savings", [0,0,0,1,0,0]), ("Practicing Karate or Science", [0,0,0,0,1,0])]},
    {"question": "Someone is being too loud next door. You...", "options": [("Join them! The more the merrier!", [1,0,0,0,0,0]), ("Yell at them to be quiet", [0,0,1,0,0,0]), ("Plan a complex scheme to stop them", [0,0,0,0,0,1])]},
    {"question": "What's your favorite food?", "options": [("A delicious Krabby Patty", [1,1,0,0,0,0]), ("Anything from the trash can", [0,1,0,0,0,0]), ("Fancy canned bread", [0,0,1,0,0,0])]},
    {"question": "Pick a quote:", "options": [("I'm ready!", [1,0,0,0,0,0]), ("Is mayonnaise an instrument?", [0,1,0,0,0,0]), ("The future is now!", [0,0,0,0,1,0])]},
    {"question": "What is your greatest fear?", "options": [("The Krusty Krab closing", [1,0,0,1,0,0]), ("Being average and boring", [0,0,1,0,0,0]), ("Whales", [0,0,0,0,0,1])]},
    {"question": "How do you handle a crisis?", "options": [("Run around screaming", [1,1,0,0,0,0]), ("Stay calm and use science", [0,0,0,0,1,1]), ("Protect your wallet", [0,0,0,1,0,0])]},
    {"question": "What's your favorite musical instrument?", "options": [("My nose", [1,0,0,0,0,0]), ("Mayonnaise (obviously)", [0,1,0,0,0,0]), ("The Clarinet", [0,0,1,0,0,0])]},
    {"question": "Your ideal home is...", "options": [("A Pineapple", [1,0,0,0,0,0]), ("Under a rock", [0,1,0,0,0,0]), ("An Easter Island Head", [0,0,1,0,0,0])]},
    {"question": "What is your secret goal?", "options": [("To be the best employee ever", [1,0,0,0,0,0]), ("To find the world's largest donut", [0,1,0,0,0,0]), ("World domination!", [0,0,0,0,0,1])]}
]

characters = ["SpongeBob SquarePants", "Patrick Star", "Squidward Tentacles", "Mr. Krabs", "Sandy Cheeks", "Sheldon J. Plankton"]

# Analysis and results data and images
analysis = [
    "You are the eternal optimist! You find joy in the smallest things and are a incredibly hard worker.",
    "You live life in the slow lane. You are a loyal friend and very relaxed.",
    "You appreciate the finer things in life, like art and silence. You feel misunderstood.",
    "You are highly motivated and have a great eye for business and value.",
    "You are adventurous, smart, and tough! You love a good challenge.",
    "You are small but mighty—and very ambitious. You never give up!"
]

results_data = {
    'SpongeBob SquarePants': {'description': analysis[0], 'image': 'https://i.pinimg.com/736x/b8/a1/c4/b8a1c420a08085e35bffa85dacd4fa59.jpg', 'traits': ['Optimistic', 'Energetic', 'Kind']},
    'Patrick Star': {'description': analysis[1], 'image': 'https://i.pinimg.com/1200x/1c/7f/59/1c7f591c29b9a51de3452726c8ac8e8f.jpg', 'traits': ['Relaxed', 'Loyal', 'Carefree']},
    'Squidward Tentacles': {'description': analysis[2], 'image': 'https://i.pinimg.com/736x/b9/a3/1d/b9a31dec23dc9858d53afeb66f867c51.jpg', 'traits': ['Artistic', 'Sophisticated', 'Cynical']},
    'Mr. Krabs': {'description': analysis[3], 'image': 'https://i.pinimg.com/736x/d4/32/d8/d432d8702499191ee6da61845bbdc97b.jpg', 'traits': ['Business-minded', 'Protective', 'Ambitious']},
    'Sandy Cheeks': {'description': analysis[4], 'image': 'https://i.pinimg.com/736x/c1/c6/04/c1c604251892106c7f9c608b653ba6b6.jpg', 'traits': ['Strong', 'Intelligent', 'Adventurous']},
    'Sheldon J. Plankton': {'description': analysis[5], 'image': 'https://i.pinimg.com/736x/d1/9b/52/d19b52a33350849d504bcdc8964cf9c7.jpg', 'traits': ['Genius', 'Persistent', 'Misunderstood']}
}

# Page and questions logic
if st.session_state.q_idx_spongebob < len(quiz):
    curr_q = quiz[st.session_state.q_idx_spongebob]
    st.progress((st.session_state.q_idx_spongebob + 1) / len(quiz))
    st.subheader(f"Question {st.session_state.q_idx_spongebob + 1} of 10")
    st.write(f"### {curr_q['question']}")

    choice = st.radio("", [opt[0] for opt in curr_q["options"]], key=f"sb_q_{st.session_state.q_idx_spongebob}")

    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.q_idx_spongebob > 0:
            if st.button("Previous"):
                st.session_state.q_idx_spongebob -= 1
                st.rerun()
    with col2:
        btn_label = "Finish Quiz" if st.session_state.q_idx_spongebob == 9 else "Next"
        if st.button(btn_label):
            selected_index = [opt[0] for opt in curr_q["options"]].index(choice)
            scores_to_add = curr_q["options"][selected_index][1]
            for i in range(len(st.session_state.user_scores_spongebob)):
                st.session_state.user_scores_spongebob[i] += scores_to_add[i]
            st.session_state.q_idx_spongebob += 1
            st.rerun()
else:
    # Results logic
    max_score = max(st.session_state.user_scores_spongebob)
    winners = [i for i, s in enumerate(st.session_state.user_scores_spongebob) if s == max_score]
    result = characters[random.choice(winners)]

    st.balloons()
    st.header(f"You are {result}!")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(results_data[result]['image'], use_container_width=True)
    with c2:
        st.write(results_data[result]['description'])
        for trait in results_data[result]['traits']:
            st.markdown(f"- **{trait}**")

    st.write("---")
    chart_data = {characters[i]: st.session_state.user_scores_spongebob[i] for i in range(len(characters))}
    st.bar_chart(chart_data)

    if st.button("Restart Quiz"):
        st.session_state.q_idx_spongebob = 0
        st.session_state.user_scores_spongebob = [0] * 6
        st.rerun()