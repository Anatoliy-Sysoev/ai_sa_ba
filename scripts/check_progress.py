#!/usr/bin/env python3
"""Считает прогресс по чек-боксам в checklist.md всех модулей."""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
modules = sorted((root / "modules").glob("*/checklist.md"))
total_done = total = 0
print(f"{'Модуль':40} {'done/all':>10}")
print("-" * 52)
for cl in modules:
    text = cl.read_text(encoding="utf-8")
    done = len(re.findall(r"- \[x\]", text, re.I))
    allb = len(re.findall(r"- \[[ x]\]", text, re.I))
    total_done += done; total += allb
    name = cl.parent.name
    print(f"{name:40} {f'{done}/{allb}':>10}")
print("-" * 52)
pct = (100 * total_done // total) if total else 0
print(f"{'ИТОГО':40} {f'{total_done}/{total}':>10}  ({pct}%)")
