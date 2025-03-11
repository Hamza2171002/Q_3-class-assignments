import streamlit as st
import re
import random
import string

# Title
st.title("🔐 Password Strength Meter")
st.markdown("Enter a password to check its strength or generate a secure password:")

# function to calculate password strength
def password_strength(password: str) -> str:
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*()]", password):
        score += 1

    # rating password strength
    if score == 4:
        return "🟢 Strong Password"
    elif score == 3:
        return "🟡 Medium Password"
    elif score == 2:
        return "🟠 Weak Password"
    else:
        return "🔴 Very Weak Password"
    
#initialize session state
if "last_passwords" not in st.session_state:
    st.session_state["last_passwords"] = []

#sidebar for tools
st.sidebar.markdown("🔐 Password Tools")
action = st.sidebar.radio("Choose an option:", ["Check Password Strength", "Generate a Strong Password"])

#password strength checker
if action == "Check Password Strength":
    password = st.text_input("🔑 Enter Password:", type="password", placeholder="Enter Your Password Here...")

    if password:
        if password in st.session_state["last_passwords"]:
            st.error("❌ You have already used this password recently. Try a different one!")
        else:
            st.session_state["last_passwords"].append(password)
            
            if len(st.session_state["last_passwords"]) > 5:
                st.session_state["last_passwords"].pop(0)

            strength = password_strength(password)
            st.markdown(strength)

            if "Very Weak" in strength:
                st.error("❌ Your password is very weak! Use mix characters to improve it.")
            elif "Weak" in strength:
                st.warning("⚠ Your password needs improvement! consider adding uppercase, lowercase, and special characters.")
            elif "Medium" in strength:
                st.info("ℹ Your password is okay but could not be stronger!")
            elif "Strong" in strength:
                st.success("✅ Your password is strong!")

    with st.expander("📜 View Last 5 Passwords"):
        for i, pwd in enumerate(st.session_state["last_passwords"], start=1):
            st.markdown(f"{i}. `{pwd}`")

elif action == "Generate a Strong Password":

    def generate_password(length: int, include_numbers: bool, include_special_chars: bool) -> str:
        characters = string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_special_chars:
            characters += "!@#$%^&*"

        return "".join(random.choice(characters) for _ in range(length))
    
    st.subheader("🔑 Generate a secure Password")
    length = st.slider("🔢 Password Length:", 8, 32, 12)
    include_numbers = st.checkbox("Include Numbers")
    include_special_chars = st.checkbox("Include Special Characters")

    if st.button("🛠 Generate Password"):
        generated_password = generate_password(length, include_numbers, include_special_chars)
        st.session_state["generated_password"] = generated_password

        st.success(f"🔑 Your Secure Password: `{generated_password}`")
        st.markdown(f"**Copy and use this password:** `{generated_password}`")
