# Download premium assets
stone-cli assets download --type=racing-cars --quality=4k
// Shaders/track_effects.glsl
void applyMarketEffects() {
  if (marketDelta > 0) {
    emitGoldenSparks(position);
    trailColor = vec3(0.0, 1.0, 0.0); // Green upward trail
  } else {
    emitSmoke(position);
    trailColor = vec3(1.0, 0.0, 0.0); // Red downward trail
  }
}
/* Wyoming Luxury Theme */
: root {
  --gold: #FFD700;
  --leather: url('assets/luxury-leather.jpg');
  --diamond-sparkle: animation: sparkle 2s infinite;
}

body {
  background: var(--leather);
  color: var(--gold);
  font-family: 'Racing Sans One', sans-serif;
}
