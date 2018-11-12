"""empty message

Revision ID: b57c5c750dba
Revises: dbc42c2cc690
Create Date: 2018-11-03 18:47:03.952237

"""

# revision identifiers, used by Alembic.
revision = 'b57c5c750dba'
down_revision = 'dbc42c2cc690'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('createddate', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'createddate')
    # ### end Alembic commands ###