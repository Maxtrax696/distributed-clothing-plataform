CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(255),
    birth_date DATE,
    phone_number VARCHAR(50)
);
