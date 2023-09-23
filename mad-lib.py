def story_selector():
    while True:
        story_select = input('Choose a number for preferred story theme [1 for funny, 2 for scary or 3 for medical: ').lower()
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
        verb = input('Enter a verb: ')
        name = input('Enter a name: ')
        object = input('Enter a small object: ')
        story = 'During my data science bootcamp, I got bored so I decided to ' + verb + ' I saw my neighbour ' + name.capitalize() + ' driving by so I decided to throw my ' + object + '.'
        print('Here is your funny story:')
        print(story)
    elif choice == 2:
        beverage = input('Enter your favorite drink: ')
        name = input('name of a singer: ')
        story = 'I went to the GYM, by chance I saw an old friend of mine ' + name.capitalize() + ' so sat in a cafe to drink ' + beverage + '.'
        print('Here is your scary story:')
        print(story)
    else:
        object = input('Enter a small object: ')
        name = input('Enter a name: ')
        story = 'During my GP appointment, I saw Dr ' + name.capitalize() + ' it turned out that I have swallowed  ' + object + '.'
        print('Here is your medical story:')
        print(story)
story_selector()