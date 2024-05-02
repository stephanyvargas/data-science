import streamlit as st
import time
import os
import platform
import numpy as np
import pandas as pd
from datetime import datetime

#file_path = "pomodoro_data.csv"


def update_statistics():
    """Update the CSV with new data."""
    # Check if file exists, if not, create it
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["date", "completed_pomodoros"])
        df.to_csv(file_path, index=False)

    # Load current data
    df = pd.read_csv(file_path)

    # Update data for today or create a new entry
    today = datetime.now().date()
    if today in df["date"].values:
        df.loc[df["date"] == today, "completed_pomodoros"] += 1
    else:
        new_data = {"date": today, "completed_pomodoros": 1}
        df = df.append(new_data, ignore_index=True)

    print('here is the dataframe', df)

    df.to_csv(file_path, index=False)

def show_statistics():
    """Display the user's historical data."""
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        st.write(df)
    else:
        st.write("No historical data available.")


def beep(duration = 1, freq = 440):
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(freq, duration * 1000)
    else:
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


def timer(minutes):
    time.sleep(minutes * 60)
    beep()


def main():

    # Layout
    left, center, right = st.columns([1,2,1])
    with center:
        st.image("tomato_image.png", width=300)

    st.markdown("<h1 style='text-align: center; color: #704070;'>Enhanced Pomodoro Timer</h1>", unsafe_allow_html=True)
    st.write("The Pomodoro Technique is a time management method that can help boost productivity. Set your timers below!")

    st.session_state.pomodoro_time=50
    st.session_state.short_break_time=10
    st.session_state.long_break_time=50
    st.session_state.total_cycles=10
    st.session_state.max_cycles=3

    # Pomodoro time
    st.write("Pomodoro time:")
    col1, col2, col3 = st.columns(3)
    if col1.button("25 min", key='pomodoro_25'):
        st.session_state.pomodoro_time = 25
    elif col2.button("50 min", key='pomodoro_50', type="primary"):
        st.session_state.pomodoro_time = 50
    elif col3.button("75 min", key='pomodoro_75'):
        st.session_state.pomodoro_time = 75


    # Short break time
    st.write("Short break time:")
    col1, col2, col3 = st.columns(3)
    if col1.button("5 min", key='short_5'):
        st.session_state.short_break_time = 5
    elif col2.button("10 min", key='short_10', type="primary"):
        st.session_state.short_break_time = 10
    elif col3.button("15 min", key='short_15'):
        st.session_state.short_break_time = 15

    # Long break time
    st.write("Long break time:")
    col1, col2, col3 = st.columns(3)
    if col1.button("30 min", key='long_30'):
        st.session_state.long_break_time = 30
    elif col2.button("50 min", key='long_50', type="primary"):
        st.session_state.long_break_time = 50
    elif col3.button("75 min", key='long_75'):
        st.session_state.long_break_time = 75

    # Total cycles
    st.write("Total number of cycles:")
    col1, col2, col3 = st.columns(3)
    if col1.button("6 cycles", key='6_cycles'):
        st.session_state.total_cycles = 6
    elif col2.button("8 cycles", key='8_cycles'):
        st.session_state.total_cycles = 8
    elif col3.button("1o cycles", key='10_cycles', type="primary"):
        st.session_state.total_cycles = 10

    # Maximum pomodoros per cycle
    st.write("Maximum pomodoros per cycle:")
    col1, col2, col3 = st.columns(3)
    if col1.button("2 cyles", key='2_cycles'):
        st.session_state.max_cycles = 2
    elif col2.button("3 cycles", key='3_cycles', type="primary"):
        st.session_state.max_cycles = 3
    elif col3.button("4 cycles", key='4_cycles'):
        st.session_state.max_cycles = 4


    # # Integrate To-Do List
    # st.write("Your To-Do List for the Pomodoro Sessions:")
    # tasks = st.text_area("List out your tasks (one per line)").split('\n')
    # task_checkboxes = []
    # for task in tasks:
    #     checkbox = st.checkbox(task)
    #     task_checkboxes.append(checkbox)

    # # Check which tasks are completed
    # completed_tasks = [tasks[i] for i, checked in enumerate(task_checkboxes) if checked]
    # st.write("Completed tasks:", ', '.join(completed_tasks))


    if st.button("Start Timer"):
        cycles_completed = 0
        progress_bar = st.progress(0)
        status_text = st.empty()
        timer_text = st.empty()

        while cycles_completed < st.session_state.total_cycles:
            for _ in range(min(st.session_state.max_cycles, st.session_state.total_cycles - cycles_completed)):
                status_text.text(f"Cycle {cycles_completed + 1}/{st.session_state.total_cycles}: Pomodoro!")

                for i in range(st.session_state.pomodoro_time * 60):
                    timer_text.text(f"Time left: {np.round(st.session_state.pomodoro_time - i/60,0)} minutes")
                    progress_bar.progress(i/(st.session_state.pomodoro_time*60))
                    time.sleep(1)

                cycles_completed += 1
                progress_bar.progress(0)

                if cycles_completed < st.session_state.total_cycles:
                    status_text.text(f"Cycle {cycles_completed}/{st.session_state.total_cycles}: Short break!")

                    for i in range(st.session_state.short_break_time * 60):
                        timer_text.text(f"Time left: {np.round(st.session_state.short_break_time*60 - i, 0)} seconds")
                        progress_bar.progress(i/(st.session_state.short_break_time*60))
                        time.sleep(1)

                    progress_bar.progress(0)

                    if cycles_completed % st.session_state.max_cycles == 0:
                        break

            if cycles_completed < st.session_state.total_cycles:
                status_text.text(f"Cycle {cycles_completed}/{st.session_state.total_cycles}: Long break!")

                for i in range(st.session_state.long_break_time * 60):
                    timer_text.text(f"Time left: {st.session_state.long_break_time*60 - i} seconds")
                    progress_bar.progress(i/(st.session_state.long_break_time*60))
                    time.sleep(1)

                progress_bar.progress(0)

        status_text.text("All Pomodoro cycles completed!")
        timer_text.text(" ")

    #update_statistics()

    # Show statistics button
    #if st.button("Show Statistics"):
    #    show_statistics()


if __name__ == "__main__":
    main()
