import os
from sqlalchemy import create_engine

link_database = os.environ.get('LINK_DATABASE_SQL', "must_be_set_in_env")

engine = create_engine(link_database)