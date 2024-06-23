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
-- Table structure for table `class_det`
--

DROP TABLE IF EXISTS `class_det`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_det` (
  `admission_no` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `class` varchar(100) DEFAULT NULL,
  `subjects` varchar(200) DEFAULT NULL,
  `pa1` varchar(200) DEFAULT NULL,
  `pa2` varchar(200) DEFAULT NULL,
  `pa3` varchar(200) DEFAULT NULL,
  `pa4` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`admission_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_det`
--

LOCK TABLES `class_det` WRITE;
/*!40000 ALTER TABLE `class_det` DISABLE KEYS */;
INSERT INTO `class_det` VALUES (1,'sriram','XII','eng,mat,chem,phy,cs',' Eng : 80   Mat : 90   Chem : 78   Phy : 99   C.S : 99',' Eng : 67   Mat : 100   Chem : 100   Phy : 100   C.S : 100',' Eng : 90   Mat : 100   Chem : 99   Phy : 89   C.S : 99','Eng : 28  Mat : 31  Chem : 20  Phy : 13  C.S : 31'),(2,'rahul','XI','eng,mat,chem,phy,cs','Eng : 22  Mat : 15  Chem : 15  Phy : 19  C.S : 26','Eng : 22  Mat : 15  Chem : 15  Phy : 19  C.S : 26','Eng : 22  Mat : 15  Chem : 15  Phy : 19  C.S : 26','Eng : 22  Mat : 15  Chem : 15  Phy : 19  C.S : 26'),(3,'isham','XII','eng,mat,chem,phy,cs',' Eng : 100   Mat : 89   Chem : 90   Phy : 99   C.S : 100','Eng : 25  Mat : 17  Chem : 20  Phy : 15  C.S : 29','Eng : 25  Mat : 17  Chem : 20  Phy : 15  C.S : 29','Eng : 25  Mat : 17  Chem : 20  Phy : 15  C.S : 29'),(4,'sabari','X','eng,mat,sci,sco,IIlang','Eng : 30  Mat : 33  Sci : 28  Sco : 37  II Lang : 39','Eng : 30  Mat : 33  Sci : 28  Sco : 37  II Lang : 39','Eng : 30  Mat : 33  Sci : 28  Sco : 37  II Lang : 39','Eng : 30  Mat : 33  Sci : 28  Sco : 37  II Lang : 39'),(5,'vishwa','VIII','eng,mat,sci,sco,IIlang','Eng : 29  Mat : 29  Sci : 28  Sco : 11  II Lang : 19','Eng : 29  Mat : 29  Sci : 28  Sco : 11  II Lang : 19','Eng : 29  Mat : 29  Sci : 28  Sco : 11  II Lang : 19','Eng : 29  Mat : 29  Sci : 28  Sco : 11  II Lang : 19'),(6,'arunachalam','XII','eng,mat,chem,phy,cs',' Eng : 89   Mat : 99   Chem : 99   Phy : 90   C.S : 99',' Eng : 89   Mat : 98   Chem : 99   Phy : 99   C.S : 90',' Eng : 90   Mat : 99   Chem : 99   Phy : 99   C.S : 99',' Eng : 100   Mat : 100   Chem : 90   Phy : 89   C.S : 100');
/*!40000 ALTER TABLE `class_det` ENABLE KEYS */;
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
