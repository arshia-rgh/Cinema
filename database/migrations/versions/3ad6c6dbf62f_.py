"""empty message

Revision ID: 3ad6c6dbf62f
Revises: 0f18c0cbd6b8, 2d5d3e170b63
Create Date: 2024-06-12 21:16:45.511091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ad6c6dbf62f'
down_revision: Union[str, None] = ('0f18c0cbd6b8', '2d5d3e170b63')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
