from survey import AnonymousSurvey
# Defin a question and make a survey.
question = "what language did you first learn to speak english?"
language_survey = AnonymousSurvey
language_survey(question)

# show the question and store response to the question.
language_survey.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response = input("languae: ")
    if response == 'q':
        break
    language_survey.store_response(response)
    
# shw the survey results.
print("\nthank you to everyone to participate in survey.")
language_survey.show_results()