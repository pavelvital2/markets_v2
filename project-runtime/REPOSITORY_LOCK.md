# REPOSITORY_LOCK

LOCK_STATUS:
accepted

WORKSPACE_TYPE:
project_workspace

PROJECT_SLUG:
markets_v2

EXPECTED_REMOTE:
https://github.com/pavelvital2/markets_v2.git

EXPECTED_GIT_REMOTE:
github.com/pavelvital2/markets_v2

EXPECTED_BRANCH:
main

ACTUAL_REMOTE_AT_LOCK:
https://github.com/pavelvital2/markets_v2.git

ACTUAL_GIT_REMOTE_AT_LOCK:
github.com/pavelvital2/markets_v2

ACTUAL_BRANCH_AT_LOCK:
main

PUSH_ALLOWED:
true

LOCK_ACCEPTED_BY:
project_owner

LOCK_ACCEPTED_AT:
2026-05-17T12:22:15Z

LOCK_ACCEPTANCE_REF:
User instruction: "Принимаю repository lock для github.com/pavelvital2/markets_v2 branch main. Baseline tracking разрешаю. PROJECT_INPUT_TRACKING_POLICY: owner-private/untracked"

PUSH_AUTHORIZATION_REF:
User instruction: "после локального checkpoint сделай пуш"

PROJECT_INPUT_TRACKING_POLICY_OVERRIDE:
tracked

PROJECT_INPUT_TRACKING_POLICY_OVERRIDE_REF:
User instruction: "PROJECT_INPUT_TRACKING_POLICY: tracked"

VALIDATION_EVIDENCE:
PROJECT_ROOT_EXPECTED=/home/pavel/projects/markets_v2; GIT_TOPLEVEL_ACTUAL=/home/pavel/projects/markets_v2; EXPECTED_GIT_REMOTE=github.com/pavelvital2/markets_v2; ACTUAL_GIT_REMOTE=github.com/pavelvital2/markets_v2; EXPECTED_BRANCH=main; ACTUAL_BRANCH=main

LAST_VALIDATED_AT:
2026-05-17T12:22:15Z

LAST_VALIDATION_STATUS:
passed

LAST_VALIDATION_ERROR:
NONE

LOCK_ACCEPTANCE_REQUIREMENTS:
- expected remote input is required
- expected branch input is required
- target .git must be rooted at PROJECT_ROOT_EXPECTED before lock acceptance
- ACTUAL_GIT_REMOTE must equal EXPECTED_GIT_REMOTE before lock acceptance
- ACTUAL_BRANCH must equal EXPECTED_BRANCH before lock acceptance
- PUSH_ALLOWED true requires LOCK_STATUS accepted
- test_fixture workspaces must keep PUSH_ALLOWED false

COPY_PROTECTION:
The package repository .git directory was not copied or reused.

BASELINE_TRACKING_REQUIREMENTS:
- Track agent-system/ in the project repository before first profile-agent dispatch.
- Track project-runtime/WORKSPACE_IDENTITY.md and project-runtime/REPOSITORY_LOCK.md before first profile-agent dispatch.
- Track runtime state records before first accepted checkpoint.
- Track .gitignore when it is used to govern baseline reproducibility.
- project-input/TZ.md may remain untracked only when owner-private/untracked input policy is explicit.
