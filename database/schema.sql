
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20) UNIQUE,
    email VARCHAR(100)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(id),
    name VARCHAR(50),
    species VARCHAR(30),
    breed VARCHAR(50)
);

CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    pet_id INTEGER REFERENCES pets(id),
    doctor_id INTEGER REFERENCES doctors(id),
    appointment_date TIMESTAMP,
    status VARCHAR(20) DEFAULT 'scheduled'
);
