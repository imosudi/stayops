#!/usr/bin/env bash
set -e

# Root project
PROJECT_ROOT="stayops"

# Create root-level files
mkdir -p "$PROJECT_ROOT"
touch "$PROJECT_ROOT/main.py" \
      "$PROJECT_ROOT/requirements.txt" \
      "$PROJECT_ROOT/pyproject.toml"

# Create the stayops package
STAYOPS_PKG="$PROJECT_ROOT/stayops"
mkdir -p "$STAYOPS_PKG"
touch "$STAYOPS_PKG/__init__.py" \
      "$STAYOPS_PKG/extensions.py"

# Config directory
mkdir -p "$STAYOPS_PKG/config"

# Domain structure
mkdir -p "$STAYOPS_PKG/domain/aggregates"
touch "$STAYOPS_PKG/domain/enums.py" \
      "$STAYOPS_PKG/domain/invariants.py"

# Application layer
mkdir -p "$STAYOPS_PKG/application/services" \
         "$STAYOPS_PKG/application/commands"

# Infrastructure layer
mkdir -p "$STAYOPS_PKG/infrastructure/db" \
         "$STAYOPS_PKG/infrastructure/events" \
         "$STAYOPS_PKG/infrastructure/repositories"

# GraphQL layer
mkdir -p "$STAYOPS_PKG/graphql"
touch "$STAYOPS_PKG/graphql/schema.py" \
      "$STAYOPS_PKG/graphql/queries.py" \
      "$STAYOPS_PKG/graphql/mutations.py"

# Migrations directory
mkdir -p "$PROJECT_ROOT/migrations"

echo "StayOps project structure scaffolded successfully."
