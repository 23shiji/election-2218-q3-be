create table records(
  ip_checksum varchar(64),
  content text
);

create table history(
  content text,
  created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP
);