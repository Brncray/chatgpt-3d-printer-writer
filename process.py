import svgwrite

def generate_svg(text, filename="output.svg"):

    dwg = svgwrite.Drawing(filename, size=(200, 50))
    dwg.add(dwg.text(text, insert=(10, 40), font_size='10px', font_family='Arial'))
    dwg.save()
    print(f"SVG saved as {filename}")

generate_svg("Lorem ipsum dolor sit amet")
