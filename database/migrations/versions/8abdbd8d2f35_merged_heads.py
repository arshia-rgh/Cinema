"""merged heads

Revision ID: 8abdbd8d2f35
Revises: 8ce4468d4077, c0f7521d0bd0
Create Date: 2024-06-11 10:00:10.375015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8abdbd8d2f35'
down_revision: Union[str, None] = ('8ce4468d4077', 'c0f7521d0bd0')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
