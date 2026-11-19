#!/usr/bin/env python3
"""Resolve merge conflict blocks in README.md by keeping the HEAD (ours) side."""

path = "README.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Before fix:")
print("  <<<<<<< HEAD count:", sum(1 for l in lines if l.strip() == "<<<<<<< HEAD"))
print("  ======= count:", sum(1 for l in lines if l.strip() == "======="))
print("  >>>>>>> count:", sum(1 for l in lines if l.strip() == ">>>>>>>"))

# Find conflict blocks
blocks = []
i = 0
while i < len(lines):
    if lines[i].strip() == "<<<<<<< HEAD" and i + 2 < len(lines):
        eq = None
        gt = None
        for j in range(i + 1, len(lines)):
            if lines[j].strip() == "=======":
                eq = j
                break
        if eq is not None:
            for j in range(eq + 1, len(lines)):
                if lines[j].strip() == ">>>>>>>":
                    gt = j
                    break
        if eq is not None and gt is not None:
            blocks.append((i, eq, gt))
            i = gt + 1
            continue
    i += 1

print(f"\nFound {len(blocks)} conflict blocks:")
for b in blocks:
    print(f"  block at 0-based [{b[0]},{b[1]},{b[2]}] = lines [{b[0]+1},{b[1]+1},{b[2]+1}]")

if not blocks:
    print("No conflict blocks found. Nothing to do.")
    exit(0)

# Build corrected file
new_lines = []
i = 0
while i < len(lines):
    if lines[i].strip() == "<<<<<<< HEAD" and i + 2 < len(lines):
        eq = None
        for j in range(i + 1, len(lines)):
            if lines[j].strip() == "=======":
                eq = j
                break
        if eq is not None:
            gt = None
            for j in range(eq + 1, len(lines)):
                if lines[j].strip() == ">>>>>>>":
                    gt = j
                    break
            if gt is not None:
                # Keep our content: lines[i+1 : eq] (exclusive of eq)
                new_lines.extend(lines[i+1 : eq])
                # Skip to after end marker
                i = gt + 1
                continue
    new_lines.append(lines[i])
    i += 1

with open(path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

# Verify
with open(path, "r", encoding="utf-8") as f:
    new_content = f.read()
new_lines = new_content.split("\n")
print(f"\nAfter fix:")
print(f"  <<<<<<< HEAD count: {sum(1 for l in new_lines if l.strip() == '<<<<<<< HEAD')}")
print(f"  ======= count: {sum(1 for l in new_lines if l.strip() == '=======')}")
print(f"  >>>>>>> count: {sum(1 for l in new_lines if l.strip() == '>>>>>>>')}")
print(f"  Total lines: {len(new_lines)}")
