"""update users_tab

Revision ID: c096c24e1437
Revises: f7e48c242423
Create Date: 2023-10-03 21:27:42.357207

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c096c24e1437"
down_revision: Union[str, None] = "f7e48c242423"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("likes_tab_tweet_id_fkey", "likes_tab", type_="foreignkey")
    op.create_foreign_key(None, "likes_tab", "tweets_tab", ["tweet_id"], ["id"])
    op.create_unique_constraint(None, "users_tab", ["api_key"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users_tab", type_="unique")
    op.drop_constraint(None, "likes_tab", type_="foreignkey")
    op.create_foreign_key(
        "likes_tab_tweet_id_fkey", "likes_tab", "users_tab", ["tweet_id"], ["id"]
    )
    # ### end Alembic commands ###
