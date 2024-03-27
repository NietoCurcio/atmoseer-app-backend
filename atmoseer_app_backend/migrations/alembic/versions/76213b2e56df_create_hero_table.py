"""create hero table

Revision ID: 76213b2e56df
Revises: 
Create Date: 2024-03-26 18:54:59.684116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76213b2e56df'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'hero',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('secret_name', sa.String(50)),
        sa.Column('age', sa.Integer, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('hero')
