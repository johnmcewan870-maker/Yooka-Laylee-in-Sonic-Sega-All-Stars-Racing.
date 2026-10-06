#!/usr/bin/env python3
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
SHEETS = ROOT / "sheets"
refs = {
    "racers.json": {"animation_set": ("animations.json","id"), "voice_set": ("audio.json","id"), "vehicle_id": ("vehicles.json","id"), "allstar_id": ("allstars.json","id")},
    "animations.json": {"racer_id": ("racers.json","id")},
    "audio.json": {"racer_id": ("racers.json","id")},
    "allstars.json": {"racer_id": ("racers.json","id"), "audio_ref": ("audio.json","id")},
    "menu.json": {"racer_id": ("racers.json","id")},
}
data = {}
for p in sorted(SHEETS.glob('*.json')):
    data[p.name] = json.loads(p.read_text())
indexes = {}
for name, doc in data.items():
    indexes[name] = {r.get('id') for r in doc['rows']}
issues=[]
for name, doc in data.items():
    cols=doc['columns']
    for i,row in enumerate(doc['rows']):
        for c in cols:
            if c not in row:
                issues.append(f'{name} row {i} missing column {c}')
                continue
            v=row[c]
            if v is None or v=="" or v==[] or v=={} or (isinstance(v,str) and 'UNVERIFIED' in v):
                issues.append(f'{name}:{row.get("id",i)}.{c} = {v!r}')
        for field,(target,key) in refs.get(name,{}).items():
            v=row.get(field)
            if v and isinstance(v,str) and 'UNVERIFIED' not in v and v not in indexes[target]:
                issues.append(f'{name}:{row.get("id",i)}.{field} -> {v!r} does not resolve in {target}.{key}')
print('PRE-FLIGHT REPORT')
print('=================')
if issues:
    print(f'BLOCKED: {len(issues)} unfinished/unverified cells or broken references')
    for x in issues: print('-',x)
    sys.exit(2)
print('CLEAN: every required cell is filled and references resolve')
