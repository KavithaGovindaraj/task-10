class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def audio_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

    def __str__(self):
        return f"Audio(name={self.name}, url={self.url}, average_rating={self.audio_average_rating()})"


class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def playlist_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

    def __str__(self):
        return f"Playlist(name={self.name}, genre={self.genre}, average_rating={self.playlist_average_rating()}, audios={[audio.name for audio in self.audios]})"


class User:
    def __init__(self):
        self.audios = []
        self.playlists = []

    def create_audio(self, name, url):
        audio = Audio(name, url)
        self.audios.append(audio)
        return audio

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def add_audio_to_playlist(self, audio_name, playlist_name):
        audio = self.search_audio_by_name(audio_name)
        playlist = self.search_playlist_by_name(playlist_name)
        if audio and playlist:
            playlist.add_audio(audio)
            return True
        return False

    def search_audio_by_name(self, name):
        for audio in self.audios:
            if audio.name == name:
                return audio
        return None

    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None

    def rate_audio(self, audio_name, rating):
        audio = self.search_audio_by_name(audio_name)
        if audio:
            audio.add_rating(rating)
            return True
        return False

    def rate_playlist(self, playlist_name, rating):
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist:
            playlist.add_rating(rating)
            return True
        return False

    def display_audios(self):
        for audio in self.audios:
            print(audio)

    def display_playlists(self):
        for playlist in self.playlists:
            print(playlist)


# Example usage
user = User()

# Create audios
audio1 = user.create_audio("Song1", "http://example.com/song1")
audio2 = user.create_audio("Song2", "http://example.com/song2")

# Create playlists
playlist1 = user.create_playlist("Playlist1", "Rock")
playlist2 = user.create_playlist("Playlist2", "Pop")

# Add audios to playlists
user.add_audio_to_playlist("Song1", "Playlist1")
user.add_audio_to_playlist("Song2", "Playlist2")

# Rate audios
user.rate_audio("Song1", 5)
user.rate_audio("Song1", 4)
user.rate_audio("Song2", 3)

# Rate playlists
user.rate_playlist("Playlist1", 4)
user.rate_playlist("Playlist2", 5)

# Display audios and playlists
user.display_audios()
user.display_playlists()

Output:

Audio(name=Song1, url=http://example.com/song1, average_rating=4.5)
Audio(name=Song2, url=http://example.com/song2, average_rating=3.0)
Playlist(name=Playlist1, genre=Rock, average_rating=4.0, audios=['Song1'])
Playlist(name=Playlist2, genre=Pop, average_rating=5.0, audios=['Song2'])