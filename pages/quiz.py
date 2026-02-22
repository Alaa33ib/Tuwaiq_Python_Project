# Imports
import streamlit as st
import random
    
# Name entry #switch to streamlit
# name = input("Enter your name: ")
# print(f"Welcome {name}! to Personality Quizes\nChoose A Quiz")

if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
if 'user_scores' not in st.session_state:
    st.session_state.user_scores = [0] * 6


#Quiz questions
quiz = [
    {
        "question": "You’re asked to teach someone a skill you’re good at. You…" ,
        "options": [
            ("Demonstrate it step by step ", [1,0,0,0,0,0]),
            ("Show it quietly and encourage independent thinking ", [0,1,0,0,0,0]),
            ("Make it fun and entertaining while teaching ", [0,0,1,0,0,0])
        ]
    },
    {
        "question": "Choose your favorite board games",
        "options": [
            ("Chess ", [0,1,0,0,0,0]),
            ("Puzzles ", [1,0,0,0,0,0]),
            ("Cards", [0,0,1,0,0,0])
        ]
    },
    {
        "question": "How do you deal with stress or fear?" ,
        "options": [
            ("Express it dramatically or humorously ", [0,0,1,0,0,0]),
            ("Distract yourself with something else ", [0,0,0,0,0,1]),
            ("Focus on duty and what is expected of you ", [0,0,0,1,0,0])
        ]
    },
    {
        "question": "Your friends describe you as:" ,
        "options": [
            ("Kind and loyal ", [0,0,0,0,1,0]),
            ("Funny and easy going ", [0,0,1,0,0,0]),
            ("Intelligent and dependable ", [0,1,0,0,0,0])
        ]
    },
    {
        "question": "You’re faced with a complicated gadget or device. You…" ,
        "options": [
            ("Experiment with it, see what creative uses you can find ", [0,0,0,0,0,1]),
            ("Ask for help ", [0,0,0,0,1,0]),
            ("Follow the guidelines ", [0,0,0,1,0,0])
        ]
    },
    {
        "question": "Your ideal weekend looks like:" ,
        "options": [
            ("Caching up on your hobbies (reading, playing video games) ", [1,0,0,0,0,0]),
            ("Quiet reflection with coffee ", [0,1,0,0,0,0]),
            ("Spending time with loved ones. ", [0,0,0,0,1,0])
        ]
    },
    {
        "question": "How do you handle failure?" ,
        "options": [
            ("Analyze what went wrong and adjust ", [1,0,0,0,0,0]),
            ("Blame circumstances or make a joke ", [0,0,1,0,0,0]),
            ("Take responsibility and ensure it doesn’t happen again ", [0,0,0,1,0,0])
        ]
    },
    {
        "question": "Choose a quote:",
        "options": [
            ("Courage is not the absence of fear, but the triumph over it. ", [0,0,0,1,0,0]),
            ("The future belongs to those who believe in the beauty of their dreams. ", [0,0,0,0,1,0]),
            ("Creativity is intelligence having fun ", [0,0,0,0,0,1])
        ]
    },
    {
        "question": "What is your weakness?" ,
        "options": [
            ("Distracted easily ", [0,0,0,0,0,1]),
            ("Rash or dramatic  ", [0,0,1,0,0,0]),
            ("Overly cautious  ", [0,1,0,0,0,0])
        ]
    },
    {
        "question": "Someone challenges your authority. You…" ,
        "options": [
            ("Prove your point with logic ", [1,0,0,0,0,0]),
            ("Handle it with patience and kindness ", [0,0,0,0,1,0]),
            ("Outthink them with wits ", [0,0,0,0,0,1])
        ]
    }
]

#Characters list and score initialization
characters = ["Conan Edogawa", "Ai Haibara", "Kogoro Mouri", "Inspecter Megure", "Ran Mouri", "Professor Agasa"]
score = [0,0,0,0,0,0]

# Analysis
analysis = ["You’re highly analytical and enjoy unraveling complex problems on your own. Your mind constantly notices patterns and connections others often miss. Even in tense situations, you remain calm and deliberate. People turn to you when clever solutions and insight are needed.",
            "You’re highly intelligent and always thinking several steps ahead. You carefully weigh risks before making decisions. Your mysterious and composed nature makes you reliable in tense situations. You combine sharp logic with a subtle, thoughtful intuition.",
            "You thrive in the spotlight and bring energy to every situation. You act boldly and react quickly, often relying on instinct. Even when plans go off course, you adapt with flair and confidence. Your charm and enthusiasm make you unforgettable to those around you.",
            "You take your responsibilities seriously and follow through with precision. Your decisions are guided by experience, careful observation, and logic. Others trust your consistency and dependability in challenging situations. You provide structure and stability when things get chaotic.",
            "You are deeply loyal and always attentive to the needs of those around you. You act courageously to protect the people you care about. Your empathy and thoughtfulness make others feel safe and valued. You quietly support others, earning trust through your consistent care.",
            "You’re imaginative, curious, and full of bright ideas. You love inspiring and helping others with creative solutions. Your energy and warmth make people feel encouraged and supported. Even when your thoughts wander, your inventive mind keeps shining."]


# Describtion of characters to display
results_data = {
    'Conan Edogawa': {
        'description': analysis[0],
        'image': 'https://i.pinimg.com/736x/37/26/72/37267280bf1022cfa390e394e12b6a44.jpg',
        'traits': ['Analytical', 'Calm', 'Insightful']
    },
    'Ai Haibara': {
        'description': analysis[1],
        'image': 'https://i.pinimg.com/736x/59/cb/bb/59cbbb323e36c0f3d38bea2d12825ee8.jpg',
        'traits': ['Strategic', 'Composed', 'Intuitive']
    },
    'Kogoro Mouri': {
        'description': analysis[2],
        'image': 'https://i.pinimg.com/736x/61/39/6f/61396f4d7f04006fb6275da72602613f.jpg',
        'traits': ['Bold', 'Adaptable', 'Enthusiastic']
    },
    'Inspector Megure': {
        'description': analysis[3],
        'image': 'https://i.pinimg.com/736x/99/c7/b9/99c7b9ea502a1109e441f1830c60e0fe.jpg',
        'traits': ['Responsible', 'Dependable', 'Consistent']
    },
    'Ran Mouri': {
        'description': analysis[4],
        'image': 'https://i.pinimg.com/736x/75/70/c4/7570c4459c133f7c96420c070899f8b3.jpg',
        'traits': ['Loyal', 'Courageous', 'Empathetic']
    },
    'Professor Agasa': {
        'description': analysis[5],
        'image': 'https://i.pinimg.com/736x/65/0b/44/650b440b7ea48787953e083c2fd70a7b.jpg',
        'traits': ['Imaginative', 'Curious', 'Inventive']
    }
}


# Questions loop #turn to streamlit
#Looping over each question and option along with asking user to choose an option.
for q in quiz:
  while True: # this will continue to ask the question until it is answered correctly.
    print("\n",q["question"])
    for index, option in enumerate(q["options"],start=1):
      print(f"{index}. {option[0]}")

    choice = input("\nChoose Option Number: ")

    #Handling incorrect input
    # use lambda for check
    valid = lambda x: x.isdecimal() and 0 < int(choice) <= len(q["options"])
    if valid(choice):
      chosen_scores = q["options"][int(choice) - 1][1]
      for i in range(len(score)): # calculate score
        score[i] += chosen_scores[i]
      break # if it is not there the loop will contiue to give the first question over and over again. No matter what is the input.
    else:
      print("Invalid option! Try again")


# Function to show results and solve tie by choosing a character randomly
def personality(score, characters):
  max_score = max(score)
  # check if there was a tie
  handle_tie = [i for i in range(len(score)) if score[i] == max_score]
  random_choice = random.choice(handle_tie)
  return characters[random_choice] + "\n" + analysis[random_choice]


# Using the personality fynction to get the results
result = personality(score, characters)

# Seperating line and title
st.markdown("---")
st.header(f"You are {result}!")

# Layout organization, two columns
col1, col2 = st.columns([1, 2]) # Ratio of column sizes

# Column 1: Character image
with col1:
    try:
        st.image(results_data[result]['image'], use_container_width=True)
    except:
        st.warning("Image file not found!")

#Column 2: Character Describtion and traits
with col2:
    st.subheader("Description")
    st.write(results_data[result]['description'])
    
    st.subheader("Key Traits")
    # Displaying traits as a list
    for trait in results_data[result]['traits']:
        st.markdown(f"- **{trait}**")

# Bar chart of score over the characters
st.write("---")
st.subheader("Your Personality Breakdown")
# Mapping scores in the chart with the character names
chart_data = {characters[i]: score[i] for i in range(len(characters))}
st.bar_chart(chart_data)