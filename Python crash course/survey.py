class AnonymousSurvey:
    """collect anonymous answers to a question survey."""
    def __init__(self, question):
        """store a question and prepare to store response."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_results(self):
        """show all the responese that have been given."""
        print("survey results.")
        for response in self.responses:
            print(f"- {response}")
