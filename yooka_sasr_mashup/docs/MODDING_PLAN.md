# Modding plan

1. Verify the installed PC build of Sonic & SEGA All-Stars Racing (Steam app 34190), including executable bitness/version and data layout.
2. Back up only files that a chosen mod route would alter.
3. Inventory public/community tooling for Sunshine Engine containers and prove one reversible read/write round-trip on a non-critical asset.
4. Identify a racer/vehicle slot strategy that does not ship original game files.
5. Fill `host_hooks.json` from evidence gathered on the installed game.
6. Run preflight; do not build while it reports BLOCKED.
7. Implement the smallest playable slice: character select -> Yooka & Laylee -> custom kart -> one solo race.
8. Add animations, audio/effects, then All-Star behavior.
9. Package only original mod assets/code/patches. Do not redistribute game assets.
10. Validate Melty recipe and one-click behavior before calling the release playable or publishable.
