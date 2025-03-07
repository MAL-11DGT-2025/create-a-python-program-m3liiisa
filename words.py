season = input('What is your favourite season: ')

season_list = ['summer', 'winter', 'autumn', 'spring']

if season.lower().strip() in season_list:  #.lower() is used so user is allowed to input answer in upper case  #.strip() is used so that user is allowed to input space before answer.
    print('That is a valid season')
else:
    print('That is not a valid season.')

