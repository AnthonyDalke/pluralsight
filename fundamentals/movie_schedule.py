current_movies = {
    "The Grinch": "11:00 AM",
    "Rudolph": "1:00 PM",
    "Frosty the Snowman": "3:00 PM",
    "Christmas Vacation": "5:00 PM",
}

print(f"We currently show the following movies:")
for key in current_movies:
    print(key)

movie = input(f"Which movie's showtime do you want?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print(f"We don't have the requested movie.")
else:
    print(f"{movie} plays at {showtime}.")
