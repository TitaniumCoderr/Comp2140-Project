"""empty message

Revision ID: 34c8c08c2cc1
Revises: 51177c909b23
Create Date: 2021-11-30 18:24:33.548503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34c8c08c2cc1'
down_revision = '51177c909b23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('log', 'Event')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('Event', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
