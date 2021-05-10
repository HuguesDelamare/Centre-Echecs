import view
import model
import datetime
import string


class PlayerController(object):
    @classmethod
    def set_player_birthdate(cls):
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

    @classmethod
    def get_all_players_in_db(cls):
        count = 0
        players_db_size = model.playermodel.get_player_db_size()

        # Display all players(names and ranks) from database
        while count < players_db_size:
            count += 1
            players = model.playermodel.get_players_by_id(count)
            view.View.display_all_players(count, players)

    # FUNCTION TO PICK THE GENDER OF THE NEW PLAYER
    @classmethod
    def set_player_gender(cls):
        while True:
            player_gender = input('Player gender: [M]ale or [F]emale ?: ')
            if player_gender.lower() == "m" or player_gender == "f":
                return player_gender.capitalize()
            else:
                continue

    # FUNCTION TO SET THE LADDER OF THE NEW PLAYER
    @classmethod
    def set_player_ladder(cls):
        while True:
            ladder_input = int(input('Player ladder: '))
            if type(ladder_input) is int:
                return ladder_input
            else:
                continue
        return ladder_input

    # FUNCTION TO CHECK IF DATA INPUT ARE VALID
    @classmethod
    def check_player_info(cls, input_text_value):
        while True:
            count = 0
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
            # print("Total digit present : ", count)
            return input_value.capitalize()

    @classmethod
    def insert_new_player(cls):
        p_firstname = cls.check_player_info("Firstname")
        p_lastname = cls.check_player_info("Lastname")
        p_birthdate = cls.set_player_birthdate()
        p_ladder = cls.set_player_ladder()
        p_gender = cls.set_player_gender()

        # INSERTING INPUT DATA IN PLAYER DB #

        new_player = model.playermodel(lastname=p_lastname, firstname=p_firstname, birthdate=p_birthdate, gender=p_gender, ladder=p_ladder, points=0)

        serialized_player = {
            'lastname': new_player.lastname,
            'firstname': new_player.firstname,
            'birthdate': new_player.birthdate,
            'gender': new_player.gender,
            'ladder': new_player.ladder,
            'points': new_player.points
        }

        result = model.playermodel.insert_new_player(serialized_player)
        view.View.show_new_player_created(result)

        return result

