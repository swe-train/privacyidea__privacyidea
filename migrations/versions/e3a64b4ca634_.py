"""v3.10: Add table nodename

Revision ID: e3a64b4ca634
Revises: 5cb310101a1f
Create Date: 2023-11-23 11:41:30.149153

"""

from datetime import datetime
from dateutil.tz import tzutc
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError, ProgrammingError

# revision identifiers, used by Alembic.
revision = "e3a64b4ca634"
down_revision = "5cb310101a1f"


def upgrade():
    try:
        # ### commands auto generated by Alembic - please adjust! ###
        op.create_table(
            "nodename",
            sa.Column("id", sa.Unicode(length=36), nullable=False),
            sa.Column("name", sa.Unicode(length=100), nullable=True),
            sa.Column(
                "lastseen",
                sa.DateTime(),
                nullable=True,
                default=datetime.now(tz=tzutc()),
            ),
            sa.PrimaryKeyConstraint("id"),
        )
        op.create_index(
            op.f("ix_nodename_lastseen"), "nodename", ["lastseen"], unique=False
        )
        op.create_index(op.f("ix_nodename_name"), "nodename", ["name"], unique=False)
        # ### end Alembic commands ###
    except (OperationalError, ProgrammingError) as exx:
        if "already exists" in str(exx.orig).lower():
            print("Ok, Table 'nodename' already exists.")
        else:
            print(exx)
    except Exception as exx:
        print("Could not add table 'nodename' to database")
        print(exx)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_nodename_name"), table_name="nodename")
    op.drop_index(op.f("ix_nodename_lastseen"), table_name="nodename")
    op.drop_table("nodename")
    # ### end Alembic commands ###
