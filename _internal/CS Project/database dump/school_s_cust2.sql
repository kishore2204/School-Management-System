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
-- Table structure for table `s_cust2`
--

DROP TABLE IF EXISTS `s_cust2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s_cust2` (
  `admission_no` bigint NOT NULL,
  `father_name` varchar(50) DEFAULT NULL,
  `father_number` bigint DEFAULT NULL,
  `mother_name` varchar(50) DEFAULT NULL,
  `mother_number` bigint DEFAULT NULL,
  `guardian_name` varchar(50) DEFAULT NULL,
  `guardian_number` bigint DEFAULT NULL,
  `annual_income` varchar(30) DEFAULT NULL,
  `1st_term_fee` varchar(20) DEFAULT NULL,
  `2nd_term_fee` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`admission_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s_cust2`
--

LOCK TABLES `s_cust2` WRITE;
/*!40000 ALTER TABLE `s_cust2` DISABLE KEYS */;
INSERT INTO `s_cust2` VALUES (1,'raj',6342346325,'divya',7835782345,'kumar',3456543213,'500000','Paid','Paid'),(2,'sharma',7865846934,NULL,NULL,NULL,NULL,'8000000','Paid','Not Paid'),(3,'neymer',4565436785,'amy',7857693475,NULL,NULL,'8500000','Paid','Paid'),(4,NULL,NULL,NULL,NULL,'ram',5678765798,'8500000','Paid','Paid'),(5,'anbu',5748395064,'aruvi',6758347692,NULL,NULL,'6700000','Paid','Paid'),(6,NULL,NULL,NULL,NULL,'kira',8975947596,'7000000','Paid','Paid');
/*!40000 ALTER TABLE `s_cust2` ENABLE KEYS */;
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
