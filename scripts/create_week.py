#!/usr/bin/env python3
"""Создаёт новый модуль из templates/module-template.
Usage: python scripts/create_week.py M2-W05-rag-indexing "RAG indexing"
"""
import sys, shutil, pathlib

if len(sys.argv) < 2:
    print("Usage: create_week.py <dir-name> [title]"); sys.exit(1)
name = sys.argv[1]
title = sys.argv[2] if len(sys.argv) > 2 else name
root = pathlib.Path(__file__).resolve().parent.parent
src = root / "templates" / "module-template"
dst = root / "modules" / name
if dst.exists():
    print(f"{dst} уже существует"); sys.exit(1)
shutil.copytree(src, dst)
for md in dst.rglob("*.md"):
    md.write_text(md.read_text(encoding="utf-8").replace("{{MODULE}}", name).replace("{{TITLE}}", title), encoding="utf-8")
print(f"Создан модуль: {dst}")
