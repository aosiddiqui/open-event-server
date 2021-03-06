"""empty message

Revision ID: 4591885edbf0
Revises: 6ffaeab2c3c2
Create Date: 2017-12-14 16:32:22.540831

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '4591885edbf0'
down_revision = '6ffaeab2c3c2'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('last_modified_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('sessions_version', sa.Column('last_modified_at', sa.DateTime(timezone=True), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sessions_version', 'last_modified_at')
    op.drop_column('sessions', 'last_modified_at')
    # ### end Alembic commands ###
