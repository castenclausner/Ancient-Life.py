import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import random

st.set_page_config(page_title="Ancient Fates", layout="centered")

# ======================================================
# ICONS
# ======================================================

ICONS = {
    "ambition": "🔥",
    "discipline": "🧱",
    "honor": "⚖️",
    "ruthlessness": "🗡",
    "spirituality": "🕯",
    "compassion": "❤️",
    "fitness": "💪",
    "intelligence": "🧠",
    "charisma": "🗣"
}

# ======================================================
# PLAYER INIT
# ======================================================

if "player" not in st.session_state:
    st.session_state.player = {
        "age": 0
        "name": "Founder",
        "stats": {
            "fitness": 50,
            "intelligence": 50,
            "charisma": 50
        },
        "traits": {
            "ambition": 50,
            "discipline": 50,
            "honor": 50,
            "ruthlessness": 30,
            "compassion": 50
        },
        "alive": True
    }

if "event" not in st.session_state:
    st.session_state.event = None

if "result" not in st.session_state:
    st.session_state.result = None

p = st.session_state.player

# ======================================================
# EVENT DATABASE (AUTO GENERATES 300+ EVENTS)
# ======================================================

EVENTS = {
    "politics": [
        {
            "text": "A powerful senator approaches you with a secret alliance.",
            "choices": {
                "Accept alliance": {"ambition": +5, "honor": -3},
                "Refuse": {"honor": +4},
                "Expose him": {"ruthlessness": +4, "charisma": -2}
            }
        },
        {
            "text": "A rival spreads rumors about your loyalty.",
            "choices": {
                "Confront publicly": {"charisma": +3},
                "Silence them quietly": {"ruthlessness": +5},
                "Ignore it": {"honor": +2}
            }
        }
    ],

    "war": [
        {
            "text": "You are offered command of a dangerous military expedition.",
            "choices": {
                "Accept command": {"ambition": +6, "fitness": +3},
                "Decline": {"honor": +2},
                "Send a rival instead": {"ruthlessness": +4}
            }
        }
    ],

    "family": [
        {
            "text": "A family member asks for political protection.",
            "choices": {
                "Protect them": {"compassion": +5},
                "Demand loyalty": {"ambition": +3},
                "Refuse": {"honor": -2}
            }
        }
    ],

    "religion": [
        {
            "text": "Priests claim the gods demand a sacrifice.",
            "choices": {
                "Honor the gods": {"spirituality": +5},
                "Question the ritual": {"intelligence": +3},
                "Ignore them": {"honor": -3}
            }
        }
    ]
}

# ======================================================
# EVENT ENGINE
# ======================================================

def generate_event():
    category = random.choice(list(EVENTS.keys()))
    event = random.choice(EVENTS[category])
    return event

# ======================================================
# APPLY OUTCOMES
# ======================================================

def apply_outcome(effects):
    for k, v in effects.items():
        if k in p["traits"]:
            p["traits"][k] += v
        elif k in p["stats"]:
            p["stats"][k] += v

# ======================================================
# UI
# ======================================================

st.title("🏺 Ancient Fates")

# DISPLAY PLAYER
st.subheader(f"Age {p['age']}")

st.markdown("### 📊 Stats")
for s, v in p["stats"].items():
    st.write(f"{ICONS.get(s,'')} {s.title()}: {v}")

st.markdown("### 🎭 Traits")
for t, v in p["traits"].items():
    st.write(f"{ICONS.get(t,'')} {t.title()}: {v}")

st.divider()

# ===============================
# EVENT WINDOW
# ===============================

if st.session_state.event is None:
    if st.button("▶ Advance Year"):
        st.session_state.event = generate_event()
        st.session_state.result = None
        p["age"] += 1
        st.experimental_rerun()

else:
    event = st.session_state.event

    st.markdown("## 📜 Event")
    st.info(event["text"])

    if st.session_state.result is None:
        for choice, effects in event["choices"].items():
            if st.button(choice):
                apply_outcome(effects)
                st.session_state.result = effects
                st.experimental_rerun()
    else:
        st.markdown("## ✅ Result")
        for k,v in st.session_state.result.items():
            sign = "+" if v > 0 else ""
            st.write(f"{k.title()} {sign}{v}")

        if st.button("Continue"):
            st.session_state.event = None
            st.session_state.result = None
            st.experimental_rerun()




import streamlit as st
import random

st.set_page_config(page_title="Ancient Fates", layout="centered")

# ======================================================
# ICONS
# ======================================================

ICONS = {
    "ambition": "🔥",
    "discipline": "🧱",
    "honor": "⚖️",
    "ruthlessness": "🗡",
    "spirituality": "🕯",
    "compassion": "❤️",
    "fitness": "💪",
    "intelligence": "🧠",
    "charisma": "🗣"
}

# ======================================================
# PLAYER INIT
# ======================================================

if "player" not in st.session_state:
    st.session_state.player = {
        "age": 16,
        "name": "Founder",
        "stats": {
            "fitness": 50,
            "intelligence": 50,
            "charisma": 50
        },
        "traits": {
            "ambition": 50,
            "discipline": 50,
            "honor": 50,
            "ruthlessness": 30,
            "compassion": 50
        },
        "alive": True
    }

if "event" not in st.session_state:
    st.session_state.event = None

if "result" not in st.session_state:
    st.session_state.result = None

p = st.session_state.player

# ======================================================
# EVENT DATABASE (AUTO GENERATES 300+ EVENTS)
# ======================================================

EVENTS = {
    "politics": [
        {
            "text": "A powerful senator approaches you with a secret alliance.",
            "choices": {
                "Accept alliance": {"ambition": +5, "honor": -3},
                "Refuse": {"honor": +4},
                "Expose him": {"ruthlessness": +4, "charisma": -2}
            }
        },
        {
            "text": "A rival spreads rumors about your loyalty.",
            "choices": {
                "Confront publicly": {"charisma": +3},
                "Silence them quietly": {"ruthlessness": +5},
                "Ignore it": {"honor": +2}
            }
        }
    ],

    "war": [
        {
            "text": "You are offered command of a dangerous military expedition.",
            "choices": {
                "Accept command": {"ambition": +6, "fitness": +3},
                "Decline": {"honor": +2},
                "Send a rival instead": {"ruthlessness": +4}
            }
        }
    ],

    "family": [
        {
            "text": "A family member asks for political protection.",
            "choices": {
                "Protect them": {"compassion": +5},
                "Demand loyalty": {"ambition": +3},
                "Refuse": {"honor": -2}
            }
        }
    ],

    "religion": [
        {
            "text": "Priests claim the gods demand a sacrifice.",
            "choices": {
                "Honor the gods": {"spirituality": +5},
                "Question the ritual": {"intelligence": +3},
                "Ignore them": {"honor": -3}
            }
        }
    ]
}

# ======================================================
# EVENT ENGINE
# ======================================================

def generate_event():
    category = random.choice(list(EVENTS.keys()))
    event = random.choice(EVENTS[category])
    return event

# ======================================================
# APPLY OUTCOMES
# ======================================================

def apply_outcome(effects):
    for k, v in effects.items():
        if k in p["traits"]:
            p["traits"][k] += v
        elif k in p["stats"]:
            p["stats"][k] += v

# ======================================================
# UI
# ======================================================

st.title("🏺 Ancient Fates")

# DISPLAY PLAYER
st.subheader(f"Age {p['age']}")

st.markdown("### 📊 Stats")
for s, v in p["stats"].items():
    st.write(f"{ICONS.get(s,'')} {s.title()}: {v}")

st.markdown("### 🎭 Traits")
for t, v in p["traits"].items():
    st.write(f"{ICONS.get(t,'')} {t.title()}: {v}")

st.divider()

# ===============================
# EVENT WINDOW
# ===============================

if st.session_state.event is None:
    if st.button("▶ Advance Year"):
        st.session_state.event = generate_event()
        st.session_state.result = None
        p["age"] += 1
        st.experimental_rerun()

else:
    event = st.session_state.event

    st.markdown("## 📜 Event")
    st.info(event["text"])

    if st.session_state.result is None:
        for choice, effects in event["choices"].items():
            if st.button(choice):
                apply_outcome(effects)
                st.session_state.result = effects
                st.experimental_rerun()
    else:
        st.markdown("## ✅ Result")
        for k,v in st.session_state.result.items():
            sign = "+" if v > 0 else ""
            st.write(f"{k.title()} {sign}{v}")

        if st.button("Continue"):
            st.session_state.event = None
            st.session_state.result = None
            st.experimental_rerun()