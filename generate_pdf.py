import os
import markdown
import webbrowser
from pathlib import Path

def generate_html():
    """Generate HTML from paper.md using markdown"""
    try:
        # Read the markdown file
        with open('paper.md', 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        
        # Create HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>AI-Driven Quantum Software Engineering</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 2cm;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 2cm;
                }}
                pre {{
                    background-color: #f5f5f5;
                    padding: 1em;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                code {{
                    font-family: 'Courier New', monospace;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: #333;
                }}
                a {{
                    color: #0066cc;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .metadata {{
                    color: #666;
                    font-size: 0.9em;
                    margin-bottom: 2em;
                }}
                .authors {{
                    margin: 1em 0;
                }}
                .affiliations {{
                    margin: 1em 0;
                    font-style: italic;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Create output directory
        os.makedirs('output', exist_ok=True)
        
        # Save HTML file
        html_path = 'output/paper.html'
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        print(f"HTML generated successfully at {html_path}")
        print("You can now:")
        print("1. Open the HTML file in your browser")
        print("2. Use your browser's 'Print to PDF' function to save as PDF")
        
        # Open the HTML file in the default browser
        webbrowser.open(html_path)
        
    except Exception as e:
        print(f"Error generating HTML: {e}")
        raise

if __name__ == '__main__':
    generate_html() 