import readline

class AnnouncementInterface(object):

    def __init__(self):
        pass

    def get_user_input(self):
        user_input = raw_input('AnnouncementInterface$ ')

    def parse_user_input(self):
        pass

def print_welcome_message():
    print 'Welcome to the AnnouncementInterface interpreter!'
    print '{:>49}'.format('Written by PChan')
    print ''
    print print_help_message()

def print_help_message():
    print 'Type "help" for more information'
    print ''
    print

def main():
    print_welcome_message()
    while True:
        user_input = raw_input('AnnouncementInterface$ ')


if __name__ == '__main__':
    main()
