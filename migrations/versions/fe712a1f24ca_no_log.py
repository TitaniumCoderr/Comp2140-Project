"""no log

Revision ID: fe712a1f24ca
Revises: 9957ce4d4b7b
Create Date: 2021-11-30 18:58:40.620012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe712a1f24ca'
down_revision = '9957ce4d4b7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('Event', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'Event')
    )
    # ### end Alembic commands ###