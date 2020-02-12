"""added user posts stories news tables

Revision ID: 4096071c3dd9
Revises: 
Create Date: 2020-02-11 23:34:48.051398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4096071c3dd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=5000), nullable=True),
    sa.Column('timeStamp', sa.DateTime(), nullable=True),
    sa.Column('sector', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_timeStamp'), 'news', ['timeStamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=200), nullable=True),
    sa.Column('about_me', sa.String(length=200), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('user_category', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=200), nullable=True),
    sa.Column('timeStamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timeStamp'), 'post', ['timeStamp'], unique=False)
    op.create_table('stories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=5000), nullable=True),
    sa.Column('timeStamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stories_timeStamp'), 'stories', ['timeStamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stories_timeStamp'), table_name='stories')
    op.drop_table('stories')
    op.drop_index(op.f('ix_post_timeStamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('followers')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_news_timeStamp'), table_name='news')
    op.drop_table('news')
    # ### end Alembic commands ###
