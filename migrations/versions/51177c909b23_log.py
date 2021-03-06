"""log

Revision ID: 51177c909b23
Revises: 7ab4d664092e
Create Date: 2021-11-30 18:23:11.636200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51177c909b23'
down_revision = '7ab4d664092e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('events', sa.String(), nullable=True))
    op.drop_index('ix_log_Event', table_name='log')
    op.create_index(op.f('ix_log_events'), 'log', ['events'], unique=False)
    op.drop_column('log', 'Event')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('Event', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_log_events'), table_name='log')
    op.create_index('ix_log_Event', 'log', ['Event'], unique=False)
    op.drop_column('log', 'events')
    # ### end Alembic commands ###
