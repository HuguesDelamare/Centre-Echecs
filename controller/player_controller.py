import view
import model
import datetime
import string


class PlayerController(object):

    # Function to set the birthdate of the new player
    @classmethod
    def set_player_birthdate(cls):

        # List of valid date format
        format_list = ["%d-%m-%Y", "%d/%m/%Y", "%d %m %Y"]

        while True:
            player_birthdate = str(input('Player Birthdate: '))
            for format in format_list:
                try:
                    date = datetime.datetime.strptime(player_birthdate, format).date()
                    return date
                except ValueError:
                    print('Asking for ' + format + ' format, ' + player_birthdate + ' given.')
                    pass

    # Function to get all the players in our DB
    @classmethod
    def get_all_players_in_db(cls):
        count = 0
        players_db_size = model.playermodel.get_player_db_size()

        while count < players_db_size:
            count += 1

            # Selecting players by their IDs
            players = model.playermodel.get_players_by_id(count)

            # Display all the players(names and ranks) from DB
            view.View.display_all_players(count, players)

    # Function to pick the gender of the player
    @classmethod
    def set_player_gender(cls):
        while True:
            player_gender = input('Player gender: [M]ale or [F]emale ?: ')
            if player_gender.lower() == "m" or player_gender == "f":
                return player_gender.capitalize()
            else:
                continue

    # Function to set the ladder of the new player
    @classmethod
    def set_player_ladder(cls):
        while True:
            ladder_input = int(input('Player ladder: '))

            # Ladder needs to be int type
            if type(ladder_input) is int:
                return ladder_input
            else:
                continue
        return ladder_input

    # Function to check if data is valid
    @classmethod
    def check_player_info(cls, input_text_value):
        while True:
            count = 0

            # Setting a list of invalid special characters
            invalidcharacters = set(string.punctuation)
            input_value = input('Player ' + input_text_value + ': ')

            # Checking if input value is a string (str)
            if type(input_value) is str:

                # Checking if input value is longer than 2
                if len(input_value) != 0 and len(input_value) >= 2:

                    # Looping through every character of the input value to check if theres digit in
                    for letter in input_value:
                        if letter.isdigit():
                            count += 1
                        else:
                            pass
                    if count >= 1:
                        print('ERROR, no numbers allowed.')
                        continue
                    else:

                        # Condition to check if theres a special characters in our input
                        if any(char in invalidcharacters for char in input_value):
                            print("ERROR, no special characters allowed.")
                            continue
                        else:
                            pass
                else:
                    print('ERROR, must be longer.')
                    continue
            else:
                print('Error, must be string text.')
                continue
            return input_value.capitalize()

    # Function to insert a new player in DB
    @classmethod
    def insert_new_player(cls):
        p_firstname = cls.check_player_info("Firstname")
        p_lastname = cls.check_player_info("Lastname")
        p_birthdate = cls.set_player_birthdate()
        p_ladder = cls.set_player_ladder()
        p_gender = cls.set_player_gender()

        # Creating new instance of our player with inputs data
        new_player = model.playermodel(lastname=p_lastname, firstname=p_firstname, birthdate=p_birthdate, gender=p_gender, ladder=p_ladder, points=0)

        # Formatting our player into a json object
        serialized_player = {
            "lastname": new_player.lastname,
            "firstname": new_player.firstname,
            "birthdate": new_player.birthdate,
            "gender": new_player.gender,
            "ladder": new_player.ladder,
            "points": new_player.points
        }

        # Sending the jsonified player in our model for insert in DB
        result = model.playermodel.insert_new_player(serialized_player)

        # Displaying the new created player
        view.View.show_new_player_created(result)

        return result

