import os
import re

def main():
    # Target replacements:
    # 1. https://www.tiasoftwaresolutions.com -> https://tiasoftwaresolutions.site
    # 2. www.tiasoftwaresolutions.com -> tiasoftwaresolutions.site
    # 3. tiasoftwaresolutions.com -> tiasoftwaresolutions.site
    
    old_domain_pattern = re.compile(r'(https://)?(www\.)?tiasoftwaresolutions\.com', re.IGNORECASE)
    
    def replacement_func(match):
        protocol = match.group(1) if match.group(1) else ""
        return f"{protocol}tiasoftwaresolutions.site"

    # Update sitemap.xml
    sitemap_path = "sitemap.xml"
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        updated_content = old_domain_pattern.sub(replacement_func, content)
        
        if updated_content != content:
            with open(sitemap_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated: {sitemap_path}")
        else:
            print(f"No changes needed for: {sitemap_path}")

    # Update HTML files
    html_files = [f for f in os.listdir(".") if f.endswith(".html")]
    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content = old_domain_pattern.sub(replacement_func, content)

        if updated_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated domain in: {file_path}")
        else:
            print(f"No changes needed for: {file_path}")

if __name__ == "__main__":
    main()
