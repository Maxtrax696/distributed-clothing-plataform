-- Base de datos ya está creada por Docker (users_db)

-- Tabla de perfiles de usuario
CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    full_name VARCHAR(255),
    birth_date DATE,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
