import pygame, sys, random
skier_images = ["skier_down.png", "skier_right1.png",
                "skier_right2.png","skier_left2.png"
                "skier_left1.pong"]

class SkierClass(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320,100]
        self.angle = 0

    def turn(self, direction) :
        self.angle = self.angle + direction
        if self.angle < -2: self.angle = -2
        if self.angle > 2: self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
    
    def move(self, speed) :
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

class ObstaClass(pygame.sprite.Sprite): 
    def __init__(self, image_flie,location, obs_type) :
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image_file = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.obs_type = obs_type
        self.passed = False

    def update(self) :
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery < -32 :
            self.kill()

def create_map() :
    global obstcles
    location = []
    for i in range(10) :
        row = randow.randint(0, 9)
        cil = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20 +640]
        if not (location in locations) :
            locations.append(location)
            obs_type = random.choice(["tree", "flag"])
            if obs_type == "tree": img = "skier_tree.pong"
            elif obs_type == "flag": img = "skier_flag.png"       
            obstacle = ObstacleCleClass(img, location, obs_type)

def animate():
    screen.fill([255, 255, 255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
obstacles = pygme.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None, 50)


running = True
while running:
    click.trck(30)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed = skier.turn(-1)
            elif even.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)
    
    map_position += speed[1]

    if map_position >= 640:
        create_map()
        map_position = 0

    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    if hit :
        if hit[0].obs_type == "tree" and not hit[0].passed:
            points = points - 100
            skier.image = pygame.image.load("skier_crash.pong") 
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.image.load("skier_down.png")
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].obs_type == "flag" and not hit[0].passed:
            points += 10
            hit[0].kill()

    obstacles.update()
    score_text = font.render("score: " + str(points), 1, (0,0,0))
    animate()
pygame.quit()