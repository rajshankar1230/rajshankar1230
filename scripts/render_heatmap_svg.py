import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

def render_heatmap():
    with open("data/contributions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data["days"]
    box_size = 11
    gap = 4
    start_x, start_y = 30, 45
    width = 860
    height = 180

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">']
    svg.append('<style>')
    svg.append('  .cell { opacity: 0; transform: translateY(-3px); animation: dropIn 0.3s forwards ease-out; }')
    svg.append('  @keyframes dropIn { to { opacity: 1; transform: translateY(0); } }')
    svg.append('</style>')
    svg.append(f'<rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d"/>')
    svg.append('<text x="30" y="28" font-family="monospace" font-size="12" fill="#58a6ff">&gt; git log --heatmap --year</text>')

    for idx, day in enumerate(days):
        col = idx // 7
        row = idx % 7
        x = start_x + col * (box_size + gap)
        y = start_y + row * (box_size + gap)
        color = PALETTE[day["level"]]
        delay = round((col + row) * 0.015, 3)

        svg.append(
            f'<rect class="cell" x="{x}" y="{y}" width="{box_size}" height="{box_size}" '
            f'fill="{color}" rx="2" style="animation-delay: {delay}s;" />'
        )

    svg.append('</svg>')
    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("Generated contrib-heatmap.svg")

if __name__ == "__main__":
    render_heatmap()
