# 🔥 JENIT'S DOOM — Flask + Jinja Raycasting Edition

A **complete playable DOOM clone** built with **Flask**, **Jinja2**, and a **pure JavaScript raycasting engine** (no external libraries except Tailwind CDN for the UI).

## How to Run

```powershell
cd "complete-website"
python app.py
```

Then open:
- **http://localhost:5000/** — Beautiful retro landing page
- **http://localhost:5000/doom** — The actual game

## What You Get

**Landing Page (`/`)**  
- Full retro DOOM aesthetic using VT323 font  
- Jinja-powered templates  
- Links to the game and an About page

**The Game (`/doom`)**  
- Authentic DDA raycasting engine (the technique that powered Wolfenstein 3D & DOOM)
- Real-time 3D walls with shading + fake texture lines
- 8 angry demons with AI that chases you
- Mouse look (click the canvas to lock pointer) + WASD / Arrow keys
- Hitscan shooting with muzzle flash
- Working health, ammo, score, kill counter
- Minimap
- Fullscreen-feeling HUD in classic DOOM style
- Retro Web Audio beeps and booms
- Win / lose states with final score
- Pause (ESC) + Restart (R)

## Technical Highlights

- `app.py` — clean Flask application with multiple Jinja routes
- `templates/` — base layout + index + doom.html + about.html (all using Jinja `extends` / `blocks`)
- `static/js/doom.js` — ~400 lines of self-contained game logic (raycaster, sprites, collision, AI, input, sound)
- `static/css/doom.css` — pixel-perfect retro styling

Everything runs instantly in the browser with **zero build step**.

## Controls (in the game)

| Key / Action          | Effect                     |
|-----------------------|----------------------------|
| Mouse move            | Look around (after click)  |
| W / A / S / D         | Move                       |
| Arrow keys            | Move (alternative)         |
| Left Click / SPACE    | Shoot                      |
| ESC                   | Pause / Resume             |
| R                     | Restart level              |

## Future Ideas (if you want to extend)

- Multiple levels / different maps
- Door interaction (E key)
- Different enemy types + sprites
- Real wall textures using small image data
- Power-ups, secret walls, proper weapon switching
- Persistent high scores using Flask sessions or SQLite

This project perfectly combines:
- Flask backend + Jinja templating (as requested)
- A true "clone of DOOM" experience

Enjoy ripping and tearing! 🩸

---

Originally created inside the `complete-website` folder on Day 56 of the 100 Days journey.