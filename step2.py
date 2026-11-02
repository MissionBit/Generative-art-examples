from PIL import Image, ImageDraw

class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        x, y = self.attributes["position"]
        size = self.attributes["size"]
        color = self.attributes["color"]
        draw_context.ellipse([x - size, y - size, x + size, y + size], fill=color)

# Step 3: the Canvas class
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

# Draw and save the second picture
canvas = Canvas((200, 200), "white")
circle = ArtElement({"position": [100, 100], "size": 50, "color": "purple"})
canvas.add_element(circle)
picture = canvas.render()
picture.save("ellipse_second.jpeg")
