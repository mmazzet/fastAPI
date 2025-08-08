"""add content column to post table

Revision ID: 59a761a27ca4
Revises: 892155c3ca2e
Create Date: 2025-08-08 22:05:27.843647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59a761a27ca4'
down_revision: Union[str, Sequence[str], None] = '892155c3ca2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
