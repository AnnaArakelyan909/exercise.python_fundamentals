# Created by Leon Hunter at 3:57 PM 10/23/2020
# Adding comment to have changes in the file to create pull request
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World" # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        a = str(value_to_be_added_to)
        b = str(value_to_add)
        c = a + b
        return c  # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        string = string_to_fetch_from[starting_index:ending_index+1]
        return string  # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        line = string_to_fetch_from[starting_index+1:ending_index]
        return line  # TODO - Implement solution

    def compare(self, first_value, second_value):
        if str(first_value) == str(second_value):
            return True
        elif first_value == None and second_value == 0:
            return True
        elif first_value == False and second_value == 0:
            return True
        elif first_value == True and second_value == 1:
            return True
        else:
            return False # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        word = string_to_fetch_from.split()
        return word[0]# TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        word2 = string_to_fetch_from.split()
        return word2[1] # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return None # TODO - Implement solution