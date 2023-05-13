-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2023 at 02:45 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `walmart_visitors`
--

-- --------------------------------------------------------

--
-- Table structure for table `visitors_log`
--

CREATE TABLE `visitors_log` (
  `id` int(11) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `age_group` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `visitors_log`
--

INSERT INTO `visitors_log` (`id`, `gender`, `age_group`, `date`, `time`) VALUES
(4, 1, 1, '2023-04-01', '12:38:19'),
(5, 1, 2, '2023-04-07', '11:41:13'),
(6, 2, 3, '2023-04-07', '11:55:18'),
(7, 2, 5, '2023-04-07', '12:10:24'),
(8, 1, 5, '2023-04-07', '12:11:23');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `visitors_log`
--
ALTER TABLE `visitors_log`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `visitors_log`
--
ALTER TABLE `visitors_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
