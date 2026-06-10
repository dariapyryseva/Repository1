"""add description to territories

Revision ID: 627f6beb2fcb
Revises: 001_create_territories_metrics
Create Date: 2026-06-10 00:12:04.800945

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "627f6beb2fcb"
down_revision: Union[str, Sequence[str], None] = "001_create_territories_metrics"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "territories",
        sa.Column("description", sa.String(length=500), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("territories", "description")
