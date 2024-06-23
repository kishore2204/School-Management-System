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
-- Table structure for table `t_cust`
--

DROP TABLE IF EXISTS `t_cust`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_cust` (
  `teacher_id` varchar(100) NOT NULL,
  `joining_date` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `blood_group` varchar(100) DEFAULT NULL,
  `mother_tongue` varchar(100) DEFAULT NULL,
  `phone_no` bigint DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_cust`
--

LOCK TABLES `t_cust` WRITE;
/*!40000 ALTER TABLE `t_cust` DISABLE KEYS */;
INSERT INTO `t_cust` VALUES ('#101','12/5/2014','KPJills','27/4/1975','male','b+ve','malayalam',9488721578),('#102','28/7/2016','Jeen Peter','17/6/1989','female','b+ve','malayalam',9500591260),('#103','20/10/2012','Romila','27/12/1985','female','o+ve','kannada',7465839264),('#104','15/4/2018','Aranganayagi','19/8/1990','female','a1+ve','tamil',6836492643),('#105','8/6/2017','Samruth Bee','6/5/1978','female','Hh','urudhu',9835469582),('#106','2/5/2014','Shanmugapriya','9/10/1989','female','ab-ve','tamil',7869534675),('#107','31/9/2021','Shamala Devi','14/3/1990','female','b-ve','tamil',8935472539),('#108','06/03/2022','Shankari','01/07/1988','female','A+ve','tamil',8769567457),('#109','08/03/2022','Valli','02/08/1984','female','B+ve','tamil',8796574687),('#110','10/03/2022','Yogesh','16/03/1994','male','A+ve','telugu',8756945786);
/*!40000 ALTER TABLE `t_cust` ENABLE KEYS */;
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
