# Repository Hygiene & Branch Strategy

To maintain the operational integrity and proprietary perception of the AI Visibility Intelligence infrastructure, the following hygiene practices are recommended.

## Branch Management Strategy

The repository structure should reflect a stable, professionally engineered deployment environment. Unnecessary or abandoned branches dilute the perceived maturity of the system.

### Active Branches
- **`main`**: The canonical operational branch. Must always represent stable, production-ready assessment infrastructure.
- **`feature/rebrand-perception-layer`**: The active commercial hardening branch (current operation). Once integrated into `main`, this branch should be safely archived and removed from active visibility.

### Safe Cleanup Recommendations
1. **Consolidate Abandoned Forks/Branches**: Any branches inheriting legacy nomenclature (e.g., branches prefixed with `geo-seo-claude-updates` or similar legacy tags) should be re-evaluated. If they contain no proprietary improvements, they should be safely deleted.
2. **Post-Merge Archival**: After a feature branch successfully undergoes perception-layer refactoring and is merged into `main`, it should be deleted.
3. **Naming Conventions**: Future branches should reflect intelligence capabilities rather than "tool hacking" (e.g., `feature/crawler-diagnostics-upgrade` instead of `fix/geo-bot`).

## Commit History & Identity
Ensure all commits and merge strategies utilize the centralized identity (`Abderraouf-yt`, AI Visibility Engineer). Mixed identities or unverified commits suggest fragmented freelancer work rather than proprietary infrastructure engineering.

**Do Not Execute Destructive Actions Automatically.** Always manually verify branch content before archival to ensure no operational logic is lost.
