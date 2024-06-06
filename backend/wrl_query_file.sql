-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema wrl
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `wrl` ;

-- -----------------------------------------------------
-- Schema wrl
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wrl` DEFAULT CHARACTER SET utf8 ;
USE `wrl` ;

-- -----------------------------------------------------
-- Table `wrl`.`department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`department` ;

CREATE TABLE IF NOT EXISTS `wrl`.`department` (
  `department_id` INT NOT NULL AUTO_INCREMENT,
  `dep_code` VARCHAR(7) NOT NULL,
  `dep_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`department_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`campus`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`campus` ;

CREATE TABLE IF NOT EXISTS `wrl`.`campus` (
  `campus_id` INT NOT NULL AUTO_INCREMENT,
  `campus_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`campus_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`program`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`program` ;

CREATE TABLE IF NOT EXISTS `wrl`.`program` (
  `program_id` INT NOT NULL AUTO_INCREMENT,
  `prog_code` VARCHAR(45) NOT NULL,
  `prog_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`program_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`level`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`level` ;

CREATE TABLE IF NOT EXISTS `wrl`.`level` (
  `level_id` INT NOT NULL,
  `level_code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`level_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`city`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`city` ;

CREATE TABLE IF NOT EXISTS `wrl`.`city` (
  `city_id` INT NOT NULL AUTO_INCREMENT,
  `city_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`city_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`company`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`company` ;

CREATE TABLE IF NOT EXISTS `wrl`.`company` (
  `company_id` INT NOT NULL AUTO_INCREMENT,
  `comp_name` VARCHAR(45) NOT NULL,
  `comp_country` VARCHAR(45) NOT NULL,
  `comp_phone` INT(15) NOT NULL,
  `comp_email` VARCHAR(45) NOT NULL,
  `comp_startdate` DATE NOT NULL,
  `city_id` INT NOT NULL,
  PRIMARY KEY (`company_id`, `city_id`),
  INDEX `fk_company_city1_idx` (`city_id` ASC) VISIBLE,
  CONSTRAINT `fk_company_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `wrl`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`supervisor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`supervisor` ;

CREATE TABLE IF NOT EXISTS `wrl`.`supervisor` (
  `supervisor_id` INT NOT NULL AUTO_INCREMENT,
  `sup_fname` VARCHAR(45) NOT NULL,
  `sup_lname` VARCHAR(45) NOT NULL,
  `staff_id` VARCHAR(20) NOT NULL,
  `sup_phone` VARCHAR(9) NOT NULL,
  `sup_email` VARCHAR(45) NOT NULL,
  `campus_id` INT NOT NULL,
  PRIMARY KEY (`supervisor_id`),
  INDEX `fk_supervisor_campus1_idx` (`campus_id` ASC) VISIBLE,
  CONSTRAINT `fk_supervisor_campus1`
    FOREIGN KEY (`campus_id`)
    REFERENCES `wrl`.`campus` (`campus_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`student` ;

CREATE TABLE IF NOT EXISTS `wrl`.`student` (
  `student_id` INT NOT NULL,
  `student_fname` VARCHAR(45) NOT NULL,
  `student_lname` VARCHAR(45) NOT NULL,
  `reg_number` VARCHAR(15) NOT NULL,
  `student_phone` INT(9) NOT NULL,
  `student_email` VARCHAR(45) NOT NULL,
  `department_id` INT NOT NULL,
  `campus_id` INT NOT NULL,
  `program_id` INT NOT NULL,
  `level_id` INT NOT NULL,
  `company_id` INT NULL,
  `supervisor_id` INT NULL,
  PRIMARY KEY (`student_id`),
  INDEX `fk_student_department_idx` (`department_id` ASC) VISIBLE,
  INDEX `fk_student_campus1_idx` (`campus_id` ASC) VISIBLE,
  INDEX `fk_student_program1_idx` (`program_id` ASC) VISIBLE,
  INDEX `fk_student_level1_idx` (`level_id` ASC) VISIBLE,
  INDEX `fk_student_company1_idx` (`company_id` ASC) VISIBLE,
  INDEX `fk_student_supervisor1_idx` (`supervisor_id` ASC) VISIBLE,
  CONSTRAINT `fk_student_department`
    FOREIGN KEY (`department_id`)
    REFERENCES `wrl`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_campus1`
    FOREIGN KEY (`campus_id`)
    REFERENCES `wrl`.`campus` (`campus_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_program1`
    FOREIGN KEY (`program_id`)
    REFERENCES `wrl`.`program` (`program_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_level1`
    FOREIGN KEY (`level_id`)
    REFERENCES `wrl`.`level` (`level_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_company1`
    FOREIGN KEY (`company_id`)
    REFERENCES `wrl`.`company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_supervisor1`
    FOREIGN KEY (`supervisor_id`)
    REFERENCES `wrl`.`supervisor` (`supervisor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`scheduling`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`scheduling` ;

CREATE TABLE IF NOT EXISTS `wrl`.`scheduling` (
  `scheduling_id` INT NOT NULL,
  `sched_date` DATE NOT NULL,
  `city_id` INT NOT NULL,
  `company_id` INT NOT NULL,
  `supervisor_id` INT NOT NULL,
  `department_id` INT NOT NULL,
  PRIMARY KEY (`scheduling_id`),
  INDEX `fk_scheduling_city1_idx` (`city_id` ASC) VISIBLE,
  INDEX `fk_scheduling_company1_idx` (`company_id` ASC) VISIBLE,
  INDEX `fk_scheduling_supervisor1_idx` (`supervisor_id` ASC) VISIBLE,
  INDEX `fk_scheduling_department1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `fk_scheduling_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `wrl`.`city` (`city_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_scheduling_company1`
    FOREIGN KEY (`company_id`)
    REFERENCES `wrl`.`company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_scheduling_supervisor1`
    FOREIGN KEY (`supervisor_id`)
    REFERENCES `wrl`.`supervisor` (`supervisor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_scheduling_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `wrl`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wrl`.`supervisor_has_department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wrl`.`supervisor_has_department` ;

CREATE TABLE IF NOT EXISTS `wrl`.`supervisor_has_department` (
  `supervisor_id` INT NOT NULL,
  `department_id` INT NOT NULL,
  PRIMARY KEY (`supervisor_id`, `department_id`),
  INDEX `fk_supervisor_has_department_department1_idx` (`department_id` ASC) VISIBLE,
  INDEX `fk_supervisor_has_department_supervisor1_idx` (`supervisor_id` ASC) VISIBLE,
  CONSTRAINT `fk_supervisor_has_department_supervisor1`
    FOREIGN KEY (`supervisor_id`)
    REFERENCES `wrl`.`supervisor` (`supervisor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_supervisor_has_department_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `wrl`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



USE wrl;

INSERT INTO campus VALUES
('1','Gweru'),
('2','Kwekwe'),
('3','Harare'),
('4','Zvishavane');

INSERT INTO city VALUES
('1', 'Harare'),
('2', 'Bulawayo'),
('3', 'Chitungwiza'),
('4', 'Mutare'),
('5', 'Gweru'),
('6', 'Kwekwe'),
('7', 'Kadoma'),
('8', 'Masvingo'),
('9', 'Chinhoyi'),
('10', 'Norton'),
('11', 'Gwanda'),
('12', 'Bindura'),
('13', 'Zvishavane'),
('14', 'Victoria Falls'),
('15', 'Hwange'),
('16', 'Redcliff'),
('17', 'Chegutu'),
('18', 'Kariba'),
('19', 'Rusape'),
('20', 'Marondera'),
('21', 'Ruwa'),
('22', 'Beitbridge'),
('23', 'Chipinge'),
('24', 'Shurugwi'),
('25', 'Chiredzi'),
('26', 'Epworth'),
('27', 'Lupane'),
('28', 'Mutoko'),
('29', 'Nyanga'),
('30', 'Banket'),
('31', 'Mazowe'),
('32', 'Murewa'),
('33', 'Shamva'),
('34', 'Mvurwi'),
('35', 'Zvimba'),
('36', 'Chimanimani'),
('37', 'Guruve'),
('38', 'Concession'),
('39', 'Mt Darwin'),
('40', 'Inyati');

INSERT INTO company VALUES
('1','Modiz','Zimbabwe','0780995944', 'admin@moiz.com','2023-03-01',1);

INSERT INTO department VALUES
('1','1234','Sample_dep');

INSERT INTO level VALUES
('1','3.2'),
('2','3.3'),
('3','4.1'),
('4','4.2');

INSERT INTO program VALUES
('1','12345','Sample_prog');

INSERT INTO student VALUES
('1','Sample','Student','R293467X','780987844','sample@students.msu.ac.zw','1','1','1','1','1','1');

INSERT INTO supervisor VALUES
('1','Sample','Supervisor','Staff001','789345644','sample@staff.msu.ac.zw','1');

INSERT INTO scheduling VALUES
('1','2024-06-07',1,1,1,1);







