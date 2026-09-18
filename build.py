import os
import json

def build_website():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Last and Found</title>
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; }
            .item { border: 1px solid #ccc; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
            .Lost { border-left: 5px solid #ff4d4d; }
            .Found { border-left: 5px solid #2ecc71; }
        </style>
    </head>
    <body>
        <h1>🕵️‍♂️ Last and Found</h1>
        <p>A community-controlled board. Submit a Pull Request to add an item!</p>
        <div id="items">
    """

    items_dir = "items"
    if os.path.exists(items_dir):
        for filename in sorted(os.listdir(items_dir), reverse=True):
            if filename.endswith(".json"):
                with open(os.path.join(items_dir, filename), "r") as f:
                    try:
                        data = json.load(f)
                        html_content += f"""
                        <div class="item {data.get('status', 'Lost')}">
                            <h3>{data.get('title', 'Untitled')} ({data.get('status', 'Unknown')})</h3>
                            <p>{data.get('description', '')}</p>
                            <small>Reported by: {data.get('reported_by', 'Anonymous')}</small>
                        </div>
                        """
                    except Exception:
                        continue

    html_content += """
        </div>
    </body>
    </html>
    """

    with open("index.html", "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    build_website()
