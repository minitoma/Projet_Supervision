# Procédure à réaliser pour monitorer les bases de données PostgreSQL

# Utilisateur avec les droits de lectures uniquement 
```sql
CREATE USER readonly  WITH ENCRYPTED PASSWORD 'cestunbonmotcetruc';
GRANT USAGE ON SCHEMA public to readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly;

-- repeat code below for each database:

GRANT CONNECT ON DATABASE foo to readonly;
\c foo
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO readonly; --- this grants privileges on new tables generated in new database "foo"
GRANT USAGE ON SCHEMA public to readonly; 
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
```