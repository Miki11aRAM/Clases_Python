#Las clases son las que tienen hijos y la subclase es el hijo que hereda de las superclase por ende es su hijo
class GameSprite()
    def _init_(self, Player_image, player_x, player_y, player_speed):

        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed

        self.rect
