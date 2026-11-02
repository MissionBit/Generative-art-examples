from PIL import Image, ImageDraw
import random

class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        x, y = self.attributes["position"]
        size = self.attributes["size"]
        color = self.attributes["color"]
        draw_context.ellipse([x - size, y - size, x + size, y + size], fill=color)

class Canvas:
    def __init__(self, size, background_color):
        self.image = Image.new("RGB", size, background_color)
        self.draw_context = ImageDraw.Draw(self.image)
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        for element in self.elements:
            element.draw(self.draw_context)
        return self.image

# Step 4: generate_artwork
def generate_artwork():
    canvas = Canvas((500, 500), "black")
    for i in range(50):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        size = random.randint(10, 60)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        info = {"position": [x, y], "size": size, "color": color}
        canvas.add_element(ArtElement(info))
    picture = canvas.render()
    picture.save("my_generative_artwork.png")

generate_artwork()
