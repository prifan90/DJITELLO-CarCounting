import tellopy
import pygame
import time

# Inisialisasi pygame
pygame.init()

class DroneController:
    def __init__(self):
        # Inisialisasi drone
        # self.drone = tellopy.Tello()
        # self.drone.connect()
        # self.drone.wait_for_connection(60.0)
        # self.altitude = 30 # dalam cm
        self.keys = []

    def run(self):
        try:
            while True:
                # Tangani event keyboard
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.drone.quit()
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        self.keys.append(event.key)
                    elif event.type == pygame.KEYUP:
                        self.keys.remove(event.key)

                # Kontrol drone menggunakan tombol keyboard
                self.handle_keys()
        except Exception as ex:
            print(ex)
        finally:
            # Putuskan koneksi ke drone saat program selesai
            # self.drone.quit()
            pygame.quit()

    def handle_keys(self):
        if pygame.K_UP in self.keys:
            print(pygame.K_UP)
            # self.drone.forward(50)
        # if pygame.K_DOWN in self.keys:
        #     # self.drone.backward(50)
        # if pygame.K_LEFT in self.keys:
        #     # self.drone.left(50)
        # if pygame.K_RIGHT in self.keys:
        #     # self.drone.right(50)
        # if pygame.K_w in self.keys:
        #     # self.drone.up(50)
        # if pygame.K_s in self.keys:
        #     # self.drone.down(50)
        # if pygame.K_a in self.keys:
        #     # self.drone.counter_clockwise(50)
        # if pygame.K_d in self.keys:
        #     # self.drone.clockwise(50)
        # if pygame.K_SPACE in self.keys:
        #     # Jalankan takeoff dengan ketinggian yang telah ditentukan
        #     # self.drone.takeoff(altitude=self.altitude)
        #     self.keys.remove(pygame.K_SPACE)
        # if pygame.K_ESCAPE in self.keys:
        #     # Jalankan landing
        #     # self.drone.land()
        #     self.keys.remove(pygame.K_ESCAPE)

# Jalankan program
controller = DroneController()
controller.run()
