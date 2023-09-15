-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recipes
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema recipes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipes` DEFAULT CHARACTER SET utf8 ;
USE `recipes` ;

-- -----------------------------------------------------
-- Table `recipes`.`usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `recipes`.`usuarios` ;

CREATE TABLE IF NOT EXISTS `recipes`.`usuarios` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(245) NULL,
  `last_name` VARCHAR(245) NULL,
  `email` VARCHAR(245) NULL,
  `password` VARCHAR(245) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes`.`recetas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `recipes`.`recetas` ;

CREATE TABLE IF NOT EXISTS `recipes`.`recetas` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(245) NULL,
  `description` VARCHAR(245) NULL,
  `instruction` TEXT NULL,
  `date_cooked` DATE NULL,
  `cooking` TINYINT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `usuario_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recetas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_recetas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `recipes`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes`.`usuarios_recetas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `recipes`.`usuarios_recetas` ;

CREATE TABLE IF NOT EXISTS `recipes`.`usuarios_recetas` (
  `usuario_id` INT UNSIGNED NOT NULL,
  `receta_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`usuario_id`, `receta_id`),
  INDEX `fk_usuarios_has_recetas_recetas1_idx` (`receta_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_recetas_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_recetas_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `recipes`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_recetas_recetas1`
    FOREIGN KEY (`receta_id`)
    REFERENCES `recipes`.`recetas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
