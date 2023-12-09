





win_width =
win_height =
window = (win_width,win_height)
#Procesamiento de eventos
for event in pygme.event.get():
    if event.type == pygame.QUIT
    run = False
    # flecha presionada
    if event.type == pygame.KEYDOWN:
        shift += speed
        local_shift = shift % win_width
    if event.key == pygame.K_LEFT:
        speed = -5
        elif event.key == pygame.K_RIGHT
        speed = 5
    #Flecha liberada
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            speed = 0
        elif event.key == pygame.K_RIGHT:
            speed = 0

