import pygame
import requests
import sys
import os


def print_image():
    response = None
    coordinates = [37.530887, 55.703118]
    mashtab = [0.002, 0.002]
    try:
        mashtab = ','.join([str(i) for i in mashtab])
        coordinates = ','.join([str(i) for i in coordinates])
        map_request = "http://static-maps.yandex.ru/1.x/?ll=" + coordinates + "&spn=" + mashtab + "&l=map"
        response = requests.get(map_request)    
        if not response:
            print("������ ���������� �������:")
            print(geocoder_request)
            print("Http ������:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
    except:
        print("������ �� ������� ���������. ��������� ������� ���� ��������.")
        sys.exit(1)
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("������ ������ ���������� �����:", ex)
        sys.exit(2)
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    os.remove(map_file)