def story_selector():
    while True:
        story_select = input('Choose a number for preferred story theme [1 for funny, 2 for scary or 3 for adventure: ').lower()
        if story_select in ['one', 'two', 'three']:
            int_story_select = {'one': 1, 'two': 2, 'three': 3}[story_select]
            print(f"You selected story {int_story_select}")
            madlib_story(int_story_select)
            return #int_story_select
        elif story_select.isdigit():
            int_story_select = int(story_select)
            if 1 <= int_story_select <= 3:
                print(f"You selected story {int_story_select}")
                madlib_story(int_story_select)
                return #int_story_select
            else:
                print('Your choice have to be a number between one and three [1, 2 or 3].')
        else:
            print('Invalid input. Please enter a number between one and three [1, 2 or 3].') 
def madlib_story(choice):
    if choice == 1:
        object = input('Enter an object: ')
        name = input('Enter a name: ')
        story = 'During my data science bootcamp, I got bored so I decided to go to my friend ' + name.capitalize() + ' so I had to leave to buy ' + object + '.'
        print('Funny Story:')
        print(story)
    elif choice == 2:
        object = input('Enter an object')
        name = input('Enter a name: ')
        story = 'I went to the GYM, I met by change my friend ' + name.capitalize() + ' so I had to leave to buy ' + object + '.'
        print('Funny Story:')
        print(story)
    else:
        object = input('Enter an object: ')
        name = input('Enter a name: ')
        story = 'During my GP appointment, I met my friend ' + name.capitalize() + ' and left behind ' + object + '.'
        print('Adventure Story:')
        print(story)
story_selector()