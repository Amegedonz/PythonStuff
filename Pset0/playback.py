#this problem will insert 3 periods in every space in the input
playback_Input = str(input('Please enter input here:'))
Space = ' '

if Space in playback_Input:
    replaced = playback_Input.replace(' ', '...')
    print(replaced)

else:
    print(playback_Input)