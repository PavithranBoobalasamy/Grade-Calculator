import streamlit as st

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    st.title("Student Grade Calculator")
    st.write("Enter the score of the student:")

    score = st.number_input("Enter score", min_value=0, max_value=100, step=1)

    if st.button("Calculate Grade"):
        grade = calculate_grade(score)
        st.write(f"The grade for the student is: {grade}")

if __name__ == "__main__":
    main()
