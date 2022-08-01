"""initial

Revision ID: 1f4fc673e1ba
Revises: 
Create Date: 2022-07-18 11:49:14.053263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f4fc673e1ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('parent_id', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('category_id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=24), nullable=False),
    sa.Column('date_created', sa.TIMESTAMP(), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=8, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('categories')
    # ### end Alembic commands ###
