def recommendation():
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.cluster import KMeans
    import random
    from IPython.core.display import display
    from IPython.display import IFrame
    df = pd.read_csv('final_hot100.csv')
    df = df.drop('Unnamed: 0', axis = 1)
    df_sug = df.copy()
    df_pop = pd.read_csv('pop_songs_cluster.csv')
    df_pop = df_pop.drop('Unnamed: 0', axis = 1)
    df_pop_sug = df_pop.copy()
    
    title = input('Please enter song title: ').lower()
    title = title.replace(" ","")
    if "".__eq__(title):
        print("Don't forget to enter your Song!")
    else:
        artist = input('Please enter artist: ').lower()
        artist = artist.replace(" ","")
        artist_correct = df.loc[df['clean_artist'].str.contains(artist), 'clean_artist'].to_string(index=False)
        title_correct = df.loc[df['clean_title'].str.contains(title), 'clean_title'].to_string(index=False)
        songname_pop_correct = df_pop.loc[df_pop['clean_songname'].str.contains(title), 'clean_songname'].sample(n=1).to_string(index=False)
        artist_pop_correct = df_pop.loc[df_pop['clean_songname'] == songname_pop_correct, 'clean_artist'].sample(n=1).to_string(index=False)
        if artist in artist_correct or artist_pop_correct:
            yoursong = df.loc[df['clean_title'] == title_correct, 'title'].to_string(index=False)
            yourartist = df.loc[df['clean_title'] == title_correct, 'artist'].to_string(index=False)
            df_sug.drop(df_sug.index[df_sug['title'] == yoursong], inplace = True)
            suggestion = df_sug['title'].sample(n=1)
            suggestion =  suggestion.to_string(index=False)
            recommendation = suggestion
            artist_sug = df.loc[df['title'] == recommendation, 'artist'].to_string(index=False)   
            if title in title_correct:
                answer = input("Did you mean: "+yoursong+", by "+yourartist+"?\nAnswer by 'yes' or 'no': ")
                if answer == 'yes':
                    print("\nBased on the song:", yoursong+", by "+yourartist+",")
                    print("here is another Billboard Hot 100 song:", recommendation+", by "+artist)
                elif answer == 'no':
                    print("\nI'm sorry to hear that! Maybe check your spelling or specify the title more exactly next time :)")
                else:
                    print("\nPlease confirm your answer by either typing 'yes' or 'no'!")
            else:
                yoursong = df_pop.loc[df_pop['clean_songname'] == songname_pop_correct, 'songname'].to_string(index=False)
                yourartist = df_pop.loc[df_pop['clean_artist'] == artist_pop_correct, 'artist'].to_string(index=False)
                df_pop_sug.drop(df_pop_sug.index[df_pop_sug['songname'] == yoursong], inplace = True)
               
                if title in songname_pop_correct:
                    answer = input("Did you mean: "+yoursong+", by "+yourartist+"?\nAnswer by 'yes' or 'no': ")
                    if answer == 'yes':
                        yoursong_cluster = df_pop.loc[df_pop['songname'] == yoursong, 'cluster'].to_string(index=False) 
                        suggestion_pop = df_pop_sug.loc[df_pop['cluster'] == int(yoursong_cluster), 'id'].sample(n=1)
                        suggestion_pop =  suggestion_pop.to_string(index=False)
                        recommendation_pop = suggestion_pop
                        artist_pop_sug = df_pop.loc[df_pop['songname'] == recommendation_pop, 'artist'].to_string(index=False)
                        print("\nBased on your song:", yoursong+", by "+yourartist+",")
                        print("here is another pop song you should like: ") 
                        display(IFrame(src=f"https://open.spotify.com/embed/track/"+str(recommendation_pop), width="500",height="100", frameborder="10", allowtransparency="true", allow="encrypted-media"))
                    elif answer == 'no':
                        print("\nI'm sorry to hear that! Maybe check your spelling or specify the title more exactly next time :)")
                    else:
                        print("\nPlease confirm your answer by either typing 'yes' or 'no'!")
                else:
                    print("\n I was unable to find your song :( Have you made sure your spelling is correct, and the pop song is from the 2000s?")
        else:
            print("\nMake sure your artist fits the song! If you're unsure about the artist's name, just leave it blank :)") 