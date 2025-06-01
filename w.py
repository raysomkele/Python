import pygame
import random

WIDTH, HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock , Paper , Scissors")

WHITE = (255,255,255)
BLACK = (0,0,0)
rock = pygame.image.load("rock.jpg")
scissors = pygame.image.load("sci.jpg")
paper = pygame.image.load("paper.jpg")

rock = pygame.transform.scale(rock,(100,100))
paper = pygame.transform.scale(paper,(100,100))
scissors = pygame.transform.scale(scissors,(100,100))

player_choice = {
    "rock":(50,250)
    "paper":(250,250)
    "scissors":(450,250)
}

computer_choices = ["rock", "paper", "scissors"]

