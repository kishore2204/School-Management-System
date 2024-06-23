-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_cust1`
--

DROP TABLE IF EXISTS `t_cust1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_cust1` (
  `teacher_id` varchar(20) NOT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `class_teaching1` varchar(100) DEFAULT NULL,
  `class_teaching2` varchar(100) DEFAULT NULL,
  `class_teacher` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `salary_status` varchar(100) DEFAULT NULL,
  `up` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_cust1`
--

LOCK TABLES `t_cust1` WRITE;
/*!40000 ALTER TABLE `t_cust1` DISABLE KEYS */;
INSERT INTO `t_cust1` VALUES ('#101','mba','social','IX','X',NULL,'administrator','90,000','KPJills#101'),('#102','m.sc eng','english','XI','XII',NULL,'administrator','80,000','JeenPeter#102'),('#103','m.a','geography','IX','X',NULL,'administrator','80,000','Romila#103'),('#104','b.sc cs','computer science','XI','XII','XI','teacher','25,000','Aranganayagi#104'),('#105','m.sc chem','chemistry','XI','XII','XII','teacher','25,000','SamruthBee#105'),('#106','bca',NULL,NULL,NULL,NULL,'office','20,000','Shanmugapriya#106'),('#107','b.sc chem','chemistry','IX','X','X','teacher','25,000','ShamalaDevi#107'),('#108','mca',NULL,NULL,NULL,NULL,'office','40,000','Shankari#108'),('#109','b.sc tamil','tamil','IX','X','None','teacher','25,000','Valli#109'),('#110','m.sc phy','physics','XI','XII','IX','teacher','45,000','Yogesh#110');
/*!40000 ALTER TABLE `t_cust1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-19 23:59:08
