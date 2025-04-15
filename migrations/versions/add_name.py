"""add name

Revision ID: 6bb1ebe95530
Revises: e5d01cfe1a7b
Create Date: 2025-04-14 16:33:28.419912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bb1ebe95530'
down_revision = 'e5d01cfe1a7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
