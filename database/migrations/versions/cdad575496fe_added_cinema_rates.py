"""added cinema_rates

Revision ID: cdad575496fe
Revises: e5889f77c3cf
Create Date: 2024-06-12 02:03:29.330101

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'cdad575496fe'
down_revision: Union[str, None] = 'e5889f77c3cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cinemas', 'rate',
               existing_type=mysql.SMALLINT(display_width=6),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('movies', 'rate',
               existing_type=mysql.SMALLINT(display_width=6),
               type_=sa.Float(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'rate',
               existing_type=sa.Float(),
               type_=mysql.SMALLINT(display_width=6),
               existing_nullable=True)
    op.alter_column('cinemas', 'rate',
               existing_type=sa.Float(),
               type_=mysql.SMALLINT(display_width=6),
               existing_nullable=True)
    # ### end Alembic commands ###
