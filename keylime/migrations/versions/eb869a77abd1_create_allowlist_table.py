"""create_allowlist_table

Revision ID: eb869a77abd1
Revises: ae898986c6e9
Create Date: 2021-01-12 10:54:45.263268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb869a77abd1'
down_revision = 'ae898986c6e9'
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
    op.create_table('allowlists',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(255), nullable=False),
                    sa.Column('tpm_policy', sa.Text(), nullable=True),
                    sa.Column('vtpm_policy', sa.Text(), nullable=True),
                    sa.Column('ima_policy', sa.Text().with_variant(sa.Text(length=429400000), "mysql"), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name', name='uniq_allowlists0name'),
                    mysql_engine='InnoDB',
                    mysql_charset='UTF8'
                    )


def downgrade_cloud_verifier():
    op.drop_table('allowlists')
