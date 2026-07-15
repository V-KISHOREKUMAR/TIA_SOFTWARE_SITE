import os
import re

def main():
    service_images = {
        "virtual-assistance.html": "virtual-assistance-services-india.webp",
        "video-motion-graphics.html": "video-production-company-india.webp",
        "ui-ux-design.html": "ui-ux-design-company-india.webp",
        "stories-reels-assets.html": "social-media-video-editing-india.webp",
        "seasonal-festive.html": "festive-graphic-design-packs-india.webp",
        "event-launch-graphics.html": "event-product-launch-branding-india.webp",
        "creative-design.html": "graphic-design-company-india.webp",
        "branding-essentials.html": "branding-logo-design-agency-india.webp",
        "digital-marketing.html": "digital-marketing-agency-india.webp"
    }

    for filename, img_name in service_images.items():
        if not os.path.exists(filename):
            print(f"Skipping {filename} (file not found)")
            continue

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        # Target the Service schema pattern: type Service followed by name
        pattern = re.compile(r'"@type"\s*:\s*"Service"\s*,\s*"name"\s*:\s*"([^"]+)"')
        replacement = f'"@type": "Product",\n    "name": "\\1",\n    "image": "https://tiasoftwaresolutions.site/assets/{img_name}"'

        updated_content = pattern.sub(replacement, content)

        if updated_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Successfully converted Service -> Product and added image schema in {filename}")
        else:
            print(f"No schema updates required or matched in {filename}")

if __name__ == "__main__":
    main()
