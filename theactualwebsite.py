import streamlit as st

title = "Noobys Stuff 2"
st.set_page_config(page_title=title)


st.markdown("""
<style>
html {
  scroll-behavior: smooth;
}
</style>
""", unsafe_allow_html=True)



td = "---"

tab0, tab1, tab2, tab3, tab4 = st.tabs(["home", "me", "gimme ideas im bored", "github page", "reviewing your ideas"])

with tab0:
    st.subheader('hello and welcome to noobys website!')
    st.write('i made this because i was really bored lmao')
    st.subheader('check the other tabs for other stuff')

with tab1:
    st.title("this is just a section about me, if u dont care leave")
    st.subheader("Who are you?")
    st.write('im nooby. what did u think?')
    st.subheader('Why did you make this website?')
    st.write("uhhhhhhhh double it and give it to the next person")
    st.subheader("Why did you double it")
    st.write("okay this tab is over")

with tab2:
    st.write('fill out these things to send me a msg also u can just use a random name (after u click send u need to complete a captcha)')
    contact_form = """
    <form action="https://formsubmit.co/amitay33126@gmail.com" method="POST" target="_blank">
     <input type="text" name="name" placeholder="ur name" required>
     <input type="email" name="email" placeholder="ur email (not required)">
     <textarea name="message" placeholder="ur msg" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    st.components.v1.html(contact_form)

with tab3:
    st.title(" ")
    st.write("[heres the github page >](https://github.com/nooby124/noobys-stuff-2/tree/main)")

with tab4:
    st.subheader("we have an idea from 'ligma' wow very original name")
    st.write("wow you really love that 2017 meme about ninja having ligma also fuck you for writing fuck you in the idea")
    st.image("asddd.png")
    st.write("---")
    st.title("no more ideas yet")
    st.write("submit your ideas at the 'gimme your ideas im bored' tab")

