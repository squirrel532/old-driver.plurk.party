"""empty message

Revision ID: 6d904f63c88e
Revises: 5f7c33ddc6ac
Create Date: 2019-07-27 02:42:36.971809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d904f63c88e'
down_revision = '5f7c33ddc6ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plurks', sa.Column('author', sa.Integer(), nullable=True))
    op.add_column('plurks', sa.Column('author_avatar', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plurks', 'author_avatar')
    op.drop_column('plurks', 'author')
    # ### end Alembic commands ###
