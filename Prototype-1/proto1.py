def recommendation():
    import pandas as pd
    import random
    df = pd.read_csv('hot_100.csv')
    df = df.drop('Unnamed: 0', axis = 1)
    df['clean_title'] = df['title']
    df['clean_title'] = df['clean_title'].str.lower()
    df['clean_title'] = df['clean_title'].str.replace(" ","")
    df['clean_artist'] = df['artist']
    df['clean_artist'] = df['clean_artist'].str.lower()
    df['clean_artist'] = df['clean_artist'].str.replace(" ","")
    df_sug = df.copy()
    
    suggestion = df_sug['title'].sample(n=1)
    suggestion =  suggestion.to_string(index=False)
    
    title = input('Please enter song title: ').lower()
    title = title.replace(" ","")
    if "".__eq__(title):
        print("Don't forget to enter your Song!")
    else:
        artist = input('Please enter artist: ').lower()
        artist = artist.replace(" ","")
        artist_correct = df.loc[df['clean_artist'].str.contains(artist), 'clean_artist'].to_string(index=False)
        title_correct = df.loc[df['clean_title'].str.contains(title), 'clean_title'].to_string(index=False)
        if artist in artist_correct:
            yoursong = df.loc[df['clean_title'] == title_correct, 'title'].to_string(index=False)
            yourartist = df.loc[df['clean_title'] == title_correct, 'artist'].to_string(index=False)
            df_sug.drop(df_sug.index[df_sug['title'] == title], inplace = True)
            recommendation = suggestion
            artist_sug = df.loc[df['title'] == recommendation, 'artist'].to_string(index=False)   
            if title in title_correct:
                answer = input("Did you mean: "+yoursong+", by "+yourartist+"?\nAnswer by 'yes' or 'no': ")
                if answer == 'yes':
                    print("\nBased on the song:", yoursong+", by "+yourartist+",")
                    print("here is another Billboard Hot 100 song:", recommendation+", by "+artist_sug)
                elif answer == 'no':
                    print("\nI'm sorry to hear that! Maybe check your spelling or specify the title more exactly next time :)")
                else:
                    print("\nPlease confirm your answer by either typing 'yes' or 'no'!")
            else:
                print("\nYour Song is not under the Billboard Hot 100 list! If you think it is, maybe check the spelling!")
        else:
            print("\nMake sure your artist fits the song! If you're unsure about the artist's name, just leave it blank :)") 