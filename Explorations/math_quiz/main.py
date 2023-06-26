# Import necessary libraries
import PySimpleGUI as sg
import random
import time
from questions import questions  # Import questions from questions.py file

class Quiz:
    def __init__(self):
        # Set the theme for PySimpleGUI
        sg.theme('DarkBlue')

        # Initialize variables for tracking score, total questions asked, and the start time of the quiz
        self.score = 0
        self.total_questions = 0
        self.start_time = time.time()

        # Define the layout of the GUI. 
        # It contains a Text element for displaying the question,
        # four Button elements for the multiple-choice answers, and a 'Next' button for moving to the next question.
        self.layout = [[sg.Text(size=(75,1),border_width=25, key='-QUESTION-', font = ('Helvetica', 20))],
                       [sg.Button(size=(20,1), key='-BUTTON-'+str(i), button_color=('white', 'blue'), font= ('Helvetica', 10)) for i in range(4)],
                       [sg.Button('Next', key='-NEXT-', size= (25,1), button_color=('white', 'green'), font= ('Helvetica', 15))]]

        # Create the PySimpleGUI Window with the defined layout
        self.window = sg.Window('Math Quiz', self.layout, finalize=True, element_justification= 'left')

        # Initialize more variables for managing the quiz
        self.questions = questions  # Load the questions
        self.current_question = None
        self.selected_answer = None
        self.question_index = 0  # Initialize the question index
        self.next_question()  # Load the first question

    def next_question(self):
    # Check if all questions have been answered
        if self.question_index == len(self.questions):
            # All questions have been answered, end the quiz
            self.finish_quiz()
            self.window.close()
            return
        # Select the next question from the question list
        self.current_question = self.questions[self.question_index]
        self.question_index += 1  # Increase the question index by 1
        # Generate the numbers to be used in the question and answer
        self.numbers = self.current_question["numbers"]()
        # Format the question string with the generated numbers
        self.formatted_question = self.current_question["question"].format(*self.numbers)
        # Calculate the correct answer
        self.correct_answer = self.current_question["answer"](*self.numbers)

        # Update the Text element in the GUI with the formatted question
        self.window['-QUESTION-'].update(self.formatted_question)

        # Generate three random options and add the correct answer
        self.options = [self.correct_answer] + [random.randint(int(self.correct_answer)-100, int(self.correct_answer)+100) for _ in range(3)]
        # Shuffle the options to ensure the correct answer isn't always in the same position
        random.shuffle(self.options)

        # Update the four Button elements in the GUI with the options
        for i, option in enumerate(self.options):
            self.window['-BUTTON-'+str(i)].update('{:.2f}'.format(option) if self.current_question["answer"] == float else str(option), button_color=('white', 'blue'))

        # Reset the selected answer
        self.selected_answer = None

    def select_answer(self, i):
        # If an answer was previously selected, reset its color
        if self.selected_answer is not None:
            self.window['-BUTTON-'+str(self.selected_answer)].update(button_color=('white', 'blue'))
        # Set the selected answer and change its color
        self.selected_answer = i
        self.window['-BUTTON-'+str(i)].update(button_color=('white', 'dark blue'))

    def evaluate_answer(self):
        # Only evaluate the answer if one was selected
        if self.selected_answer is not None:
            # Increment the total questions asked
            self.total_questions += 1
            # If the selected answer is correct, increment the score
            if self.options[self.selected_answer] == self.correct_answer:
                self.score += 1
            # If 20 questions have been asked, end the quiz, otherwise move to the next question
            if self.total_questions >= 20:
                self.finish_quiz()  # Call it as a function with parentheses
            else:
                self.next_question()


    def finish_quiz(self):
        # Calculate the end time and total duration of the quiz
        end_time = time.time()
        total_time = end_time - self.start_time
        # Show a popup with the quiz results
        sg.popup(f"Total Questions: {self.total_questions}\n"
                 f"Correct Answers: {self.score}\n"
                 f"Percentage Correct: {round(self.score / self.total_questions * 100)}%\n"
                 f"Total Time: {total_time:.2f} seconds", title="Quiz Result",
                 line_width= 50)
        # Close the quiz window
        self.window.close()

    def run(self):
        # Main event loop for the quiz
        while True:
            # Read the next event and values from the window
            event, values = self.window.read()
            # If the window is closed, break the loop
            if event == sg.WINDOW_CLOSED:
                break
            # If the 'Next' button is pressed, evaluate the selected answer
            if event == '-NEXT-':
                self.evaluate_answer()
            # If one of the answer buttons is pressed, select that answer
            elif '-BUTTON-' in event:
                self.select_answer(int(event.split('-')[2]))
                
            if event is None or event == 'Exit':
                break

            # Add this check to see if the window has been closed
            if not self.window:
                break

# Create an instance of the Quiz class and run the quiz
quiz = Quiz()
quiz.run()



