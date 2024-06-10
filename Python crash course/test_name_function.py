from name_function import get_formatted_name
def test_first_last_name():
    """Do names like abdul majeed work?"""
    formatted_name = get_formatted_name("Abdul", "Majeed")
    assert formatted_name == "Abdul Majeed"
    
    # now run and in the terminal 
    # run pytest if does not recoganies 
    # write python -m pytest to see the test is passed or failed.
    
    #  The single dot after the name of the file tells us that a single test passed,
    # and the 100% makes it clear 
    # last line tells that it took less than 0.01 seconds to run the test.
    
    # let’s take a closer look at this function
    # 1 it must start with test_
    # 2 Then define a test function: in this case, test_first_last_name()
    # 3 call the function get_formatted_name() with arguments 'janis' and 'joplin'
    # 4 make an assertion An assertion is a claim about a condion
    
    # What does a failing test look like? Let’s modify get_formatted_name
    # with middle name and run test