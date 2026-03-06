-- ==========================================
-- 1. DATABASE SETUP
-- ==========================================
CREATE DATABASE IF NOT EXISTS slot_booking;
USE slot_booking;

-- ==========================================
-- 2. TABLE CREATION
-- ==========================================
-- Table to manage the actual daily time slots
CREATE TABLE IF NOT EXISTS slots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    slot_time VARCHAR(50),
    booked BOOLEAN DEFAULT 0,
    booked_by VARCHAR(100) DEFAULT NULL
);

-- Table to keep a detailed history of all bookings
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    booking_date DATE,
    start_time TIME,
    status VARCHAR(20) DEFAULT 'Booked'
);

-- ==========================================
-- 3. INITIAL DATA (Seed Data)
-- ==========================================
-- Insert the standard working hours into the slots table
INSERT INTO slots (slot_time, booked, booked_by) VALUES
('09:00 AM - 10:00 AM', 0, NULL),
('10:00 AM - 11:00 AM', 0, NULL),
('11:00 AM - 12:00 PM', 0, NULL),
('12:00 PM - 01:00 PM', 0, NULL),
('02:00 PM - 03:00 PM', 0, NULL),
('03:00 PM - 04:00 PM', 0, NULL);


-- ==========================================
-- 4. OPERATIONAL QUERIES (For your Application)
-- ==========================================
-- Note: These are commented out with '--' so they don't run automatically 
-- during setup, but you will use these in your application code!

-- To view all available slots:
-- SELECT * FROM slots WHERE booked = 0;

-- To book a specific slot (e.g., booking slot id 1):
-- UPDATE slots SET booked = 1, booked_by = 'Customer Name' WHERE id = 1;

-- To cancel a booking (e.g., freeing up slot id 1):
-- UPDATE slots SET booked = 0, booked_by = NULL WHERE id = 1;

-- To add a brand new time slot to the schedule:
-- INSERT INTO slots (slot_time, booked) VALUES ('04:00 PM - 05:00 PM', 0);