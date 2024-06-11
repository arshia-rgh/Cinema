"""empty message

Revision ID: b51500eb069a
Revises: 8ce4468d4077, c0f7521d0bd0
Create Date: 2024-06-11 15:15:25.313569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b51500eb069a'
down_revision: Union[str, None] = ('8ce4468d4077', 'c0f7521d0bd0')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
