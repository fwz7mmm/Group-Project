"""empty message

Revision ID: 17694282ddad
Revises: 
Create Date: 2021-04-25 18:13:35.089227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17694282ddad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('birth', sa.String(length=50), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('userinfo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userinfo',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('user_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('password', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=True),
    sa.Column('phone', sa.INTEGER(), nullable=True),
    sa.Column('birth', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###