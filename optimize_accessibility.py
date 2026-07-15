import os
import re

def replace_font_link(match):
    url = match.group(1) or match.group(2)
    return (
        f'<link rel="preload" as="style" href="{url}" />\n'
        f'  <link href="{url}" rel="stylesheet" media="print" onload="this.media=\'all\'" />\n'
        f'  <noscript><link href="{url}" rel="stylesheet" /></noscript>'
    )

def main():
    # Regex to find Google Fonts link
    font_link_regex = re.compile(
        r'<link\s+[^>]*href=["\'](https://fonts\.googleapis\.com/css2\?[^"\']+)["\'][^>]*rel=["\']stylesheet["\'][^>]*>|'
        r'<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\'](https://fonts\.googleapis\.com/css2\?[^"\']+)["\'][^>]*>',
        re.DOTALL
    )

    html_files = [f for f in os.listdir(".") if f.endswith(".html")]

    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content = content

        # 1. Optimize Google Fonts loading
        updated_content = font_link_regex.sub(replace_font_link, updated_content)

        # 2. Fix heading structure issues
        if file_path in ["index.html", "about.html"]:
            # Promote all h4 to h3 in these files (specifically for .about-vm-card and .why-card)
            updated_content = updated_content.replace("<h4>", "<h3>").replace("</h4>", "</h3>")
            print(f"Fixed heading structure (h4 -> h3) in {file_path}")

        elif file_path == "process.html":
            # Change timeline card h3 headings to h2
            updated_content = re.sub(
                r'<div class="card-content">\s*<h3>(.*?)</h3>',
                r'<div class="card-content">\n              <h2>\1</h2>',
                updated_content
            )
            # Update inline CSS selector from h3 to h2
            updated_content = updated_content.replace(".card-content h3 {", ".card-content h2 {")
            print(f"Fixed timeline heading structure (h3 -> h2) and inline CSS in {file_path}")

        elif file_path == "faq.html":
            # Change FAQ question h3 headings to h2
            updated_content = re.sub(
                r'<h3 style="font-family: var\(--font-syne\);([^"]+)">\s*(.*?)\s*</h3>',
                r'<h2 style="font-family: var(--font-syne);\1">\2</h2>',
                updated_content
            )
            print(f"Fixed FAQ heading structure (h3 -> h2) in {file_path}")

        if updated_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Optimized Accessibility in: {file_path}")
        else:
            print(f"No changes needed for accessibility in: {file_path}")

if __name__ == "__main__":
    main()
