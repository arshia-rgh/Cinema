"""BankAccount table added

Revision ID: 8ce4468d4077
Revises: cdbb410119e0
Create Date: 2024-06-09 18:50:43.812850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ce4468d4077'
down_revision: Union[str, None] = 'cdbb410119e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank_accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('card_number', sa.String(length=16), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('cvv2', sa.String(length=3), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('card_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bank_accounts')
    # ### end Alembic commands ###
