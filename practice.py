# Imports
from Game import Game
from Question import Question
from random import choice

# *************** Games ***************
sci_fi_games = (
    Game("No Man's Sky", 2016, 8.1, 9.0, "PS4", True),
    Game("Kerb's Space Program", 2013, 7.7, 9.3, ["PS4", "XBOX ONE"], False),
    Game("Mass Effect", 2016, 8.1, 9.0, ["PS4", "XBOX ONE"], True),
    Game("X-COM", 2016, 8.1, 9.0, "XBOX ONE", False),
)
adventure_games = (
    Game("Uncharted 4", 2016, 9.2, 9.6, ["PS4", "Nintendo Switch"], False),
    Game("Tomb Raider", 2015, 8.6, 8.1, ["PS4", "XBOX ONE"], False),
    Game("Dragon Quest XI", 2016, 8.1, 9.0, ["PS4", "Nintendo Switch"], True),
    Game("Final Fantasy XV", 2016, 8.1, 9.0, ["PS4", "XBOX ONE"], True),
    Game("Persona 4 The Golden", 2005, 9.0, 9.9, ["PS Vita"], True)
)
horror_games = (
    Game("Resident Evil 2", 2019, 9.0, 9.2, ["PS4", "XBOX ONE"], False),
    Game("Silent Hill", 2002, 9.1, 10, ["XBOX ONE", "Nintendo Switch"], True),
    Game("Resident Evil 7", 2016, 8.1, 9.0, ["PS4", "XBOX ONE", "Nintendo Switch"], False),
    Game("Outlast", 2016, 8.1, 9.0, ["PS4", "XBOX ONE"], True),
    Game("Corpse Party", 2016, 8.1, 9.0, ["PS4", "PS Vita"], False),
)
action_games = (
    Game("Soul Calibur", 2010, 9.1, 7.6, "XBOX ONE", False),
    Game("Tekken", 2012, 7.6, 6.1, ["PS4", "XBOX ONE", "Nintendo Switch"], True),
    Game("UFC", 2016, 8.1, 9.0, ["PS4", "XBOX ONE", "Nintendo Switch", "PS Vita"], False),
)

# *************** Questions ***************
questions_group1 = [
    Question("What kind of games do you like?\n (a) Sci-fi\n (b) Adventure\n (c) Horror\n (d) Action\n", 0),
    Question("What systems do you have?\n (a) PS4\n (b) Nintendo Switch\n (c) XBOX ONE\n (d) PS Vita\n", 1),
    Question("How many hours a week do you play games?\n (a) 0-2\n (b) 3-5\n (c) 6-8\n (d) 9+\n", 2)
]


# *************** Functions ***************

# ***** Ask questions *****
def survey_questions(questions):
    answers = []
    for question in questions:
        answer = input(question.prompt)
        while answer.lower() not in "abcd":
            answer = input("I'm sorry, that is invalid. Please try again: ")
        if question.key == 0:
            if answer.lower() == "a":
                answer = "sci-fi"
            elif answer.lower() == "b":
                answer = "adventure"
            elif answer.lower() == "c":
                answer = "horror"
            else:
                answer = "action"
        elif question.key == 1:
            if answer.lower() == "a":
                answer = "PS4"
            elif answer.lower() == "b":
                answer = "Nintendo Switch"
            elif answer.lower() == "c":
                answer = "XBOX ONE"
            else:
                answer = "PS Vita"
        else:
            if answer.lower() == "a":
                answer = "0-2"
            elif answer.lower() == "b":
                answer = "3-5"
            elif answer.lower() == "c":
                answer = "6-8"
            else:
                answer = "9+"
        answers.append(answer)
    return answers


# ***** Filter Genre, Then Get Randomized Recommendation *****
def game_generator(user_answers):
    if user_answers[0] == "sci-fi":
        recommend_game = game_filter(sci_fi_games, user_answers[1])
        return recommend_game
    elif user_answers[0] == "adventure":
        recommend_game = game_filter(adventure_games, user_answers[1])
        return recommend_game
    elif user_answers[0] == "horror":
        recommend_game = game_filter(horror_games, user_answers[1])
        return recommend_game
    else:
        recommend_game = game_filter(action_games, user_answers[1])
        return recommend_game


# ***** Filter Console *****
def game_filter(genre, answer):
    def console_filter(games, console):
        game_selection = []
        for game in games:
            if console in game.consoles:
                game_selection.append(game)
        return game_selection
    recommended_game = choice(console_filter(genre, answer))
    return recommended_game.title


# ***** Base App Function; Ask questions, generate recommended game *****
def run_survey(questions_group):
    user_answers = survey_questions(questions_group)
    recommend_game = game_generator(user_answers)

    print("So you like " + user_answers[0] + " on "
          + user_answers[1] + " and usually play for "
          + user_answers[2] + " hours a week. I suggest you play "
          + recommend_game + " based on your answers!")


run_survey(questions_group1)
