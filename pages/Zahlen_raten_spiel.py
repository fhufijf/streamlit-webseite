#td limited versuche, höher oder tiefer

import streamlit as st
import random
import time

#---------------------------------------------------
p = "primary"
s = "secondary"
t = "tertiary"
#---------------------------------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []
    
if "y" not in st.session_state:
    st.session_state.y = (int(random.randrange(1,11)))

if "versucht" not in st.session_state:
    st.session_state.versucht = 0

if "TF" not in st.session_state:
    st.session_state.TF = False
#---------------------------------------------------
with st.chat_message("ai"):
    st.write("Robot: Rate ein Nummer von 1 bis 10")

#answer = []
def dialog(input):
#  if len(st.session_state.chat) > 0:
    if int(input) == st.session_state.y:
      return f"Robot: Richtig!!!, die zahl war {st.session_state.y}"
    else:   
      if st.session_state.y > int(input):
        return "Robot: zu tief"
        
      else:
        return "Robot: zu hoch"

    
prompt = st.chat_input("Sag etwas", disabled = st.session_state.TF)

def reset():
  st.session_state.chat = []
  st.session_state.y = (int(random.randrange(1,11)))
  st.session_state.versucht = 0
  st.session_state.TF = False
  st.rerun()

#linie 22 testet ob der user etwas geschieben hat wen ja testet linie 23 ob es ein nummer ist und wenn ja wird es zu den liste hinzugefügt
if prompt:
  if prompt.isnumeric():
    st.session_state.versucht += 1
    if st.session_state.versucht >= 3:
      st.session_state.TF = True
      answer = "Robot: du hast dein 3 versuche benutzt"

    else:
      answer = dialog(prompt)
    st.session_state.chat.append({
      "human": prompt,
      "ai": answer,})
  else:
    st.session_state.chat.append({
      "human": prompt,
      "ai": "Roboter: Muss eine Nummer sein.",})

for message in st.session_state.chat:
  with st.chat_message("human"):
    st.write(message["human"])
  with st.chat_message("ai"):
    st.write(message["ai"])  

if st.session_state.versucht >= 3:
      time.sleep(1)
      reset()


if st.button("Reset", type=p, width="stretch"):
  reset()
  
def debug():
  st.write("Die Nummer", st.session_state.y)
  st.write("Länge der Dict", len(st.session_state.chat))
  st.write("Das Dict", (st.session_state.chat))
  if len(st.session_state.chat) > 0:
    st.write("Das letzte element der Dict", (st.session_state.chat[-1]))
    st.write("Ob das letzte Element des Dicts und Die Nummer Gleich sind", (st.session_state.chat[-1]) == st.session_state.y)
  st.write("die versuche die man benutzt hat", st.session_state.versucht)

