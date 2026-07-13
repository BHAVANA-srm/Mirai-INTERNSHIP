import streamlit as st

# ----------------------------
# Task 1: UI Shell
# ----------------------------
st.title("The Identity Echo Interface")

st.write(
    "Welcome! Please enter your name and a message, then click **Transmit**."
)

# ----------------------------
# Task 2: Multi-Data Collection
# ----------------------------
user_name = st.text_input("Enter your Name")

user_message = st.text_input("Enter your Message")

# ----------------------------
# Task 3: Action Gate
# ----------------------------
if st.button("Transmit"):

    # ----------------------------
    # Task 4: Conditional Routing
    # ----------------------------
    if user_name.strip() == "":
        st.error("Please provide your name.")

    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")

    else:
        # ----------------------------
        # Task 5: Formatted Output
        # ----------------------------
        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        # ----------------------------
        # Advanced Challenge
        # ----------------------------
        total_characters = len(user_message)
        token_count = total_characters / 4

        st.info(
            f"System Check: Your message will consume approximately {token_count:.2f} tokens from our context window."
        )