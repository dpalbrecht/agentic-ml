#!/usr/bin/env bash
# Install agentic-ml tooling into a target project directory.
#
# Usage:
#   ./install.sh /path/to/target-project
#
# Copies the tooling files (commands, Docker setup, conventions) into the target.
# Re-running overwrites tooling files but leaves project artifacts alone.

set -euo pipefail

# --- arg parsing ---
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 /path/to/target-project" >&2
    exit 1
fi

TARGET="$1"
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ ! -d "$TARGET" ]]; then
    echo "Target directory does not exist: $TARGET" >&2
    echo "Create it first (e.g. \`mkdir -p $TARGET\`) and re-run." >&2
    exit 1
fi

echo "Installing agentic-ml tooling into: $TARGET"
echo "From: $SOURCE"
echo

# --- files that get copied (and overwritten on re-run) ---
# Tooling files that define how the workflow operates.
TOOLING_FILES=(
    "CLAUDE.md"
    "Dockerfile"
    "requirements.txt"
)

# Slash commands for Claude Code.
COMMAND_FILES=(
    ".claude/commands/ml-frame.md"
    ".claude/commands/ml-explore.md"
    ".claude/commands/ml-design.md"
    ".claude/commands/ml-baseline.md"
    ".claude/commands/ml-experiment.md"
)

# --- directories that get created but never overwritten ---
# Project artifacts live here. Only created if missing.
PROJECT_DIRS=(
    ".ml-workflow"
    "data"
    "scripts"
    "experiments"
)

# --- copy tooling files (overwrite) ---
echo "Copying tooling files..."
for file in "${TOOLING_FILES[@]}"; do
    if [[ ! -f "$SOURCE/$file" ]]; then
        echo "  ! Missing source file: $file (skipping)" >&2
        continue
    fi
    mkdir -p "$TARGET/$(dirname "$file")"
    cp "$SOURCE/$file" "$TARGET/$file"
    echo "  ✓ $file"
done

# --- copy command files (overwrite) ---
echo
echo "Copying slash commands..."
for file in "${COMMAND_FILES[@]}"; do
    if [[ ! -f "$SOURCE/$file" ]]; then
        echo "  ! Missing source file: $file (skipping)" >&2
        continue
    fi
    mkdir -p "$TARGET/$(dirname "$file")"
    cp "$SOURCE/$file" "$TARGET/$file"
    echo "  ✓ $file"
done

# --- create project directories (don't overwrite) ---
echo
echo "Creating project directories..."
for dir in "${PROJECT_DIRS[@]}"; do
    if [[ -d "$TARGET/$dir" ]]; then
        echo "  · $dir/ (already exists)"
    else
        mkdir -p "$TARGET/$dir"
        echo "  ✓ $dir/"
    fi
done

echo
echo "Done. Next steps:"
echo "  1. cd $TARGET"
echo "  2. git init (if not already a git repo — required for Claude Code to pick up commands)"
echo "  3. Drop your dataset into data/"
echo "  4. Open Claude Code and run /ml-frame"
