-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Smartphone-scraper
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Smartphone-scraper
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Smartphone-scraper` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema pdars
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema smartphone-scraper
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema smartphone-scraper
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `smartphone-scraper` DEFAULT CHARACTER SET utf8 ;
USE `Smartphone-scraper` ;

-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Product` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Product` (
  `Product_id` INT NOT NULL,
  `Product_Name` VARCHAR(45) NOT NULL,
  `Other_Data` VARCHAR(245) NULL,
  PRIMARY KEY (`Product_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Product_Categories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Product_Categories` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Product_Categories` (
  `idProduct_Categories` INT NOT NULL,
  PRIMARY KEY (`idProduct_Categories`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Categories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Categories` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Categories` (
  `idCategories` INT NOT NULL AUTO_INCREMENT,
  `Category_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCategories`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Misc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Misc` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Misc` (
  `Colors` VARCHAR(245) NOT NULL,
  `Model` VARCHAR(245) NOT NULL,
  `SAR` VARCHAR(245) NOT NULL,
  `SAR_EU` VARCHAR(245) NOT NULL,
  `Price` VARCHAR(245) NOT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Battary`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Battary` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Battary` (
  `Type` VARCHAR(245) NULL,
  `Charging` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Features`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Features` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Features` (
  `Sensors` VARCHAR(245) NOT NULL,
  `Other` VARCHAR(245) NOT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Comms`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Comms` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Comms` (
  `WLAN` VARCHAR(245) NULL,
  `Bluetooth` VARCHAR(245) NULL,
  `GPS` VARCHAR(245) NULL,
  `NFC` VARCHAR(245) NULL,
  `Radio` VARCHAR(245) NULL,
  `USB` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Sound`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Sound` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Sound` (
  `Loudspeaker` VARCHAR(245) NULL,
  `3.5mm_jack` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Selfie_Camera`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Selfie_Camera` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Selfie_Camera` (
  `Single` VARCHAR(245) NULL,
  `features` VARCHAR(245) NULL,
  `Video` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Main_Camera`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Main_Camera` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Main_Camera` (
  `Quad` VARCHAR(245) NULL,
  `Features` VARCHAR(245) NULL,
  `Video` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Memory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Memory` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Memory` (
  `Card_slot` VARCHAR(245) NULL,
  `Internal` VARCHAR(245) NULL,
  `other` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Platform`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Platform` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Platform` (
  `OS` VARCHAR(245) NULL,
  `Chipset` VARCHAR(245) NULL,
  `CPU` VARCHAR(245) NULL,
  `GPU` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Display`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Display` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Display` (
  `Type` VARCHAR(245) NULL,
  `Size` VARCHAR(245) NULL,
  `Resolution` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Body`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Body` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Body` (
  `Dimensions` VARCHAR(245) NULL,
  `Weight` VARCHAR(245) NULL,
  `Build` VARCHAR(245) NULL,
  `SIM` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Launch`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Launch` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Launch` (
  `Announced` VARCHAR(245) NULL,
  `Status` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Network`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Network` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Network` (
  `Technology` VARCHAR(245) NULL,
  `GPRS` VARCHAR(245) NULL,
  `EDGE` VARCHAR(245) NULL,
  `2G_band` VARCHAR(245) NULL,
  `3G_band` VARCHAR(245) NULL,
  `4G_band` VARCHAR(245) NULL,
  `Speed` VARCHAR(245) NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Smartphone-scraper`.`Battary`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Smartphone-scraper`.`Battary` ;

CREATE TABLE IF NOT EXISTS `Smartphone-scraper`.`Battary` (
  `Type` VARCHAR(245) NULL,
  `Charging` VARCHAR(245) NULL)
ENGINE = InnoDB;

USE `smartphone-scraper` ;

-- -----------------------------------------------------
-- Table `smartphone-scraper`.`battary`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`battary` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`battary` (
  `Type` VARCHAR(245) NULL DEFAULT NULL,
  `Charging` VARCHAR(245) NULL DEFAULT NULL,
  `B_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`B_id`),
  UNIQUE INDEX `id_UNIQUE` (`B_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`body`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`body` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`body` (
  `Dimensions` VARCHAR(245) NULL DEFAULT NULL,
  `Weight` VARCHAR(245) NULL DEFAULT NULL,
  `Build` VARCHAR(245) NULL DEFAULT NULL,
  `SIM` VARCHAR(245) NULL DEFAULT NULL,
  `b_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`b_id`),
  UNIQUE INDEX `b_id_UNIQUE` (`b_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`platform`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`platform` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`platform` (
  `OS` VARCHAR(245) NULL DEFAULT NULL,
  `Chipset` VARCHAR(245) NULL DEFAULT NULL,
  `CPU` VARCHAR(245) NULL DEFAULT NULL,
  `GPU` VARCHAR(245) NULL DEFAULT NULL,
  `P_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`P_id`),
  UNIQUE INDEX `P_id_UNIQUE` (`P_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`display`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`display` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`display` (
  `Type` VARCHAR(245) NULL DEFAULT NULL,
  `Size` VARCHAR(245) NULL DEFAULT NULL,
  `Resolution` VARCHAR(245) NULL DEFAULT NULL,
  `D_id` VARCHAR(45) NULL,
  `displaycol` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`displaycol`),
  UNIQUE INDEX `displaycol_UNIQUE` (`displaycol` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`comms`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`comms` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`comms` (
  `WLAN` VARCHAR(245) NULL DEFAULT NULL,
  `Bluetooth` VARCHAR(245) NULL DEFAULT NULL,
  `GPS` VARCHAR(245) NULL DEFAULT NULL,
  `NFC` VARCHAR(245) NULL DEFAULT NULL,
  `Radio` VARCHAR(245) NULL DEFAULT NULL,
  `USB` VARCHAR(245) NULL DEFAULT NULL,
  `C_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`C_id`),
  UNIQUE INDEX `C_id_UNIQUE` (`C_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`selfie_camera`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`selfie_camera` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`selfie_camera` (
  `Single` VARCHAR(245) NULL DEFAULT NULL,
  `features` VARCHAR(245) NULL DEFAULT NULL,
  `Video` VARCHAR(245) NULL DEFAULT NULL,
  `SC_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`SC_id`),
  UNIQUE INDEX `SC_id_UNIQUE` (`SC_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`misc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`misc` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`misc` (
  `Colors` VARCHAR(245) NOT NULL,
  `Model` VARCHAR(245) NOT NULL,
  `SAR` VARCHAR(245) NOT NULL,
  `SAR_EU` VARCHAR(245) NOT NULL,
  `Price` VARCHAR(245) NOT NULL,
  `MI_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`MI_id`),
  UNIQUE INDEX `MI_id_UNIQUE` (`MI_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`network`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`network` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`network` (
  `Technology` VARCHAR(245) NULL DEFAULT NULL,
  `GPRS` VARCHAR(245) NULL DEFAULT NULL,
  `EDGE` VARCHAR(245) NULL DEFAULT NULL,
  `2G_band` VARCHAR(245) NULL DEFAULT NULL,
  `3G_band` VARCHAR(245) NULL DEFAULT NULL,
  `4G_band` VARCHAR(245) NULL DEFAULT NULL,
  `Speed` VARCHAR(245) NULL DEFAULT NULL,
  `N_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`N_id`),
  UNIQUE INDEX `id_UNIQUE` (`N_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`launch`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`launch` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`launch` (
  `Announced` VARCHAR(245) NULL DEFAULT NULL,
  `Status` VARCHAR(245) NULL DEFAULT NULL,
  `L_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`L_id`),
  UNIQUE INDEX `id_UNIQUE` (`L_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`sound`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`sound` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`sound` (
  `Loudspeaker` VARCHAR(245) NULL DEFAULT NULL,
  `3.5mm_jack` VARCHAR(245) NULL DEFAULT NULL,
  `S_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`S_id`),
  UNIQUE INDEX `id_UNIQUE` (`S_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`memory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`memory` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`memory` (
  `Card_slot` VARCHAR(245) NULL DEFAULT NULL,
  `Internal` VARCHAR(245) NULL DEFAULT NULL,
  `other` VARCHAR(245) NULL DEFAULT NULL,
  `M_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`M_id`),
  UNIQUE INDEX `M_id_UNIQUE` (`M_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`features`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`features` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`features` (
  `Sensors` VARCHAR(245) NOT NULL,
  `Other` VARCHAR(245) NOT NULL,
  `f_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`f_id`),
  UNIQUE INDEX `f_id_UNIQUE` (`f_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`main_camera`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`main_camera` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`main_camera` (
  `Quad` VARCHAR(245) NULL DEFAULT NULL,
  `Features` VARCHAR(245) NULL DEFAULT NULL,
  `Video` VARCHAR(245) NULL DEFAULT NULL,
  `MC_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`MC_id`),
  UNIQUE INDEX `id_UNIQUE` (`MC_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`product` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`product` (
  `Product_id` INT NOT NULL AUTO_INCREMENT,
  `Product_Name` VARCHAR(45) NOT NULL,
  `Other_Data` VARCHAR(245) NULL DEFAULT NULL,
  `body_b_id` INT NOT NULL,
  `platform_P_id` INT NOT NULL,
  `display_displaycol` INT NOT NULL,
  `comms_C_id` INT NOT NULL,
  `selfie_camera_SC_id` INT NOT NULL,
  `misc_MI_id` INT NOT NULL,
  `network_N_id` INT NOT NULL,
  `launch_L_id` INT NOT NULL,
  `sound_S_id` INT NOT NULL,
  `memory_M_id` INT NOT NULL,
  `features_f_id` INT NOT NULL,
  `main_camera_MC_id` INT NOT NULL,
  `battary_B_id` INT NOT NULL,
  PRIMARY KEY (`Product_id`, `body_b_id`, `platform_P_id`, `display_displaycol`, `comms_C_id`, `selfie_camera_SC_id`, `misc_MI_id`, `network_N_id`, `launch_L_id`, `sound_S_id`, `memory_M_id`, `features_f_id`, `main_camera_MC_id`, `battary_B_id`),
  INDEX `fk_product_body1_idx` (`body_b_id` ASC) VISIBLE,
  INDEX `fk_product_platform1_idx` (`platform_P_id` ASC) VISIBLE,
  INDEX `fk_product_display1_idx` (`display_displaycol` ASC) VISIBLE,
  INDEX `fk_product_comms1_idx` (`comms_C_id` ASC) VISIBLE,
  INDEX `fk_product_selfie_camera1_idx` (`selfie_camera_SC_id` ASC) VISIBLE,
  INDEX `fk_product_misc1_idx` (`misc_MI_id` ASC) VISIBLE,
  INDEX `fk_product_network1_idx` (`network_N_id` ASC) VISIBLE,
  INDEX `fk_product_launch1_idx` (`launch_L_id` ASC) VISIBLE,
  INDEX `fk_product_sound1_idx` (`sound_S_id` ASC) VISIBLE,
  INDEX `fk_product_memory1_idx` (`memory_M_id` ASC) VISIBLE,
  INDEX `fk_product_features1_idx` (`features_f_id` ASC) VISIBLE,
  INDEX `fk_product_main_camera1_idx` (`main_camera_MC_id` ASC) VISIBLE,
  INDEX `fk_product_battary1_idx` (`battary_B_id` ASC) VISIBLE,
  CONSTRAINT `fk_product_body1`
    FOREIGN KEY (`body_b_id`)
    REFERENCES `smartphone-scraper`.`body` (`b_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_platform1`
    FOREIGN KEY (`platform_P_id`)
    REFERENCES `smartphone-scraper`.`platform` (`P_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_display1`
    FOREIGN KEY (`display_displaycol`)
    REFERENCES `smartphone-scraper`.`display` (`displaycol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_comms1`
    FOREIGN KEY (`comms_C_id`)
    REFERENCES `smartphone-scraper`.`comms` (`C_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_selfie_camera1`
    FOREIGN KEY (`selfie_camera_SC_id`)
    REFERENCES `smartphone-scraper`.`selfie_camera` (`SC_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_misc1`
    FOREIGN KEY (`misc_MI_id`)
    REFERENCES `smartphone-scraper`.`misc` (`MI_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_network1`
    FOREIGN KEY (`network_N_id`)
    REFERENCES `smartphone-scraper`.`network` (`N_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_launch1`
    FOREIGN KEY (`launch_L_id`)
    REFERENCES `smartphone-scraper`.`launch` (`L_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_sound1`
    FOREIGN KEY (`sound_S_id`)
    REFERENCES `smartphone-scraper`.`sound` (`S_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_memory1`
    FOREIGN KEY (`memory_M_id`)
    REFERENCES `smartphone-scraper`.`memory` (`M_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_features1`
    FOREIGN KEY (`features_f_id`)
    REFERENCES `smartphone-scraper`.`features` (`f_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_main_camera1`
    FOREIGN KEY (`main_camera_MC_id`)
    REFERENCES `smartphone-scraper`.`main_camera` (`MC_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_product_battary1`
    FOREIGN KEY (`battary_B_id`)
    REFERENCES `smartphone-scraper`.`battary` (`B_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`product_categories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`product_categories` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`product_categories` (
  `idProduct_Categories` INT NOT NULL AUTO_INCREMENT,
  `product_Product_id` INT NOT NULL,
  PRIMARY KEY (`idProduct_Categories`, `product_Product_id`),
  INDEX `fk_product_categories_product1_idx` (`product_Product_id` ASC) VISIBLE,
  CONSTRAINT `fk_product_categories_product1`
    FOREIGN KEY (`product_Product_id`)
    REFERENCES `smartphone-scraper`.`product` (`Product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smartphone-scraper`.`categories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smartphone-scraper`.`categories` ;

CREATE TABLE IF NOT EXISTS `smartphone-scraper`.`categories` (
  `idCategories` INT NOT NULL AUTO_INCREMENT,
  `Category_Name` VARCHAR(45) NOT NULL,
  `product_categories_idProduct_Categories` INT NOT NULL,
  PRIMARY KEY (`idCategories`, `product_categories_idProduct_Categories`),
  INDEX `fk_categories_product_categories1_idx` (`product_categories_idProduct_Categories` ASC) VISIBLE,
  CONSTRAINT `fk_categories_product_categories1`
    FOREIGN KEY (`product_categories_idProduct_Categories`)
    REFERENCES `smartphone-scraper`.`product_categories` (`idProduct_Categories`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
