
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pets (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    species VARCHAR(20) NOT NULL,
    breed VARCHAR(50),
    birth_year INTEGER,
    weight DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS veterinarians (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    license_number VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS doctor_schedules (
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER NOT NULL REFERENCES veterinarians(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    UNIQUE(doctor_id, date)
);

CREATE TABLE IF NOT EXISTS appointments (
    id SERIAL PRIMARY KEY,
    pet_id INTEGER NOT NULL REFERENCES pets(id) ON DELETE CASCADE,
    doctor_id INTEGER NOT NULL REFERENCES veterinarians(id),
    service_id INTEGER NOT NULL REFERENCES services(id),
    schedule_id INTEGER NOT NULL REFERENCES doctor_schedules(id),
    appointment_time TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'scheduled',
    symptoms TEXT,
    diagnosis TEXT,
    recommendations TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для ускорения поиска
CREATE INDEX IF NOT EXISTS idx_appointments_status ON appointments(status);
CREATE INDEX IF NOT EXISTS idx_appointments_time ON appointments(appointment_time);
CREATE INDEX IF NOT EXISTS idx_pets_owner_id ON pets(owner_id);
