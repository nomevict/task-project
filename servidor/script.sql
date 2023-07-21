-- MySQL Script generated by MySQL Workbench
-- Mon May 22 19:50:59 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Drop schema if exists project_tarefa
DROP SCHEMA IF EXISTS `project_tarefa`;

-- Create schema project_tarefa
CREATE SCHEMA IF NOT EXISTS `project_tarefa` DEFAULT CHARACTER SET utf8;
USE `project_tarefa`;

-- Create table usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` INT AUTO_INCREMENT PRIMARY KEY,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  UNIQUE (username),
  UNIQUE (email)
)
ENGINE = InnoDB;

SELECT * FROM usuario;
DELETE FROM usuario WHERE id_usuario = 22;

-- Create table tarefa
CREATE TABLE IF NOT EXISTS `tarefa` (
  `id_tarefa`  INT AUTO_INCREMENT PRIMARY KEY,
  `titulo` VARCHAR(100) NOT NULL,
  `descricao` VARCHAR(500) NOT NULL,
  `prazo` DATE NOT NULL,
  `id_usuario` INT NOT NULL,
  `concluido` BOOLEAN DEFAULT 0,
  CONSTRAINT `usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
)
ENGINE = InnoDB;

SELECT * FROM tarefa;
-- DELETE FROM tarefa WHERE id_tarefa = 'uuuuu';
SHOW INDEX FROM `tarefa`;
ALTER TABLE `tarefa` DROP FOREIGN KEY usuario;
DROP INDEX `usuario` ON `tarefa`;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
