"""empty message

Revision ID: cd8478482956
Revises: e9e8381a3e24
Create Date: 2023-09-11 20:00:25.886856

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cd8478482956'
down_revision = 'e9e8381a3e24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson_response', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment_time', sa.DateTime(), nullable=True))
        batch_op.drop_column('command_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson_response', schema=None) as batch_op:
        batch_op.add_column(sa.Column('command_time', mysql.DATETIME(), nullable=True))
        batch_op.drop_column('comment_time')

    # ### end Alembic commands ###