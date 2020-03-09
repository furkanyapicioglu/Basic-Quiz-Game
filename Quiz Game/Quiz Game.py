import random
def Log_in():
    while True:
        class Questions_without_correct_answer:                                     #HERE THE CLASSES FOR THE QUESTIONS#
            def __init__(self,Question_number,Question,answer1_corrrect,answer2,answer3):
                self.Question_number = Question_number
                self.Question = Question
                self.answer1 = answer1_corrrect
                self.answer2 = answer2
                self.answer3 = answer3
        Question1 = Questions_without_correct_answer(1,"What is the prime minister of Turkey?","ans.1 Recep Tayyip Erdogan","ans.2 Dilber Ay","ans.3 Nihat Dogan")
        Question2 = Questions_without_correct_answer(2,"Which team has a honor to carry four star in his logos at Turkey Super League?","ans.1 Galatasaray","ans.2 Fenerbahce","ans.3 Trabzonspor")
        QuestionNew = Questions_without_correct_answer(" ", " ", " ", " ", " ")
        database_users = {"5533":["Mahmut","5.2"],"2831":["Saniye","2.3"],"3340":["Izzet","3.1"],"5337":["Hamdi","2.5"],"3320":["Figen","3.9"],"5520":["Hasan","3.4",],"3540":["Hayriye","4.1"],"3290":["Keramettin","2.7"],"6677":["3.1","Emrullah"],
                                                        "2210":["1.7","Celal"]}  #USED DICTIONARIES FOR ENTERING THE GAME
        database_users_game = {random.randint(1,3):"5533",random.randint(1,3):"2831",random.randint(1,3):"3340",random.randint(1,3):"5337",random.randint(1,3):"3320",random.randint(1,3):"5520",random.randint(1,3):"3540",random.randint(1,3):"3290",random.randint(1,3):"6677",
                                                        random.randint(1,3):"2210"} #USED ANOTHER DICTIONARIES FOR THE ELIMINATING OTHER PLAYERS
        class Users_data:
            def __init__(self,name,balance,number):                                   #HERE THE CLASSES FOR THE USERS DATA#
                self.name = name
                self.balance = balance
                self.number = number                                                 #HERE THE PRIZE CLASSES
        class Prize:
            def __init__(self,admin_prize = 10000):
                self.prize = admin_prize
        Users1 = Users_data("Mahmut",5.2,5533)
        Users2 = Users_data("Saniye",2.3,2831)
        Users3 = Users_data("Izzet",3.1,3340)
        Users4 = Users_data("Hamdi",2.5,5337)
        Users5 = Users_data("Figen",3.9,3320)
        Users6 = Users_data("Hasan",3.4,5520)
        Users7 = Users_data("Hayriye",4.1,3540)
        Users8 = Users_data("Keramettin",2.7,3290)
        Users9 = Users_data("Emrullah",3.1,6677)
        Users10 = Users_data("Celal",1.7,2210)
        while True:
            print("Welcome To The Sehir University HADI Game")                                         #NOW WE USE WHILE LOOP FOR ADMIN SECTION
            password_question = input("Please enter your number in order to sign:")
            if password_question == "**":
                        while True:
                            print("Here are the options which you can select..")
                            print("1-) Please set prize for the next competition..")
                            print("2-) Show questions for the competition..")
                            print("3-) Add questions for the competition..")
                            print("4-) Delete questions for the competition..")
                            print("5-) See users data..")
                            print("6-) Log out..")
                            admin_options_answer = input("")
                            if admin_options_answer == "1":
                                admin_prize = input("Please type the total prize of next competition:")
                                print("Setting prize " + admin_prize)
                                print("Going back to Admin Area..")
                                continue
                            elif admin_options_answer == "2":
                                print(Question1.Question_number , Question1.Question)
                                print(" ", Question1.answer1 , Question1.answer2 , Question1.answer3)
                                print(Question2.Question_number , Question2.Question)
                                print(" ", Question2.answer1 , Question2.answer2 , Question2.answer3)
                                print(QuestionNew.Question_number , QuestionNew.Question +  "?")
                                print(" ", QuestionNew.answer1 , QuestionNew.answer2 , QuestionNew.answer3)
                                continue
                            elif admin_options_answer == "3":
                                add_new_question1_number = input("Please type the question number:")
                                add_new_question1 = input("Please type the new questions:")  # WE HAVE A RAW-INPUT SECTIONS FOR ADDING QUESTIONS AND ITS ANSWERS..
                                add_new_correct_answer1 = input("Please type the correct answer:")
                                add_new_incorrect_answer1 = input("Please type the incorrect answer1:")
                                add_new_incorrect_answer2 = input("Please type the incorrect answer2:")
                                # Questions["4:"] = input(add_new_question1)
                                QuestionNew = Questions_without_correct_answer(add_new_question1_number,add_new_question1,add_new_correct_answer1,add_new_incorrect_answer1,add_new_incorrect_answer2)
                                print("Adding new questions..")
                                print("Success..")
                                continue
                            elif admin_options_answer == "4":  # WE CAN DELETE QUESTIONS WITH DICTIONARY
                                print("Q1-) What is the prime minister of Turkey?")
                                print("Q2-) Which team has a honor to carry four star in his logos at Turkey Super League?")
                                print("Q" + QuestionNew.Question_number + "-) " + QuestionNew.Question + " ?")
                                delete_question = input("")
                                if delete_question == QuestionNew.Question_number:
                                    QuestionNew = Questions_without_correct_answer(" ", " ", " ", " ", " ")
                                    print("Success..")
                                elif delete_question == "1":
                                    Question1 = Questions_without_correct_answer(" ", " ", " ", " ", " ")
                                    print("Success..")
                                elif delete_question == "2":
                                    Question2 = Questions_without_correct_answer(" ", " ", " ", " ", " ")
                                    print("Success..")
                                else:
                                    print("You typed invalid question number..")
                                continue
                            elif admin_options_answer == "5":  # DISPLAYING DATA'S WITH USING CLASSES
                                print(Users1.name , Users1.balance , Users1.number)
                                print(Users2.name , Users2.balance , Users2.number)
                                print(Users3.name , Users3.balance , Users3.number)
                                print(Users4.name , Users4.balance , Users4.number)
                                print(Users5.name , Users5.balance , Users5.number)
                                print(Users6.name , Users6.balance , Users6.number)
                                print(Users7.name , Users7.balance , Users7.number)
                                print(Users8.name , Users8.balance , Users8.number)
                                print(Users9.name , Users9.balance , Users9.number)
                                print(Users10.name, Users10.balance , Users10.number)
                                continue
                            elif admin_options_answer == "6":
                                print("Logging out..")
                            break
            if password_question == "5533" or password_question == "2831" or password_question == "3340" or password_question == "5337" or password_question == "3320" or password_question == "5520" or password_question == "3540" or password_question == "3290" or password_question == "6677" or password_question == "2210":
                    print("Welcome " + str(database_users[password_question]))
                    del database_users[password_question]
                    print("Competition will be start soon..")
                    print("Here is the First Round*******************")
                    print(Question1.Question_number , Question1.Question)
                    print(" ", Question1.answer1 , Question1.answer2 , Question1.answer3)
                    answer1_for_game = input("What is your answer?:****************")
                    if answer1_for_game != "1":
                        print("You eliminated..")
                        break
                    else:
                        print("You eliminated..")
                        print("Congratulations..You passed first round****************")
                        print("Here are the users which are passed first round..")
                        print(database_users_game.get(1))
                        print(database_users_game.get(1))
                        del(database_users_game[2 or 3])
                        print("Here is the Second Round*******************")
                        print(Question2.Question_number, Question2.Question)
                        print(" ", Question2.answer1, Question2.answer2, Question2.answer3)
                        answer2_for_game = input("What is your answer?:****************")
                        if answer2_for_game != "1":
                            print("You eliminated..")
                            break
                        else:
                            print("Congratulations..You passed second round****************")
                            print("Here are the users which are passed second round..")
                            print(database_users_game.get(2))
                            print(database_users_game.get(2))
                            del (database_users_game[1 or 3])
                        print("Here is the Third Round*******************")
                        print(QuestionNew.Question_number, QuestionNew.Question)
                        print(" ", QuestionNew.answer1, QuestionNew.answer2, QuestionNew.answer3)
                        answer3_for_game = input("What is your answer?:****************")
                        if answer3_for_game != "1":
                            print("You eliminated..")
                            break
                        else:
                            print("Congratulations..You passed third round****************")
                            print("Here are the users which are passed third round..")
                            print(database_users_game.get(3))
                            del(database_users_game[1])
                            print("Here is the prize " + admin_prize)
                            def adding_prize(self, admin_prize):
                                self.balance = (self.balance + admin_prize)
        else:
            print("you typed invalid number..")
            Log_in()
Log_in()