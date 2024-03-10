import streamlit as st
from battleground_tab import BattlegroundTab


def main():
    st.title("Embedding Arena")
    tab1, tab2, tab3 = st.tabs(["Battleground", "Leaderboard", "About"])

    with tab1:
        BattlegroundTab().ui()

    with tab2:
        st.header("Leaderboard")
        st.write("#TODO")

    with tab3:
        st.header("About")
        st.write("#TODO")


# Run the main function when the app is executed
if __name__ == "__main__":
    main()
