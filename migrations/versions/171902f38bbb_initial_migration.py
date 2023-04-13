"""initial migration

Revision ID: 171902f38bbb
Revises: 
Create Date: 2023-04-13 21:38:43.158584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '171902f38bbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categories', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('icon', sa.String(length=30), nullable=True),
    sa.Column('text', sa.Text(length=20000), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('image_name', sa.String(length=30), nullable=True),
    sa.Column('image_alt', sa.String(length=80), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_user_id'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('article_category',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], name='fk_article_id'),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='fk_category_id'),
    sa.PrimaryKeyConstraint('article_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_category')
    op.drop_table('article')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
