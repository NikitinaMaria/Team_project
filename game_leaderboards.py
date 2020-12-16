def save_score(txt):
    try:
        # Write the file to disk
        file = open("leaderboards.txt", "a+")
        file.write(txt + '\n' )
        file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")
