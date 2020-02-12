"""private messaging added

Revision ID: 592f89894707
Revises: 45584388e23c
Create Date: 2020-02-13 00:27:55.129788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '592f89894707'
down_revision = '45584388e23c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    op.add_column('user', sa.Column('last_message_read_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_message_read_time')
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_table('message')
    # ### end Alembic commands ###