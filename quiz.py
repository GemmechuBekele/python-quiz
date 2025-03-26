questions = (
   "1. If you are working with decimal number which numeric data you can use?",
   "2. How tuple differ from list?",
   "3. During naming variable which one is invalid?",
   "4. If you are working with text which data type you can use?",
   "5. How you can retrieve elements in list?"
)

options = (("A. int", "B. string", "C. float", "D. decimal"), 
           ("A. Tuple is mutable", "B. Tuple is immutable", "C. Element in tuple is not accessible", "D. All"),
           ("A. Using underscore at the first", "B. Using key words", "C. Using camel case", "D. Using underscore between two words"),
           ("A. float", "B. string", "C. text", "D. alphanumeric"),
           ("A. By using append", "B. By using element name", "C. By using import key words", "D. By using index"))

answers = ("C", "B", "B", "B", "D")
guesses = []
Score = 0
Questuon_number = 0
for question in questions:
   print("---------------------------------------------------------------")
   print(question)
   for option in options[Questuon_number]:
      print(option)
      
   guess = input("Enter your annswer (A, B, C, D): " ).upper()
   guesses.append(guess)  
   if guess == answers[Questuon_number]:
      Score+=1
      print("Correct")
   else:
      print("Incorrect")
      print(f"{answers[Questuon_number]} is correct answer!")
   Questuon_number+=1
   
print("---------------------------------------------------------------")
print("  Results       ")
print(f"Result: {Score} out of {len(questions)}")
print()
print("Your answer:")
for guess in guesses:
   print(guess, end="")
print("Correct answer:")
for answer in answers:
   print(answer, end="")
