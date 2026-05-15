"""Phase 0 foundational migration plan placeholder.

This revision intentionally does not create tables yet. It reserves the first
transactional migration anchor and captures the ordered schema plan that
subsequent revisions will implement.
"""

# pylint: disable=invalid-name,no-member

from __future__ import annotations

from collections.abc import Sequence

from alembic import op

revision: str = "20260512_000001"
down_revision: str | None = None
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    """Record the migration anchor for phase-zero transactional schema rollout."""

    op.execute("SELECT 1")


def downgrade() -> None:
    """Downgrade the migration anchor."""

    op.execute("SELECT 1")
