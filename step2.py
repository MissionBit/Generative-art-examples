# Step 1: set up
from PIL import Image, ImageDraw

# Step 2: the ArtElement class
class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        x, y = self.attributes["position"]
        size = self.attributes["size"]
        color = self.attributes["color"]
        # top-left corner = position minus size, bottom-right = position plus size
        draw_context.ellipse([x - size, y - size, x + size, y + size], fill=color)

# Draw and save the first picture
image = Image.new("RGB", (200, 200), "white")
draw_context = ImageDraw.Draw(image)

circle_info = {"position": [100, 100], "size": 50, "color": "purple"}
circle = ArtElement(circle_info)
circle.draw(draw_context)

image.save("ellipse_first.jpeg")
