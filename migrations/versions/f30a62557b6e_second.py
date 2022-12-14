"""second

Revision ID: f30a62557b6e
Revises: c145dcacb7b2
Create Date: 2022-09-07 19:46:52.133135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f30a62557b6e'
down_revision = 'c145dcacb7b2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('microblog posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(length=350), nullable=True),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microblog posts_id'), 'microblog posts', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_microblog posts_id'), table_name='microblog posts')
    op.drop_table('microblog posts')
    # ### end Alembic commands ###
