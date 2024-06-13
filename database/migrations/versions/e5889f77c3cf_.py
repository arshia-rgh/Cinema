"""empty message

Revision ID: e5889f77c3cf
Revises: 3f8a2f87e4b6, 6748ce996cdd
Create Date: 2024-06-11 19:21:26.800427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5889f77c3cf'
down_revision: Union[str, None] = ('3f8a2f87e4b6', '6748ce996cdd')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
