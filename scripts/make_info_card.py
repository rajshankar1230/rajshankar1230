def make_card(output_path="info-card.svg"):
    rows = [
        ("user", "rajshankar1230@github"),
        ("os", "Windows / Linux"),
        ("stack", "Python, Git, Web"),
        ("focus", "Software Development"),
        ("editor", "VS Code"),
        ("status", "Building cool things")
    ]

    width, height = 490, 360
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">']
    svg.append('<style>')
    svg.append('  .title { font-family: monospace; font-size: 14px; font-weight: bold; fill: #58a6ff; }')
    svg.append('  .key { font-family: monospace; font-size: 12px; fill: #7ee787; font-weight: bold; }')
    svg.append('  .val { font-family: monospace; font-size: 12px; fill: #c9d1d9; }')
    svg.append('  .line { opacity: 0; animation: fadeIn 0.4s forwards; }')
    svg.append('  @keyframes fadeIn { to { opacity: 1; } }')
    svg.append('</style>')
    svg.append(f'<rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d"/>')
    svg.append('<text x="20" y="35" class="title">&gt; neofetch --minimal</text>')
    svg.append('<line x1="20" y1="48" x2="470" y2="48" stroke="#30363d" />')

    for i, (k, v) in enumerate(rows):
        delay = round(0.2 + i * 0.1, 2)
        y = 80 + i * 36
        svg.append(f'<g class="line" style="animation-delay: {delay}s;">')
        svg.append(f'  <text x="20" y="{y}" class="key">{k}:</text>')
        svg.append(f'  <text x="100" y="{y}" class="val">{v}</text>')
        svg.append('</g>')

    svg.append('</svg>')
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

if __name__ == "__main__":
    make_card()
