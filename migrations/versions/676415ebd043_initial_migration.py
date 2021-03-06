"""Initial Migration

Revision ID: 676415ebd043
Revises: 28bdb9c5b33b
Create Date: 2020-02-19 14:15:32.257790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '676415ebd043'
down_revision = '28bdb9c5b33b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=1000), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('blog', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog'], ['blogs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
