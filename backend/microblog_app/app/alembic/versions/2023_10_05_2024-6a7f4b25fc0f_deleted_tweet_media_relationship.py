"""deleted Tweet - Media relationship

Revision ID: 6a7f4b25fc0f
Revises: 798fcab40b4b
Create Date: 2023-10-05 20:24:15.582238

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6a7f4b25fc0f"
down_revision: Union[str, None] = "798fcab40b4b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("medias_tab_tweet_id_fkey", "medias_tab", type_="foreignkey")
    op.drop_column("medias_tab", "tweet_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "medias_tab",
        sa.Column("tweet_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "medias_tab_tweet_id_fkey", "medias_tab", "tweets_tab", ["tweet_id"], ["id"]
    )
    # ### end Alembic commands ###