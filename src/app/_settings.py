"""
This file is for web application settings

Author: Amir Mofakhar <pangan@gmail.com>
"""

SERVER_BASE_ADDRESS = 'http://localhost'
SERVER_PORT = 80
SHORT_ADDRESS_LIFE_TIME_IN_SECOND = 10000
DATABASE = 'sqlite:///url_shortening.db'
SHORT_ADDRESS_LENGTH = 4
MAX_NUMBER_OF_TRIES_TO_FIND_UNASSIGNED_SHORT_ADDRESS = 100
