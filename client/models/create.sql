ALTER DATABASE sql12778065 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE superadmin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(16) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE information (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(16) NOT NULL UNIQUE,
    hoten VARCHAR(50) NOT NULL,
    gioitinh CHAR(01) NOT NULL,
    ngsinh DATETIME NOT NULL
);

CREATE TABLE login_sessions (
    id INT AUTO_INCREMENT,
    username VARCHAR(16) NOT NULL,
    device_uuid CHAR(36) NOT NULL,
    created_at DATETIME,
    expired_at DATETIME,
    is_active BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id, username, device_uuid)
);

CREATE TABLE unit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    unit_code VARCHAR(4) NOT NULL,
    unit_name VARCHAR(30) NOT NULL,
    create_by VARCHAR(16) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_by VARCHAR(16),
    update_at TIMESTAMP,
    validflag VARCHAR(1) NOT NULL DEFAULT '1'
); -- unit_name = "Người"

CREATE TABLE captinh (
    id INT AUTO_INCREMENT PRIMARY KEY,
    province_code VARCHAR(4) NOT NULL,
    province_name VARCHAR(30) NOT NULL,
    create_by VARCHAR(16) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_by VARCHAR(16),
    update_at TIMESTAMP,
    validflag VARCHAR(1) NOT NULL DEFAULT '1'
);

CREATE TABLE dansotrungbinh (
    id INT AUTO_INCREMENT PRIMARY KEY,
    province_code VARCHAR(4) NOT NULL,
    unit_code VARCHAR(4) NOT NULL DEFAULT "HUMA",
    info_type VARCHAR(4) DEFAULT "DSTB", 
    create_by VARCHAR(16) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_by VARCHAR(16),
    update_at TIMESTAMP,
    validflag VARCHAR(1) NOT NULL DEFAULT '1'
);

CREATE TABLE thongtinsolieu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    province_code VARCHAR(4) NOT NULL,
    info_type VARCHAR(4) NOT NULL,
    info_year INT,
    info_quantity DECIMAL(16),
    create_by VARCHAR(16) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_by VARCHAR(16),
    update_at TIMESTAMP,
    validflag VARCHAR(1) NOT NULL DEFAULT '1'
);

ALTER TABLE information CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE captinh CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

--start
-- truy cập: https://www.phpmyadmin.co/db_sql.php?db=sql12778065

delete from `superadmin`
delete from `information`
delete from `login_sessions`

INSERT INTO superadmin (username, email, role, password) VALUES
('superadmin1', '23410165@ms.uit.edu.com', 'superadmin', 'e10adc3949ba59abbe56e057f20f883e'),
('superadmin2', '23410154@ms.uit.edu.com', 'superadmin', 'e10adc3949ba59abbe56e057f20f883e');
('admin1', 'admin1@ms.uit.edu.com', 'admin', 'e10adc3949ba59abbe56e057f20f883e');

INSERT INTO information (username, hoten, gioitinh, ngsinh) VALUES
('superadmin1', 'Cao Thanh Lâm', 'M', '1991-10-01 00:00:00'),
('superadmin2', 'Cao Trung Hiếu', 'M', '1995-05-20 00:00:00');
('admin1', 'admin1', 'M', '1997-12-20 00:00:00');

INSERT INTO unit (unit_code, unit_name, create_by) VALUES 
( 'HUMA', 'Người', 'admin1');
