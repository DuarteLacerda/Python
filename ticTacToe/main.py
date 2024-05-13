import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load("ticTacToe/assets/Tic_tac_toe.png"))
WINDOW_WITH = 720
PIXEL_WITH = WINDOW_WITH // 3
screen = pygame.display.set_mode((WINDOW_WITH, WINDOW_WITH))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font('ticTacToe/assets/Roboto.ttf', 32)
text = font.render("", True, ("green"))
textRect = text.get_rect()
textRect.center = (WINDOW_WITH // 2 - PIXEL_WITH // 2, WINDOW_WITH // 2)

def load_icons(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, (resolution))

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

icon_x = load_icons("ticTacToe/assets/x.png", [PIXEL_WITH, PIXEL_WITH])
icon_o = load_icons("ticTacToe/assets/o.png", [PIXEL_WITH, PIXEL_WITH])
grid = load_icons("ticTacToe/assets/grid.png", [WINDOW_WITH, WINDOW_WITH])
player_1 = 0
player_2 = 1
player = player_1

    
screen.blit(grid, (0, 0))
    
def play_turn(current_player):
    current_pos = pygame.math.Vector2(pygame.mouse.get_pos()) // PIXEL_WITH
    if (pygame.mouse.get_pressed()[0]):
        col, row = map(int, current_pos)
        board[row][col] = 0 if current_player == 0 else 1
        print(board)
        global player
        player = 1 if player == 0 else 0

def draw_icons():
    for i, row in enumerate(board):
        for j, col in enumerate(board[i]):
            if board[i][j] == 0:
                screen.blit(icon_x, (j * PIXEL_WITH, i * PIXEL_WITH))
            elif board[i][j] == 1:
                screen.blit(icon_o, (j * PIXEL_WITH, i * PIXEL_WITH))

def has_equal_icons(elements, game_player):
    for element in elements:
        if element != game_player:
            return False
    return True
    
def has_winning_row(player):
    return has_equal_icons(board[0], player) \
    or has_equal_icons(board[1], player) \
    or has_equal_icons(board[2], player)

def has_winning_col(player):
    return has_equal_icons([board[0][0], board[1][0], board[2][0]], player) \
    or has_equal_icons([board[0][1], board[1][1], board[2][1]], player) \
    or has_equal_icons([board[0][2], board[1][2], board[2][2]], player)

def has_winning_diagonal(player):
    return has_equal_icons([board[0][0], board[1][1], board[2][2]], player) \
    or has_equal_icons([board[0][2], board[1][1], board[2][0]], player)

def is_winner(player):
    return has_winning_row(player) \
    or has_winning_col(player) \
    or has_winning_diagonal( player)

def check_victory():
    global text
    if is_winner(player_1):
        text = font.render("Player 1 wins!", True, ("green"))
        return True
    elif is_winner(player_2):
        text = font.render("Player 2 wins!", True, ("green"))
        return True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # RENDER YOUR GAME HERE
    pygame.display.flip()
    screen.fill("white")
    screen.blit(grid, (0, 0))
    play_turn(player)
    pygame.event.wait()
    draw_icons()
    if check_victory():
        screen.blit(text, textRect)
pygame.quit()