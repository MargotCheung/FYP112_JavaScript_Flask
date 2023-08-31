"""empty message

Revision ID: a97146a6db9b
Revises: 9d6cc9f209fe
Create Date: 2023-08-31 23:36:21.691613

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a97146a6db9b'
down_revision = '9d6cc9f209fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lesson_response',
    sa.Column('index', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_name', sa.String(length=30), nullable=True),
    sa.Column('user_id', sa.String(length=30), nullable=True),
    sa.Column('response', sa.Text(), nullable=True),
    sa.Column('command_time', sa.DateTime(), nullable=True),
    sa.Column('liked', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_name'], ['course_info.course_name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_profile.username'], ),
    sa.PrimaryKeyConstraint('index')
    )
    op.create_table('user_grades',
    sa.Column('index', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=30), nullable=True),
    sa.Column('grade', sa.String(length=4), nullable=False),
    sa.Column('course_name', sa.String(length=30), nullable=True),
    sa.Column('course_type', sa.String(length=30), nullable=True),
    sa.Column('course_credit', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_credit'], ['course_info.course_credit'], ),
    sa.ForeignKeyConstraint(['course_name'], ['course_info.course_name'], ),
    sa.ForeignKeyConstraint(['course_type'], ['course_info.course_type'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_profile.username'], ),
    sa.PrimaryKeyConstraint('index')
    )
    op.drop_table('course_teacher')
    with op.batch_alter_table('course_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('course_year', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('course_type', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('course_credit', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('course_intro', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('math', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('coding', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('logic', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('creative', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('solve', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('math_txt', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('coding_txt', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('logic_txt', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('creative_txt', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('solve_txt', sa.Text(), nullable=True))
        batch_op.alter_column('course_id',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('course_name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=30),
               existing_nullable=False)
        batch_op.alter_column('teacher_name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=10),
               existing_nullable=False)
        batch_op.drop_column('id')

    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ability_coding', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('ability_logic', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('ability_creative', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('ability_solve', sa.Float(), nullable=True))
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.drop_column('ability_solve')
        batch_op.drop_column('ability_creative')
        batch_op.drop_column('ability_logic')
        batch_op.drop_column('ability_coding')

    with op.batch_alter_table('course_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
        batch_op.alter_column('teacher_name',
               existing_type=sa.String(length=10),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('course_name',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('course_id',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False,
               autoincrement=True)
        batch_op.drop_column('solve_txt')
        batch_op.drop_column('creative_txt')
        batch_op.drop_column('logic_txt')
        batch_op.drop_column('coding_txt')
        batch_op.drop_column('math_txt')
        batch_op.drop_column('solve')
        batch_op.drop_column('creative')
        batch_op.drop_column('logic')
        batch_op.drop_column('coding')
        batch_op.drop_column('math')
        batch_op.drop_column('course_intro')
        batch_op.drop_column('course_credit')
        batch_op.drop_column('course_type')
        batch_op.drop_column('course_year')

    op.create_table('course_teacher',
    sa.Column('course_name', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('tc_name', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('index', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user_grades')
    op.drop_table('lesson_response')
    # ### end Alembic commands ###
