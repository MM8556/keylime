"""Store keyrings learned from IMA log

Revision ID: c3842cc9ee69
Revises: 257fe0f0c039
Create Date: 2021-09-14 13:12:29.306841

"""
from alembic import op
import sqlalchemy as sa

import keylime

# revision identifiers, used by Alembic.
revision = 'c3842cc9ee69'
down_revision = '257fe0f0c039'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_registrar():
    pass


def downgrade_registrar():
    pass


def upgrade_cloud_verifier():
    op.add_column('verifiermain', sa.Column('learned_ima_keyrings', keylime.db.verifier_db.JSONPickleType(), nullable=True))


def downgrade_cloud_verifier():
    op.drop_column('verifiermain', 'learned_ima_keyrings')
