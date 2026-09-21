# MigrationMedic

> Portable agent for detecting suspicious duplicate database migration versions.

## What it does

MigrationMedic inspects migration filenames and looks for duplicate version numbers. When multiple migration files appear to claim the same version, it reports the evidence and recommends reviewing migration ordering.

### Diagnostic fingerprint

**Migration history → version collision → evidence → repair plan**

## Why this agent is distinct

MigrationMedic focuses on the temporal structure of database changes. It is not a schema-diff engine and does not assume that every naming irregularity is a production failure.

Its key signal is simple: multiple migration files containing the same version identifier.

## Workflow

```text
Migration files
      ↓
Version extraction
      ↓
Duplicate-version rule
      ↓
Evidence-backed finding
      ↓
Ordering / migration review
```

## Verification

The repository includes:
- OpenGAP passport metadata
- duplicate-version migration fixture
- behavior and explainability contracts
- four framework portability adapters
- automated adapter verification

OpenGAP validation passed and all four generated framework exports have been exercised successfully.

## Design principle

**Migration history is operational data.** MigrationMedic treats version collisions as an observable integrity signal and keeps the recommendation tied to that evidence.

## Medic family

MigrationMedic is the database-migration specialist in the Medic family, sharing the same portable passport contract while owning a distinct diagnostic domain.