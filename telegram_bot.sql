-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 07-Mar-2021 às 21:08
-- Versão do servidor: 10.4.11-MariaDB
-- versão do PHP: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `telegram_bot`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `admins`
--

CREATE TABLE `admins` (
  `ID` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `present` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `admins`
--

INSERT INTO `admins` (`ID`, `username`, `present`) VALUES
(222618635, 'GabrielGollo', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `commands`
--

CREATE TABLE `commands` (
  `comando` varchar(255) NOT NULL,
  `resultado` varchar(255) NOT NULL,
  `arguments` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `commands`
--

INSERT INTO `commands` (`comando`, `resultado`, `arguments`) VALUES
('add', 'self.database.insertMsg(\'{}\', \'{}\')', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `dicionario`
--

CREATE TABLE `dicionario` (
  `key-answer` varchar(255) NOT NULL,
  `answer` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `dicionario`
--

INSERT INTO `dicionario` (`key-answer`, `answer`) VALUES
('olá', 'Olá!\r\ntudo bem?');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`ID`,`username`);

--
-- Índices para tabela `commands`
--
ALTER TABLE `commands`
  ADD PRIMARY KEY (`comando`);

--
-- Índices para tabela `dicionario`
--
ALTER TABLE `dicionario`
  ADD PRIMARY KEY (`key-answer`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
