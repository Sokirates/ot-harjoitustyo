#import unittest
#from unittest.mock import MagicMock
#from src.services.gameloop import *
#from src.ui.game_view import *
#import pygame
#
#
#class TestStartGame(unittest.TestCase):
#    def setUp(self):
#        self.mock_screen = MagicMock()
#        self.width = 800
#    
#    def test_start_game(self):
#        # Stub Pygame functions
#        pygame.font.SysFont = MagicMock(return_value=MagicMock())
#        
#        start_game(self.mock_screen, self.width)
#        
#        # Assert that the start screen was drawn
#        self.mock_screen.fill.assert_called_once()  # Example assertion, adjust as needed
#        
#        game_loop.assert_called_once_with(
#            self.mock_screen, False, pygame.time.Clock(), MagicMock(), MagicMock(), self.width
#        )