"""Create Table Planetas

Revision ID: 981b8bba3f5a
Revises: 
Create Date: 2024-09-20 10:45:00.978764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '981b8bba3f5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetas',
    sa.Column('id_planeta', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('distancia_sol', sa.Integer(), nullable=True),
    sa.Column('numero_satelites', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_planeta')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planetas')
    # ### end Alembic commands ###
