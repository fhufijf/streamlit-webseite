import streamlit as st

adsa = 0

videos = [
    ("Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    ("Bouncing DVD Logo Screensaver 4K 60fps - 10 hours NO LOOP", "https://www.youtube.com/watch?v=5mGuCdlCcNM&t=1s"),
    ("Der große McDonald’s Monopoly Betrug", "https://www.youtube.com/watch?v=5gmqFXnAslc"),
    ("$0 to $1 Billion on Minecraft's Largest Server", "https://www.youtube.com/watch?v=fYf_5RHHKBQ"),
    ("The God Man - Full Film (9.5min)", "https://www.youtube.com/watch?v=WY9CTDM3l4M"),
    ("Trigger Me Elmo | World's First Race Detecting Toy", "https://www.youtube.com/watch?v=Q8QlNuTUe4M"),
    ("Microsoft HQ absolutely cooked right now.", "https://www.youtube.com/watch?v=AgrcwZxCkzM"),
    ("I Built a Dog Catapult", "https://www.youtube.com/watch?v=oA85M9JHsW0"),
    ("SCP:GALLIONIC | Official Trailer", "https://www.youtube.com/watch?v=RSbPdf3CGD8"),
    ("Backrooms | Official Teaser HD | A24", "https://www.youtube.com/watch?v=tKGhxMi50y8"),
    ("I Bully Youtube's Greatest Scam Artist", "https://www.youtube.com/watch?v=aSc8CpkDiQY"),
    ("How Vitamin Water Can Put You in a Coma", "https://www.youtube.com/watch?v=8IzkgYHMUps"),
    ("We Finally Found Out Why Charon Is Broken", "https://www.youtube.com/watch?v=FTx2O7Zm4Jc"),
    ("The Player Who Was Found Burning", "https://www.youtube.com/watch?v=wjlV9nJSIFg"),
    ("This Horror Mod Distorts Your Memories", "https://www.youtube.com/watch?v=y-_7qS1HF7g"),
]

if "videos" not in st.session_state:
    st.session_state.videos = videos

length = len(videos)

a = length / 2

st.title("Mini Youtube")

def video_test():
    col1, col2 = st.columns(2)

#loop über nummerierte liste, i ist der index
    for i, (title, url) in enumerate(st.session_state.videos):
#%2 == 0 überprüft ob der index(i) gerade ist, wir brauchen die kurzform von if else
        with (col1 if i % 2 == 0 else col2):
            with st.container(border=True):
                st.text(title)
                st.video(url)
video_test()