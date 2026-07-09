import os
import re
import subprocess

def run_cmd(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr}")
    else:
        print("Success")
    return res.returncode == 0

def main():
    # 1. Minify CSS
    css_ok = run_cmd("npx --yes clean-css-cli -o style.min.css style.css")
    
    # 2. Minify JS
    js_ok = run_cmd("npx --yes terser script.js -o script.min.js --compress --mangle")
    
    if not (css_ok and js_ok):
        print("Asset minification failed. Aborting HTML replacement.")
        return

    # 3. Update HTML files
    html_files = [f for f in os.listdir(".") if f.endswith(".html")]
    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace style.css with style.min.css
        updated_content = re.sub(
            r'href=["\']style\.css["\']',
            'href="style.min.css"',
            content
        )

        # Replace script.js with script.min.js defer
        updated_content = re.sub(
            r'<script\s+src=["\']script\.js["\']\s*></script>',
            '<script src="script.min.js" defer></script>',
            updated_content
        )

        # Add aria-label to hamburger button for accessibility
        updated_content = re.sub(
            r'<button\s+class=["\']hamburger["\']\s+id=["\']hamburger["\']\s*>',
            '<button class="hamburger" id="hamburger" aria-label="Toggle navigation menu">',
            updated_content
        )

        if updated_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Optimized HTML: {file_path}")
        else:
            print(f"No changes needed for: {file_path}")

if __name__ == "__main__":
    main()
