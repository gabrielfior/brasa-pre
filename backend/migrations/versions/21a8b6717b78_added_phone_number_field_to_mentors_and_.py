"""Added phone number field to mentors and mentees

Revision ID: 21a8b6717b78
Revises: b1b9d640a5ad
Create Date: 2020-04-21 21:23:14.087402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21a8b6717b78'
down_revision = 'b1b9d640a5ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mentees', sa.Column('phone_number', sa.String(length=15), nullable=True))
    op.create_unique_constraint(None, 'mentees', ['phone_number'])
    op.add_column('mentors', sa.Column('phone_number', sa.String(length=15), nullable=True))
    op.create_unique_constraint(None, 'mentors', ['phone_number'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mentors', type_='unique')
    op.drop_column('mentors', 'phone_number')
    op.drop_constraint(None, 'mentees', type_='unique')
    op.drop_column('mentees', 'phone_number')
    # ### end Alembic commands ###
