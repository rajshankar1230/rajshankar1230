import sys
import os
from PIL import Image, ImageEnhance

# Character ramp from sparse (bright background) to dense (dark details)
RAMP = " .`:-=+*cs#%@"

def generate_ascii_svg(image_path="source-photo.jpg", output_path="avi-ascii.svg", cols=70):
    if not os.path.exists(image_path):
        print(f"Error: Could not find '{image_path}'. Place your image in the project root first.")
        return

    # 1. Open and convert to grayscale
    img = Image.open(image_path).convert("L")

    # 2. Boost contrast so features stand out
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.8)

    # 3. Resize to terminal grid dimensions (0.55 compensates for monospace font height)
    w, h = img.size
    aspect_ratio = h / w
    rows = int(cols * aspect_ratio * 0.55)
    img = img.resize((cols, rows), Image.Resampling.LANCZOS)

    # 4. Map pixel brightness values to ASCII glyphs
    ascii_lines = []
    for y in range(rows):
        line = ""
        for x in range(cols):
            val = img.getpixel((x, y))
            idx = int(val / 256 * len(RAMP))
            line += RAMP[idx]
        ascii_lines.append(line)

    # 5. Build self-typing SVG layout
    char_w, line_h = 7.2, 13
    svg_w = int(cols * char_w + 30)
    svg_h = int(rows * line_h + 30)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">'
    ]
    svg.append('<style>')
    svg.append('  .term-text { font-family: "Courier New", monospace; font-size: 11px; fill: #58a6ff; white-space: pre; }')
    svg.append('  .row { opacity: 0; animation: typeRow 0.05s forwards; }')
    svg.append('  @keyframes typeRow { to { opacity: 1; } }')
    svg.append('</style>')
    svg.append(f'<rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d"/>')

    for i, line in enumerate(ascii_lines):
        delay = round(i * 0.035, 3)
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg.append(f'<text x="15" y="{25 + i * line_h}" class="term-text row" style="animation-delay: {delay}s;">{escaped_line}</text>')

    svg.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path} successfully.")

if __name__ == "__main__":
    img_file = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    generate_ascii_svg(img_file)
