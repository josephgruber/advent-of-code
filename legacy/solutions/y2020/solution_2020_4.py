import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + '/')  # NOQA: E402

from lib.helper import execution_timer, read_input  # pylint: disable=import-error,no-name-in-module # NOQA: E402


@execution_timer
def validate_passports(data, enhanced_security):
    valid_passports = 0

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    ignored_fields = ['cid']
    validate_fields = [field for field in required_fields if field not in ignored_fields]

    for passport in data.split('\n\n'):
        passport_fields = passport.replace('\n', ' ').split()

        if all(field in ''.join(passport_fields) for field in validate_fields):
            if enhanced_security:
                valid = True

                for field in passport_fields:
                    field_name, field_value = field.split(':')

                    if field_name == 'byr' and int(field_value) not in range(1920, 2003):
                        valid = False
                        break

                    if field_name == 'iyr' and int(field_value) not in range(2010, 2021):
                        valid = False
                        break

                    if field_name == 'eyr' and int(field_value) not in range(2020, 2031):
                        valid = False
                        break

                    if field_name == 'ecl' and field_value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        valid = False
                        break

                    if field_name == 'hgt':
                        if field_value[-2:] not in ['cm', 'in']:
                            valid = False
                            break

                        if field_value[-2:] == 'cm' and int(field_value[:-2]) not in range(150, 194):
                            valid = False
                            break

                        if field_value[-2:] == 'in' and int(field_value[:-2]) not in range(59, 77):
                            valid = False
                            break

                    if field_name == 'hcl' and (field_value[0] != '#' or
                                                len(field_value[1:]) != 6 or
                                                not all(char in
                                                        ['0', '1', '2', '3', '4', '5', '6', '7',
                                                            '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
                                                        for char in field_value[1:])):
                        valid = False
                        break

                    if field_name == 'pid' and not (len(field_value) == 9 and field_value.isdigit()):
                        valid = False
                        break

                if valid:
                    valid_passports += 1
            else:
                valid_passports += 1

    return valid_passports


def main():
    puzzle_input = read_input('2020_4.txt')

    print(f'Part 1: {validate_passports(puzzle_input, False)}\n')
    print(f'Part 2: {validate_passports(puzzle_input, True)}')


if __name__ == '__main__':
    main()
