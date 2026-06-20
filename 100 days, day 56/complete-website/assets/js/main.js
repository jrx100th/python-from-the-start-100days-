// ============================================
// Jenit's Complete Personal Website
// Interactive JavaScript
// ============================================

document.addEventListener('DOMContentLoaded', () => {
  initTailwind();
  initMobileMenu();
  initSmoothScroll();
  initScrollSpy();
  initProjectFilters();
  initProjectModals();
  initTestimonialCarousel();
  initContactForm();
  initScrollAnimations();
  initStatCounters();
  initNavbarScroll();
});

// Tailwind script configuration (play CDN)
function initTailwind() {
  // Tailwind is loaded via CDN in HTML. This enhances config at runtime.
  if (typeof tailwind !== 'undefined') {
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            'sans': ['Inter', 'system-ui', 'sans-serif']
          },
          colors: {
            primary: '#6366f1',
            accent: '#a855f7'
          }
        }
      }
    };
  }
}

// Mobile Hamburger Menu
function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (!menuBtn || !mobileMenu) return;

  menuBtn.addEventListener('click', () => {
    const isOpen = mobileMenu.classList.toggle('open');
    menuBtn.innerHTML = isOpen 
      ? `<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>`;
  });

  // Close on nav click (mobile)
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      menuBtn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>`;
    });
  });
}

// Smooth scrolling for all anchor links
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        e.preventDefault();
        const navOffset = 70;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.scrollY - navOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

// Navbar scroll effect + background
function initNavbarScroll() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;

    if (currentScroll > 50) {
      navbar.classList.add('bg-slate-900/95', 'backdrop-blur-lg', 'border-b', 'border-white/10');
    } else {
      navbar.classList.remove('bg-slate-900/95', 'backdrop-blur-lg', 'border-b', 'border-white/10');
    }

    lastScroll = currentScroll;
  });
}

// Active section highlighting (scrollspy)
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  function updateActiveLink() {
    let current = '';
    const scrollPosition = window.scrollY + 120;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (scrollPosition >= sectionTop) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', updateActiveLink, { passive: true });
  updateActiveLink(); // initial
}

// Project Filter System
function initProjectFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  if (!filterBtns.length || !projectCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Update active states
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;

      projectCards.forEach(card => {
        const categories = (card.dataset.categories || '').split(' ');

        if (filter === 'all' || categories.includes(filter)) {
          card.style.display = '';
          // trigger reflow for nice fade effect
          card.style.opacity = '0';
          setTimeout(() => {
            card.style.transition = 'opacity .25s ease, transform .3s ease';
            card.style.opacity = '1';
          }, 10);
        } else {
          card.style.transition = 'opacity .2s ease';
          card.style.opacity = '0';
          setTimeout(() => {
            card.style.display = 'none';
          }, 180);
        }
      });
    });
  });
}

// Project Modal
let currentModal = null;

function initProjectModals() {
  const cards = document.querySelectorAll('.project-card');
  const modal = document.getElementById('project-modal');
  const modalClose = document.getElementById('modal-close');
  const modalContent = document.getElementById('modal-content');

  if (!modal || !modalContent) return;

  // Project data (enriched for modal)
  const projectData = {
    'taskflow': {
      title: 'TaskFlow',
      subtitle: 'Modern Project & Task Management Platform',
      description: 'TaskFlow is a beautiful, fast, and collaborative task management tool. Built to replace cluttered spreadsheets and legacy tools. Features drag-and-drop kanban, real-time updates, team workspaces, powerful search, and beautiful reporting dashboards.',
      longDescription: 'I led the design and frontend architecture. The backend is a clean Python + FastAPI service. Key challenges included building a performant real-time sync layer (using WebSockets) and crafting delightful micro-interactions.',
      role: 'Lead Developer & Designer',
      duration: 'Jan 2025 – Mar 2025',
      impact: 'Used by 14,000+ professionals across 42 countries. Helped teams increase productivity by an average of 37%.',
      stack: ['React', 'Tailwind', 'Python', 'FastAPI', 'PostgreSQL', 'WebSockets'],
      live: 'https://taskflow-demo.vercel.app',
      github: 'https://github.com/jenit/taskflow',
      image: 'https://picsum.photos/id/1015/1200/630',
      category: 'Web App'
    },
    'pixelcraft': {
      title: 'PixelCraft',
      subtitle: 'Intuitive Vector Design Tool',
      description: 'A fast and elegant browser-based design tool for interface designers and marketers. Includes powerful pen tool, auto-layouts, real-time collaboration cursors, and export to SVG/PNG/PDF.',
      longDescription: 'Built completely from scratch using vanilla canvas APIs + React for the UI shell. I implemented a highly optimized rendering engine capable of handling 1000+ vector objects at 60fps.',
      role: 'Solo Founder & Developer',
      duration: 'Sep 2024 – Dec 2024',
      impact: 'Featured on Product Hunt. Reached #3 Product of the Day. 8.6k monthly active users.',
      stack: ['React', 'TypeScript', 'Canvas API', 'Tailwind', 'Vercel'],
      live: 'https://pixelcraft.design',
      github: 'https://github.com/jenit/pixelcraft',
      image: 'https://picsum.photos/id/160/1200/630',
      category: 'Design Tool'
    },
    'ecotrack': {
      title: 'EcoTrack',
      subtitle: 'Mobile Sustainability Companion',
      description: 'EcoTrack helps everyday people measure, reduce, and offset their carbon footprint. It uses smart heuristics, beautiful visualizations, gamification and integrates with Apple Health / Google Fit.',
      longDescription: 'My first serious cross-platform mobile project. I used React Native + Reanimated for buttery-smooth animations. The backend calculates personalized climate impact using real regional emissions data.',
      role: 'Full-stack Developer',
      duration: 'May 2024 – Aug 2024',
      impact: 'Featured by multiple climate organizations. Over 22k downloads. Average user reduces their footprint by 18%.',
      stack: ['React Native', 'Expo', 'Python', 'Node', 'MongoDB'],
      live: 'https://apps.apple.com/app/ecotrack',
      github: 'https://github.com/jenit/ecotrack',
      image: 'https://picsum.photos/id/201/1200/630',
      category: 'Mobile'
    },
    'devconnect': {
      title: 'DevConnect',
      subtitle: 'The Social Network for Developers',
      description: 'A focused community platform where developers showcase side projects, find collaborators, and get feedback on their work. Features threaded discussions, live coding rooms, and smart matching.',
      longDescription: 'Created because I wanted a less noisy alternative to Twitter + LinkedIn. Built with a modern stack and a very careful attention to community moderation tooling.',
      role: 'Creator & Engineer',
      duration: 'Ongoing (2024–)',
      impact: 'Community of 31,000+ developers. 120+ open source projects launched from within the platform.',
      stack: ['Next.js', 'TypeScript', 'Prisma', 'tRPC', 'PostgreSQL', 'Tailwind'],
      live: 'https://devconnect.app',
      github: 'https://github.com/jenit/devconnect',
      image: 'https://picsum.photos/id/251/1200/630',
      category: 'Web App'
    },
    'financedash': {
      title: 'FinanceDash',
      subtitle: 'Beautiful Personal Finance Dashboard',
      description: 'FinanceDash gives you total clarity over your finances. It connects to bank accounts, provides net worth tracking, beautiful spending breakdowns, goal tracking and smart budgeting recommendations powered by simple ML.',
      longDescription: 'The most polished product I have shipped. Everything was meticulously designed and animated. Includes a fully accessible data table experience and exportable reports.',
      role: 'Product Engineer',
      duration: 'Feb 2024 – Jun 2024',
      impact: 'Helps 6,800 users manage over $23M in assets. 4.96/5 average rating.',
      stack: ['Vue.js', 'Python', 'Plaid API', 'Chart.js', 'Tailwind'],
      live: 'https://financedash.app',
      github: 'https://github.com/jenit/financedash',
      image: 'https://picsum.photos/id/180/1200/630',
      category: 'Web App'
    },
    'wanderlust': {
      title: 'Wanderlust',
      subtitle: 'Immersive Travel Storytelling Platform',
      description: 'Wanderlust is a premium platform for travel creators. It provides gorgeous templates, rich multimedia embeds, interactive maps, and seamless monetization options for writers and photographers.',
      longDescription: 'Passion project built with a very small team. I designed the entire frontend experience and the custom rich text + map rendering system. Emphasis was placed on slow, beautiful loading and typography.',
      role: 'Design Engineer',
      duration: 'Oct 2023 – Feb 2024',
      impact: 'Featured by National Geographic Travel and over 40 travel creators. 200k monthly readers.',
      stack: ['Astro', 'Svelte', 'Mapbox', 'Sanity CMS', 'Tailwind'],
      live: 'https://wanderlust.studio',
      github: 'https://github.com/jenit/wanderlust',
      image: 'https://picsum.photos/id/1005/1200/630',
      category: 'UI/UX'
    }
  };

  // Attach click listeners to project cards
  cards.forEach(card => {
    const projectId = card.dataset.project;
    if (!projectId) return;

    // Make whole card clickable except buttons inside
    card.addEventListener('click', (e) => {
      // Ignore if user clicked one of the live/code buttons
      if (e.target.closest('a')) return;
      
      const data = projectData[projectId];
      if (data) openProjectModal(data, modal, modalContent);
    });

    // Also support keyboard access
    card.setAttribute('tabindex', '0');
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const data = projectData[projectId];
        if (data) openProjectModal(data, modal, modalContent);
      }
    });
  });

  // Close handlers
  if (modalClose) {
    modalClose.addEventListener('click', () => closeModal(modal));
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal(modal);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeModal(modal);
    }
  });

  function openProjectModal(data, modalEl, contentEl) {
    contentEl.innerHTML = `
      <div>
        <img src="${data.image}" alt="${data.title}" class="w-full h-64 md:h-80 object-cover rounded-xl mb-8 shadow-lg">
        
        <div class="flex items-center gap-x-3 mb-4">
          <span class="inline-block px-4 py-1 text-sm font-semibold rounded-full bg-indigo-500/10 text-indigo-400">${data.category}</span>
          <span class="text-slate-400 text-sm">${data.duration}</span>
        </div>

        <h2 class="text-4xl font-semibold tracking-tight mb-2">${data.title}</h2>
        <p class="text-xl text-slate-300 mb-6">${data.subtitle}</p>

        <div class="prose prose-invert max-w-none mb-8">
          <p class="text-lg text-slate-300">${data.description}</p>
          <p class="text-slate-400">${data.longDescription}</p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 mb-8">
          <div>
            <h4 class="uppercase tracking-[1px] text-xs font-semibold text-slate-500 mb-3">My Role</h4>
            <p class="text-slate-200">${data.role}</p>
          </div>
          <div>
            <h4 class="uppercase tracking-[1px] text-xs font-semibold text-slate-500 mb-3">Impact</h4>
            <p class="text-slate-200">${data.impact}</p>
          </div>
        </div>

        <div class="mb-8">
          <h4 class="uppercase tracking-[1px] text-xs font-semibold text-slate-500 mb-3">Tech Stack</h4>
          <div class="flex flex-wrap gap-2">
            ${data.stack.map(tech => `
              <span class="px-3.5 py-1 text-sm rounded-lg bg-slate-800 text-slate-300 border border-slate-700">${tech}</span>
            `).join('')}
          </div>
        </div>

        <div class="flex flex-wrap gap-4">
          <a href="${data.live}" target="_blank" rel="noopener"
             class="btn-primary inline-flex items-center justify-center gap-x-2 px-7 py-3.5 rounded-2xl text-white font-semibold text-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
            </svg>
            <span>View Live Project</span>
          </a>
          <a href="${data.github}" target="_blank" rel="noopener"
             class="inline-flex items-center justify-center gap-x-2 px-7 py-3.5 rounded-2xl border border-white/30 hover:bg-white/5 font-semibold text-sm transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            <span>View Source Code</span>
          </a>
        </div>
      </div>
    `;

    modalEl.classList.remove('hidden');
    modalEl.classList.add('flex');
    document.body.style.overflow = 'hidden';
    currentModal = modalEl;
  }

  function closeModal(modalEl) {
    modalEl.classList.remove('flex');
    modalEl.classList.add('hidden');
    document.body.style.overflow = '';
  }
}

// Testimonials simple auto-rotating carousel
function initTestimonialCarousel() {
  const track = document.getElementById('testimonial-track');
  const prevBtn = document.getElementById('testimonial-prev');
  const nextBtn = document.getElementById('testimonial-next');
  const dotsContainer = document.getElementById('testimonial-dots');

  if (!track) return;

  const slides = Array.from(track.children);
  if (slides.length === 0) return;

  let currentIndex = 0;
  let autoplayInterval = null;

  // Create dots
  if (dotsContainer) {
    slides.forEach((_, idx) => {
      const dot = document.createElement('button');
      dot.className = `w-2 h-2 rounded-full transition-all ${idx === 0 ? 'bg-indigo-400 w-6' : 'bg-slate-600 hover:bg-slate-500'}`;
      dot.addEventListener('click', () => goToSlide(idx));
      dotsContainer.appendChild(dot);
    });
  }

  function updateCarousel() {
    const offset = -currentIndex * 100;
    track.style.transform = `translateX(${offset}%)`;

    // update dots
    if (dotsContainer) {
      Array.from(dotsContainer.children).forEach((dot, i) => {
        if (i === currentIndex) {
          dot.className = 'w-6 h-2 rounded-full bg-indigo-400 transition-all';
        } else {
          dot.className = 'w-2 h-2 rounded-full bg-slate-600 hover:bg-slate-500 transition-all';
        }
      });
    }
  }

  function goToSlide(index) {
    currentIndex = index;
    updateCarousel();
    resetAutoplay();
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateCarousel();
  }

  function resetAutoplay() {
    if (autoplayInterval) clearInterval(autoplayInterval);
    autoplayInterval = setInterval(() => {
      nextSlide();
    }, 4800);
  }

  if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetAutoplay(); });
  if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetAutoplay(); });

  // Touch / swipe support
  let touchStartX = 0;

  track.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
  }, { passive: true });

  track.addEventListener('touchend', (e) => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
      if (diff > 0) nextSlide();
      else prevSlide();
      resetAutoplay();
    }
  });

  // Start autoplay
  resetAutoplay();

  // Pause on hover
  const container = track.parentElement;
  if (container) {
    container.addEventListener('mouseenter', () => clearInterval(autoplayInterval));
    container.addEventListener('mouseleave', resetAutoplay);
  }

  // Keyboard arrows
  document.addEventListener('keydown', (e) => {
    if (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowRight') { nextSlide(); resetAutoplay(); }
    if (e.key === 'ArrowLeft') { prevSlide(); resetAutoplay(); }
  });

  // Initial render
  updateCarousel();
}

// Contact Form Handling
function initContactForm() {
  const form = document.getElementById('contact-form');
  const statusEl = document.getElementById('form-status');

  if (!form || !statusEl) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const message = form.message.value.trim();

    // Very simple validation
    if (!name || !email || !message) {
      showStatus('Please fill out all fields.', 'error');
      return;
    }

    if (!isValidEmail(email)) {
      showStatus('Please enter a valid email address.', 'error');
      return;
    }

    // Simulate sending (in real world would POST to a serverless function)
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;

    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <span class="flex items-center justify-center gap-x-2">
        <svg class="animate-spin h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
        </svg>
        Sending...
      </span>
    `;

    await new Promise(resolve => setTimeout(resolve, 1150)); // simulate network

    // Success UI
    form.reset();
    submitBtn.disabled = false;
    submitBtn.innerHTML = originalText;

    showStatus(`Thanks, ${name.split(' ')[0]}! Your message has been sent. I'll get back to you within 24 hours.`, 'success');

    // Hide success after a while
    setTimeout(() => {
      if (statusEl.classList.contains('success')) {
        statusEl.classList.add('hidden');
      }
    }, 6200);
  });

  function showStatus(msg, type) {
    statusEl.textContent = msg;
    statusEl.className = `mt-4 text-sm p-3 rounded-xl border ${type === 'success' 
      ? 'bg-emerald-500/10 border-emerald-500/40 text-emerald-400 success' 
      : 'bg-red-500/10 border-red-500/40 text-red-400'}`;
    statusEl.classList.remove('hidden');
  }

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
}

// Subtle scroll-triggered entrance animations
function initScrollAnimations() {
  const animatedElements = document.querySelectorAll('.animate-on-scroll');

  if (!('IntersectionObserver' in window)) {
    // Fallback: just show all
    animatedElements.forEach(el => el.classList.add('opacity-100'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-fade-in-up');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

  animatedElements.forEach(el => {
    el.classList.add('opacity-0', 'translate-y-4');
    observer.observe(el);
  });

  // Inject animation styles once
  if (!document.getElementById('scroll-anim-styles')) {
    const style = document.createElement('style');
    style.id = 'scroll-anim-styles';
    style.textContent = `
      .animate-fade-in-up {
        animation: fadeInUp 0.65s cubic-bezier(0.22, 1, 0.36, 1) forwards;
      }
      @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(18px); }
        to { opacity: 1; transform: translateY(0); }
      }
    `;
    document.head.appendChild(style);
  }
}

// Animated number counters for stats
function initStatCounters() {
  const stats = document.querySelectorAll('.stat-number');

  if (!stats.length) return;

  const animateValue = (el, start, end, duration) => {
    const range = end - start;
    const startTime = performance.now();

    const step = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3); // easeOutCubic
      const value = Math.floor(start + range * ease);

      if (el.dataset.suffix) {
        el.textContent = value + el.dataset.suffix;
      } else {
        el.textContent = value.toLocaleString();
      }

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        if (el.dataset.suffix) el.textContent = end + el.dataset.suffix;
        else el.textContent = end.toLocaleString();
      }
    };

    requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const final = parseInt(el.dataset.count, 10) || 0;
        const suffix = el.dataset.suffix || '';

        animateValue(el, 0, final, 1450);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.6 });

  stats.forEach(stat => observer.observe(stat));
}

// Easter egg: Konami code → fun little animation on hero
(function konami() {
  const code = [38,38,40,40,37,39,37,39,66,65]; // ↑↑↓↓←→←→BA
  let pos = 0;
  document.addEventListener('keydown', (e) => {
    if (e.keyCode === code[pos]) {
      pos++;
      if (pos === code.length) {
        pos = 0;
        triggerKonami();
      }
    } else {
      pos = 0;
    }
  });

  function triggerKonami() {
    const hero = document.getElementById('hero');
    if (!hero) return;
    hero.style.transition = 'transform 120ms ease';
    hero.style.transform = 'scale(0.985)';
    setTimeout(() => {
      hero.style.transform = 'scale(1.005)';
    }, 120);
    setTimeout(() => {
      hero.style.transform = '';
      hero.style.transition = '';
    }, 420);

    // Bonus: temporarily boost accent colors
    document.documentElement.style.setProperty('--primary', '#f472b6');
    setTimeout(() => {
      document.documentElement.style.setProperty('--primary', '#6366f1');
    }, 1800);
  }
})();

console.log('%c[Jenit Site] Complete personal portfolio ready. Have a great day!', 'color:#64748b');