/* ============================================================
   TIA SOFTWARE SOLUTIONS — MAIN SCRIPT
   Canvas Tech Background | Parallax | Cursor | Interactions
   ============================================================ */

(function () {
  "use strict";

  // ─── CANVAS TECH BACKGROUND ───────────────────────────────
  const canvas = document.getElementById("techCanvas");
  const ctx = canvas.getContext("2d");

  const PURPLE = "#953A8E";
  const PURPLE_DIM = "rgba(149,58,142,";

  let W, H;
  let nodes = [];
  let gridLines = [];
  let dataPackets = [];
  let scanLine = 0;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
    initNodes();
    initGrid();
  }

  // Node graph
  function initNodes() {
    nodes = [];
    const count = Math.floor((W * H) / 22000);
    for (let i = 0; i < count; i++) {
      nodes.push({
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        r: Math.random() * 1.8 + 0.6,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: Math.random() * 0.03 + 0.01,
        active: Math.random() > 0.7,
      });
    }
  }

  // Grid / circuit lines
  function initGrid() {
    gridLines = [];
    const cols = 14, rows = 9;
    const cw = W / cols, ch = H / rows;
    for (let r = 0; r <= rows; r++) {
      for (let c = 0; c <= cols; c++) {
        if (Math.random() > 0.55) {
          gridLines.push({
            x1: c * cw, y1: r * ch,
            x2: (c + (Math.random() > 0.5 ? 1 : 0)) * cw,
            y2: (r + (Math.random() > 0.5 ? 1 : 0)) * ch,
            alpha: Math.random() * 0.07 + 0.02,
          });
        }
      }
    }
  }

  function spawnPacket() {
    if (nodes.length < 2) return;
    const idx = Math.floor(Math.random() * nodes.length);
    const target = Math.floor(Math.random() * nodes.length);
    dataPackets.push({
      sx: nodes[idx].x, sy: nodes[idx].y,
      ex: nodes[target].x, ey: nodes[target].y,
      progress: 0,
      speed: Math.random() * 0.012 + 0.005,
    });
  }

  let frame = 0;

  function drawFrame() {
    ctx.clearRect(0, 0, W, H);

    // Subtle grid
    gridLines.forEach(l => {
      ctx.beginPath();
      ctx.moveTo(l.x1, l.y1);
      ctx.lineTo(l.x2, l.y2);
      ctx.strokeStyle = `rgba(149,58,142,${l.alpha})`;
      ctx.lineWidth = 0.5;
      ctx.stroke();
    });

    // Scan line (slow moving horizontal glow)
    scanLine = (scanLine + 0.3) % H;
    const scanGrad = ctx.createLinearGradient(0, scanLine - 60, 0, scanLine + 60);
    scanGrad.addColorStop(0, "rgba(149,58,142,0)");
    scanGrad.addColorStop(0.5, "rgba(149,58,142,0.03)");
    scanGrad.addColorStop(1, "rgba(149,58,142,0)");
    ctx.fillStyle = scanGrad;
    ctx.fillRect(0, scanLine - 60, W, 120);

    // Connections between nearby nodes
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x;
        const dy = nodes[i].y - nodes[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const maxDist = 140;
        if (dist < maxDist) {
          const alpha = (1 - dist / maxDist) * 0.12;
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = `rgba(149,58,142,${alpha})`;
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }
    }

    // Nodes
    nodes.forEach(n => {
      n.x += n.vx;
      n.y += n.vy;
      if (n.x < 0 || n.x > W) n.vx *= -1;
      if (n.y < 0 || n.y > H) n.vy *= -1;

      n.pulse += n.pulseSpeed;
      const glow = n.active ? 0.8 + Math.sin(n.pulse) * 0.2 : 0.3;

      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(149,58,142,${glow * 0.45})`;
      ctx.fill();

      if (n.active) {
        const grad = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, 14);
        grad.addColorStop(0, `rgba(149,58,142,${0.1 * glow})`);
        grad.addColorStop(1, "rgba(149,58,142,0)");
        ctx.beginPath();
        ctx.arc(n.x, n.y, 14, 0, Math.PI * 2);
        ctx.fillStyle = grad;
        ctx.fill();
      }
    });

    // Data packets
    for (let idx = dataPackets.length - 1; idx >= 0; idx--) {
      const p = dataPackets[idx];
      p.progress += p.speed;
      const x = p.sx + (p.ex - p.sx) * p.progress;
      const y = p.sy + (p.ey - p.sy) * p.progress;

      ctx.beginPath();
      ctx.arc(x, y, 2.5, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(192,96,186,0.6)";
      ctx.fill();

      // Tail
      for (let t = 1; t <= 5; t++) {
        const tp = Math.max(0, p.progress - t * 0.015);
        const tx = p.sx + (p.ex - p.sx) * tp;
        const ty = p.sy + (p.ey - p.sy) * tp;
        ctx.beginPath();
        ctx.arc(tx, ty, 1.5, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(149,58,142,${0.5 - t * 0.08})`;
        ctx.fill();
      }

      if (p.progress >= 1) dataPackets.splice(idx, 1);
    }

    // Spawn packets
    if (frame % 80 === 0 && nodes.length > 1) spawnPacket();
    if (frame % 120 === 0) {
      if (gridLines.length > 0) {
        const idx = Math.floor(Math.random() * gridLines.length);
        gridLines[idx].alpha = Math.random() * 0.07 + 0.01;
      }
    }

    frame++;
    requestAnimationFrame(drawFrame);
  }

  window.addEventListener("resize", resize);
  resize();
  drawFrame();

  // ─── CUSTOM CURSOR ────────────────────────────────────────
  const cursor = document.getElementById("cursor");
  const follower = document.getElementById("cursorFollower");

  let mx = -100, my = -100;
  let fx = -100, fy = -100;

  document.addEventListener("mousemove", e => {
    mx = e.clientX;
    my = e.clientY;
    cursor.style.left = mx + "px";
    cursor.style.top = my + "px";
  });

  function animateFollower() {
    fx += (mx - fx) * 0.12;
    fy += (my - fy) * 0.12;
    follower.style.left = fx + "px";
    follower.style.top = fy + "px";
    requestAnimationFrame(animateFollower);
  }
  animateFollower();

  document.querySelectorAll("a, button, .service-card, .portfolio-card").forEach(el => {
    el.addEventListener("mouseenter", () => {
      cursor.classList.add("expanded");
      follower.classList.add("expanded");
    });
    el.addEventListener("mouseleave", () => {
      cursor.classList.remove("expanded");
      follower.classList.remove("expanded");
    });
  });

  // ─── NAVBAR SCROLL ────────────────────────────────────────
  const navbar = document.getElementById("navbar");
  window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 50);
  });

  // ─── HAMBURGER ────────────────────────────────────────────
  const hamburger = document.getElementById("hamburger");
  const mobileMenu = document.getElementById("mobileMenu");

  hamburger.addEventListener("click", () => {
    mobileMenu.classList.toggle("open");
  });

  mobileMenu.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => mobileMenu.classList.remove("open"));
  });

  // ─── PARALLAX SCROLLING ───────────────────────────────────
  const parallaxLayers = document.querySelectorAll("[data-speed]");

  function updateParallax() {
    const scrollY = window.scrollY;
    parallaxLayers.forEach(layer => {
      const speed = parseFloat(layer.dataset.speed);
      const offset = scrollY * speed;
      layer.style.transform = `translateY(${offset}px)`;
    });
  }

  window.addEventListener("scroll", updateParallax, { passive: true });

  // ─── FLOATING CODE SNIPPETS ───────────────────────────────
  const codeSnippets = [
    `const api = await fetch('/v1/campaign')\nreturn api.json()`,
    `function deploy(website) {\n  return cloud.push(website);\n}`,
    `git commit -m "feat: go-live"\ngit push origin main`,
    `import { SEO } from 'tia-studio'\nconst rank = SEO.optimize()`,
    `@media (max-width: 768px)\n  { display: flex; }`,
    `SELECT * FROM campaigns\nWHERE status = 'active'`,
    `npm run build\n> tia-solutions v2.0.0`,
    `curl -X POST /api/instagram\n-H "auth: Bearer $TOKEN"`,
    `const leads = await CRM.fetch()\nconsole.log(leads.count)`,
    `<meta name="keywords"\n  content="digital marketing">`,
  ];

  const floatingCode = document.getElementById("floatingCode");

  function spawnCodeSnippet() {
    const el = document.createElement("div");
    el.className = "code-snippet";
    el.textContent = codeSnippets[Math.floor(Math.random() * codeSnippets.length)];
    el.style.left = Math.random() * 80 + 5 + "%";
    el.style.animationDuration = (Math.random() * 14 + 18) + "s";
    el.style.animationDelay = Math.random() * 4 + "s";
    el.style.fontSize = (Math.random() * 3 + 10) + "px";
    floatingCode.appendChild(el);
    setTimeout(() => el.remove(), 28000);
  }

  for (let i = 0; i < 5; i++) setTimeout(spawnCodeSnippet, i * 1200);
  setInterval(spawnCodeSnippet, 4000);

  // ─── SCROLL REVEAL ────────────────────────────────────────
  const revealEls = document.querySelectorAll(
    ".service-card, .process-step, .why-card, .about-vm-card, .about-intro, .testimonial-card, .section-header"
  );

  revealEls.forEach(el => el.classList.add("reveal"));

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const siblings = Array.from(entry.target.parentElement.children);
        const idx = siblings.indexOf(entry.target);
        setTimeout(() => {
          entry.target.classList.add("visible");
        }, idx * 90);
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: "0px 0px -40px 0px" });

  revealEls.forEach(el => revealObserver.observe(el));

  // ─── CONTACT FORM ─────────────────────────────────────────
  const contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", e => {
      e.preventDefault();
      const btn = contactForm.querySelector(".btn-primary");
      const originalHTML = btn.innerHTML;
      btn.innerHTML = "<span>Message Sent ✓</span>";
      btn.style.background = "#4CAF50";
      btn.disabled = true;
      setTimeout(() => {
        btn.innerHTML = originalHTML;
        btn.style.background = "";
        btn.disabled = false;
        contactForm.reset();
      }, 3000);
    });
  }

  // ─── TICKER PAUSE ON HOVER ────────────────────────────────
  const ticker = document.querySelector(".ticker");
  if (ticker) {
    ticker.addEventListener("mouseenter", () => {
      ticker.style.animationPlayState = "paused";
    });
    ticker.addEventListener("mouseleave", () => {
      ticker.style.animationPlayState = "running";
    });
  }

  // ─── ACTIVE NAV LINK ON SCROLL ────────────────────────────
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav-links a");

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.style.color = "";
          if (link.getAttribute("href") === `#${entry.target.id}`) {
            if (!link.classList.contains("nav-cta")) {
              link.style.color = "var(--purple)";
            }
          }
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => sectionObserver.observe(s));

  // ─── CARD MOUSE TILT ─────────────────────────────────────
  document.querySelectorAll(".glass-card").forEach(card => {
    card.addEventListener("mousemove", e => {
      const rect = card.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = (e.clientX - cx) / (rect.width / 2);
      const dy = (e.clientY - cy) / (rect.height / 2);
      card.style.transform = `
        translateY(-4px)
        rotateY(${dx * 4}deg)
        rotateX(${-dy * 4}deg)
      `;
      card.style.transition = "transform 0.1s ease";
    });

    card.addEventListener("mouseleave", () => {
      card.style.transform = "";
      card.style.transition = "all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94)";
    });
  });

  // ─── WHATSAPP FAB PULSE ───────────────────────────────────
  const whatsappFab = document.querySelector(".whatsapp-fab");
  if (whatsappFab) {
    setInterval(() => {
      whatsappFab.style.transform = "translateY(-3px) scale(1.06)";
      setTimeout(() => {
        whatsappFab.style.transform = "";
      }, 300);
    }, 4000);
  }

  console.log(
    `%c[TIA SOFTWARE SOLUTIONS] — v2.0.0\n%cDesigning Your Digital Future.`,
    "color:#953A8E; font-family:monospace; font-size:14px; font-weight:700;",
    "color:#888; font-family:monospace; font-size:11px;"
  );

})();
