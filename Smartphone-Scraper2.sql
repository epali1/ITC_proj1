
CREATE TABLE IF NOT EXISTS `Product` (
  `Product_id`          INT NOT NULL AUTO_INCREMENT,
  `Product_Name`        VARCHAR(255) NOT NULL,
  `display_displaycol`  INT NOT NULL,
  `Other_Data`          VARCHAR(255) NULL DEFAULT NULL,
  `body_b_id`           INT NOT NULL,
  `platform_P_id`       INT NOT NULL,
  `comms_C_id`          INT NOT NULL,
  `selfie_camera_SC_id` INT NOT NULL,
  `misc_MI_id`          INT NOT NULL,
  `network_N_id`        INT NOT NULL,
  `launch_L_id`         INT NOT NULL,
  `sound_S_id`          INT NOT NULL,
  `memory_M_id`         INT NOT NULL,
  `features_f_id`       INT NOT NULL,
  `main_camera_MC_id`   INT NOT NULL,
  `battary_B_id`        INT NOT NULL,
  `display_D_id`        INT NOT NULL,
  PRIMARY KEY (`Product_id`, `body_b_id`, `platform_P_id`, `display_displaycol`, `comms_C_id`, `selfie_camera_SC_id`, `misc_MI_id`, `network_N_id`, `launch_L_id`, `sound_S_id`, `memory_M_id`, `features_f_id`, `main_camera_MC_id`, `battary_B_id`)
);


CREATE TABLE IF NOT EXISTS `platform` (
  `P_id`                 INT NOT NULL AUTO_INCREMENT,
  `OS` VARCHAR(255)      NULL DEFAULT NULL,
  `Chipset` VARCHAR(255) NULL DEFAULT NULL,
  `CPU` VARCHAR(255)     NULL DEFAULT NULL,
  `GPU` VARCHAR(255)     NULL DEFAULT NULL,
  PRIMARY KEY (`P_id`)
);


CREATE TABLE IF NOT EXISTS `body` (
  `b_id` INT NOT NULL AUTO_INCREMENT,
  `Dimensions` VARCHAR(255) NULL DEFAULT NULL,
  `Weight` VARCHAR(255) NULL DEFAULT NULL,
  `Build` VARCHAR(255) NULL DEFAULT NULL,
  `SIM` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`b_id`)
);


CREATE TABLE IF NOT EXISTS `display` (
  `D_id`  INT NOT NULL AUTO_INCREMENT,
  `Type` VARCHAR(255) NULL DEFAULT NULL,
  `Size` VARCHAR(255) NULL DEFAULT NULL,
  `Resolution` VARCHAR(255) NULL DEFAULT NULL,

  PRIMARY KEY (`D_id`)
);


CREATE TABLE IF NOT EXISTS `comms` (
  `C_id` INT NOT NULL AUTO_INCREMENT,
  `WLAN` VARCHAR(255) NULL DEFAULT NULL,
  `Bluetooth` VARCHAR(255) NULL DEFAULT NULL,
  `GPS` VARCHAR(255) NULL DEFAULT NULL,
  `NFC` VARCHAR(255) NULL DEFAULT NULL,
  `Radio` VARCHAR(255) NULL DEFAULT NULL,
  `USB` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`C_id`)
);


CREATE TABLE IF NOT EXISTS `selfie_camera` (
  `SC_id` INT NOT NULL AUTO_INCREMENT,
  `Single` VARCHAR(255) NULL DEFAULT NULL,
  `features` VARCHAR(255) NULL DEFAULT NULL,
  `Video` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`SC_id`)
);


CREATE TABLE IF NOT EXISTS `misc` (
  `MI_id` INT NOT NULL AUTO_INCREMENT,
  `Colors` VARCHAR(255) NOT NULL,
  `Model` VARCHAR(255) NOT NULL,
  `SAR` VARCHAR(255) NOT NULL,
  `SAR_EU` VARCHAR(255) NOT NULL,
  `Price` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`MI_id`)
);


CREATE TABLE IF NOT EXISTS `network` (
  `N_id` INT NOT NULL AUTO_INCREMENT,
  `Technology` VARCHAR(255) NULL DEFAULT NULL,
  `GPRS` VARCHAR(255) NULL DEFAULT NULL,
  `EDGE` VARCHAR(255) NULL DEFAULT NULL,
  `2G_band` VARCHAR(255) NULL DEFAULT NULL,
  `3G_band` VARCHAR(255) NULL DEFAULT NULL,
  `4G_band` VARCHAR(255) NULL DEFAULT NULL,
  `Speed` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`N_id`)
);


CREATE TABLE IF NOT EXISTS `launch` (
  `L_id` INT NOT NULL AUTO_INCREMENT,
  `Announced` VARCHAR(255) NULL DEFAULT NULL,
  `Status` VARCHAR(255) NULL DEFAULT NULL,
  
  PRIMARY KEY (`L_id`)
);


CREATE TABLE IF NOT EXISTS `features` (
  `f_id` INT NOT NULL AUTO_INCREMENT,
  `Sensors` TEXT,
  `Other` TEXT,
  
  PRIMARY KEY (`f_id`)
);


CREATE TABLE IF NOT EXISTS `sound` (
  `S_id` INT NOT NULL AUTO_INCREMENT,
  `Loudspeaker` VARCHAR(255) NULL DEFAULT NULL,
  `3.5mm_jack` VARCHAR(255) NULL DEFAULT NULL,
  
  PRIMARY KEY (`S_id`)
);


CREATE TABLE IF NOT EXISTS `main_camera` (
  `MC_id` INT NOT NULL AUTO_INCREMENT,
  `Quad` VARCHAR(255) NULL DEFAULT NULL,
  `Features` VARCHAR(255) NULL DEFAULT NULL,
  `Video` VARCHAR(255) NULL DEFAULT NULL,
  
  PRIMARY KEY (`MC_id`)
);


CREATE TABLE IF NOT EXISTS `Battary` (
  `B_id` INT NOT NULL AUTO_INCREMENT,
  `Type` VARCHAR(255) NULL DEFAULT NULL,
  `Charging` VARCHAR(255) NULL DEFAULT NULL,
    
    PRIMARY KEY (`B_id`)
);


CREATE TABLE IF NOT EXISTS `memory` (
  `M_id` INT NOT NULL AUTO_INCREMENT,
  `Card_slot` VARCHAR(255) NULL DEFAULT NULL,
  `Internal` VARCHAR(255) NULL DEFAULT NULL,
  `other` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`M_id`)
);

ALTER TABLE Product  ADD FOREIGN KEY (body_b_id)           REFERENCES body(b_id);
ALTER TABLE Product  ADD FOREIGN KEY (platform_P_id)       REFERENCES platform(P_id);
ALTER TABLE Product  ADD FOREIGN KEY (comms_C_id)          REFERENCES comms(C_id);
ALTER TABLE Product  ADD FOREIGN KEY (selfie_camera_SC_id) REFERENCES selfie_camera(SC_id);
ALTER TABLE Product  ADD FOREIGN KEY (misc_MI_id)          REFERENCES misc(MI_id);
ALTER TABLE Product  ADD FOREIGN KEY (network_N_id)        REFERENCES network(N_id);
ALTER TABLE Product  ADD FOREIGN KEY (launch_L_id)         REFERENCES launch(L_id);
ALTER TABLE Product  ADD FOREIGN KEY (sound_S_id)          REFERENCES sound(S_id);
ALTER TABLE Product  ADD FOREIGN KEY (memory_M_id)         REFERENCES memory(M_id);
ALTER TABLE Product  ADD FOREIGN KEY (features_f_id)       REFERENCES features(f_id);
ALTER TABLE Product  ADD FOREIGN KEY (main_camera_MC_id)   REFERENCES main_camera(MC_id);
ALTER TABLE Product  ADD FOREIGN KEY (battary_B_id)        REFERENCES Battary(b_id);
ALTER TABLE Product  ADD FOREIGN KEY (display_D_id)        REFERENCES display(D_id);