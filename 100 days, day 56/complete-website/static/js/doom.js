// =============================================
// JENIT'S DOOM CLONE — Pure JS Raycaster + Sprites
// Classic 1993 style first-person shooter in the browser
// =============================================

const WIDTH = 960;
const HEIGHT = 600;
const FOV = Math.PI / 2.8; // ~64 degrees
const NUM_RAYS = 240;      // lower = faster, higher = sharper
const MAX_DEPTH = 22;

let canvas, ctx;
let minimap, minimapCtx;
let player = { x: 3.5, y: 3.5, angle: 0, speed: 0 };
let keys = {};
let enemies = [];
let bullets = [];
let score = 0;
let kills = 0;
let health = 100;
let ammo = 24;
let gameRunning = false;
let gameWon = false;
let paused = false;
let lastTime = 0;
let frame = 0;

// Simple 2D level map. 1 = wall, 0 = floor, 2 = enemy spawn
const MAP = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,1,0,0,0,0,0,0,1],
  [1,0,1,1,0,0,1,0,1,1,1,1,0,1],
  [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
  [1,0,1,0,1,1,1,1,1,1,0,1,0,1],
  [1,0,0,0,1,0,0,0,0,1,0,0,0,1],
  [1,1,1,0,1,0,1,1,0,1,1,1,0,1],
  [1,0,0,0,0,0,1,0,0,0,0,0,0,1],
  [1,0,1,1,1,1,1,0,1,1,1,1,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
];

const MAP_WIDTH = MAP[0].length;
const MAP_HEIGHT = MAP.length;
const TILE = 1; // world unit per tile

let pointerLocked = false;

// Audio context for retro sounds
let audioCtx;

function initAudio() {
  try {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  } catch (e) {}
}

function playSound(type) {
  if (!audioCtx) return;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  const filter = audioCtx.createBiquadFilter();

  osc.type = 'sawtooth';
  filter.type = 'lowpass';

  if (type === 'shoot') {
    osc.frequency.value = 110;
    filter.frequency.value = 900;
    gain.gain.value = 0.35;
    setTimeout(() => gain.gain.linearRampToValueAtTime(0.001, audioCtx.currentTime + 0.18), 20);
    osc.frequency.linearRampToValueAtTime(60, audioCtx.currentTime + 0.2);
  } else if (type === 'hit') {
    osc.type = 'square';
    osc.frequency.value = 180;
    gain.gain.value = 0.6;
    filter.frequency.value = 1200;
    setTimeout(() => gain.gain.linearRampToValueAtTime(0.001, audioCtx.currentTime + 0.09), 10);
  } else if (type === 'death') {
    osc.frequency.value = 70;
    gain.gain.value = 0.7;
    filter.frequency.value = 600;
    osc.frequency.linearRampToValueAtTime(30, audioCtx.currentTime + 0.6);
    gain.gain.linearRampToValueAtTime(0.001, audioCtx.currentTime + 0.7);
  } else if (type === 'pain') {
    osc.type = 'sawtooth';
    osc.frequency.value = 140;
    gain.gain.value = 0.5;
    filter.frequency.value = 500;
    setTimeout(() => gain.gain.linearRampToValueAtTime(0.001, audioCtx.currentTime + 0.3), 30);
  } else if (type === 'win') {
    osc.frequency.value = 320;
    gain.gain.value = 0.4;
    filter.frequency.value = 2200;
    setTimeout(() => { osc.frequency.value = 480; }, 140);
    gain.gain.linearRampToValueAtTime(0.001, audioCtx.currentTime + 0.9);
  }

  const master = audioCtx.createGain();
  master.gain.value = 0.75;

  osc.connect(filter);
  filter.connect(gain);
  gain.connect(master);
  master.connect(audioCtx.destination);

  osc.start();
  setTimeout(() => osc.stop(), 900);
}

// Initialize everything
function initGame() {
  canvas = document.getElementById('game-canvas');
  ctx = canvas.getContext('2d', { alpha: false });

  minimap = document.getElementById('minimap');
  minimapCtx = minimap.getContext('2d');

  // Reset state
  player = { x: 3.5, y: 3.5, angle: 1.2, speed: 3.8 };
  keys = {};
  enemies = [];
  bullets = [];
  score = 0;
  kills = 0;
  health = 100;
  ammo = 24;
  gameRunning = true;
  gameWon = false;
  paused = false;
  pointerLocked = false;

  // Spawn enemies from map
  for (let y = 0; y < MAP_HEIGHT; y++) {
    for (let x = 0; x < MAP_WIDTH; x++) {
      if (MAP[y][x] === 2) {
        enemies.push({
          x: x + 0.5,
          y: y + 0.5,
          size: 0.35,
          health: 3,
          speed: 1.2,
          alive: true,
        });
        // Clear spawn marker
        MAP[y][x] = 0;
      }
    }
  }

  // If no enemies were defined in map, add some manually
  if (enemies.length === 0) {
    const spawns = [
      [5.5, 2.5], [10.5, 4.5], [2.5, 6.5], [11.5, 8.5],
      [4.5, 8.5], [8.5, 1.5], [7.5, 9.5], [12.5, 2.5]
    ];
    spawns.forEach(([x, y]) => {
      enemies.push({ x, y, size: 0.35, health: 3, speed: 1.15, alive: true });
    });
  }

  updateHUD();
  initAudio();

  // Input listeners
  window.addEventListener('keydown', onKeyDown, { once: false });
  window.addEventListener('keyup', onKeyUp);
  canvas.addEventListener('click', requestPointerLock);
  document.addEventListener('pointerlockchange', onPointerLockChange);
  canvas.addEventListener('mousedown', onMouseDown);
  document.addEventListener('mousemove', onMouseMove);
  window.addEventListener('keypress', onKeyPress);

  // Touch support for mobile (very basic)
  let touchStartX = 0;
  canvas.addEventListener('touchstart', (e) => {
    if (!gameRunning || paused) return;
    touchStartX = e.touches[0].clientX;
    shoot();
  }, { passive: true });

  // Start game loop
  gameRunning = true;
  requestAnimationFrame(gameLoop);

  // Show intro overlay briefly
  showOverlay('PREPARE YOURSELF', 'Click canvas to lock mouse • Kill all demons', 1600);
}

// Input handlers
function onKeyDown(e) {
  keys[e.key.toLowerCase()] = true;
  if (e.key === 'Escape') {
    e.preventDefault();
    togglePause();
  }
  if ((e.key.toLowerCase() === 'r') && gameRunning) {
    restartGame();
  }
  if (e.key === ' ' && gameRunning && !paused) {
    e.preventDefault();
    shoot();
  }
}

function onKeyUp(e) {
  keys[e.key.toLowerCase()] = false;
}

function onKeyPress(e) {
  if (e.key.toLowerCase() === 'e' && gameRunning && !paused) {
    // Future: interact / open door
  }
}

function onMouseDown(e) {
  if (e.button === 0 && gameRunning && !paused) {
    shoot();
  }
}

function onMouseMove(e) {
  if (!pointerLocked || !gameRunning || paused) return;

  const sensitivity = 0.0022;
  player.angle += e.movementX * sensitivity;

  // Clamp angle
  if (player.angle < 0) player.angle += Math.PI * 2;
  if (player.angle > Math.PI * 2) player.angle -= Math.PI * 2;
}

function requestPointerLock() {
  if (!gameRunning || paused) return;
  canvas.requestPointerLock = canvas.requestPointerLock || canvas.mozRequestPointerLock;
  canvas.requestPointerLock();
}

function onPointerLockChange() {
  pointerLocked = document.pointerLockElement === canvas;
}

function togglePause() {
  if (!gameRunning || gameWon) return;
  paused = !paused;
  if (paused) {
    showOverlay('PAUSED', 'Press ESC to resume', 999999);
    document.exitPointerLock && document.exitPointerLock();
  } else {
    hideOverlay();
    // Re-lock if needed
    if (!pointerLocked) canvas.requestPointerLock?.();
  }
}

// Movement + Collision
function movePlayer(dt) {
  if (paused || !gameRunning) return;

  let moveX = 0, moveY = 0;
  const speed = player.speed * dt;

  if (keys['w'] || keys['arrowup']) {
    moveX += Math.cos(player.angle) * speed;
    moveY += Math.sin(player.angle) * speed;
  }
  if (keys['s'] || keys['arrowdown']) {
    moveX -= Math.cos(player.angle) * speed;
    moveY -= Math.sin(player.angle) * speed;
  }
  if (keys['a'] || keys['arrowleft']) {
    moveX += Math.cos(player.angle - Math.PI / 2) * speed * 0.85;
    moveY += Math.sin(player.angle - Math.PI / 2) * speed * 0.85;
  }
  if (keys['d'] || keys['arrowright']) {
    moveX += Math.cos(player.angle + Math.PI / 2) * speed * 0.85;
    moveY += Math.sin(player.angle + Math.PI / 2) * speed * 0.85;
  }

  // New position with collision
  let newX = player.x + moveX;
  let newY = player.y + moveY;

  // Wall collision (circle vs square tiles)
  if (!isWall(newX, player.y)) player.x = newX;
  if (!isWall(player.x, newY)) player.y = newY;

  // Weapon bob effect
  const weaponEl = document.getElementById('weapon');
  if (weaponEl) {
    if (Math.abs(moveX) + Math.abs(moveY) > 0.001) {
      weaponEl.classList.add('bobbing');
    } else {
      weaponEl.classList.remove('bobbing');
    }
  }
}

function isWall(x, y) {
  const mx = Math.floor(x);
  const my = Math.floor(y);
  if (mx < 0 || my < 0 || mx >= MAP_WIDTH || my >= MAP_HEIGHT) return true;
  return MAP[my][mx] === 1;
}

// Core Raycasting (DDA)
function castRay(rayAngle) {
  let rayX = player.x;
  let rayY = player.y;

  const dirX = Math.cos(rayAngle);
  const dirY = Math.sin(rayAngle);

  let mapX = Math.floor(rayX);
  let mapY = Math.floor(rayY);

  const deltaDistX = Math.abs(1 / dirX);
  const deltaDistY = Math.abs(1 / dirY);

  let sideDistX, sideDistY;
  let stepX, stepY;

  if (dirX < 0) {
    stepX = -1;
    sideDistX = (rayX - mapX) * deltaDistX;
  } else {
    stepX = 1;
    sideDistX = (mapX + 1 - rayX) * deltaDistX;
  }

  if (dirY < 0) {
    stepY = -1;
    sideDistY = (rayY - mapY) * deltaDistY;
  } else {
    stepY = 1;
    sideDistY = (mapY + 1 - rayY) * deltaDistY;
  }

  let hit = false;
  let side = 0; // 0 = vertical wall, 1 = horizontal
  let distance = 0;

  for (let i = 0; i < MAX_DEPTH; i++) {
    if (sideDistX < sideDistY) {
      sideDistX += deltaDistX;
      mapX += stepX;
      side = 0;
    } else {
      sideDistY += deltaDistY;
      mapY += stepY;
      side = 1;
    }

    if (mapX < 0 || mapY < 0 || mapX >= MAP_WIDTH || mapY >= MAP_HEIGHT) {
      distance = MAX_DEPTH;
      break;
    }

    if (MAP[mapY][mapX] === 1) {
      hit = true;
      if (side === 0) {
        distance = (mapX - rayX + (1 - stepX) / 2) / dirX;
      } else {
        distance = (mapY - rayY + (1 - stepY) / 2) / dirY;
      }
      break;
    }
  }

  return {
    distance: distance || MAX_DEPTH,
    side,
    hitX: rayX + dirX * (distance || MAX_DEPTH),
    hitY: rayY + dirY * (distance || MAX_DEPTH),
  };
}

// Render the 3D view
function render3D() {
  ctx.fillStyle = '#111';
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  // Ceiling
  const gradCeil = ctx.createLinearGradient(0, 0, 0, HEIGHT * 0.52);
  gradCeil.addColorStop(0, '#0a0806');
  gradCeil.addColorStop(1, '#1f1812');
  ctx.fillStyle = gradCeil;
  ctx.fillRect(0, 0, WIDTH, HEIGHT * 0.52);

  // Floor
  const gradFloor = ctx.createLinearGradient(0, HEIGHT * 0.48, 0, HEIGHT);
  gradFloor.addColorStop(0, '#1f1812');
  gradFloor.addColorStop(1, '#0d0905');
  ctx.fillStyle = gradFloor;
  ctx.fillRect(0, HEIGHT * 0.48, WIDTH, HEIGHT);

  const rayStep = FOV / NUM_RAYS;
  const startAngle = player.angle - FOV / 2;

  for (let i = 0; i < NUM_RAYS; i++) {
    const rayAngle = startAngle + i * rayStep;
    const ray = castRay(rayAngle);

    // Fix fish-eye
    let corrected = ray.distance * Math.cos(rayAngle - player.angle);
    if (corrected < 0.1) corrected = 0.1;

    const wallHeight = Math.min(HEIGHT, Math.floor((TILE / corrected) * (HEIGHT / 1.6)));
    const wallTop = Math.floor((HEIGHT - wallHeight) / 2);

    // Wall color by side + slight distance shading
    let intensity = Math.max(0.35, 1 - (corrected / MAX_DEPTH) * 0.9);
    let wallColor = ray.side === 0 ? '#6b4633' : '#4a3122';

    // Add a little variety per column
    if (i % 3 === 0) wallColor = ray.side === 0 ? '#5a3a29' : '#3f2a22';

    ctx.fillStyle = wallColor;

    // Draw the wall strip with simple "texture" lines
    const stripWidth = Math.ceil(WIDTH / NUM_RAYS) + 1;
    const x = Math.floor(i * (WIDTH / NUM_RAYS));

    ctx.fillRect(x, wallTop, stripWidth, wallHeight);

    // Vertical lines to fake texture
    ctx.fillStyle = `rgba(0,0,0,${ray.side === 0 ? 0.25 : 0.45})`;
    for (let t = 0; t < 3; t++) {
      const tx = x + Math.floor((stripWidth / 4) * (t + 1));
      ctx.fillRect(tx, wallTop, 1, wallHeight);
    }

    // Darker edges
    ctx.fillStyle = `rgba(0,0,0,${0.3 + (1 - intensity) * 0.3})`;
    ctx.fillRect(x, wallTop, stripWidth, 3); // top shadow
    ctx.fillRect(x, wallTop + wallHeight - 3, stripWidth, 3); // bottom
  }
}

// Enemy logic + rendering
function updateEnemies(dt) {
  if (!gameRunning || paused) return;

  enemies.forEach((enemy) => {
    if (!enemy.alive) return;

    const dx = player.x - enemy.x;
    const dy = player.y - enemy.y;
    const dist = Math.hypot(dx, dy);

    // Move toward player if not too close
    if (dist > 0.6) {
      const moveSpeed = enemy.speed * dt;
      const nx = enemy.x + (dx / dist) * moveSpeed;
      const ny = enemy.y + (dy / dist) * moveSpeed;

      if (!isWall(nx, enemy.y)) enemy.x = nx;
      if (!isWall(enemy.x, ny)) enemy.y = ny;
    }

    // Hurt player if very close
    if (dist < 0.75 && health > 0) {
      health -= 18 * dt;
      if (health <= 0) {
        health = 0;
        endGame(false);
      }
      updateHUD();
    }
  });
}

function renderEnemies() {
  // Collect visible sprites
  const sprites = [];

  enemies.forEach((enemy, idx) => {
    if (!enemy.alive) return;

    const dx = enemy.x - player.x;
    const dy = enemy.y - player.y;
    const dist = Math.hypot(dx, dy);

    let angleToEnemy = Math.atan2(dy, dx) - player.angle;
    // Normalize angle
    while (angleToEnemy > Math.PI) angleToEnemy -= Math.PI * 2;
    while (angleToEnemy < -Math.PI) angleToEnemy += Math.PI * 2;

    if (Math.abs(angleToEnemy) < FOV * 0.75 && dist > 0.2) {
      sprites.push({
        x: enemy.x,
        y: enemy.y,
        dist,
        angleToEnemy,
        size: enemy.size,
        health: enemy.health,
        idx
      });
    }
  });

  // Sort back-to-front
  sprites.sort((a, b) => b.dist - a.dist);

  sprites.forEach((sprite) => {
    const correctedDist = sprite.dist * Math.cos(sprite.angleToEnemy);
    if (correctedDist < 0.15) return;

    const spriteScreenX = Math.floor((WIDTH / 2) * (1 + sprite.angleToEnemy / (FOV / 2)));
    const spriteHeight = Math.floor((HEIGHT / correctedDist) * 1.35);
    const spriteWidth = Math.floor(spriteHeight * 0.7);
    const spriteTop = Math.floor((HEIGHT - spriteHeight) / 2);

    const x = spriteScreenX - spriteWidth / 2;

    // Draw enemy as a menacing red imp-like shape
    ctx.save();
    ctx.translate(x + spriteWidth / 2, spriteTop + spriteHeight * 0.35);

    const scale = spriteWidth / 48;

    // Body
    ctx.fillStyle = sprite.health > 1 ? '#9d2a1f' : '#6b1f15';
    ctx.fillRect(-18 * scale, -30 * scale, 36 * scale, 52 * scale);

    // Head
    ctx.fillStyle = '#3a1a14';
    ctx.beginPath();
    ctx.arc(0, -24 * scale, 13 * scale, 0, Math.PI * 2);
    ctx.fill();

    // Eyes (glowing)
    ctx.fillStyle = '#ffeb3b';
    ctx.fillRect(-7 * scale, -29 * scale, 4 * scale, 4 * scale);
    ctx.fillRect(3 * scale, -29 * scale, 4 * scale, 4 * scale);

    // Horns
    ctx.fillStyle = '#2a1f17';
    ctx.fillRect(-13 * scale, -40 * scale, 5 * scale, 14 * scale);
    ctx.fillRect(8 * scale, -40 * scale, 5 * scale, 14 * scale);

    ctx.restore();

    // Very simple distance fog
    if (sprite.dist > 5) {
      ctx.fillStyle = `rgba(10,8,6,${Math.min(0.6, (sprite.dist - 5) / 9)})`;
      ctx.fillRect(x, spriteTop, spriteWidth, spriteHeight);
    }
  });
}

// Shooting system
function shoot() {
  if (!gameRunning || paused || ammo <= 0) return;

  ammo--;
  updateHUD();

  // Visual + sound
  playSound('shoot');
  showMuzzleFlash();

  // Center screen ray for hitscan
  const hitRay = castRay(player.angle);

  let closestEnemy = null;
  let closestDist = Infinity;

  enemies.forEach((enemy, idx) => {
    if (!enemy.alive) return;

    const dx = enemy.x - player.x;
    const dy = enemy.y - player.y;
    const distToEnemy = Math.hypot(dx, dy);
    const angleToEnemy = Math.atan2(dy, dx);

    // Check if roughly in front of player and in the hitscan cone
    let diff = angleToEnemy - player.angle;
    while (diff > Math.PI) diff -= Math.PI * 2;
    while (diff < -Math.PI) diff += Math.PI * 2;

    const cone = 0.18; // generous

    if (Math.abs(diff) < cone && distToEnemy < hitRay.distance + 0.8 && distToEnemy < closestDist) {
      closestDist = distToEnemy;
      closestEnemy = { enemy, idx };
    }
  });

  if (closestEnemy) {
    const { enemy } = closestEnemy;
    enemy.health -= 1;

    playSound('hit');

    if (enemy.health <= 0) {
      enemy.alive = false;
      kills++;
      score += 250;
      playSound('death');

      // Check win condition
      if (enemies.every(e => !e.alive)) {
        setTimeout(() => endGame(true), 220);
      }
    } else {
      score += 35;
    }
    updateHUD();
  }
}

function showMuzzleFlash() {
  const muzzle = document.getElementById('muzzle');
  if (!muzzle) return;

  muzzle.classList.remove('hidden');
  muzzle.classList.add('muzzle-flash');

  setTimeout(() => {
    muzzle.classList.add('hidden');
    muzzle.classList.remove('muzzle-flash');
  }, 110);
}

// Simple bullet particles (purely visual)
function updateBullets(dt) {
  // We actually use instant hitscan, but we can add a few tracer effects if wanted.
  // For now bullets array is reserved for future expansion.
}

function updateHUD() {
  const healthEl = document.getElementById('health');
  const ammoEl = document.getElementById('ammo');
  const scoreEl = document.getElementById('score');
  const killsEl = document.getElementById('kills');

  if (healthEl) healthEl.textContent = Math.max(0, Math.floor(health));
  if (ammoEl) ammoEl.textContent = Math.max(0, ammo);
  if (scoreEl) scoreEl.textContent = String(Math.floor(score)).padStart(5, '0');
  if (killsEl) killsEl.innerHTML = `KILLS: <span class="text-white">${String(kills).padStart(2, '0')} / ${String(enemies.length).padStart(2, '0')}</span>`;
}

// Minimap
function renderMinimap() {
  const mctx = minimapCtx;
  const size = 160;
  const scale = size / (MAP_WIDTH * 1.1);

  mctx.fillStyle = '#0a0806';
  mctx.fillRect(0, 0, size, size);

  // Draw walls
  for (let y = 0; y < MAP_HEIGHT; y++) {
    for (let x = 0; x < MAP_WIDTH; x++) {
      if (MAP[y][x] === 1) {
        mctx.fillStyle = '#5a4636';
        mctx.fillRect(x * scale, y * scale, scale, scale);
      }
    }
  }

  // Draw enemies
  mctx.fillStyle = '#9d2a1f';
  enemies.forEach(e => {
    if (!e.alive) return;
    mctx.fillRect(e.x * scale - 1.5, e.y * scale - 1.5, 3.5, 3.5);
  });

  // Draw player
  mctx.fillStyle = '#ffeb3b';
  const px = player.x * scale;
  const py = player.y * scale;
  mctx.beginPath();
  mctx.arc(px, py, 3, 0, Math.PI * 2);
  mctx.fill();

  // Direction line
  mctx.strokeStyle = '#ffeb3b';
  mctx.lineWidth = 1.5;
  mctx.beginPath();
  mctx.moveTo(px, py);
  mctx.lineTo(px + Math.cos(player.angle) * 12, py + Math.sin(player.angle) * 12);
  mctx.stroke();
}

// Main game loop
function gameLoop(timestamp = 0) {
  if (!gameRunning) return;

  const dt = Math.min((timestamp - lastTime) / 1000 || 0.016, 0.05);
  lastTime = timestamp;
  frame++;

  if (!paused) {
    movePlayer(dt);
    updateEnemies(dt);
    updateBullets(dt);
  }

  // Render
  render3D();
  renderEnemies();
  renderMinimap();

  // Occasional enemy growl (very subtle)
  if (!paused && frame % 110 === 0 && Math.random() < 0.4) {
    // very quiet pain sound for atmosphere
    if (audioCtx && Math.random() < 0.3) playSound('pain');
  }

  updateHUD();

  // Game over overlay check
  if (health <= 0 && !paused) {
    // handled in updateEnemies already
  }

  requestAnimationFrame(gameLoop);
}

// Overlay helpers
function showOverlay(title, subtitle, duration = 1500) {
  const overlay = document.getElementById('overlay');
  const titleEl = document.getElementById('overlay-title');
  const subEl = document.getElementById('overlay-subtitle');

  titleEl.textContent = title;
  subEl.textContent = subtitle || '';
  overlay.classList.remove('hidden');
  overlay.classList.add('flex');

  if (duration < 9000) {
    setTimeout(() => {
      if (!paused) hideOverlay();
    }, duration);
  }
}

function hideOverlay() {
  const overlay = document.getElementById('overlay');
  overlay.classList.remove('flex');
  overlay.classList.add('hidden');
}

// End game
function endGame(won) {
  gameRunning = false;
  gameWon = won;
  paused = true;

  const overlay = document.getElementById('overlay');
  const titleEl = document.getElementById('overlay-title');
  const subEl = document.getElementById('overlay-subtitle');

  if (won) {
    playSound('win');
    titleEl.textContent = 'YOU WON';
    subEl.innerHTML = `DEMONS SLAIN: ${kills}<br>FINAL SCORE: ${Math.floor(score)}<br><span class="text-lg">Press R to replay</span>`;
    overlay.classList.remove('hidden');
    overlay.classList.add('flex');
  } else {
    titleEl.textContent = 'YOU DIED';
    subEl.innerHTML = `Score: ${Math.floor(score)}<br><span class="text-lg">Press R to try again</span>`;
    overlay.classList.remove('hidden');
    overlay.classList.add('flex');
  }
}

function restartGame() {
  // Full reset
  const overlay = document.getElementById('overlay');
  overlay.classList.add('hidden');
  overlay.classList.remove('flex');

  // Rebuild map enemy markers if needed (in case they were cleared)
  initGame();
}

// Boot the game automatically when the page loads
window.addEventListener('load', () => {
  initGame();

  // Helpful tip after a few seconds
  setTimeout(() => {
    const overlay = document.getElementById('overlay');
    if (overlay && overlay.classList.contains('hidden') && !paused && gameRunning) {
      // Only show if user is still alive and not already in overlay
    }
  }, 4800);
});

// Make functions available globally for buttons
window.restartGame = restartGame;
window.togglePause = togglePause;