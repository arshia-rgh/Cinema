"""user changed to customer

Revision ID: 2d5d3e170b63
Revises: dececa2dd09d
Create Date: 2024-06-12 15:00:07.786733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '2d5d3e170b63'
down_revision: Union[str, None] = 'dececa2dd09d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cinema_rates', sa.Column('customer_id', sa.Integer(), nullable=True))
    op.drop_constraint('cinema_rates_ibfk_2', 'cinema_rates', type_='foreignkey')
    op.create_foreign_key(None, 'cinema_rates', 'customers', ['customer_id'], ['id'], ondelete='CASCADE')
    op.drop_column('cinema_rates', 'user_id')
    op.add_column('movie_rates', sa.Column('customer_id', sa.Integer(), nullable=True))
    op.drop_constraint('movie_rates_ibfk_2', 'movie_rates', type_='foreignkey')
    op.create_foreign_key(None, 'movie_rates', 'customers', ['customer_id'], ['id'], ondelete='CASCADE')
    op.drop_column('movie_rates', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie_rates', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'movie_rates', type_='foreignkey')
    op.create_foreign_key('movie_rates_ibfk_2', 'movie_rates', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('movie_rates', 'customer_id')
    op.add_column('cinema_rates', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'cinema_rates', type_='foreignkey')
    op.create_foreign_key('cinema_rates_ibfk_2', 'cinema_rates', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('cinema_rates', 'customer_id')
    # ### end Alembic commands ###