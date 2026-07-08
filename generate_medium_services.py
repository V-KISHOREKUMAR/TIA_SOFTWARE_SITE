import json
import re
import os

services = [
    {
        "id": "01",
        "filename": "virtual-assistance.html",
        "title": "Virtual Assistance",
        "desc": "Administrative, scheduling & inbox support in India",
        "meta_title": "Virtual Assistant Services in India | TIA Software Solutions",
        "meta_desc": "Top virtual assistant services in India. TIA Software Solutions offers professional admin support, calendar management, and customer service.",
        "schema_name": "Virtual Assistant Services in India",
        "schema_desc": "Professional virtual assistant services in India including admin support, customer service, calendar scheduling, and data entry.",
        "service_type": "Virtual Assistance",
        "breadcrumb_name": "Virtual Assistance",
        "intro_title": "Reliable Virtual Assistance Services in India",
        "intro": "Empower your business with top-tier virtual assistance services in India. We handle the time-consuming administrative tasks, scheduling, and email management so you can focus on scaling your core operations.",
        "image": "assets/virtual-assistance-services-india.webp",
        "img_width": 800,
        "img_height": 450,
        "features": ["Email & Inbox Management", "Calendar & Scheduling", "Customer Support"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Virtual Assistance is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and support that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique needs and objectives. Our collaborative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India virtual assistance experts means expecting transparency, high-quality support, and a commitment to your daily productivity. Whether you need calendar management, billing coordination, or customer support in India, we deliver streamlined solutions tailored to your schedule.",
        "faqs": [
            {
                "q": "What is a virtual assistant (VA)?",
                "a": "A virtual assistant is a remote professional who provides administrative, technical, creative, or customer support services to clients from a remote location."
            },
            {
                "q": "How much does a virtual assistant cost in India?",
                "a": "Our virtual assistance services in India are highly cost-effective, starting at competitive rates customized to your project hours and skill requirements."
            },
            {
                "q": "What tasks can a virtual assistant handle?",
                "a": "Our VAs handle email management, calendar scheduling, customer queries, data entry, social media coordination, research, and invoicing."
            },
            {
                "q": "How do you guarantee data security and confidentiality?",
                "a": "We use secure cloud vaults, sign comprehensive NDAs, and restrict access to authorized team members only to ensure maximum data safety."
            },
            {
                "q": "What are the working hours of your virtual assistants?",
                "a": "Our virtual assistants in India work flexible hours, accommodating Indian Standard Time (IST), UK Greenwich Mean Time (GMT), or US time zones as needed."
            },
            {
                "q": "Do I need to provide software or training for the VA?",
                "a": "No, our virtual assistants are pre-trained in standard office tools (G Suite, Microsoft 365, Slack, Trello). Any proprietary software training is quick and seamless."
            },
            {
                "q": "How do we communicate and track tasks?",
                "a": "We use client-preferred tools like Slack, WhatsApp, email, or Trello, providing daily or weekly progress reports to keep you updated."
            },
            {
                "q": "Can I start with a part-time VA and scale up?",
                "a": "Yes! We offer scalable packages, letting you start with part-time virtual assistance in India and scale to full-time support as your business grows."
            },
            {
                "q": "What is the turnaround time for task completion?",
                "a": "Standard tasks are completed within 24 hours, while urgent requests are prioritized to match your project timeline."
            },
            {
                "q": "Why choose TIA Software Solutions for virtual assistance in India?",
                "a": "We combine local administrative experts in India with global quality standards, offering reliable support that acts as a natural extension of your team."
            }
        ]
    },
    {
        "id": "02",
        "filename": "branding-essentials.html",
        "title": "Branding Essentials",
        "desc": "Logo design & brand identity systems in India",
        "meta_title": "Branding & Logo Design Agency in India | TIA Software Solutions",
        "meta_desc": "Leading branding & logo design agency in India. TIA Software Solutions offers professional logo design, brand guidelines, and corporate identity.",
        "schema_name": "Branding & Logo Design Agency in India",
        "schema_desc": "Professional branding & logo design services in India including custom logos, typography, color palettes, brand guidelines, and stationery.",
        "service_type": "Branding Essentials",
        "breadcrumb_name": "Branding Essentials",
        "intro_title": "Impactful Brand & Logo Design in India",
        "intro": "Your brand is your business's visual identity. We craft compelling, memorable, and unique brand identity systems in India, that resonate with your target audience and stand out in competitive markets.",
        "image": "assets/branding-logo-design-agency-india.webp",
        "img_width": 800,
        "img_height": 1000,
        "features": ["Logo Design & Variations", "Brand Guidelines", "Business Cards & Stationery"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Branding Essentials is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India branding design specialists means expecting transparency, high-quality design systems, and a commitment to your visual footprint. Whether you are building a startup brand in India or revitalizing an established identity across India, we deliver custom vector assets and guidelines designed to elevate your company.",
        "faqs": [
            {
                "q": "What is included in your Branding Essentials package?",
                "a": "It includes custom logo designs, primary/secondary logos, brand color palettes, typography guidelines, and corporate stationery mockups (business cards, letterheads)."
            },
            {
                "q": "How much does brand identity design cost in India?",
                "a": "Brand design pricing varies depending on the business size and collateral requirements. Contact TIA's India office for a custom, transparent quote."
            },
            {
                "q": "How long does it take to design a complete brand identity?",
                "a": "The complete branding process, from market research to delivery of style guides, typically takes 2 to 4 weeks."
            },
            {
                "q": "Do I get the source files and commercial rights for the logos?",
                "a": "Yes, you receive 100% full commercial rights and all vector source files (AI, EPS, PDF, SVG, high-res PNG) upon project completion."
            },
            {
                "q": "What if I already have a logo and just need a brand refresh?",
                "a": "We offer brand revitalization services to modernize your existing identity while maintaining recognition among your India client base."
            },
            {
                "q": "Can you help with trademark registration in India?",
                "a": "While we provide the vector designs and brand naming advice, actual legal trademark registration should be handled by a certified IP lawyer in India."
            },
            {
                "q": "How many logo design concepts do you provide?",
                "a": "We present 3 distinct logo concepts based on your design brief, then refine your chosen design through collaborative feedback cycles."
            },
            {
                "q": "Do you design business cards, letterheads, and print collateral?",
                "a": "Yes, we design print-ready stationery, marketing flyers, brochures, and digital banners matching your newly created brand guidelines."
            },
            {
                "q": "What details do you need to start the branding process?",
                "a": "We start with a brand questionnaire detailing your target audience, core values, preferred design aesthetics, and industry competitors."
            },
            {
                "q": "How do you ensure our brand design stands out in the India market?",
                "a": "We analyze local and global design trends, crafting a unique visual voice that instantly connects with India consumers and positions you above competitors."
            }
        ]
    },
    {
        "id": "03",
        "filename": "digital-marketing.html",
        "title": "Digital Marketing",
        "desc": "Social ads, SEO & campaigns in India",
        "meta_title": "Digital Marketing Agency in India | TIA Software Solutions",
        "meta_desc": "Top digital marketing agency in India. TIA Software Solutions offers data-driven SEO, social media ads, content marketing, and campaign management.",
        "schema_name": "Digital Marketing Agency in India",
        "schema_desc": "Data-driven digital marketing in India including SEO, social media advertising, content marketing, and campaign management to grow your business online.",
        "service_type": "Digital Marketing",
        "breadcrumb_name": "Digital Marketing",
        "intro_title": "Result-Driven Digital Marketing in India",
        "intro": "Accelerate your growth with data-driven digital marketing in India. We plan, execute, and optimize conversion-focused campaigns that reach the right audience, capture leads, and boost sales.",
        "image": "assets/digital-marketing-agency-india.webp",
        "img_width": 800,
        "img_height": 570,
        "features": ["Search Engine Optimization", "Social Media Ads", "Content Marketing"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Digital Marketing is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India marketing experts means expecting transparency, ROI-focused deliverables, and a commitment to your growth. Whether you are launching a new campaign in India or optimizing search visibility across India, we deliver precise, high-impact marketing results.",
        "faqs": [
            {
                "q": "How much does digital marketing cost in India?",
                "a": "Our digital marketing packages are custom-tailored to your budget, business objectives, and chosen campaign channels."
            },
            {
                "q": "How long does it take to see results from SEO and ads?",
                "a": "Paid ad campaigns (Google/Facebook/Instagram) deliver leads immediately, whereas organic SEO campaigns in India typically show compounding results within 3 to 6 months."
            },
            {
                "q": "Do you run Google Ads, Facebook Ads, and Instagram Ads?",
                "a": "Yes, we plan, build, and optimize high-converting campaigns across search, social media, display networks, and retargeting ads."
            },
            {
                "q": "Can you help with local SEO in India?",
                "a": "Yes! We specialize in local search optimization, getting your business ranking on Google Maps and localized search terms for target suburbs."
            },
            {
                "q": "Do you create the content and design the ad creatives?",
                "a": "Yes, our creative studio designs custom image/video ad assets and writes engaging copy tailored to grab the attention of local consumers."
            },
            {
                "q": "What industries do you specialize in marketing?",
                "a": "We manage successful campaigns for startups, e-commerce stores, real estate agencies, healthcare professionals, and professional services across India."
            },
            {
                "q": "Do we get monthly performance reports?",
                "a": "Yes, we provide comprehensive, easy-to-read reports detailing key metrics like ad spend, conversions, cost-per-lead, and website ranking improvements."
            },
            {
                "q": "Is there a long-term contract requirement?",
                "a": "No, we work on flexible monthly retainers. We earn your business month-after-month through measurable, ROI-driven marketing results."
            },
            {
                "q": "How do you determine the best marketing strategy for our business?",
                "a": "We evaluate your industry competition, audit your current online presence, identify high-intent keywords, and design an omnichannel plan."
            },
            {
                "q": "Why is TIA Software Solutions considered a top digital marketing agency in India?",
                "a": "We combine localized SEO expertise, conversion-focused ad management, and premium visual design under one roof to maximize marketing return."
            }
        ]
    },
    {
        "id": "04",
        "filename": "creative-design.html",
        "title": "Creative Design",
        "desc": "Social media posts & custom graphics in India",
        "meta_title": "Graphic Design Company in India | TIA Software Solutions",
        "meta_desc": "Premier graphic design company in India. TIA Software Solutions specializes in social media posts, brochure designs, flyer designs, and custom graphics.",
        "schema_name": "Graphic Design Company in India",
        "schema_desc": "Professional graphic design services in India including social media graphics, brochures, flyers, and custom visual content.",
        "service_type": "Creative Design",
        "breadcrumb_name": "Creative Design",
        "intro_title": "Stunning Creative Graphic Design in India",
        "intro": "Bring your ideas to life with high-impact creative designs in India. We ensure your social media graphics, brochures, and marketing collateral captivate your audience and communicate your values effectively.",
        "image": "assets/graphic-design-company-india.webp",
        "img_width": 800,
        "img_height": 1000,
        "features": ["Social Media Graphics", "Flyers & Brochures", "Presentation Design"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Creative Design is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India graphic designers means expecting transparency, pixel-perfect visuals, and a commitment to your brand guidelines. Whether you need a flyer design in India or ongoing social media assets for your business in India, we deliver precise, high-impact marketing materials.",
        "faqs": [
            {
                "q": "What types of creative design services do you offer in India?",
                "a": "We offer social media graphics, custom flyers, corporate brochures, corporate presentation decks, event banners, and digital marketing creatives."
            },
            {
                "q": "How much do graphic design services cost in India?",
                "a": "Costs depend on scope and volume. We offer project-based pricing as well as affordable monthly graphic design retainers for businesses."
            },
            {
                "q": "What is the typical turnaround time for a design project?",
                "a": "Standard graphic designs are completed within 2 to 3 business days. Complex projects like multi-page brochures might take 5 to 7 days."
            },
            {
                "q": "Do you provide unlimited revisions?",
                "a": "We offer unlimited revision rounds during the draft phase to ensure your final design aligns 100% with your creative vision."
            },
            {
                "q": "Can you design marketing materials for print as well as digital?",
                "a": "Yes, all print collateral is designed in CMYK color mode at 300 DPI, exported in print-ready PDF formats with proper bleed margins."
            },
            {
                "q": "What file formats will I receive for my designs?",
                "a": "You receive high-resolution print PDFs, web-optimized PNGs/JPEGs, and original design source files (Photoshop, Illustrator, or Figma)."
            },
            {
                "q": "Do you use stock photos, or do we need to provide them?",
                "a": "We use high-quality, royalty-free stock imagery from premium databases, but we welcome any product or team photos you want to feature."
            },
            {
                "q": "Can you design presentations or pitch decks?",
                "a": "Yes, we craft professionally designed PowerPoint, Google Slides, or PDF presentation templates that engage investors and clients."
            },
            {
                "q": "How do we submit design requests and feedback?",
                "a": "Requests and feedback are submitted via our client portal, email, or WhatsApp, keeping communication streamlined and centralized."
            },
            {
                "q": "Why choose TIA Software Solutions for your creative graphics in India?",
                "a": "Our team combines creative art direction with marketing psychology, designing assets that don't just look beautiful but also drive conversions."
            }
        ]
    },
    {
        "id": "05",
        "filename": "ui-ux-design.html",
        "title": "UI/UX Design",
        "desc": "Modern interfaces & prototypes in India",
        "meta_title": "UI UX Design Company in India | TIA Software Solutions",
        "meta_desc": "Top UI UX design company in India. TIA Software Solutions offers mobile app & web interface design, wireframing, interactive prototyping, and user testing.",
        "schema_name": "UI UX Design Company in India",
        "schema_desc": "Professional UI/UX design in India including wireframing, prototyping, high-fidelity interfaces, and usability testing for seamless user experiences.",
        "service_type": "UI/UX Design",
        "breadcrumb_name": "UI/UX Design",
        "intro_title": "Intuitive UI/UX Design Solutions in India",
        "intro": "We build intuitive, engaging, and beautiful user interfaces that guarantee a seamless experience for your users across India, and globally.",
        "image": "assets/ui-ux-design-company-india.webp",
        "img_width": 800,
        "img_height": 533,
        "features": ["Wireframing & Prototyping", "High-Fidelity UI Design", "Usability Testing"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in UI/UX Design is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India UI/UX design specialists means expecting transparency, high-quality deliverables, and a commitment to your success. Whether you are launching a new initiative in India or revamping an existing one, we deliver precise, high-impact results designed to elevate your brand.",
        "faqs": [
            {
                "q": "What is the difference between UI and UX design?",
                "a": "UI (User Interface) is the visual skin and styling of an app (colors, buttons, typography). UX (User Experience) is the functional logic, flow, and ease of navigation."
            },
            {
                "q": "How much does UI/UX design cost for a mobile app or website in India?",
                "a": "Interface design costs depend on wireframe complexity, number of screens, and interactive features. Contact TIA's design team for a custom quote."
            },
            {
                "q": "How long does the UI/UX design process take?",
                "a": "A standard website UI/UX project takes 3 to 5 weeks, while complex mobile/SaaS applications can take 6 to 10 weeks of collaborative design."
            },
            {
                "q": "Do you design for both web and mobile platforms?",
                "a": "Yes, we specialize in responsive web layouts, iOS app designs, Android app designs, and custom dashboard interfaces."
            },
            {
                "q": "Do you write code (HTML/CSS/JS) or just deliver design files?",
                "a": "We specialize in UI/UX layout design and prototyping. However, our development team is ready to fully code and build your designs if needed."
            },
            {
                "q": "What tools do you use for wireframing and prototyping?",
                "a": "We use Figma as our primary design tool, enabling real-time collaboration, comments, and interactive clickable prototypes."
            },
            {
                "q": "Do you conduct usability testing with real users?",
                "a": "Yes, we perform interactive prototype testing to observe navigation flows, gather user feedback, and refine layout logic before code development."
            },
            {
                "q": "Can you redesign an existing application or website?",
                "a": "Yes! We perform UX audits on current sites to identify drop-off points, then design an updated user-friendly interface."
            },
            {
                "q": "Do you provide design systems for developers?",
                "a": "Yes, we deliver comprehensive UI kits containing component libraries, spacing grids, typography tokens, and style guides for smooth handoff."
            },
            {
                "q": "Why is TIA Software Solutions the leading UI/UX agency in India?",
                "a": "We combine human-centered design research with cutting-edge visual aesthetics, creating software interfaces that users love."
            }
        ]
    },
    {
        "id": "06",
        "filename": "video-motion-graphics.html",
        "title": "Video & Motion Graphics",
        "desc": "Reels, animations & brand videos in India",
        "meta_title": "Video Production Company in India | TIA Software Solutions",
        "meta_desc": "Top video production company in India. TIA Software Solutions specializes in 2D/3D animation, explainer videos, promo videos, and corporate video editing.",
        "schema_name": "Video Production Company in India",
        "schema_desc": "Dynamic video and motion graphics in India including 2D/3D animation, explainer videos, reels, and brand video production.",
        "service_type": "Video Production",
        "breadcrumb_name": "Video & Motion Graphics",
        "intro_title": "Dynamic Video & Motion Graphics in India",
        "intro": "Capture attention instantly with dynamic motion graphics and video content in India, that effectively tell your brand story and increase social media engagement.",
        "image": "assets/video-production-company-india.webp",
        "img_width": 800,
        "img_height": 533,
        "features": ["2D & 3D Animation", "Explainer Videos", "Video Editing"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Video & Motion Graphics is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India video production crew means expecting transparency, high-quality animations, and a video that connects with viewers. Whether you need an explainer animation in India or short-form video editing for social channels across India, we deliver high-impact results.",
        "faqs": [
            {
                "q": "What type of video production services do you offer in India?",
                "a": "We produce 2D explainer animations, 3D motion designs, brand introduction videos, social media video ads, and corporate video edits."
            },
            {
                "q": "How much does a 2D or 3D animated explainer video cost?",
                "a": "Animation costs are determined by length (in seconds/minutes), voiceover talent, asset complexity, and animation style."
            },
            {
                "q": "How long does it take to produce a 60-second video?",
                "a": "A custom 60-second explainer animation takes 3 to 4 weeks, including scripting, storyboarding, voiceover, and final render."
            },
            {
                "q": "Do you write the video script and record the voiceover?",
                "a": "Yes, we write professional marketing scripts and record voices using multi-lingual professional voiceover artists (Tamil, English, Hindi, etc.)."
            },
            {
                "q": "Can you edit raw footage for corporate videos and Reels?",
                "a": "Yes, we cut raw videos, perform color grading, insert smooth transitions, add subtitles, and apply sound design to make it engaging."
            },
            {
                "q": "Do you provide royalty-free background music and sound effects?",
                "a": "Yes, all sound elements used in TIA videos are commercially licensed, protecting your brand from copyright claims online."
            },
            {
                "q": "What is your revision policy for video and animation projects?",
                "a": "We offer revision rounds at script, storyboard, and final animation stages to ensure you are fully satisfied with the story progression."
            },
            {
                "q": "Do you create storyboards before starting the animation?",
                "a": "Yes! We draw and share static storyboards showing scene layouts, guaranteeing you approve the visual flow before we animate."
            },
            {
                "q": "In what formats do you deliver the final video files?",
                "a": "We deliver high-definition MP4/MOV files optimized for web, YouTube, Facebook, or Instagram upload."
            },
            {
                "q": "Why choose TIA Software Solutions for video production in India?",
                "a": "We deliver premium, studio-quality motion graphics and professional edits that communicate complex business ideas in seconds."
            }
        ]
    },
    {
        "id": "07",
        "filename": "stories-reels-assets.html",
        "title": "Stories & Reels Assets",
        "desc": "Short-form video assets & templates in India",
        "meta_title": "Social Media Video Editing in India | TIA Software Solutions",
        "meta_desc": "Top social media video editing services in India. TIA Software Solutions creates high-retention Reels, TikToks, Shorts, and custom graphic templates.",
        "schema_name": "Social Media Video Editing in India",
        "schema_desc": "High-retention social media video editing and assets in India, including Reels, Shorts, and TikTok video templates.",
        "service_type": "Social Media Assets",
        "breadcrumb_name": "Stories & Reels Assets",
        "intro_title": "High-Retention Stories & Reels Editing in India",
        "intro": "Dominate Instagram, TikTok, and YouTube with our custom vertical video edits and stories templates in India, tailored to maximize retention and local reach.",
        "image": "assets/social-media-video-editing-india.webp",
        "img_width": 800,
        "img_height": 600,
        "features": ["Custom Reel Templates", "Trending Audio Sync", "Vertical Video Edits"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Stories & Reels Assets is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India short-form video editors means expecting transparency, trendy visual layouts, and sound design that boosts algorithm exposure. Whether you are marketing a product in India or scaling an influencer presence across India, we deliver optimized vertical video assets.",
        "faqs": [
            {
                "q": "What are Stories & Reels Assets?",
                "a": "These are short-form vertical video assets (9:16 aspect ratio) designed to capture attention quickly on platforms like Instagram Reels, TikTok, and YouTube Shorts."
            },
            {
                "q": "How much does it cost to get custom social media video templates in India?",
                "a": "Contact TIA for pricing. We offer flexible packages for single campaigns or monthly subscription models for ongoing reel assets."
            },
            {
                "q": "Can you edit TikToks, Reels, and YouTube Shorts for us?",
                "a": "Yes! You send your raw recordings, and we edit them with dynamic captions, sound effects, zoom effects, and overlays."
            },
            {
                "q": "Do you provide vertical video templates that we can edit ourselves?",
                "a": "Yes, we create custom templates on popular platforms like Canva or CapCut, designed with your corporate brand guidelines."
            },
            {
                "q": "How do you sync videos with trending audio?",
                "a": "We track trending sounds weekly, cutting and pacing your video transitions to the beat of the audio for algorithm boost."
            },
            {
                "q": "How many assets are included in a typical package?",
                "a": "We package reels in sets of 10, 20, or 30 videos per month, tailored to support your content calendar frequency in India."
            },
            {
                "q": "Can you help with thumbnail designs for Reels and Shorts?",
                "a": "Yes! Eye-catching covers are crucial. We design high-CTR thumbnails for all vertical videos we produce."
            },
            {
                "q": "What video editing software do you use?",
                "a": "We edit using Adobe Premiere Pro, After Effects, and Figma, ensuring the highest visual quality and seamless motion graphics."
            },
            {
                "q": "Do you offer caption writing and hashtag research?",
                "a": "Yes, each asset comes with optimized titles, caption copy, and targeted hashtags to maximize reach across India and globally."
            },
            {
                "q": "How do social assets from TIA help grow our presence in India?",
                "a": "By creating highly engaging, trendy, and polished vertical videos, we keep your business top-of-mind and algorithm-friendly."
            }
        ]
    },
    {
        "id": "08",
        "filename": "seasonal-festive.html",
        "title": "Seasonal & Festive",
        "desc": "Holiday & festive design packs in India",
        "meta_title": "Festive Graphic Design Packs in India | TIA Software Solutions",
        "meta_desc": "Custom festive graphic design packs in India. TIA Software Solutions offers holiday greeting cards, social posts, and seasonal banners.",
        "schema_name": "Festive Graphic Design Packs in India",
        "schema_desc": "Custom seasonal and festive graphic designs in India, including holiday posts, greeting cards, and website banners.",
        "service_type": "Festive Graphics",
        "breadcrumb_name": "Seasonal & Festive",
        "intro_title": "Engaging Festive Campaign Design in India",
        "intro": "Celebrate holidays and regional festivals like Pongal or Diwali with custom festive design packs in India, designed to align with your brand while engaging local customers.",
        "image": "assets/festive-graphic-design-packs-india.webp",
        "img_width": 800,
        "img_height": 534,
        "features": ["Holiday Social Posts", "Website Banners", "Greeting Cards"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Seasonal & Festive is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting in outcomes that exceed expectations.",
        "expect_text": "Partnering with our India festive designers means expecting transparency, culturally resonant graphics, and prompt delivery ahead of major events. Whether you are running a Diwali sale banner in India or greeting cards across India, we deliver customized high-impact graphics.",
        "faqs": [
            {
                "q": "What is included in a Seasonal & Festive design pack?",
                "a": "It includes holiday-themed social media posts, seasonal website homepage banners, customized greeting cards, and festive email templates."
            },
            {
                "q": "Why should my business use seasonal branding in India?",
                "a": "Local consumers engage highly with brands that celebrate regional culture. Custom festive posts humanize your business and drive sales."
            },
            {
                "q": "How much do festive graphic design packs cost?",
                "a": "We offer affordable seasonal packs matching individual holiday requirements or annual packages covering major festivals."
            },
            {
                "q": "When should we place orders for holiday banner designs?",
                "a": "We recommend starting design campaigns at least 2 to 3 weeks before a festival or holiday sale event begins."
            },
            {
                "q": "Do you customize designs for specific regional festivals like Pongal or Diwali?",
                "a": "Yes, we customize graphics for Pongal, Diwali, Eid, Christmas, New Year, and national holidays, aligning them with your brand colors."
            },
            {
                "q": "Can we use these festive designs for print greeting cards?",
                "a": "Yes, we supply print-ready files (CMYK, 300 DPI) for cards, tags, and product boxes, alongside your web graphics."
            },
            {
                "q": "What file formats are delivered for website seasonal banners?",
                "a": "We supply web-optimized JPG, PNG, and WebP formats to ensure quick page loading speeds for your online store in India."
            },
            {
                "q": "Do you design custom digital greeting cards for WhatsApp?",
                "a": "Yes, we design high-impact vertical graphics and animations perfect for sharing with clients via WhatsApp and Telegram."
            },
            {
                "q": "Can we get a year-round subscription for seasonal graphics?",
                "a": "Yes! We provide an annual calendar subscription where our team delivers custom festive packs automatically before every key holiday."
            },
            {
                "q": "Why is TIA the best choice for holiday campaigns in India?",
                "a": "We understand Tamil cultural nuances, ensuring your holiday marketing graphics are creative, respectful, and highly effective."
            }
        ]
    },
    {
        "id": "09",
        "filename": "event-launch-graphics.html",
        "title": "Event & Launch Graphics",
        "desc": "Product launches & event visuals in India",
        "meta_title": "Event & Product Launch Branding in India | TIA Software Solutions",
        "meta_desc": "Professional event & product launch branding in India. TIA Software Solutions designs teaser campaigns, registration landing pages, and invitations.",
        "schema_name": "Event & Product Launch Branding in India",
        "schema_desc": "Professional event and product launch graphic design services in India, including teaser campaigns and digital invitations.",
        "service_type": "Event Graphics",
        "breadcrumb_name": "Event & Launch Graphics",
        "intro_title": "Memorable Event & Launch Branding in India",
        "intro": "Make your next product launch or corporate event unforgettable in India, with custom event invitation designs, teaser graphics, and countdown visual layouts.",
        "image": "assets/event-product-launch-branding-india.webp",
        "img_width": 800,
        "img_height": 533,
        "features": ["Teaser Campaigns", "Event Registration Pages", "Digital Invitations"],
        "why_matters": "In today's highly competitive digital landscape, a strong foundation in Event & Launch Graphics is not just an option—it's a necessity. We help bridge the gap between where your India business is and where it needs to be, providing the essential tools and strategies that foster long-term, sustainable growth.",
        "our_approach": "We believe in a customized approach for our clients in India. From the initial consultation to final delivery, we take the time to understand your brand's unique voice and objectives. Our iterative process ensures that you are involved at every crucial step, resulting outcomes that exceed expectations.",
        "expect_text": "Partnering with our India event design specialists means expecting transparency, professional brand coordination, and print-ready digital templates. Whether you are planning a conference in India or launching a new product across India, we deliver graphics that maximize RSVP rates.",
        "faqs": [
            {
                "q": "What graphics do I need for a successful product launch or event in India?",
                "a": "You need teaser countdown posts, event banners, registration landing pages, email invitations, and digital badges/agendas."
            },
            {
                "q": "How much does an event graphic design package cost in India?",
                "a": "We structure pricing according to event size, assets required, and whether you need landing page development."
            },
            {
                "q": "What is the turnaround time for designing event banners and invitations?",
                "a": "A standard event set is ready within 5 to 7 business days, while comprehensive launch visual campaigns take 2 weeks."
            },
            {
                "q": "Can you build a custom event registration page or landing page?",
                "a": "Yes, we design and code conversion-friendly, responsive landing pages that integrate with RSVP forms and email systems."
            },
            {
                "q": "Do you design printed event materials like roll-up banners and badges?",
                "a": "Yes, we design backdrop walls, roll-ups, entry badges, agendas, swag bags, and flyer print collaterals."
            },
            {
                "q": "What details do you need to start designing launch visuals?",
                "a": "We need the launch date, brand guidelines, color palette, key messaging, registration links, and format requirements."
            },
            {
                "q": "Can you create teaser video animations for product launches?",
                "a": "Yes, we create 15-second and 30-second promo videos to build excitement on social media channels in India and beyond."
            },
            {
                "q": "Do you offer social media countdown graphics?",
                "a": "Yes, we design cohesive multi-day countdown templates for Instagram, LinkedIn, and Facebook feeds."
            },
            {
                "q": "Do you provide files optimized for both email and social media?",
                "a": "Yes, all graphic sizes are customized to render perfectly in email newsletters, mobile feeds, and desktop banners."
            },
            {
                "q": "Why choose TIA Software Solutions for your event branding in India?",
                "a": "We deliver premium, eye-catching visual themes that build immense anticipation, helping you sell out tickets and maximize registrations."
            }
        ]
    }
]

# Read index.html layout to extract structural components
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract NAV section with mobile menu and wrapping elements
# We capture from body opening to the end of mobile menu
body_prefix_match = re.search(r'<body>(.*?)<!-- NAV -->.*?</nav>', content, re.DOTALL)
body_prefix_html = "<body>" + body_prefix_match.group(1) + "<!-- NAV -->\n" + re.search(r'<!-- NAV -->(.*?)</nav>', content, re.DOTALL).group(0)
body_prefix_html = body_prefix_html.replace('href="#', 'href="index.html#')

# Extract bottom section (Contact + Footer + script import)
bottom_match = re.search(r'(<!-- CONTACT -->.*)', content, re.DOTALL)
bottom_html = bottom_match.group(1)
bottom_html = bottom_html.replace('href="#', 'href="index.html#')

# Generate pages
for s in services:
    # 1. Build features HTML
    features_html = ""
    for feat in s['features']:
        features_html += f'<li style="margin-bottom: 15px; font-size: 1.1rem; display: flex; align-items: center;"><span style="color:var(--accent); margin-right: 15px; font-size: 1.4rem;">✔</span>{feat}</li>'

    # 2. Build visual FAQs HTML
    faqs_html = ""
    for faq in s['faqs']:
        faqs_html += f"""
        <div class="faq-item">
          <div class="faq-question">
            <span>{faq['q']}</span>
            <span class="faq-icon">+</span>
          </div>
          <div class="faq-answer">
            <p>{faq['a']}</p>
          </div>
        </div>"""

    # 3. Build schema-compatible FAQ JSON list
    faq_schema_list = []
    for faq in s['faqs']:
        faq_schema_list.append({
            "@type": "Question",
            "name": faq['q'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['a']
            }
        })
    s_faq_schema = json.dumps(faq_schema_list, ensure_ascii=False)

    # 4. Construct service detail layout
    service_content = f"""
  <section class="services-detail" style="padding-top: 150px; padding-bottom: 80px;">
    <div class="container">
      
      <!-- HEADER -->
      <div class="section-header" style="text-align: center; margin-bottom: 60px;">
        <span class="section-tag">SERVICE {s['id']}</span>
        <h1 class="section-title" style="font-size: 3.5rem; margin-bottom: 15px;"><span class="accent">{s['schema_name']}</span></h1>
        <p class="section-sub" style="font-size: 1.25rem; max-width: 650px; margin: 0 auto; color: var(--grey); line-height: 1.6;">{s['desc']}</p>
      </div>

      <!-- IMAGE & OVERVIEW ROW -->
      <div class="service-optimal-layout" style="display: flex; flex-wrap: wrap; gap: 50px; align-items: center; margin-bottom: 80px;">
        <div style="flex: 1; min-width: 300px;">
            <img src="{s['image']}" alt="{s['schema_name']}" width="{s['img_width']}" height="{s['img_height']}" loading="lazy" style="width: 100%; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05); box-shadow: 0 15px 40px rgba(0,0,0,0.4); object-fit: cover; height: 100%; min-height: 350px;" />
        </div>
        <div style="flex: 1; min-width: 300px; padding: 20px 0;">
            <h2 style="font-size: 2.2rem; margin-bottom: 25px; color: var(--white);">{s['intro_title']}</h2>
            <p style="color: var(--grey); line-height: 1.8; margin-bottom: 20px; font-size: 1.1rem;">
                {s['intro']}
            </p>
            <p style="color: var(--grey); line-height: 1.8; margin-bottom: 35px; font-size: 1.1rem;">
                Our expert team in India is dedicated to delivering streamlined, effective solutions tailored to your unique requirements. As a premier provider of {s['title']} in India, we act as an extension of your team to ensure maximum impact and measurable results.
            </p>
            <ul style="list-style: none; padding: 0; color: var(--white); margin-bottom: 45px;">
                {features_html}
            </ul>
            <a href="index.html#contact" class="btn-primary" style="padding: 14px 35px; font-size: 1.1rem;">Get a Free India Consultation</a>
        </div>
      </div>

      <!-- ADDITIONAL INFO COLUMNS -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px; margin-bottom: 80px;">
        <div class="glass-card" style="padding: 40px;">
            <h3 style="font-size: 1.6rem; color: var(--accent); margin-bottom: 20px;">Why This Matters</h3>
            <p style="color: var(--grey); line-height: 1.7;">{s['why_matters']}</p>
        </div>
        <div class="glass-card" style="padding: 40px;">
            <h3 style="font-size: 1.6rem; color: var(--accent); margin-bottom: 20px;">Our Approach</h3>
            <p style="color: var(--grey); line-height: 1.7;">{s['our_approach']}</p>
        </div>
        <div class="glass-card" style="padding: 40px;">
            <h3 style="font-size: 1.6rem; color: var(--accent); margin-bottom: 20px;">What You Can Expect</h3>
            <p style="color: var(--grey); line-height: 1.7;">{s['expect_text']}</p>
        </div>
      </div>

    </div>
  </section>

  <!-- EXPLORE MORE SERVICES -->
  <section class="explore-services" style="padding: 60px 0; background: rgba(149, 58, 142, 0.03); border-top: 1px solid var(--glass-border); border-bottom: 1px solid var(--glass-border);">
    <div class="container">
      <div class="section-header" style="text-align: center; margin-bottom: 40px;">
        <span class="section-tag">SERVICES</span>
        <h2 class="section-title" style="font-size: 2.2rem;">Other Premium <span class="accent">Solutions</span></h2>
        <p class="section-sub" style="font-size: 1.05rem; max-width: 600px; margin: 0 auto; color: var(--grey);">
          Boost your business growth across India, with our full suite of digital agency services.
        </p>
      </div>
      
      <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; max-width: 900px; margin: 0 auto;">
        <a href="ui-ux-design.html" class="glass-card" style="padding: 15px 25px; text-decoration: none; display: flex; align-items: center; gap: 10px; font-weight: 600; color: var(--white); transition: var(--transition);">
          <span style="color: var(--purple);">✦</span> UI/UX Design
        </a>
        <a href="branding-essentials.html" class="glass-card" style="padding: 15px 25px; text-decoration: none; display: flex; align-items: center; gap: 10px; font-weight: 600; color: var(--white); transition: var(--transition);">
          <span style="color: var(--purple);">✦</span> Branding Essentials
        </a>
        <a href="digital-marketing.html" class="glass-card" style="padding: 15px 25px; text-decoration: none; display: flex; align-items: center; gap: 10px; font-weight: 600; color: var(--white); transition: var(--transition);">
          <span style="color: var(--purple);">✦</span> Digital Marketing
        </a>
        <a href="creative-design.html" class="glass-card" style="padding: 15px 25px; text-decoration: none; display: flex; align-items: center; gap: 10px; font-weight: 600; color: var(--white); transition: var(--transition);">
          <span style="color: var(--purple);">✦</span> Creative Design
        </a>
        <a href="virtual-assistance.html" class="glass-card" style="padding: 15px 25px; text-decoration: none; display: flex; align-items: center; gap: 10px; font-weight: 600; color: var(--white); transition: var(--transition);">
          <span style="color: var(--purple);">✦</span> Virtual Assistance
        </a>
        <a href="index.html#contact" class="glass-card" style="padding: 15px 25px; text-decoration: none; display: flex; align-items: center; gap: 10px; font-weight: 600; color: var(--purple); border-color: var(--purple); transition: var(--transition);">
          <span style="color: var(--purple);">✉</span> Contact India Office
        </a>
      </div>
    </div>
  </section>

  <!-- FAQ SECTION -->
  <section class="faq-section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">FAQ</span>
        <h2 class="section-title">Frequently Asked <span class="accent">Questions</span></h2>
        <p class="section-sub">Have questions? We have answers. Find everything you need to know about our {s['title']} services in India.</p>
      </div>
      
      <div class="faq-accordion">
        {faqs_html}
      </div>
    </div>
  </section>
"""

    # 5. Build full HTML document
    head_html = f"""<!DOCTYPE html>
<html lang="en">

<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-97DXKC53G1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-97DXKC53G1');
  </script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{s['meta_title']}</title>
  <meta name="description" content="{s['meta_desc']}" />
  <link rel="canonical" href="https://www.tiasoftwaresolutions.com/{s['filename']}" />

  <!-- Favicon & PWA -->
  <link rel="icon" type="image/webp" href="assets/logo.webp" />
  <link rel="apple-touch-icon" href="apple-touch-icon.webp" />
  <link rel="manifest" href="manifest.webmanifest" />
  <meta name="theme-color" content="#953a8e" />

  <!-- Schema.org: Service -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{s['schema_name']}",
    "description": "{s['schema_desc']}",
    "provider": {{
      "@type": "Organization",
      "name": "TIA Software Solutions",
      "url": "https://www.tiasoftwaresolutions.com/"
    }},
    "url": "https://www.tiasoftwaresolutions.com/{s['filename']}",
    "serviceType": "{s['service_type']}",
    "areaServed": [
          {{
            "@type": "Country",
            "name": "India"
          }}
        ],
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "24"
    }},
    "review": [
      {{
        "@type": "Review",
        "author": {{
          "@type": "Person",
          "name": "Priya"
        }},
        "reviewRating": {{
          "@type": "Rating",
          "ratingValue": "5"
        }},
        "reviewBody": "Professional team, fast delivery, and great results. They built our business website in record time and we started getting inquiries the same week it launched."
      }},
      {{
        "@type": "Review",
        "author": {{
          "@type": "Person",
          "name": "Luca Chris"
        }},
        "reviewRating": {{
          "@type": "Rating",
          "ratingValue": "5"
        }},
        "reviewBody": "Best digital marketing service we've used so far. Our Google ranking improved from page 5 to page 1 within three months. Highly recommend TIA Software Solutions!"
      }}
    ]
  }}
  </script>

  <!-- Schema.org: BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://www.tiasoftwaresolutions.com/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Services",
        "item": "https://www.tiasoftwaresolutions.com/#services"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{s['breadcrumb_name']}",
        "item": "https://www.tiasoftwaresolutions.com/{s['filename']}"
      }}
    ]
  }}
  </script>

  <!-- Schema.org: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": {s_faq_schema}
  }}
  </script>

  <link rel="stylesheet" href="style.css" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Syne:wght@400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet" />
</head>
"""

    page_html = head_html + "\n" + body_prefix_html + "\n" + service_content + "\n" + bottom_html

    with open(s['filename'], 'w', encoding='utf-8') as out:
        out.write(page_html)
    print(f"Generated fully SEO-optimized & Localized FAQ Page: {s['filename']}")
