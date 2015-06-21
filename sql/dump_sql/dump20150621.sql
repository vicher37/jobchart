-- MySQL dump 10.13  Distrib 5.6.22, for osx10.8 (x86_64)
--
-- Host: localhost    Database: chart
-- ------------------------------------------------------
-- Server version	5.6.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comp_ratings`
--

DROP TABLE IF EXISTS `comp_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comp_ratings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(30) NOT NULL,
  `FB_likes` int(11) NOT NULL,
  `FB_likes_score` decimal(3,2) NOT NULL,
  `overall_rating` decimal(3,2) NOT NULL,
  `senior_leadership_rating` decimal(3,2) NOT NULL,
  `work_life_balance_rating` decimal(3,2) NOT NULL,
  `recommend_to_friend_rating` decimal(3,2) NOT NULL,
  `culture_and_values_rating` decimal(3,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comp_ratings`
--

LOCK TABLES `comp_ratings` WRITE;
/*!40000 ALTER TABLE `comp_ratings` DISABLE KEYS */;
INSERT INTO `comp_ratings` VALUES (1,'Walmart',34888377,1.03,2.90,2.50,2.60,0.40,2.80),(2,'Cisco',687255,0.02,3.60,3.70,4.00,1.00,4.00),(3,'Pepsi',34539206,1.02,3.40,2.90,2.80,0.60,3.30),(4,'Facebook',170037735,5.00,4.50,4.30,3.90,0.90,4.50),(5,'General Motors',627787,0.02,3.50,3.00,3.50,0.70,3.20),(6,'Honda',3546483,0.10,3.30,0.00,0.00,0.00,0.00),(7,'Ford Motor Company',2974230,0.09,3.40,3.00,3.10,0.60,3.30),(8,'Visa',18004602,0.53,3.00,2.40,3.20,0.50,2.60),(9,'VMware',171841,0.01,3.60,3.10,3.70,0.70,3.70),(10,'RealMassive',488,0.00,0.00,0.00,0.00,0.00,0.00),(11,'Microsoft',6700244,1.34,3.80,3.00,3.50,0.80,3.50),(12,'Google',18737993,3.74,4.40,3.80,4.00,0.90,4.40),(13,'IBM',443385,0.09,3.10,2.40,3.20,0.50,2.90),(14,'BMW',18754923,3.74,4.00,0.00,0.00,0.00,0.00),(15,'Intel',25070768,5.00,3.90,3.20,3.60,0.80,3.80),(16,'GE',1382036,0.28,3.70,3.20,3.40,0.80,3.60),(17,'Siemens',200322,0.04,3.60,3.10,3.50,0.80,3.40),(18,'Sony',6912320,1.38,3.40,3.00,3.70,0.60,3.50),(19,'BP',167692,0.16,3.50,2.90,3.80,0.70,3.50),(20,'P&G',5383231,5.00,3.80,3.20,3.40,0.80,3.80),(21,'Shell',5284055,4.91,3.70,3.40,3.90,0.80,3.70),(22,'Volkswagen',1687307,1.57,3.90,3.00,2.60,0.60,3.40),(23,'Johnson & Johnson',655474,0.61,3.80,3.30,3.80,0.80,3.90),(24,'McKinsey & Company',163638,0.15,4.20,4.00,2.80,0.90,4.30),(25,'HP',3674232,3.41,3.30,2.60,3.40,0.50,3.20),(26,'BP',167693,0.16,3.50,2.90,3.80,0.70,3.50);
/*!40000 ALTER TABLE `comp_ratings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-21 11:52:11
