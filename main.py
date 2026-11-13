import streamlit as st

st.set_page_config(page_title="Maya's Portfolio", page_icon="🚀")

# ------------------------------------------------
# ✏️ Change the words below to make it yours!
# ------------------------------------------------

# ---------- Top of the page ----------
st.title("👋 Hi, I'm XYZ!")
st.subheader("I draw, I code tiny games, and I love my cat Biscuit 🐱")

# st.image("me.jpg", width=200)   # <- remove the # and add your own photo!

st.divider()

# ---------- About me ----------
st.header("🌟 About me")
st.write(
    "I'm 12 years old and I love making things. "
    "I taught myself Scratch last year, and now I'm learning Python!"
)

st.divider()

# ---------- My projects ----------
# Each project is a box. Copy one block to add more!
st.header("🛠️ Things I made")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("🎮 Space Dodger")
        st.write("A game where you steer a rocket through falling asteroids.")
        st.caption("Made with Scratch")

with col2:
    with st.container(border=True):
        st.subheader("📖 Biscuit's Adventures")
        st.write("A comic about a cat who thinks he's a detective.")
        st.caption("Made with pencils and markers")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.subheader("✌️ Rock-Paper-Scissor")
        st.write("A game where you pull fingers and see who wins based on the `rock-paper-scissor` rule.(https://gamerockpapersciapprsgit-gpqfwcunczgr9f39une2dp.streamlit.app/)")
        st.caption("Made with Python")

with col4:
    with st.container(border=True):
        st.subheader("🏙️ LEGO Skyline")
        st.write("A city with 14 buildings and a working train.")
        st.caption("Made with LEGO")

st.divider()

# ---------- Skills ----------
# Numbers go from 0 to 100
st.header("💪 What I'm good at")
st.progress(90, text="🎨 Drawing")
st.progress(80, text="🧑‍💻 Scratch")
st.progress(45, text="🐍 Python")

st.divider()

# ---------- My favorite things ----------
st.header("❤️ My favorite things")
tab1, tab2, tab3 = st.tabs(["🍕 Food", "🎮 Games", "📚 Books"])

with tab1:
    st.write("Pizza, mango smoothies, and chocolate chip cookies!")
with tab2:
    st.write("Minecraft, Mario Kart, and any game with a cute animal.")
with tab3:
    st.write("Anything with dragons in it 🐉")

# ---------- Fun fact ----------
with st.expander("🎁 Click to see a fun fact about me"):
    st.write("I can solve a Rubik's cube in under 2 minutes!")

st.divider()

# ---------- Say hi ----------
st.header("💌 Say hi!")
name = st.text_input("What's your name?")

if st.button("Say hi to Me 🚀"):
    st.balloons()
    st.success(f"Yay! Thanks for visiting, {name}! 🎉")
