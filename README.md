# Database for Test
# *******
## E-commerce
### 1. Customers Table
```
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT
)
```

## Education
```
CREATE TABLE platforms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    platform_id INTEGER,
    FOREIGN KEY (platform_id) REFERENCES platforms (id)
);

CREATE TABLE keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE solutions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problem_id INTEGER,
    query TEXT NOT NULL,
    keyword_id INTEGER,
    FOREIGN KEY (problem_id) REFERENCES problems (id),
    FOREIGN KEY (keyword_id) REFERENCES keywords (id)
);

```
