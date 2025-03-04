import streamlit as st
import re
import random
import string

# Common Weak Passwords List
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password1", "admin", "welcome"]

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check for Common Passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("❌ This is a commonly used weak password. Choose a unique one.")

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Function to Generate a Strong Password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Check your password strength & get suggestions for improvement!")

# Password Input
password = st.text_input("Enter Your Password", type="password")

# Check Button
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Strength Bar
        st.progress(score / 4)

        # Show Score and Strength Level
        if score == 4:
            st.success("✅ Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider improving it.")
        else:
            st.error("❌ Weak Password - Make changes based on the suggestions below.")

        # Show Feedback
        for msg in feedback:
            st.write(msg)
    else:
        st.error("Please enter a password!")

# Password Generator Section
st.subheader("🔑 Need a Strong Password?")
if st.button("Generate Password"):
    strong_password = generate_password()
    st.text_input("Suggested Strong Password", strong_password, disabled=True)

# Footer
st.write("---")
st.write("🔹 **Created with ❤️ in Python & Streamlit**")
