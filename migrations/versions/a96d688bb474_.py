"""empty message

Revision ID: a96d688bb474
Revises: 
Create Date: 2021-11-28 16:05:23.584751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a96d688bb474'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('species_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classification', sa.String(length=250), nullable=False),
    sa.Column('designation', sa.String(length=250), nullable=False),
    sa.Column('average_height', sa.Integer(), nullable=False),
    sa.Column('average_lifespan', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=250), nullable=False),
    sa.Column('eye_color', sa.String(length=250), nullable=False),
    sa.Column('homeworld', sa.String(length=250), nullable=False),
    sa.Column('language', sa.String(length=250), nullable=False),
    sa.Column('people', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('_password', sa.String(length=80), nullable=False),
    sa.Column('_is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('species_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['species_id'], ['species_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('speciesfavourites',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('species_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'species_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('speciesfavourites')
    op.drop_table('species')
    op.drop_table('user')
    op.drop_table('species_details')
    # ### end Alembic commands ###
