-- Tabla principal: usuarios (padre)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    email VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone_number VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de direcciones (cada usuario puede tener muchas)
CREATE TABLE IF NOT EXISTS addresses (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    street VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    address_type VARCHAR(50), -- shipping, billing
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Tabla de roles del sistema
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
);

-- Relación muchos a muchos: usuarios y roles
CREATE TABLE IF NOT EXISTS user_roles (
    user_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);

-- Roles predeterminados
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM roles WHERE name = 'cliente') THEN
        INSERT INTO roles (name, description) VALUES ('cliente', 'Rol básico para usuarios registrados');
    END IF;

    IF NOT EXISTS (SELECT 1 FROM roles WHERE name = 'administrator') THEN
        INSERT INTO roles (name, description) VALUES ('administrator', 'Rol con privilegios de administrador');
    END IF;
END $$;