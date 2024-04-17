import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((300, 100))
        pygame.display.set_caption("Music Player")
        self.clock = pygame.time.Clock()
        self.music_dir = r"C:\Users\ayush\Music"
  # Replace "your_music_directory" with your actual music directory
        self.playlist = os.listdir(self.music_dir)
        self.current_track_index = 0

    def play_music(self):
        pygame.mixer.music.load(os.path.join(self.music_dir, self.playlist[self.current_track_index]))
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.stop_music()
        self.play_music()

    def prev_track(self):
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.stop_music()
        self.play_music()

    def run(self):
        self.play_music()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pygame.mixer.music.get_busy():
                            self.pause_music()
                        else:
                            self.unpause_music()
                    elif event.key == pygame.K_n:
                        self.next_track()
                    elif event.key == pygame.K_p:
                        self.prev_track()
                    elif event.key == pygame.K_s:
                        self.stop_music()
            self.clock.tick(30)
        pygame.quit()

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
