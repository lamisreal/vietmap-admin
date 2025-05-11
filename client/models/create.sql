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

ALTER TABLE information CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO superadmin (username, email, role, password) VALUES
('admin1', 'admin1@example.com', 'superadmin', 'e10adc3949ba59abbe56e057f20f883e'),
('admin2', 'admin2@example.com', 'superadmin', 'e10adc3949ba59abbe56e057f20f883e'),
('admin3', 'root@example.com', 'admin', 'e10adc3949ba59abbe56e057f20f883e');

INSERT INTO information (username, hoten, gioitinh, ngsinh) VALUES
('admin1', 'Cao Thanh Lâm', 'M', '1991-10-01 00:00:00'),
('admin2', 'Cao Trung Hiếu', 'M', '1995-05-20 00:00:00'),
('admin3', 'Lê Văn C', 'M', '1996-12-15 00:00:00');
