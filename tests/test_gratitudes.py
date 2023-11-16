from lib.gratitudes import Gratitudes

#Checks if the format method returns the expected string when there are no gratitudes added
#def __init___ in class has empty brackets that need to be tested out first.
#We are writing a test for gratitudes to test the format as seen in the last method in the class. 
#Start off with an instance (remember to differeniate using a lowercase or different name) (Gratitudes is because of the class name)
#Use the assert statement with the frist instance we created from this method and pair with the thrid method (.format - format is the method in the class)
#on the same line, check to see if it passes what we want the output to be.
#Note if you remove the space after the colon and run the test it will fail. This is because the space after the colon is what we are testing this method out for. 
def test_empty_gratitude_string():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

#Now we are testing to see if the added words appear in the 2nd method we have.
#Use the same instances as before.
#Now add the gratitude we want the outcome to say i.e. being alive, breathing today etc.
#To understand the code and see you mistake more clearly, create a variable named result (or anything) and assign your outcome of the second method. 
#Use the assert statement to check if you new variable (exepcted_result) is == to the frist and third method 
#Because you added the second method to the end of the first method, your expected_result should be (first method outcome + second method outcome).
#.format() is there because it refers this test to the class and the third method requires a formatted output.
#.format() also ensure that the outcome is a string. 
def test_add_words_to_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("being alive")
    gratitude.add("breathing today")
    gratitude.add("having good health")
    gratitude.add("anything & everything")
    expected_result = "Be grateful for: being alive, breathing today, having good health, anything & everything"
    assert expected_result == gratitude.format() 

#Finally add your frist method's instance and your second method's .add (your gratitiude texts) and bring them over to this method.
#Create a variable to check if the test passes with what the method is asking. 
#In this case, join the strings together and add the commas.
#Use the assert statement to check the result == gratitude.format()(variable made in the first method).(method name of what the test is for)
def test_join_the_words_of_gratitude_together_in_format():
    gratitude = Gratitudes()
    gratitude.add("being alive")
    gratitude.add("breathing today")
    gratitude.add("having good health")
    gratitude.add("anything & everything")
    result = "Be grateful for: being alive, breathing today, having good health, anything & everything"
    assert result == gratitude.format()

