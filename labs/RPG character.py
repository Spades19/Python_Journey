full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    # 1. Name Validation
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name.strip() == '':  # .strip() handles empty strings and just spaces
        return 'The character should have a name'
    if ' ' in name:
        return 'The character name should not contain spaces'
    if len(name) > 9:  # Check if length is greater than 9
        return 'The character name is too long'

    # 2. Stat Validation (Grouping them for easy checking)
    all_stats = (strength, intelligence, charisma)

    for stat in all_stats:
        if not isinstance(stat, int):
            return 'All stats should be integers'
        if stat < 1:
            return 'All stats should be no less than 1'
        if stat > 4:
            return 'All stats should be no more than 4'

    if sum(all_stats) != 7:
        return 'The character should start with 7 points'

   # 3. Success! Create the "Dots" representation
    # We multiply the dot characters by the numbers directly
    str_dots = (full_dot * strength) + (empty_dot * (10 - strength))
    int_dots = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_dots = (full_dot * charisma) + (empty_dot * (10 - charisma))

    # The lab specifically asked for a string with four lines, not a dictionary!
    return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"


# Testing it out
print(create_character("Uriel", 2, 3, 2))


# L3
# full_dot = '●'
# empty_dot = '○'


# def create_character(name, strength, intelligence, charisma):
# wrong  def stats(int) : strength , intelligence , charisma
# need to use a tuple to check
# full_dot * strength + empty_dot *()
# if not isinstance(name, str):
#   return 'The character name should be a string'
# elif name == '':
#   return 'The character should have a name'
# not using ' ' + name + ' '
# elif ' ' in name:
#    return 'The character name should not contain spaces'
# elif len(name) > 9:
#   return 'The character name is too long '
# stats = (strength, intelligence, charisma)
# if not all(isinstance(stats, int) for stat in stats):
#    return 'All stats should be integers'
# elif any(stat < 1 for stat in stats):
#    return 'All stats should be no less than 1'
# elif any(stat > 4 for stat in stats):
#    return 'All stats should be no more than 4'
# elif sum(stats) > 7 or sum(stats) < 7:
#      return 'The character should start with 7 points'
#   return name, stats

# return {'Character_Name:',name 'STR:',strength}
# print(create_character('ren', 1, 2, 8))
# elif sum(stats)>7 :
#    return 'The character should start with 7 points'
# elif sum(stats)<7 :
#   return 'The character should start with 7 points'
# print('*'*7)
# need to print dot to represent charcter stats
