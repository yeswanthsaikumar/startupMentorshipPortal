"""database created

Revision ID: 323414f830c5
Revises: 0bb30cde126d
Create Date: 2020-02-20 04:07:30.995695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '323414f830c5'
down_revision = '0bb30cde126d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_facebook', table_name='user')
    op.create_index(op.f('ix_user_facebook'), 'user', ['facebook'], unique=False)
    op.drop_index('ix_user_linkedin', table_name='user')
    op.create_index(op.f('ix_user_linkedin'), 'user', ['linkedin'], unique=False)
    op.drop_index('ix_user_twitter', table_name='user')
    op.create_index(op.f('ix_user_twitter'), 'user', ['twitter'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_twitter'), table_name='user')
    op.create_index('ix_user_twitter', 'user', ['twitter'], unique=True)
    op.drop_index(op.f('ix_user_linkedin'), table_name='user')
    op.create_index('ix_user_linkedin', 'user', ['linkedin'], unique=True)
    op.drop_index(op.f('ix_user_facebook'), table_name='user')
    op.create_index('ix_user_facebook', 'user', ['facebook'], unique=True)
    # ### end Alembic commands ###
