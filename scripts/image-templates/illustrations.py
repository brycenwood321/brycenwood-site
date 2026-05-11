"""
SVG illustration templates for brycenwood.com.
Each function returns inline SVG markup matching the brand DNA
(dark bg, lime accent #00ff88, monospace details).
"""


def illu_dashboard_mockup():
    """Abstract business OS dashboard: header, KPI cards, sparkline, log feed."""
    return """
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0c0d14"/>
      <stop offset="100%" stop-color="#080910"/>
    </linearGradient>
    <linearGradient id="spark" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#00ff88" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#00ff88" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#00ff88" stroke-opacity="0.04" stroke-width="0.5"/>
    </pattern>
    <filter id="glow"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>

  <!-- Container -->
  <rect x="0" y="0" width="800" height="500" rx="8" fill="url(#bg)" stroke="#1c1e2a" stroke-width="1"/>
  <rect x="0" y="0" width="800" height="500" rx="8" fill="url(#grid)"/>

  <!-- Header bar -->
  <rect x="20" y="20" width="760" height="48" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
  <circle cx="44" cy="44" r="6" fill="#00ff88" filter="url(#glow)"/>
  <text x="62" y="48" font-family="'JetBrains Mono', monospace" font-size="11" fill="#e8e8f0" font-weight="600" letter-spacing="2">LIVE · BUSINESS OS</text>
  <text x="760" y="48" font-family="'JetBrains Mono', monospace" font-size="11" fill="#55556a" text-anchor="end">24/7</text>

  <!-- KPI cards row -->
  <g>
    <rect x="20" y="84" width="180" height="90" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
    <text x="34" y="106" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">REVENUE MTD</text>
    <text x="34" y="138" font-family="'Outfit', sans-serif" font-size="28" font-weight="800" fill="#e8e8f0">$48.2K</text>
    <text x="34" y="158" font-family="'JetBrains Mono', monospace" font-size="10" fill="#00ff88">↑ 24% vs LM</text>

    <rect x="212" y="84" width="180" height="90" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
    <text x="226" y="106" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">LEADS THIS WEEK</text>
    <text x="226" y="138" font-family="'Outfit', sans-serif" font-size="28" font-weight="800" fill="#e8e8f0">142</text>
    <text x="226" y="158" font-family="'JetBrains Mono', monospace" font-size="10" fill="#00ff88">↑ 18 vs LW</text>

    <rect x="404" y="84" width="180" height="90" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
    <text x="418" y="106" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">CLOSE RATE</text>
    <text x="418" y="138" font-family="'Outfit', sans-serif" font-size="28" font-weight="800" fill="#e8e8f0">31.2%</text>
    <text x="418" y="158" font-family="'JetBrains Mono', monospace" font-size="10" fill="#00ff88">↑ 2.4 pts</text>

    <rect x="596" y="84" width="184" height="90" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
    <text x="610" y="106" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">SYSTEMS LIVE</text>
    <text x="610" y="138" font-family="'Outfit', sans-serif" font-size="28" font-weight="800" fill="#e8e8f0">80+</text>
    <text x="610" y="158" font-family="'JetBrains Mono', monospace" font-size="10" fill="#55556a">all green</text>
  </g>

  <!-- Sparkline chart -->
  <g>
    <rect x="20" y="186" width="500" height="220" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
    <text x="34" y="208" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">REVENUE · LAST 30 DAYS</text>
    <text x="510" y="208" font-family="'JetBrains Mono', monospace" font-size="9" fill="#00ff88" text-anchor="end">+187%</text>

    <!-- Filled area under the line -->
    <path d="M 40,360 L 80,340 L 120,348 L 160,318 L 200,328 L 240,300 L 280,310 L 320,278 L 360,290 L 400,254 L 440,240 L 480,232 L 510,224 L 510,386 L 40,386 Z" fill="url(#spark)"/>
    <!-- Line -->
    <path d="M 40,360 L 80,340 L 120,348 L 160,318 L 200,328 L 240,300 L 280,310 L 320,278 L 360,290 L 400,254 L 440,240 L 480,232 L 510,224" fill="none" stroke="#00ff88" stroke-width="2" filter="url(#glow)"/>
    <!-- End point -->
    <circle cx="510" cy="224" r="5" fill="#00ff88" filter="url(#glow)"/>

    <!-- Axis dots -->
    <line x1="40" y1="386" x2="510" y2="386" stroke="#1c1e2a" stroke-width="1"/>
    <text x="40" y="402" font-family="'JetBrains Mono', monospace" font-size="8" fill="#55556a">Apr 10</text>
    <text x="510" y="402" font-family="'JetBrains Mono', monospace" font-size="8" fill="#55556a" text-anchor="end">May 10</text>
  </g>

  <!-- Activity log -->
  <g>
    <rect x="532" y="186" width="248" height="220" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
    <text x="546" y="208" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">ACTIVITY · LIVE</text>

    <g font-family="'JetBrains Mono', monospace" font-size="10">
      <circle cx="552" cy="232" r="3" fill="#00ff88"/>
      <text x="562" y="236" fill="#e8e8f0">lead.score 87 · WSJ</text>
      <text x="770" y="236" fill="#55556a" text-anchor="end">02:14</text>

      <circle cx="552" cy="256" r="3" fill="#00ff88"/>
      <text x="562" y="260" fill="#e8e8f0">email.send · 142</text>
      <text x="770" y="260" fill="#55556a" text-anchor="end">02:13</text>

      <circle cx="552" cy="280" r="3" fill="#00ff88"/>
      <text x="562" y="284" fill="#e8e8f0">review.req · job 4821</text>
      <text x="770" y="284" fill="#55556a" text-anchor="end">02:11</text>

      <circle cx="552" cy="304" r="3" fill="#00ff88"/>
      <text x="562" y="308" fill="#e8e8f0">cron · ghl.sync ok</text>
      <text x="770" y="308" fill="#55556a" text-anchor="end">02:10</text>

      <circle cx="552" cy="328" r="3" fill="#00ff88"/>
      <text x="562" y="332" fill="#e8e8f0">dm.reply · 3 sent</text>
      <text x="770" y="332" fill="#55556a" text-anchor="end">02:08</text>

      <circle cx="552" cy="352" r="3" fill="#00ff88"/>
      <text x="562" y="356" fill="#e8e8f0">invoice.paid · $4,200</text>
      <text x="770" y="356" fill="#55556a" text-anchor="end">02:05</text>

      <circle cx="552" cy="376" r="3" fill="#00ff88"/>
      <text x="562" y="380" fill="#e8e8f0">deploy · brycenwood</text>
      <text x="770" y="380" fill="#55556a" text-anchor="end">02:02</text>
    </g>
  </g>

  <!-- Bottom status bar -->
  <g>
    <rect x="20" y="418" width="760" height="62" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
    <circle cx="44" cy="449" r="5" fill="#00ff88" filter="url(#glow)"/>
    <text x="58" y="453" font-family="'JetBrains Mono', monospace" font-size="10" fill="#e8e8f0" font-weight="600">ALL SYSTEMS NOMINAL</text>
    <text x="58" y="468" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a">80/80 live · 10 APIs · 24 cron jobs</text>

    <g transform="translate(360,440)" font-family="'JetBrains Mono', monospace" font-size="9">
      <text x="0" y="0" fill="#55556a" letter-spacing="1.5">GHL</text><circle cx="20" cy="-3" r="3" fill="#00ff88"/>
      <text x="50" y="0" fill="#55556a" letter-spacing="1.5">IG</text><circle cx="64" cy="-3" r="3" fill="#00ff88"/>
      <text x="94" y="0" fill="#55556a" letter-spacing="1.5">YT</text><circle cx="110" cy="-3" r="3" fill="#00ff88"/>
      <text x="140" y="0" fill="#55556a" letter-spacing="1.5">GMAIL</text><circle cx="180" cy="-3" r="3" fill="#00ff88"/>
      <text x="210" y="0" fill="#55556a" letter-spacing="1.5">QB</text><circle cx="226" cy="-3" r="3" fill="#00ff88"/>
      <text x="256" y="0" fill="#55556a" letter-spacing="1.5">GSC</text><circle cx="278" cy="-3" r="3" fill="#00ff88"/>
    </g>

    <text x="760" y="453" font-family="'JetBrains Mono', monospace" font-size="9" fill="#00ff88" text-anchor="end">v 2.4.1</text>
    <text x="760" y="468" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" text-anchor="end">uptime: 47d 12h</text>
  </g>
</svg>
"""


def illu_system_flow():
    """Abstract automation pipeline: nodes connected by glowing edges."""
    return """
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0c0d14"/>
      <stop offset="100%" stop-color="#080910"/>
    </linearGradient>
    <pattern id="grid2" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#00ff88" stroke-opacity="0.04" stroke-width="0.5"/>
    </pattern>
    <radialGradient id="glow-orb" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#00ff88" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#00ff88" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow2"><feGaussianBlur stdDeviation="2.5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>

  <rect x="0" y="0" width="800" height="500" rx="8" fill="url(#bg2)" stroke="#1c1e2a" stroke-width="1"/>
  <rect x="0" y="0" width="800" height="500" rx="8" fill="url(#grid2)"/>

  <!-- Background glow orbs -->
  <circle cx="200" cy="120" r="180" fill="url(#glow-orb)"/>
  <circle cx="620" cy="380" r="200" fill="url(#glow-orb)"/>

  <!-- Connection lines (drawn before nodes so nodes overlap them) -->
  <g stroke="#00ff88" fill="none" filter="url(#glow2)">
    <!-- Lead source → CRM -->
    <path d="M 120 120 Q 200 130 280 180" stroke-width="1.5" stroke-opacity="0.6"/>
    <path d="M 120 200 Q 200 200 280 220" stroke-width="1.5" stroke-opacity="0.6"/>
    <path d="M 120 280 Q 200 270 280 260" stroke-width="1.5" stroke-opacity="0.6"/>
    <!-- CRM → branches -->
    <path d="M 380 220 Q 460 130 560 110" stroke-width="1.5" stroke-opacity="0.7"/>
    <path d="M 380 220 Q 460 220 560 220" stroke-width="1.5" stroke-opacity="0.7"/>
    <path d="M 380 260 Q 460 320 560 340" stroke-width="1.5" stroke-opacity="0.7"/>
    <!-- Branches → outcome -->
    <path d="M 660 110 Q 720 200 700 280" stroke-width="1.5" stroke-opacity="0.5"/>
    <path d="M 660 220 Q 720 240 700 280" stroke-width="1.5" stroke-opacity="0.5"/>
    <path d="M 660 340 Q 720 320 700 280" stroke-width="1.5" stroke-opacity="0.5"/>
  </g>

  <!-- Source nodes (left) -->
  <g font-family="'JetBrains Mono', monospace" font-size="11" fill="#e8e8f0">
    <g>
      <rect x="36" y="100" width="84" height="40" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
      <text x="78" y="124" text-anchor="middle">Forms</text>
    </g>
    <g>
      <rect x="36" y="180" width="84" height="40" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
      <text x="78" y="204" text-anchor="middle">Calls</text>
    </g>
    <g>
      <rect x="36" y="260" width="84" height="40" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
      <text x="78" y="284" text-anchor="middle">DMs</text>
    </g>
    <text x="78" y="80" text-anchor="middle" font-size="9" fill="#55556a" letter-spacing="1.5">LEAD SOURCES</text>
  </g>

  <!-- CRM hub (center) -->
  <g>
    <rect x="280" y="180" width="100" height="100" rx="6" fill="#0a0b12" stroke="#00ff88" stroke-width="1.5" filter="url(#glow2)"/>
    <text x="330" y="220" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">CRM</text>
    <text x="330" y="244" text-anchor="middle" font-family="'Outfit', sans-serif" font-size="20" font-weight="800" fill="#e8e8f0">AI</text>
    <text x="330" y="262" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8" fill="#00ff88">scoring · routing</text>
  </g>

  <!-- Action nodes (right of CRM) -->
  <g font-family="'JetBrains Mono', monospace" font-size="11" fill="#e8e8f0">
    <g>
      <rect x="560" y="90" width="100" height="40" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
      <text x="610" y="114" text-anchor="middle">Email seq.</text>
    </g>
    <g>
      <rect x="560" y="200" width="100" height="40" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
      <text x="610" y="224" text-anchor="middle">SMS / DM</text>
    </g>
    <g>
      <rect x="560" y="320" width="100" height="40" rx="4" fill="#0a0b12" stroke="#1c1e2a"/>
      <text x="610" y="344" text-anchor="middle">Review req.</text>
    </g>
    <text x="610" y="70" text-anchor="middle" font-size="9" fill="#55556a" letter-spacing="1.5">AUTOMATED ACTIONS</text>
  </g>

  <!-- Outcome node (right edge) -->
  <g>
    <circle cx="700" cy="280" r="44" fill="#0a0b12" stroke="#00ff88" stroke-width="1.5" filter="url(#glow2)"/>
    <text x="700" y="270" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9" fill="#55556a" letter-spacing="1.5">RESULT</text>
    <text x="700" y="294" text-anchor="middle" font-family="'Outfit', sans-serif" font-size="16" font-weight="800" fill="#00ff88">6× REV</text>
  </g>

  <!-- Stat strip at bottom -->
  <g>
    <line x1="40" y1="420" x2="760" y2="420" stroke="#1c1e2a"/>
    <g font-family="'JetBrains Mono', monospace" font-size="10">
      <text x="40" y="445" fill="#55556a" letter-spacing="2">RESPONSE TIME</text>
      <text x="40" y="465" fill="#00ff88" font-weight="700" font-size="14">&lt; 60s</text>

      <text x="220" y="445" fill="#55556a" letter-spacing="2">FOLLOW-UPS</text>
      <text x="220" y="465" fill="#00ff88" font-weight="700" font-size="14">24/7</text>

      <text x="400" y="445" fill="#55556a" letter-spacing="2">LEAD CAPTURE</text>
      <text x="400" y="465" fill="#00ff88" font-weight="700" font-size="14">100%</text>

      <text x="580" y="445" fill="#55556a" letter-spacing="2">NEW HEADCOUNT</text>
      <text x="580" y="465" fill="#00ff88" font-weight="700" font-size="14">0</text>
    </g>
  </g>

  <!-- Small label corner -->
  <text x="40" y="48" font-family="'JetBrains Mono', monospace" font-size="10" fill="#00ff88" letter-spacing="2.5">AUTOMATION PIPELINE</text>
  <text x="760" y="48" font-family="'JetBrains Mono', monospace" font-size="10" fill="#55556a" text-anchor="end" letter-spacing="2">BUILT WITH CLAUDE CODE</text>
</svg>
"""


def illu_terminal_code():
    """Faux terminal showing a Claude Code conversation."""
    return """
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0c0d14"/>
      <stop offset="100%" stop-color="#080910"/>
    </linearGradient>
    <filter id="glow3"><feGaussianBlur stdDeviation="2" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>

  <rect x="0" y="0" width="800" height="500" rx="8" fill="url(#bg3)" stroke="#1c1e2a"/>

  <!-- Terminal window chrome -->
  <rect x="40" y="40" width="720" height="420" rx="8" fill="#0a0b12" stroke="#1c1e2a"/>
  <rect x="40" y="40" width="720" height="32" rx="8" fill="#0d0e16"/>
  <rect x="40" y="62" width="720" height="10" fill="#0d0e16"/>
  <circle cx="60" cy="56" r="5" fill="#ff5f56" opacity="0.7"/>
  <circle cx="78" cy="56" r="5" fill="#ffbd2e" opacity="0.7"/>
  <circle cx="96" cy="56" r="5" fill="#27c93f" opacity="0.7"/>
  <text x="400" y="60" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="10" fill="#55556a">~ claude-code · summit-wraps</text>

  <!-- Terminal body -->
  <g font-family="'JetBrains Mono', monospace" font-size="12">
    <!-- User prompt -->
    <text x="60" y="105" fill="#00ff88">›</text>
    <text x="76" y="105" fill="#e8e8f0">Build me a lead scoring system that pulls</text>
    <text x="76" y="123" fill="#e8e8f0">contacts from GHL, scores each one A/B/C</text>
    <text x="76" y="141" fill="#e8e8f0">based on industry fit, and writes hot</text>
    <text x="76" y="159" fill="#e8e8f0">leads to Slack.</text>

    <!-- Claude response -->
    <rect x="60" y="180" width="14" height="14" rx="3" fill="#00ff88" filter="url(#glow3)"/>
    <text x="84" y="192" fill="#55556a" font-size="10" letter-spacing="1.5">CLAUDE · THINKING</text>

    <text x="60" y="220" fill="#e8e8f0">I'll build this in 4 steps:</text>
    <text x="60" y="244" fill="#00ff88">  1.</text><text x="90" y="244" fill="#e8e8f0">Pull contacts via GHL API</text>
    <text x="60" y="262" fill="#00ff88">  2.</text><text x="90" y="262" fill="#e8e8f0">Score each by industry × revenue</text>
    <text x="60" y="280" fill="#00ff88">  3.</text><text x="90" y="280" fill="#e8e8f0">Tag A/B/C in GHL custom field</text>
    <text x="60" y="298" fill="#00ff88">  4.</text><text x="90" y="298" fill="#e8e8f0">POST hot leads to Slack webhook</text>

    <!-- Tool call -->
    <text x="60" y="332" fill="#55556a" font-size="10" letter-spacing="1.5">⚙ TOOL · Write</text>
    <rect x="60" y="342" width="640" height="36" rx="4" fill="#0d0e16" stroke="#1c1e2a"/>
    <text x="76" y="358" fill="#e8e8f0" font-size="11">summit-wraps/lead-engine/score_and_route.py</text>
    <text x="76" y="372" fill="#00ff88" font-size="10">+ 142 lines</text>

    <!-- Final status -->
    <text x="60" y="408" fill="#55556a" font-size="10" letter-spacing="1.5">✓ DEPLOYED</text>
    <text x="60" y="430" fill="#e8e8f0">Live now. Cron set to fire every 5 min.</text>
    <text x="60" y="448" fill="#e8e8f0">First batch scored: 142 leads, 9 hot.</text>
  </g>
</svg>
"""


ILLUSTRATIONS = {
    "dashboard-mockup": illu_dashboard_mockup,
    "system-flow": illu_system_flow,
    "terminal-code": illu_terminal_code,
}
