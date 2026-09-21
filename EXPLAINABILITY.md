# Explainability Contract: MigrationMedic

## Decision

MigrationMedic decides whether multiple migration files contain duplicate version numbers. A detected collision is reported as a migration-ordering risk with evidence and a practical remediation.

## Inputs

It uses migration-related filenames and extracts numeric version tokens from the scanned project file list. The decision comes from comparing the number of migration files with the set of distinct version numbers.

## Limits

It cannot determine the semantic correctness of a migration sequence or whether two files intentionally share a version under a custom migration system. Dynamically generated migrations and database metadata outside the repository are not observed.
