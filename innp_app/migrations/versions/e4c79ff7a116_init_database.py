"""init database

Revision ID: e4c79ff7a116
Revises: 
Create Date: 2018-05-03 09:49:54.692249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c79ff7a116'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'miniac', ['dec'])
    op.create_unique_constraint(None, 'miniac', ['source'])
    op.create_unique_constraint(None, 'miniac', ['content'])
    op.create_unique_constraint(None, 'miniac', ['images'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'miniac', type_='unique')
    op.drop_constraint(None, 'miniac', type_='unique')
    op.drop_constraint(None, 'miniac', type_='unique')
    op.drop_constraint(None, 'miniac', type_='unique')
    # ### end Alembic commands ###