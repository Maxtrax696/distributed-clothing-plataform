<<<<<<< HEAD
-- Tabla principal: usuarios (padre)
=======
-- Tabla de usuarios
>>>>>>> qa
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
<<<<<<< HEAD
    birth_date DATE,
    email VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone_number VARCHAR(50),
=======
    birth_date DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    phone_number VARCHAR(20),
>>>>>>> qa
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

<<<<<<< HEAD
-- Tabla de direcciones (cada usuario puede tener muchas)
=======
-- Tabla de perfiles
CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    full_name VARCHAR(255),
    birth_date DATE,
    phone_number VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Tabla de direcciones
>>>>>>> qa
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

<<<<<<< HEAD
-- Tabla de roles del sistema
=======
-- Tabla de roles
>>>>>>> qa
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

<<<<<<< HEAD
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
=======
-- Inserts iniciales
INSERT INTO roles (name, description)
SELECT 'cliente', 'Rol básico para usuarios registrados'
WHERE NOT EXISTS (SELECT 1 FROM roles WHERE name = 'cliente');

INSERT INTO roles (name, description)
SELECT 'administrator', 'Rol con privilegios de administrador'
WHERE NOT EXISTS (SELECT 1 FROM roles WHERE name = 'administrator');
>>>>>>> qa
