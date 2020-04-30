"""users jwt

Revision ID: 967b12181258
Revises: fe45835779a1
Create Date: 2019-10-16 10:54:25.439471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '967b12181258'
down_revision = 'fe45835779a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('token_expiration')
        batch_op.drop_column('token')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.VARCHAR(length=32), nullable=True))
        batch_op.add_column(sa.Column('token_expiration', sa.DATETIME(), nullable=True))

    # ### end Alembic commands ###