cat microblog_backup.sql | docker exec -i postgres psql -U developer -d microblog_db
