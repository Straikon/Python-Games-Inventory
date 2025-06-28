class VideoGame:
    def __init__(self, name, platforms, release_date, developers, publishers, genres):
        """
        Inicializa un videojuego con todos sus campos principales.
        """
        self.name = name
        self.platforms = platforms
        self.release_date = release_date
        self.developers = developers
        self.publishers = publishers
        self.genres = genres

    def __str__(self):
        """
        Devuelve una representación legible del objeto cuando uses print().
        """
        return (
            f"🎮 {self.name}\n"
            f"📅 Fecha de estreno: {self.release_date}\n"
            f"🕹️ Plataformas: {', '.join(self.platforms)}\n"
            f"🎭 Géneros: {', '.join(self.genres)}\n"
            f"🏢 Desarrolladora(s): {', '.join(self.developers)}\n"
            f"🚚 Distribuidora(s): {', '.join(self.publishers)}\n"
        )

