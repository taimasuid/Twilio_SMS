"""empty message

Revision ID: 11931186e391
Revises: 792f35723f18
Create Date: 2020-06-04 09:17:27.131682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11931186e391'
down_revision = '792f35723f18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('shipped', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'shipped')
    # ### end Alembic commands ###
