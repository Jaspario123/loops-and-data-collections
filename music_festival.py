artist_count = {}

while True:
    artist = input("Enter a Musician: ")
    if artist.lower() == 'done':
        break
    
    artist_count[artist.lower()] = artist_count.get(artist.lower(), 0) + 1
artist_list = [artist.lower() for artist in artist_count.keys()]
artist_list.sort()
print("\n Votes:")
for artist in artist_list:
    print(artist, ":", artist_count[artist])