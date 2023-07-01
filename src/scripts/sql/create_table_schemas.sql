-- creating tables and their constrains
CREATE TABLE IF NOT EXISTS hired_employees (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR (60),
	datetime VARCHAR (60),
	department_id INTEGER,
	job_id INTEGER
);

CREATE TABLE IF NOT EXISTS departments (
	id INTEGER PRIMARY KEY NOT NULL,
	department VARCHAR (60)
);

CREATE TABLE IF NOT EXISTS jobs (
	id INTEGER PRIMARY KEY NOT NULL,
	job VARCHAR (120)
);

ALTER TABLE hired_employees ADD CONSTRAINT fk_hired_employees_departments FOREIGN KEY (department_id) REFERENCES departments (id);
ALTER TABLE hired_employees ADD CONSTRAINT fk_hired_employees_jobs FOREIGN KEY (job_id) REFERENCES jobs (id);