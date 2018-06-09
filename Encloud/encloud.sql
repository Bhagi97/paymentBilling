-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: encloud
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `app_appointment`
--

DROP TABLE IF EXISTS `app_appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_appointment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_code` varchar(6) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `doctor_name` varchar(50) NOT NULL,
  `receptionist_name` varchar(30) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `franchise_id` int(11) DEFAULT NULL,
  `request` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_code` (`customer_code`),
  KEY `app_appointment_franchise_id_1539b1a5_fk_app_franchise_id` (`franchise_id`),
  CONSTRAINT `app_appointment_franchise_id_1539b1a5_fk_app_franchise_id` FOREIGN KEY (`franchise_id`) REFERENCES `app_franchise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_appointment`
--

LOCK TABLES `app_appointment` WRITE;
/*!40000 ALTER TABLE `app_appointment` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_auditreport`
--

DROP TABLE IF EXISTS `app_auditreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_auditreport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `type` varchar(30) NOT NULL,
  `bill` varchar(30) NOT NULL,
  `no` int(11) NOT NULL,
  `no_items` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `status` varchar(30) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_auditreport`
--

LOCK TABLES `app_auditreport` WRITE;
/*!40000 ALTER TABLE `app_auditreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_auditreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_category`
--

DROP TABLE IF EXISTS `app_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(30) NOT NULL,
  `category_code` varchar(20) NOT NULL,
  `category_description` varchar(200) DEFAULT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_category_category_name_franchise_code_dfdd1ce3_uniq` (`category_name`,`franchise_code`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_category`
--

LOCK TABLES `app_category` WRITE;
/*!40000 ALTER TABLE `app_category` DISABLE KEYS */;
INSERT INTO `app_category` VALUES (1,'Arishtam','ASH','',0),(2,'Tailams/Kuzhambus','T/K','',0),(3,'Kashayam','KSH','',0),(4,'Ghritam','GHR','',0),(5,'Lehyam','LHM','',0),(6,'Choornam','CHR','',0),(7,'Rasakriya','RSK','',0),(8,'Choornam Tablet','CHR_T','',0),(9,'Gulikas','GLK','',0),(10,'Gulikas - DS','GLK_DS','',0),(11,'Kashayam Tablet','KSH_T','',0);
/*!40000 ALTER TABLE `app_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_country`
--

DROP TABLE IF EXISTS `app_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `district_code` varchar(8) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=677 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_country`
--

LOCK TABLES `app_country` WRITE;
/*!40000 ALTER TABLE `app_country` DISABLE KEYS */;
INSERT INTO `app_country` VALUES (1,'India','Andaman and Nicobar (AN)','South Andaman','SA'),(2,'India','Andaman and Nicobar (AN)','North and Middle Andaman','NA'),(3,'India','Andaman and Nicobar (AN)','Nicobar','NI'),(4,'India','Andhra Pradesh (AP)','East Godavari','EG'),(5,'India','Andhra Pradesh (AP)','Guntur','GU'),(6,'India','Andhra Pradesh (AP)','Krishna','KR'),(7,'India','Andhra Pradesh (AP)','Visakhapatnam','VS'),(8,'India','Andhra Pradesh (AP)','Chittoor','CH'),(9,'India','Andhra Pradesh (AP)','Anantapur','AN'),(10,'India','Andhra Pradesh (AP)','Kurnool','KU'),(11,'India','Andhra Pradesh (AP)','West Godavari','WG'),(12,'India','Andhra Pradesh (AP)','Prakasam','PR'),(13,'India','Andhra Pradesh (AP)','Sri Potti Sriramulu Nellore','NE'),(14,'India','Andhra Pradesh (AP)','Kadapa','CU'),(15,'India','Andhra Pradesh (AP)','Srikakulam','SR'),(16,'India','Andhra Pradesh (AP)','Vizianagaram','VZ'),(17,'India','Arunachal Pradesh (AR)','Papum Pare','PA'),(18,'India','Arunachal Pradesh (AR)','Changlang','CH'),(19,'India','Arunachal Pradesh (AR)','Lohit','EL'),(20,'India','Arunachal Pradesh (AR)','West Siang','WS'),(21,'India','Arunachal Pradesh (AR)','Tirap','TI'),(22,'India','Arunachal Pradesh (AR)','East Siang','ES'),(23,'India','Arunachal Pradesh (AR)','Kurung Kumey','KK'),(24,'India','Arunachal Pradesh (AR)','West Kameng','WK'),(25,'India','Arunachal Pradesh (AR)','Upper Subansiri','UB'),(26,'India','Arunachal Pradesh (AR)','Lower Subansiri','LB'),(27,'India','Arunachal Pradesh (AR)','East Kameng','EK'),(28,'India','Arunachal Pradesh (AR)','Lower Dibang Valley','DV'),(29,'India','Arunachal Pradesh (AR)','Tawang','TA'),(30,'India','Arunachal Pradesh (AR)','Upper Siang','US'),(31,'India','Arunachal Pradesh (AR)','Anjaw','AJ'),(32,'India','Arunachal Pradesh (AR)','Dibang Valley','UD'),(33,'India','Arunachal Pradesh (AR)','Longding','LD'),(34,'India','Assam (AS)','Nagaon','NG'),(35,'India','Assam (AS)','Dhubri','DB'),(36,'India','Assam (AS)','Sonitpur','SO'),(37,'India','Assam (AS)','Cachar','CA'),(38,'India','Assam (AS)','Barpeta','BA'),(39,'India','Assam (AS)','Kamrup','KR'),(40,'India','Assam (AS)','Dibrugarh','DI'),(41,'India','Assam (AS)','Tinsukia','TI'),(42,'India','Assam (AS)','Kamrup Metropolitan','KM'),(43,'India','Assam (AS)','Karimganj','KR'),(44,'India','Assam (AS)','Sivasagar','SI'),(45,'India','Assam (AS)','Jorhat','JO'),(46,'India','Assam (AS)','Golaghat','GG'),(47,'India','Assam (AS)','Lakhimpur','LA'),(48,'India','Assam (AS)','Goalpara','GP'),(49,'India','Assam (AS)','Karbi Anglong','KA'),(50,'India','Assam (AS)','Morigaon','MA'),(51,'India','Assam (AS)','Baksa','BK'),(52,'India','Assam (AS)','Darrang','DA'),(53,'India','Assam (AS)','Kokrajhar','KK'),(54,'India','Assam (AS)','Udalguri','UD'),(55,'India','Assam (AS)','Nalbari','NL'),(56,'India','Assam (AS)','Bongaigaon','BO'),(57,'India','Assam (AS)','Dhemaji','DM'),(58,'India','Assam (AS)','Hailakandi','HA'),(59,'India','Assam (AS)','Chirang','CH'),(60,'India','Assam (AS)','Dima Hasao','NC'),(61,'India','Bihar (BR)','Patna','PA'),(62,'India','Bihar (BR)','East Champaran','EC'),(63,'India','Bihar (BR)','Muzaffarpur','MZ'),(64,'India','Bihar (BR)','Madhubani','MB'),(65,'India','Bihar (BR)','Gaya','GA'),(66,'India','Bihar (BR)','Samastipur','SM'),(67,'India','Bihar (BR)','Saran','SR'),(68,'India','Bihar (BR)','West Champaran','WC'),(69,'India','Bihar (BR)','Darbhanga','DA'),(70,'India','Bihar (BR)','Vaishali','VA'),(71,'India','Bihar (BR)','Sitamarhi','ST'),(72,'India','Bihar (BR)','Siwan','SW'),(73,'India','Bihar (BR)','Purnia','PU'),(74,'India','Bihar (BR)','Katihar','KT'),(75,'India','Bihar (BR)','Bhagalpur','BG'),(76,'India','Bihar (BR)','Rohtas','RO'),(77,'India','Bihar (BR)','Begusarai','BE'),(78,'India','Bihar (BR)','Nalanda','NL'),(79,'India','Bihar (BR)','Araria','AR'),(80,'India','Bihar (BR)','Bhojpur','BJ'),(81,'India','Bihar (BR)','Gopalganj','GO'),(82,'India','Bihar (BR)','Aurangabad','AU'),(83,'India','Bihar (BR)','Supaul','SU'),(84,'India','Bihar (BR)','Nawada','NW'),(85,'India','Bihar (BR)','Banka','BA'),(86,'India','Bihar (BR)','Madhepura','MP'),(87,'India','Bihar (BR)','Saharsa','SH'),(88,'India','Bihar (BR)','Jamui','JA'),(89,'India','Bihar (BR)','Buxar','BU'),(90,'India','Bihar (BR)','Kishanganj','KI'),(91,'India','Bihar (BR)','Khagaria','KH'),(92,'India','Bihar (BR)','Kaimur','KM'),(93,'India','Bihar (BR)','Munger','MG'),(94,'India','Bihar (BR)','Jehanabad','JE'),(95,'India','Bihar (BR)','Lakhisarai','LA'),(96,'India','Bihar (BR)','Arwal','AR'),(97,'India','Bihar (BR)','Sheohar','SO'),(98,'India','Bihar (BR)','Sheikhpura','SP'),(99,'India','Chandigarh (CH)','Chandigarh','CH'),(100,'India','Chhattisgarh (CG)','Raipur','RP'),(101,'India','Chhattisgarh (CG)','Durg','DU'),(102,'India','Chhattisgarh (CG)','Bilaspur','BI'),(103,'India','Chhattisgarh (CG)','Janjgir-Champa','JC'),(104,'India','Chhattisgarh (CG)','Rajnandgaon','RN'),(105,'India','Chhattisgarh (CG)','Raigarh','RG'),(106,'India','Chhattisgarh (CG)','Bastar','BA'),(107,'India','Chhattisgarh (CG)','Korba','KB'),(108,'India','Chhattisgarh (CG)','Mahasamund','MA'),(109,'India','Chhattisgarh (CG)','Jashpur','JA'),(110,'India','Chhattisgarh (CG)','Dhamtari','DH'),(111,'India','Chhattisgarh (CG)','Kanker','KK'),(112,'India','Chhattisgarh (CG)','Surajpur','SJ'),(113,'India','Chhattisgarh (CG)','Koriya','KJ'),(114,'India','Chhattisgarh (CG)','Kabirdham (formerly Kawardha)','KW'),(115,'India','Chhattisgarh (CG)','Dantewada','DA'),(116,'India','Chhattisgarh (CG)','Surguja','SJ'),(117,'India','Chhattisgarh (CG)','Bijapur','BJ'),(118,'India','Chhattisgarh (CG)','Sukma','SK'),(119,'India','Chhattisgarh (CG)','Narayanpur','NR'),(120,'India','Chhattisgarh (CG)','Balrampur',''),(121,'India','Chhattisgarh (CG)','Bemetara',''),(122,'India','Chhattisgarh (CG)','Balod',''),(123,'India','Chhattisgarh (CG)','Baloda Bazar',''),(124,'India','Chhattisgarh (CG)','Gariaband',''),(125,'India','Chhattisgarh (CG)','Kondagaon',''),(126,'India','Chhattisgarh (CG)','Mungeli',''),(127,'India','Dadra and Nagar Haveli (DN)','Dadra and Nagar Haveli','DN'),(128,'India','Daman and Diu (DD)','Daman','DA'),(129,'India','Daman and Diu (DD)','Diu','DI'),(130,'India','Delhi (DL)','North West Delhi','NW'),(131,'India','Delhi (DL)','South Delhi','SD'),(132,'India','Delhi (DL)','West Delhi','WD'),(133,'India','Delhi (DL)','South West Delhi','SW'),(134,'India','Delhi (DL)','North East Delhi','NE'),(135,'India','Delhi (DL)','East Delhi','ED'),(136,'India','Delhi (DL)','North Delhi','NO'),(137,'India','Delhi (DL)','Central Delhi','CD'),(138,'India','Delhi (DL)','New Delhi','ND'),(139,'India','Delhi (DL)','Shahdara',''),(140,'India','Delhi (DL)','South East Delhi',''),(141,'India','Goa (GA)','North Goa','NG'),(142,'India','Goa (GA)','South Goa','SG'),(143,'India','Gujarat (GJ)','Ahmedabad','AH'),(144,'India','Gujarat (GJ)','Surat','ST'),(145,'India','Gujarat (GJ)','Vadodara','VD'),(146,'India','Gujarat (GJ)','Rajkot','RA'),(147,'India','Gujarat (GJ)','Banaskantha','BK'),(148,'India','Gujarat (GJ)','Bhavnagar','BV'),(149,'India','Gujarat (GJ)','Junagadh','JU'),(150,'India','Gujarat (GJ)','Sabarkantha','SK'),(151,'India','Gujarat (GJ)','Panchmahal','PM'),(152,'India','Gujarat (GJ)','Kheda','KH'),(153,'India','Gujarat (GJ)','Jamnagar','JA'),(154,'India','Gujarat (GJ)','Dahod','DA'),(155,'India','Gujarat (GJ)','Kutch','KA'),(156,'India','Gujarat (GJ)','Anand','AN'),(157,'India','Gujarat (GJ)','Mehsana','MA'),(158,'India','Gujarat (GJ)','Surendranagar','SN'),(159,'India','Gujarat (GJ)','Valsad','VL'),(160,'India','Gujarat (GJ)','Bharuch','BR'),(161,'India','Gujarat (GJ)','Amreli district','AM'),(162,'India','Gujarat (GJ)','Gandhinagar','GA'),(163,'India','Gujarat (GJ)','Patan','PA'),(164,'India','Gujarat (GJ)','Navsari','NV'),(165,'India','Gujarat (GJ)','Gir Somnath',''),(166,'India','Gujarat (GJ)','Chhota Udaipur',''),(167,'India','Gujarat (GJ)','Aravalli','AR'),(168,'India','Gujarat (GJ)','Mahisagar','MH'),(169,'India','Gujarat (GJ)','Morbi',''),(170,'India','Gujarat (GJ)','Tapi','TA'),(171,'India','Gujarat (GJ)','Devbhoomi Dwarka',''),(172,'India','Gujarat (GJ)','Botad',''),(173,'India','Gujarat (GJ)','Narmada','NR'),(174,'India','Gujarat (GJ)','Porbandar','PO'),(175,'India','Gujarat (GJ)','Dang','DG'),(176,'India','Haryana (HR)','Faridabad','FR'),(177,'India','Haryana (HR)','Hissar','HI'),(178,'India','Haryana (HR)','Bhiwani','BH'),(179,'India','Haryana (HR)','Gurgaon','GU'),(180,'India','Haryana (HR)','Karnal','KR'),(181,'India','Haryana (HR)','Sonipat','SNP'),(182,'India','Haryana (HR)','Jind','JI'),(183,'India','Haryana (HR)','Sirsa','SI'),(184,'India','Haryana (HR)','Yamuna Nagar','YN'),(185,'India','Haryana (HR)','Panipat','PP'),(186,'India','Haryana (HR)','Ambala','AM'),(187,'India','Haryana (HR)','Mewat','MW'),(188,'India','Haryana (HR)','Kaithal','KT'),(189,'India','Haryana (HR)','Rohtak','RO'),(190,'India','Haryana (HR)','Palwal','PW'),(191,'India','Haryana (HR)','Kurukshetra','KU'),(192,'India','Haryana (HR)','Jhajjar','JH'),(193,'India','Haryana (HR)','Fatehabad','FT'),(194,'India','Haryana (HR)','Mahendragarh','MA'),(195,'India','Haryana (HR)','Rewari','RE'),(196,'India','Haryana (HR)','Panchkula','PK'),(197,'India','Himachal Pradesh (HP)','Kangra','KA'),(198,'India','Himachal Pradesh (HP)','Mandi','MA'),(199,'India','Himachal Pradesh (HP)','Shimla','SH'),(200,'India','Himachal Pradesh (HP)','Solan','SO'),(201,'India','Himachal Pradesh (HP)','Sirmaur','SI'),(202,'India','Himachal Pradesh (HP)','Una','UNA'),(203,'India','Himachal Pradesh (HP)','Chamba','CH'),(204,'India','Himachal Pradesh (HP)','Hamirpur','HA'),(205,'India','Himachal Pradesh (HP)','Kullu','KU'),(206,'India','Himachal Pradesh (HP)','Bilaspur','BI'),(207,'India','Himachal Pradesh (HP)','Kinnaur','KI'),(208,'India','Himachal Pradesh (HP)','Lahaul and Spiti','LS'),(209,'India','Jammu and Kashmir (JK)','Jammu','JA'),(210,'India','Jammu and Kashmir (JK)','Srinagar','SR'),(211,'India','Jammu and Kashmir (JK)','Anantnag','AN'),(212,'India','Jammu and Kashmir (JK)','Baramulla','BR'),(213,'India','Jammu and Kashmir (JK)','Kupwara','KU'),(214,'India','Jammu and Kashmir (JK)','Badgam','BD'),(215,'India','Jammu and Kashmir (JK)','Rajouri','RA'),(216,'India','Jammu and Kashmir (JK)','Kathua','KT'),(217,'India','Jammu and Kashmir (JK)','Pulwama','PU'),(218,'India','Jammu and Kashmir (JK)','Udhampur','UD'),(219,'India','Jammu and Kashmir (JK)','Poonch','PO'),(220,'India','Jammu and Kashmir (JK)','Kulgam','KG'),(221,'India','Jammu and Kashmir (JK)','Doda','DO'),(222,'India','Jammu and Kashmir (JK)','Bandipora','BPR'),(223,'India','Jammu and Kashmir (JK)','Samba','SB'),(224,'India','Jammu and Kashmir (JK)','Reasi','RS'),(225,'India','Jammu and Kashmir (JK)','Ganderbal','GB'),(226,'India','Jammu and Kashmir (JK)','Ramban','RB'),(227,'India','Jammu and Kashmir (JK)','Shopian','SH'),(228,'India','Jammu and Kashmir (JK)','Kishtwar','KW'),(229,'India','Jammu and Kashmir (JK)','Leh','LE'),(230,'India','Jammu and Kashmir (JK)','Kargil','KR'),(231,'India','Jharkhand (JH)','Ranchi','RA'),(232,'India','Jharkhand (JH)','Dhanbad','DH'),(233,'India','Jharkhand (JH)','Giridih','GI'),(234,'India','Jharkhand (JH)','East Singhbhum','ES'),(235,'India','Jharkhand (JH)','Bokaro','BO'),(236,'India','Jharkhand (JH)','Palamu','PL'),(237,'India','Jharkhand (JH)','Hazaribag','HA'),(238,'India','Jharkhand (JH)','West Singhbhum','WS'),(239,'India','Jharkhand (JH)','Deoghar','DE'),(240,'India','Jharkhand (JH)','Garhwa','GA'),(241,'India','Jharkhand (JH)','Dumka','DU'),(242,'India','Jharkhand (JH)','Godda','GO'),(243,'India','Jharkhand (JH)','Sahibganj','SA'),(244,'India','Jharkhand (JH)','Seraikela Kharsawan','SK'),(245,'India','Jharkhand (JH)','Chatra','CH'),(246,'India','Jharkhand (JH)','Gumla','GU'),(247,'India','Jharkhand (JH)','Ramgarh','RM'),(248,'India','Jharkhand (JH)','Pakur','PK'),(249,'India','Jharkhand (JH)','Jamtara','JA'),(250,'India','Jharkhand (JH)','Latehar','LA'),(251,'India','Jharkhand (JH)','Koderma','KO'),(252,'India','Jharkhand (JH)','Simdega','SI'),(253,'India','Jharkhand (JH)','Khunti','KH'),(254,'India','Jharkhand (JH)','Lohardaga','LO'),(255,'India','Karnataka (KA)','Bangalore Urban','BN'),(256,'India','Karnataka (KA)','Belgaum','BG'),(257,'India','Karnataka (KA)','Mysore','MY'),(258,'India','Karnataka (KA)','Tumkur','TU'),(259,'India','Karnataka (KA)','Gulbarga','GU'),(260,'India','Karnataka (KA)','Bellary','BL'),(261,'India','Karnataka (KA)','Vijayapura','BJ'),(262,'India','Karnataka (KA)','Dakshina Kannada','DK'),(263,'India','Karnataka (KA)','Davanagere','DA'),(264,'India','Karnataka (KA)','Raichur','RA'),(265,'India','Karnataka (KA)','Bagalkot','BK'),(266,'India','Karnataka (KA)','Dharwad','DH'),(267,'India','Karnataka (KA)','Mandya','MA'),(268,'India','Karnataka (KA)','Hassan','HS'),(269,'India','Karnataka (KA)','Shimoga','SH'),(270,'India','Karnataka (KA)','Bidar','BD'),(271,'India','Karnataka (KA)','Chitradurga','CT'),(272,'India','Karnataka (KA)','Haveri district','HV'),(273,'India','Karnataka (KA)','Kolar','KL'),(274,'India','Karnataka (KA)','Koppal','KP'),(275,'India','Karnataka (KA)','Uttara Kannada','UK'),(276,'India','Karnataka (KA)','Chikkaballapur','CK'),(277,'India','Karnataka (KA)','Udupi','UD'),(278,'India','Karnataka (KA)','Yadgir','YG'),(279,'India','Karnataka (KA)','Chikkamagaluru','CK'),(280,'India','Karnataka (KA)','Ramanagara','RM'),(281,'India','Karnataka (KA)','Gadag','GA'),(282,'India','Karnataka (KA)','Chamarajnagar','CJ'),(283,'India','Karnataka (KA)','Bangalore Rural','BR'),(284,'India','Karnataka (KA)','Kodagu','KD'),(285,'India','Kerala (KL)','Malappuram','MA'),(286,'India','Kerala (KL)','Thiruvananthapuram','TV'),(287,'India','Kerala (KL)','Ernakulam','ER'),(288,'India','Kerala (KL)','Thrissur','TS'),(289,'India','Kerala (KL)','Kozhikode','KZ'),(290,'India','Kerala (KL)','Palakkad','PL'),(291,'India','Kerala (KL)','Kollam','KL'),(292,'India','Kerala (KL)','Kannur','KN'),(293,'India','Kerala (KL)','Alappuzha','AL'),(294,'India','Kerala (KL)','Kottayam','KT'),(295,'India','Kerala (KL)','Kasaragod','KS'),(296,'India','Kerala (KL)','Pathanamthitta','PT'),(297,'India','Kerala (KL)','Idukki','ID'),(298,'India','Kerala (KL)','Wayanad','WA'),(299,'India','Lakshadweep (LD)','Lakshadweep','LD'),(300,'India','Madhya Pradesh (MP)','Indore','IN'),(301,'India','Madhya Pradesh (MP)','Jabalpur','JA'),(302,'India','Madhya Pradesh (MP)','Sagar','SG'),(303,'India','Madhya Pradesh (MP)','Bhopal','BP'),(304,'India','Madhya Pradesh (MP)','Rewa','RE'),(305,'India','Madhya Pradesh (MP)','Satna','ST'),(306,'India','Madhya Pradesh (MP)','Dhar','DH'),(307,'India','Madhya Pradesh (MP)','Chhindwara','CN'),(308,'India','Madhya Pradesh (MP)','Gwalior','GW'),(309,'India','Madhya Pradesh (MP)','Ujjain','UJ'),(310,'India','Madhya Pradesh (MP)','Morena','MO'),(311,'India','Madhya Pradesh (MP)','Khargone (West Nimar)','WN'),(312,'India','Madhya Pradesh (MP)','Chhatarpur','CT'),(313,'India','Madhya Pradesh (MP)','Shivpuri','SV'),(314,'India','Madhya Pradesh (MP)','Bhind','BD'),(315,'India','Madhya Pradesh (MP)','Balaghat','BL'),(316,'India','Madhya Pradesh (MP)','Betul','BE'),(317,'India','Madhya Pradesh (MP)','Dewas','DE'),(318,'India','Madhya Pradesh (MP)','Rajgarh','RG'),(319,'India','Madhya Pradesh (MP)','Shajapur','SJ'),(320,'India','Madhya Pradesh (MP)','Vidisha','VI'),(321,'India','Madhya Pradesh (MP)','Ratlam','RL'),(322,'India','Madhya Pradesh (MP)','Tikamgarh','TI'),(323,'India','Madhya Pradesh (MP)','Barwani','BR'),(324,'India','Madhya Pradesh (MP)','Seoni','SO'),(325,'India','Madhya Pradesh (MP)','Mandsaur','MS'),(326,'India','Madhya Pradesh (MP)','Raisen','RS'),(327,'India','Madhya Pradesh (MP)','Sehore','SR'),(328,'India','Madhya Pradesh (MP)','Khandwa (East Nimar)','EN'),(329,'India','Madhya Pradesh (MP)','Katni','KA'),(330,'India','Madhya Pradesh (MP)','Damoh','DM'),(331,'India','Madhya Pradesh (MP)','Hoshangabad','HO'),(332,'India','Madhya Pradesh (MP)','Guna','GU'),(333,'India','Madhya Pradesh (MP)','Singrauli','SN'),(334,'India','Madhya Pradesh (MP)','Sidhi','SI'),(335,'India','Madhya Pradesh (MP)','Narsinghpur','NA'),(336,'India','Madhya Pradesh (MP)','Shahdol','SH'),(337,'India','Madhya Pradesh (MP)','Mandla','ML'),(338,'India','Madhya Pradesh (MP)','Jhabua','JH'),(339,'India','Madhya Pradesh (MP)','Panna','PA'),(340,'India','Madhya Pradesh (MP)','Ashok Nagar','AS'),(341,'India','Madhya Pradesh (MP)','Neemuch','NE'),(342,'India','Madhya Pradesh (MP)','Datia','DT'),(343,'India','Madhya Pradesh (MP)','Burhanpur','BU'),(344,'India','Madhya Pradesh (MP)','Anuppur','AP'),(345,'India','Madhya Pradesh (MP)','Alirajpur','AL'),(346,'India','Madhya Pradesh (MP)','Dindori','DI'),(347,'India','Madhya Pradesh (MP)','Sheopur','SP'),(348,'India','Madhya Pradesh (MP)','Umaria','UM'),(349,'India','Madhya Pradesh (MP)','Harda','HA'),(350,'India','Madhya Pradesh (MP)','Agar','AG'),(351,'India','Maharashtra (MH)','Thane','TH'),(352,'India','Maharashtra (MH)','Pune','PU'),(353,'India','Maharashtra (MH)','Mumbai suburban','MU'),(354,'India','Maharashtra (MH)','Nashik','NS'),(355,'India','Maharashtra (MH)','Nagpur','NG'),(356,'India','Maharashtra (MH)','Ahmednagar','AH'),(357,'India','Maharashtra (MH)','Solapur','SO'),(358,'India','Maharashtra (MH)','Jalgaon','JG'),(359,'India','Maharashtra (MH)','Kolhapur','KO'),(360,'India','Maharashtra (MH)','Aurangabad','AU'),(361,'India','Maharashtra (MH)','Nanded','ND'),(362,'India','Maharashtra (MH)','Mumbai City','MC'),(363,'India','Maharashtra (MH)','Satara','ST'),(364,'India','Maharashtra (MH)','Amravati','AM'),(365,'India','Maharashtra (MH)','Sangli','SN'),(366,'India','Maharashtra (MH)','Yavatmal','YA'),(367,'India','Maharashtra (MH)','Raigad','RG'),(368,'India','Maharashtra (MH)','Buldhana','BU'),(369,'India','Maharashtra (MH)','Beed','BI'),(370,'India','Maharashtra (MH)','Latur','LA'),(371,'India','Maharashtra (MH)','Chandrapur','CH'),(372,'India','Maharashtra (MH)','Dhule','DH'),(373,'India','Maharashtra (MH)','Jalna','JN'),(374,'India','Maharashtra (MH)','Parbhani','PA'),(375,'India','Maharashtra (MH)','Akola','AK'),(376,'India','Maharashtra (MH)','Osmanabad','OS'),(377,'India','Maharashtra (MH)','Nandurbar','NB'),(378,'India','Maharashtra (MH)','Ratnagiri','RT'),(379,'India','Maharashtra (MH)','Gondia','GO'),(380,'India','Maharashtra (MH)','Wardha','WR'),(381,'India','Maharashtra (MH)','Bhandara','BH'),(382,'India','Maharashtra (MH)','Washim','WS'),(383,'India','Maharashtra (MH)','Hingoli','HI'),(384,'India','Maharashtra (MH)','Gadchiroli','GA'),(385,'India','Maharashtra (MH)','Sindhudurg','SI'),(386,'India','Maharashtra (MH)','Palghar','-'),(387,'India','Manipur (MN)','Imphal West','WI'),(388,'India','Manipur (MN)','Imphal East','EI'),(389,'India','Manipur (MN)','Thoubal','TH'),(390,'India','Manipur (MN)','Senapati','SE'),(391,'India','Manipur (MN)','Churachandpur','CC'),(392,'India','Manipur (MN)','Bishnupur','BI'),(393,'India','Manipur (MN)','Ukhrul','UK'),(394,'India','Manipur (MN)','Chandel','CD'),(395,'India','Manipur (MN)','Tamenglong','TA'),(396,'India','Meghalaya (ML)','East Khasi Hills','EK'),(397,'India','Meghalaya (ML)','West Garo Hills','WG'),(398,'India','Meghalaya (ML)','West Khasi Hills','WK'),(399,'India','Meghalaya (ML)','East Garo Hills','EG'),(400,'India','Meghalaya (ML)','West Jaintia Hills','WG'),(401,'India','Meghalaya (ML)','Ri Bhoi','RB'),(402,'India','Meghalaya (ML)','South Garo Hills','SG'),(403,'India','Meghalaya (ML)','East Jaintia Hills',''),(404,'India','Meghalaya (ML)','North Garo Hills',''),(405,'India','Meghalaya (ML)','South West Khasi Hills',''),(406,'India','Meghalaya (ML)','South West Garo Hills',''),(407,'India','Mizoram (MZ)','Tuensang','TU'),(408,'India','Mizoram (MZ)','Aizawl','AI'),(409,'India','Mizoram (MZ)','Dimapur','DI'),(410,'India','Mizoram (MZ)','Kohima','KO'),(411,'India','Mizoram (MZ)','Mon','MN'),(412,'India','Mizoram (MZ)','Mokokchung','MK'),(413,'India','Mizoram (MZ)','Wokha','WO'),(414,'India','Mizoram (MZ)','Peren','PE'),(415,'India','Mizoram (MZ)','Phek','PH'),(416,'India','Mizoram (MZ)','Lunglei','LU'),(417,'India','Mizoram (MZ)','Zunheboto','ZU'),(418,'India','Mizoram (MZ)','Champhai','CH'),(419,'India','Mizoram (MZ)','Lawngtlai','LA'),(420,'India','Mizoram (MZ)','Mamit','MA'),(421,'India','Mizoram (MZ)','Kolasib','KO'),(422,'India','Mizoram (MZ)','Kiphire','KI'),(423,'India','Mizoram (MZ)','Serchhip','SE'),(424,'India','Mizoram (MZ)','Saiha','SA'),(425,'India','Mizoram (MZ)','Longleng','LO'),(426,'India','Odisha (OD)','Ganjam','GN'),(427,'India','Odisha (OD)','Cuttack','CU'),(428,'India','Odisha (OD)','Mayurbhanj','MY'),(429,'India','Odisha (OD)','Balasore','BW'),(430,'India','Odisha (OD)','Khordha','KH'),(431,'India','Odisha (OD)','Sundargarh','SU'),(432,'India','Odisha (OD)','Jajpur','JP'),(433,'India','Odisha (OD)','Kendujhar (Keonjhar)','KJ'),(434,'India','Odisha (OD)','Puri','PU'),(435,'India','Odisha (OD)','Balangir','BL'),(436,'India','Odisha (OD)','Kalahandi','KL'),(437,'India','Odisha (OD)','Bhadrak','BH'),(438,'India','Odisha (OD)','Bargarh (Baragarh)','BR'),(439,'India','Odisha (OD)','Kendrapara','KP'),(440,'India','Odisha (OD)','Koraput','KO'),(441,'India','Odisha (OD)','Angul','AN'),(442,'India','Odisha (OD)','Nabarangpur','NB'),(443,'India','Odisha (OD)','Dhenkanal','DH'),(444,'India','Odisha (OD)','Jagatsinghpur','JS'),(445,'India','Odisha (OD)','Sambalpur','SA'),(446,'India','Odisha (OD)','Nayagarh','NY'),(447,'India','Odisha (OD)','Rayagada','RA'),(448,'India','Odisha (OD)','Kandhamal','KN'),(449,'India','Odisha (OD)','Subarnapur (Sonepur)','SO'),(450,'India','Odisha (OD)','Malkangiri','ML'),(451,'India','Odisha (OD)','Nuapada','NU'),(452,'India','Odisha (OD)','Jharsuguda','JH'),(453,'India','Odisha (OD)','Gajapati','GP'),(454,'India','Odisha (OD)','Boudh (Bauda)','BD'),(455,'India','Odisha (OD)','Debagarh (Deogarh)','DE'),(456,'India','Puducherry (PY)','Pondicherry','PO'),(457,'India','Puducherry (PY)','Karaikal','KA'),(458,'India','Puducherry (PY)','Yanam','YA'),(459,'India','Puducherry (PY)','Mahe','MA'),(460,'India','Punjab (PB)','Ludhiana','LU'),(461,'India','Punjab (PB)','Patiala','PA'),(462,'India','Punjab (PB)','Amritsar','AM'),(463,'India','Punjab (PB)','Gurdaspur','GU'),(464,'India','Punjab (PB)','Jalandhar','JA'),(465,'India','Punjab (PB)','Firozpur','FI'),(466,'India','Punjab (PB)','Pathankot','PA'),(467,'India','Punjab (PB)','Sangrur','SA'),(468,'India','Punjab (PB)','Hoshiarpur','HO'),(469,'India','Punjab (PB)','Bathinda','BA'),(470,'India','Punjab (PB)','Tarn Taran','TT'),(471,'India','Punjab (PB)','Moga','MO'),(472,'India','Punjab (PB)','Sahibzada Ajit Singh Nagar','SAS'),(473,'India','Punjab (PB)','Sri Muktsar Sahib','MU'),(474,'India','Punjab (PB)','Kapurthala','KA'),(475,'India','Punjab (PB)','Mansa','MA'),(476,'India','Punjab (PB)','Rupnagar','RU'),(477,'India','Punjab (PB)','Faridkot','FR'),(478,'India','Punjab (PB)','Shahid Bhagat Singh Nagar','PB'),(479,'India','Punjab (PB)','Fatehgarh Sahib','FT'),(480,'India','Punjab (PB)','Barnala','BNL'),(481,'India','Punjab (PB)','Fazilka','FA'),(482,'India','Rajasthan (RJ)','Jaipur','JP'),(483,'India','Rajasthan (RJ)','Jodhpur','JO'),(484,'India','Rajasthan (RJ)','Alwar','AL'),(485,'India','Rajasthan (RJ)','Nagaur','NA'),(486,'India','Rajasthan (RJ)','Udaipur','UD'),(487,'India','Rajasthan (RJ)','Sikar','SK'),(488,'India','Rajasthan (RJ)','Barmer','BM'),(489,'India','Rajasthan (RJ)','Ajmer','AJ'),(490,'India','Rajasthan (RJ)','Bharatpur','BP'),(491,'India','Rajasthan (RJ)','Bhilwara','BW'),(492,'India','Rajasthan (RJ)','Bikaner','BI'),(493,'India','Rajasthan (RJ)','Jhunjhunu','JJ'),(494,'India','Rajasthan (RJ)','Churu','CR'),(495,'India','Rajasthan (RJ)','Pali','PA'),(496,'India','Rajasthan (RJ)','Ganganagar','GA'),(497,'India','Rajasthan (RJ)','Kota','KO'),(498,'India','Rajasthan (RJ)','Jalore','JL'),(499,'India','Rajasthan (RJ)','Banswara','BN'),(500,'India','Rajasthan (RJ)','Hanumangarh','HA'),(501,'India','Rajasthan (RJ)','Dausa','DA'),(502,'India','Rajasthan (RJ)','Chittorgarh','CT'),(503,'India','Rajasthan (RJ)','Karauli','KA'),(504,'India','Rajasthan (RJ)','Tonk','TO'),(505,'India','Rajasthan (RJ)','Jhalawar','JW'),(506,'India','Rajasthan (RJ)','Dungapur','DU'),(507,'India','Rajasthan (RJ)','Sawai Madhopur','SM'),(508,'India','Rajasthan (RJ)','Baran','BR'),(509,'India','Rajasthan (RJ)','Dholpur','DH'),(510,'India','Rajasthan (RJ)','Rajsamand','RA'),(511,'India','Rajasthan (RJ)','Bundi','BU'),(512,'India','Rajasthan (RJ)','Sirohi','SR'),(513,'India','Rajasthan (RJ)','Pratapgarh','PG'),(514,'India','Rajasthan (RJ)','Jaisalmer','JS'),(515,'India','Sikkim (SK)','East Sikkim','ES'),(516,'India','Sikkim (SK)','South Sikkim','SS'),(517,'India','Sikkim (SK)','West Sikkim','WS'),(518,'India','Sikkim (SK)','North Sikkim','NS'),(519,'India','Tamil Nadu (TN)','Chennai','CH'),(520,'India','Tamil Nadu (TN)','Madurai','MA'),(521,'India','Tamil Nadu (TN)','Kanchipuram','KC'),(522,'India','Tamil Nadu (TN)','Vellore','VE'),(523,'India','Tamil Nadu (TN)','Tiruvallur','TL'),(524,'India','Tamil Nadu (TN)','Salem','SA'),(525,'India','Tamil Nadu (TN)','Coimbatore','CO'),(526,'India','Tamil Nadu (TN)','Viluppuram','VL'),(527,'India','Tamil Nadu (TN)','Tirunelveli','TI'),(528,'India','Tamil Nadu (TN)','Kanyakumari','KK'),(529,'India','Tamil Nadu (TN)','Tiruchirappalli','TC'),(530,'India','Tamil Nadu (TN)','Cuddalore','CU'),(531,'India','Tamil Nadu (TN)','Tirupur','TP'),(532,'India','Tamil Nadu (TN)','Tiruvannamalai','TV'),(533,'India','Tamil Nadu (TN)','Thanjavur','TJ'),(534,'India','Tamil Nadu (TN)','Erode','ER'),(535,'India','Tamil Nadu (TN)','Dindigul','DI'),(536,'India','Tamil Nadu (TN)','Virudhunagar','VR'),(537,'India','Tamil Nadu (TN)','Pudukkottai','PU'),(538,'India','Tamil Nadu (TN)','Krishnagiri','KR'),(539,'India','Tamil Nadu (TN)','Thoothukudi','TK'),(540,'India','Tamil Nadu (TN)','Namakkal','NM'),(541,'India','Tamil Nadu (TN)','Nagapattinam','NG'),(542,'India','Tamil Nadu (TN)','Dharmapuri','DH'),(543,'India','Tamil Nadu (TN)','Sivaganga','SI'),(544,'India','Tamil Nadu (TN)','Ramanathapuram','RA'),(545,'India','Tamil Nadu (TN)','Tiruvarur','TR'),(546,'India','Tamil Nadu (TN)','Theni','TH'),(547,'India','Tamil Nadu (TN)','Karur','KA'),(548,'India','Tamil Nadu (TN)','Ariyalur','AY'),(549,'India','Tamil Nadu (TN)','Nilgiris','NI'),(550,'India','Tamil Nadu (TN)','Perambalur','PE'),(551,'India','Telangana (TS)','Ranga Reddy','RA'),(552,'India','Telangana (TS)','Mahbubnagar','MA'),(553,'India','Telangana (TS)','Hyderabad','HY'),(554,'India','Telangana (TS)','Karimnagar','KA'),(555,'India','Telangana (TS)','Warangal','WA'),(556,'India','Telangana (TS)','Nalgonda','NA'),(557,'India','Telangana (TS)','Medak','ME'),(558,'India','Telangana (TS)','Khammam','KH'),(559,'India','Telangana (TS)','Adilabad','AD'),(560,'India','Telangana (TS)','Nizamabad','NI'),(561,'India','Tripura (TR)','West Tripura','WT'),(562,'India','Tripura (TR)','Sepahijala','SP'),(563,'India','Tripura (TR)','Gomati','GM'),(564,'India','Tripura (TR)','South Tripura','ST'),(565,'India','Tripura (TR)','North Tripura','NT'),(566,'India','Tripura (TR)','Dhalai','DH'),(567,'India','Tripura (TR)','Khowai','KH'),(568,'India','Tripura (TR)','Unokoti','UK'),(569,'India','Uttar Pradesh (UP)','Allahabad','AH'),(570,'India','Uttar Pradesh (UP)','Moradabad','MO'),(571,'India','Uttar Pradesh (UP)','Ghaziabad','GZ'),(572,'India','Uttar Pradesh (UP)','Azamgarh','AZ'),(573,'India','Uttar Pradesh (UP)','Lucknow','LU'),(574,'India','Uttar Pradesh (UP)','Kanpur Nagar','KN'),(575,'India','Uttar Pradesh (UP)','Jaunpur district','JU'),(576,'India','Uttar Pradesh (UP)','Sitapur','SI'),(577,'India','Uttar Pradesh (UP)','Bareilly','BR'),(578,'India','Uttar Pradesh (UP)','Gorakhpur','GR'),(579,'India','Uttar Pradesh (UP)','Agra','AG'),(580,'India','Uttar Pradesh (UP)','Muzaffarnagar','MU'),(581,'India','Uttar Pradesh (UP)','Hardoi','HR'),(582,'India','Uttar Pradesh (UP)','Lakhimpur Kheri','LK'),(583,'India','Uttar Pradesh (UP)','Sultanpur','SU'),(584,'India','Uttar Pradesh (UP)','Budaun','BD'),(585,'India','Uttar Pradesh (UP)','Bijnor','BI'),(586,'India','Uttar Pradesh (UP)','Varanasi','VA'),(587,'India','Uttar Pradesh (UP)','Aligarh','AL'),(588,'India','Uttar Pradesh (UP)','Ghazipur','GP'),(589,'India','Uttar Pradesh (UP)','Kushinagar','KU'),(590,'India','Uttar Pradesh (UP)','Bulandshahr','BU'),(591,'India','Uttar Pradesh (UP)','Saharanpur','SA'),(592,'India','Uttar Pradesh (UP)','Meerut','ME'),(593,'India','Uttar Pradesh (UP)','Gonda','GN'),(594,'India','Uttar Pradesh (UP)','Raebareli','RB'),(595,'India','Uttar Pradesh (UP)','Barabanki','BB'),(596,'India','Uttar Pradesh (UP)','Ballia','BL'),(597,'India','Uttar Pradesh (UP)','Pratapgarh','PR'),(598,'India','Uttar Pradesh (UP)','Unnao','UN'),(599,'India','Uttar Pradesh (UP)','Deoria','DE'),(600,'India','Uttar Pradesh (UP)','Shahjahanpur','SJ'),(601,'India','Uttar Pradesh (UP)','Maharajganj','MG'),(602,'India','Uttar Pradesh (UP)','Fatehpur','FT'),(603,'India','Uttar Pradesh (UP)','Siddharthnagar','SN'),(604,'India','Uttar Pradesh (UP)','Mathura','MT'),(605,'India','Uttar Pradesh (UP)','Firozabad','FI'),(606,'India','Uttar Pradesh (UP)','Mirzapur','MI'),(607,'India','Uttar Pradesh (UP)','Faizabad','FZ'),(608,'India','Uttar Pradesh (UP)','Basti','BS'),(609,'India','Uttar Pradesh (UP)','Ambedkar Nagar','AN'),(610,'India','Uttar Pradesh (UP)','Bahraich','BH'),(611,'India','Uttar Pradesh (UP)','Rampur','RA'),(612,'India','Uttar Pradesh (UP)','Sambhal(Bheem Nagar)','SM'),(613,'India','Uttar Pradesh (UP)','Mau','MB'),(614,'India','Uttar Pradesh (UP)','Balrampur','BP'),(615,'India','Uttar Pradesh (UP)','Pilibhit','PI'),(616,'India','Uttar Pradesh (UP)','Jhansi','JH'),(617,'India','Uttar Pradesh (UP)','Chandauli','CD'),(618,'India','Uttar Pradesh (UP)','Farrukhabad','FR'),(619,'India','Uttar Pradesh (UP)','Sonbhadra','SO'),(620,'India','Uttar Pradesh (UP)','Mainpuri','MP'),(621,'India','Uttar Pradesh (UP)','Jyotiba Phule Nagar','JP'),(622,'India','Uttar Pradesh (UP)','Banda','BN'),(623,'India','Uttar Pradesh (UP)','Kanpur Dehat (Ramabai Nagar)','KD'),(624,'India','Uttar Pradesh (UP)','Etah','ET'),(625,'India','Uttar Pradesh (UP)','Sant Kabir Nagar','SK'),(626,'India','Uttar Pradesh (UP)','Gautam Buddh Nagar','GB'),(627,'India','Uttar Pradesh (UP)','Jalaun','JL'),(628,'India','Uttar Pradesh (UP)','Kannauj','KJ'),(629,'India','Uttar Pradesh (UP)','Kaushambi','KS'),(630,'India','Uttar Pradesh (UP)','Etawah','EW'),(631,'India','Uttar Pradesh (UP)','Hathras (Mahamaya Nagar)','HT'),(632,'India','Uttar Pradesh (UP)','Sant Ravidas Nagar','SR'),(633,'India','Uttar Pradesh (UP)','Hapur (Panchsheel Nagar)','PN'),(634,'India','Uttar Pradesh (UP)','Kanshi Ram Nagar','KR'),(635,'India','Uttar Pradesh (UP)','Auraiya','AU'),(636,'India','Uttar Pradesh (UP)','Bagpat','BG'),(637,'India','Uttar Pradesh (UP)','Lalitpur','LA'),(638,'India','Uttar Pradesh (UP)','Shravasti','SV'),(639,'India','Uttar Pradesh (UP)','Hamirpur','HM'),(640,'India','Uttar Pradesh (UP)','Chitrakoot','CT'),(641,'India','Uttar Pradesh (UP)','Mahoba','MH'),(642,'India','Uttar Pradesh (UP)','Shamli','SH'),(643,'India','Uttar Pradesh (UP)','Amethi (Chhatrapati Shahuji Maharaj Nagar)','CS'),(644,'India','Uttarakhand (UK)','Haridwar','HA'),(645,'India','Uttarakhand (UK)','Dehradun','DD'),(646,'India','Uttarakhand (UK)','Udham Singh Nagar','US'),(647,'India','Uttarakhand (UK)','Nainital','NA'),(648,'India','Uttarakhand (UK)','Pauri Garhwal','PG'),(649,'India','Uttarakhand (UK)','Almora','AL'),(650,'India','Uttarakhand (UK)','Tehri Garhwal','TG'),(651,'India','Uttarakhand (UK)','Pithoragarh','PI'),(652,'India','Uttarakhand (UK)','Chamoli','CL'),(653,'India','Uttarakhand (UK)','Uttarkashi','UT'),(654,'India','Uttarakhand (UK)','Bageshwar','BA'),(655,'India','Uttarakhand (UK)','Champawat','CP'),(656,'India','Uttarakhand (UK)','Rudraprayag','RP'),(657,'India','West Bengal (WB)','North 24 Parganas','PN'),(658,'India','West Bengal (WB)','South 24 Parganas','PS'),(659,'India','West Bengal (WB)','Bardhaman','BR'),(660,'India','West Bengal (WB)','Murshidabad','MSD'),(661,'India','West Bengal (WB)','Hooghly','HG'),(662,'India','West Bengal (WB)','Nadia','NA'),(663,'India','West Bengal (WB)','Paschim Medinipur','PM'),(664,'India','West Bengal (WB)','Howrah','HR'),(665,'India','West Bengal (WB)','Kolkata','KO'),(666,'India','West Bengal (WB)','Purba Medinipur','PR'),(667,'India','West Bengal (WB)','Maldah','MA'),(668,'India','West Bengal (WB)','Jalpaiguri','JA'),(669,'India','West Bengal (WB)','Bankura','BN'),(670,'India','West Bengal (WB)','Birbhum','BI'),(671,'India','West Bengal (WB)','Uttar Dinajpur','UD'),(672,'India','West Bengal (WB)','Purulia','PU'),(673,'India','West Bengal (WB)','Cooch Behar','KB'),(674,'India','West Bengal (WB)','Darjeeling','DA'),(675,'India','West Bengal (WB)','Alipurduar','AD'),(676,'India','West Bengal (WB)','Dakshin Dinajpur','DD');
/*!40000 ALTER TABLE `app_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_customer`
--

DROP TABLE IF EXISTS `app_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `phoneno` varchar(15) NOT NULL,
  `emailid` varchar(30) NOT NULL,
  `gstno` varchar(30) NOT NULL,
  `address` varchar(100) NOT NULL,
  `dob` datetime(6) NOT NULL,
  `district` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `customer_code` varchar(10) NOT NULL,
  `phoneno_sec` varchar(15) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `gender` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_code` (`customer_code`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_customer`
--

LOCK TABLES `app_customer` WRITE;
/*!40000 ALTER TABLE `app_customer` DISABLE KEYS */;
INSERT INTO `app_customer` VALUES (11,'Dennis Peter George','432432','dennisgeorge.mec@gmail.com','','SRA 22-ACrash Road','1990-02-11 18:30:00.000000','Ernakulam','Kerala (KL)','India','KLER11','',1,'','Male');
/*!40000 ALTER TABLE `app_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_discount`
--

DROP TABLE IF EXISTS `app_discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_discount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `discount_type` varchar(10) NOT NULL,
  `value` double NOT NULL,
  `franchise_code` int(11) NOT NULL,
  `pid_id` int(11) DEFAULT NULL,
  `proid_id` int(11) DEFAULT NULL,
  `sid_id` int(11) DEFAULT NULL,
  `subject` varchar(25) NOT NULL,
  `tid_id` int(11) DEFAULT NULL,
  `franchise_name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_discount_pid_id_b711fb4d_fk_app_package_id` (`pid_id`),
  KEY `app_discount_proid_id_6a167a80_fk_app_product_id` (`proid_id`),
  KEY `app_discount_sid_id_0e3d67fb_fk_app_service_id` (`sid_id`),
  KEY `app_discount_tid_id_db6725e0_fk_app_treatment_id` (`tid_id`),
  CONSTRAINT `app_discount_pid_id_b711fb4d_fk_app_package_id` FOREIGN KEY (`pid_id`) REFERENCES `app_package` (`id`),
  CONSTRAINT `app_discount_proid_id_6a167a80_fk_app_product_id` FOREIGN KEY (`proid_id`) REFERENCES `app_product` (`id`),
  CONSTRAINT `app_discount_sid_id_0e3d67fb_fk_app_service_id` FOREIGN KEY (`sid_id`) REFERENCES `app_service` (`id`),
  CONSTRAINT `app_discount_tid_id_db6725e0_fk_app_treatment_id` FOREIGN KEY (`tid_id`) REFERENCES `app_treatment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_discount`
--

LOCK TABLES `app_discount` WRITE;
/*!40000 ALTER TABLE `app_discount` DISABLE KEYS */;
INSERT INTO `app_discount` VALUES (1,'%',5,5,NULL,1,NULL,'Product',NULL,'Calicut Medical Centre'),(2,'%',5,1,NULL,NULL,NULL,'Additional Procedure',1,'My Medical Store'),(3,'price',40,1,NULL,4,NULL,'Product',NULL,'My Medical Store'),(4,'%',25,0,36,NULL,NULL,'Package',NULL,'Head Office'),(5,'%',20,0,NULL,NULL,1,'Service',NULL,'Head Office');
/*!40000 ALTER TABLE `app_discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_enquiry`
--

DROP TABLE IF EXISTS `app_enquiry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_enquiry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `country` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `city` varchar(30) NOT NULL,
  `type` varchar(10) DEFAULT NULL,
  `tid` varchar(10) NOT NULL,
  `franchise_code` int(11) DEFAULT NULL,
  `status` varchar(15) NOT NULL,
  `pid` int(11) DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  `p_id` int(11) DEFAULT NULL,
  `s_id` int(11) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `lastchanged` datetime(6) DEFAULT NULL,
  `confirmed_time` datetime(6) DEFAULT NULL,
  `requested_time` datetime(6) DEFAULT NULL,
  `t_id` int(11) DEFAULT NULL,
  `trid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_enquiry_p_id_ca18358b_fk_app_package_id` (`p_id`),
  KEY `app_enquiry_s_id_2113d393_fk_app_service_id` (`s_id`),
  KEY `app_enquiry_t_id_8b770a01_fk_app_treatmentmaster_id` (`t_id`),
  CONSTRAINT `app_enquiry_p_id_ca18358b_fk_app_package_id` FOREIGN KEY (`p_id`) REFERENCES `app_package` (`id`),
  CONSTRAINT `app_enquiry_s_id_2113d393_fk_app_service_id` FOREIGN KEY (`s_id`) REFERENCES `app_service` (`id`),
  CONSTRAINT `app_enquiry_t_id_8b770a01_fk_app_treatmentmaster_id` FOREIGN KEY (`t_id`) REFERENCES `app_treatmentmaster` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_enquiry`
--

LOCK TABLES `app_enquiry` WRITE;
/*!40000 ALTER TABLE `app_enquiry` DISABLE KEYS */;
INSERT INTO `app_enquiry` VALUES (11,'James','dennispetergeorge@gmail.com','9895',NULL,'India','Kerala','Ernakulam','Brahmi','Treatment',1,'Pending',NULL,NULL,NULL,NULL,'2018-03-06 06:27:35.493571',NULL,NULL,'2018-02-20 10:00:00.000000',1,1);
/*!40000 ALTER TABLE `app_enquiry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_franchise`
--

DROP TABLE IF EXISTS `app_franchise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_franchise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `franchise_name` varchar(100) NOT NULL,
  `franchise_type` varchar(10) NOT NULL,
  `phoneno` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `district` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `pincode` varchar(10) NOT NULL,
  `owner` varchar(20) NOT NULL,
  `ownercontact` varchar(10) NOT NULL,
  `remarks` varchar(300) DEFAULT NULL,
  `permbs1` tinyint(1) NOT NULL,
  `permbs2` tinyint(1) NOT NULL,
  `currency` varchar(10) NOT NULL,
  `permb3` tinyint(1) NOT NULL,
  `permb4` tinyint(1) NOT NULL,
  `permb5` tinyint(1) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `distributor_id` int(11) NOT NULL,
  `website` varchar(50) NOT NULL,
  `admin_id` int(11) DEFAULT NULL,
  `sales_today` double NOT NULL,
  `customers_today` double NOT NULL,
  `new_customers` double NOT NULL,
  `bankaccountno` varchar(50) NOT NULL,
  `ifsccode` varchar(20) NOT NULL,
  `bankname` varchar(50) NOT NULL,
  `town` varchar(20) NOT NULL,
  `gstno` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `franchise_name` (`franchise_name`),
  KEY `app_franchise_distributor_id_0a256a67_fk_app_profile_id` (`distributor_id`),
  KEY `app_franchise_admin_id_48960294_fk_app_profile_id` (`admin_id`),
  CONSTRAINT `app_franchise_admin_id_48960294_fk_app_profile_id` FOREIGN KEY (`admin_id`) REFERENCES `app_profile` (`id`),
  CONSTRAINT `app_franchise_distributor_id_0a256a67_fk_app_profile_id` FOREIGN KEY (`distributor_id`) REFERENCES `app_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_franchise`
--

LOCK TABLES `app_franchise` WRITE;
/*!40000 ALTER TABLE `app_franchise` DISABLE KEYS */;
INSERT INTO `app_franchise` VALUES (1,'My Medical Store','Brahmi','8129054175','ABC Road','Ernakulam','Kerala (KL)','India','682021','Sreejith','8129054175','',0,0,'False',0,0,0,1,9,'',NULL,0,0,0,'','','','Thrikkakara',''),(5,'Calicut Medical Centre','Tulsi','9985123456','Opposite Grand Mall, XYZ Road','Kozhikode','Kerala (KL)','India','699212','Joy','8129054175','',1,1,'False',1,1,1,1,9,'',2,0,0,0,'1234 HGFD 5678 POIU','UTIB0003426','','',''),(6,'My New Franchisee','Brahmi','535','fwe efw','Alappuzha','Kerala (KL)','India','23425','Dre','9676455647','',0,0,'False',0,0,0,1,18,'',17,0,0,0,'','','','','');
/*!40000 ALTER TABLE `app_franchise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_hoproduct`
--

DROP TABLE IF EXISTS `app_hoproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_hoproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(50) NOT NULL,
  `MRP` double DEFAULT NULL,
  `SKU` varchar(15) NOT NULL,
  `stock` int(11) NOT NULL,
  `tax_CGST` double NOT NULL,
  `tax_SGST` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_hoproduct`
--

LOCK TABLES `app_hoproduct` WRITE;
/*!40000 ALTER TABLE `app_hoproduct` DISABLE KEYS */;
INSERT INTO `app_hoproduct` VALUES (1,'Stationary',1000,'nos',14,5,5),(2,'Banner',2000,'nos',9,2.5,2.5);
/*!40000 ALTER TABLE `app_hoproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_implementation`
--

DROP TABLE IF EXISTS `app_implementation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_implementation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `franchise_code` int(11) NOT NULL,
  `date` date NOT NULL,
  `painting` tinyint(1) NOT NULL,
  `electrification` tinyint(1) NOT NULL,
  `signboard` tinyint(1) NOT NULL,
  `installation_of_required_equipment` tinyint(1) NOT NULL,
  `inaugration_date` date NOT NULL,
  `distributor_id` int(11) NOT NULL,
  `comments` varchar(100) NOT NULL,
  `date_mou` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_implementation_distributor_id_32909fe6_fk_app_profile_id` (`distributor_id`),
  CONSTRAINT `app_implementation_distributor_id_32909fe6_fk_app_profile_id` FOREIGN KEY (`distributor_id`) REFERENCES `app_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_implementation`
--

LOCK TABLES `app_implementation` WRITE;
/*!40000 ALTER TABLE `app_implementation` DISABLE KEYS */;
INSERT INTO `app_implementation` VALUES (1,6,'2018-01-13',1,1,0,0,'2018-02-22',18,'','2018-01-13'),(2,6,'2018-01-13',1,1,0,0,'2018-02-22',18,'','2018-01-13'),(3,6,'2018-01-13',1,1,0,0,'2018-02-22',18,'','2018-01-13'),(4,6,'2018-01-13',1,1,0,0,'2018-02-22',18,'','2018-01-13'),(5,6,'2018-01-13',1,1,0,0,'2018-03-23',18,'','2018-01-12');
/*!40000 ALTER TABLE `app_implementation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_inspection`
--

DROP TABLE IF EXISTS `app_inspection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_inspection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `franchise_code` int(11) NOT NULL,
  `date` date NOT NULL,
  `staff_behaviour` varchar(10) NOT NULL,
  `distributor_id` int(11) NOT NULL,
  `comments` varchar(100) NOT NULL,
  `v1` varchar(10) NOT NULL,
  `v2` varchar(10) NOT NULL,
  `v3` varchar(10) NOT NULL,
  `v4` varchar(10) NOT NULL,
  `v5` varchar(10) NOT NULL,
  `v6` varchar(10) NOT NULL,
  `v7` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_inspection_distributor_id_122d9727_fk_app_profile_id` (`distributor_id`),
  CONSTRAINT `app_inspection_distributor_id_122d9727_fk_app_profile_id` FOREIGN KEY (`distributor_id`) REFERENCES `app_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_inspection`
--

LOCK TABLES `app_inspection` WRITE;
/*!40000 ALTER TABLE `app_inspection` DISABLE KEYS */;
INSERT INTO `app_inspection` VALUES (1,1,'2017-12-03','Good',9,'','Poor','Poor','Poor','Poor','Poor','Poor','Poor'),(2,1,'2017-12-28','Excellent',9,'None','Good','Excellent','Excellent','Excellent','Excellent','Good','Poor'),(3,1,'2017-12-28','Excellent',9,'None whatsoever','Poor','Average','Poor','Excellent','Poor','Poor','Good'),(4,6,'2018-01-13','Average',18,'','Good','Average','Excellent','Excellent','Average','Average','Excellent'),(5,1,'2018-02-08','Poor',9,'','Poor','Average','Excellent','Poor','Average','Poor','Good');
/*!40000 ALTER TABLE `app_inspection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_note`
--

DROP TABLE IF EXISTS `app_note`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_note` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `body` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `pic` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_note`
--

LOCK TABLES `app_note` WRITE;
/*!40000 ALTER TABLE `app_note` DISABLE KEYS */;
INSERT INTO `app_note` VALUES (2,'csa','ac','2018-01-05 03:22:01.392472','Feedbackform-Ittiam.jpg');
/*!40000 ALTER TABLE `app_note` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_package`
--

DROP TABLE IF EXISTS `app_package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_package` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `package_code` varchar(20) NOT NULL,
  `rates` varchar(30) NOT NULL,
  `body_part` varchar(30) DEFAULT NULL,
  `tax_CGST` double DEFAULT NULL,
  `tax_SGST` double DEFAULT NULL,
  `remarks` varchar(200) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_package_package_code_5caca94f_uniq` (`package_code`),
  UNIQUE KEY `app_package_name_3c0c2437_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_package`
--

LOCK TABLES `app_package` WRITE;
/*!40000 ALTER TABLE `app_package` DISABLE KEYS */;
INSERT INTO `app_package` VALUES (1,' Sukhachikitsa ( wellness package) : 7 Days','1','12000,15000,12000,19500','Full body',0,0,'','7 Days','This wellness package includes Body pack, whole body massage, Siro abhyangam, Mukha abhyangam, Nasyam, Steam bath, Padha Abhyangam, fish Spa, Sirodhara oil/ milk and Njavara theppu',''),(2,' Sukhachikitsa ( wellness package) : 14 Days','2','23000,28000,23000,36500','Full body',0,0,'','14 Days','',''),(3,'Panchakarma/Detoxification packages : 7 Days','3','13000,15000,13000,19500','Full body',0,0,'','7 Days','Quite often we tend to forget that our body is a host of quite a lot of toxins from food, surroundings and our own habits  etc..  These toxins accumulate in our body and slowly weakening our resistance power, resulting in numerous diseases.  This treatment is for creating healthy body, not against any disease.  It includes Abhyangam, Kizhi treatment traditional, Nasyam, Steam,  Kashaya Vasthi/ Vamanam/ Virechanam, Sirodhara, Thalapothichil, Pizhichil and Snehapanam',''),(4,'Panchakarma/Detoxification packages : 14 Days','4','24000,28000,24000,36500','Full body',0,0,'','14 days','',''),(5,'Panchakarma/Detoxification packages  : 21 Days','5','32000,36000,32000,47000','Full body',0,0,'','21 days','',''),(6,'Panchakarma/Detoxification packages  : 28 Days','6','48000,50000,48000,65000','Full body',0,0,'','28 days','',''),(7,' Club Ayurveda special - Fruit Wrap - Summer Special','7','1600,2000,1600,3000','',0,0,'','','In this treatment body is wrapped with medicated powder and fruits. It is summer special treatment to protect your body from the climate change.','Fruit_Wrap_Summer_Special_yyhrjpM.jpg'),(8,' Postnatal Care (Special Care to Woman after Delivery): 1 Day','8','2000,2400,2000,3150','Full body',0,0,'','1 day ','In Ayurvedic postnatal treatment external treatments should be done only after the complete healing of wounds in case of caesarean. The medicines given in the first stage (15 days) will help in the healing of surgical wound, increase production of milk, help proper digestion and bowl movements. Give relief to constipation, help contraction of uterus, enhance excretion of waste, relieve body pain etc..',''),(9,' Postnatal Care (Special Care to Woman after Delivery): 7 Days','9','14000,16800,14000,21850','Full body',0,0,'','7 days ','',''),(10,' Postnatal Care (Special Care to Woman after Delivery): 15 Days','10','30000,36000,30000,47000','',0,0,'','','','postnatal_2.jpg'),(11,'Bride and Groom package (Kallyanapurva Chikitsa) :1 Day','11','1500,1800,1500,2350','Full body',0,0,'','1 day ','It increases the stamina and  rejuvenating each cells of body and refreshes the mind also. This package is specialized for Bride and Grooms and it is a skin tone enhancing package, Includes Fruit massage, oil massage, Steam bath, Njavaratheppu, kesha kanthi massage, Antidandruff treatment and Mukhalepam are doing on this package.',''),(12,'Bride and Groom package (Kallyanapurva Chikitsa) :7 Day','12','9000,11100,9000,14450','Full body',0,0,'','7 days ','',''),(13,'Bride and Groom package (Kallyanapurva Chikitsa) :14 Day','13','17000,21200,17000,27550','',0,0,'','','','Bride_and_Groom_PackageKalyanapurva_chikitsa_qu1sAcE.jpg'),(14,'Club Ayurveda Special Couples package','14','3800,4500,3800,5850','',0,0,'','','It is one of the special treatment for young couples in which marmas been anointed with medicated oil, it keeps you calm physically and mentally, balances all doshas in your body, rejuvenates each body cells, increases blood circulation to the reproductive organs and rehydrates your body.','Club_ayurveda-_Special_Coples_Package.jpg'),(15,' Arogya Raksha Chikitsa ( Health Maintenance Package): 7 Days','15','7000,9800,7000,12750','Full body',0,0,'','7 days',' Our body needs maintenance-The feeling of tiredness, irritability or troubles of stomach or body ache which will last for shorter duration will affect our moods and capability to work. This package includes  Abyangam, Elakizhi, Virechanam and Steam bath. We offer Arogya Raksha Chikitsa under two different packages.',''),(16,' Arogya Raksha Chikitsa ( Health Maintenance Package): 14 Days','16','13000,18600,13000,24150','',0,0,'','','','Arogya_raksha_chikitsaHealth_Maintenance_package_onaNBuM.jpg'),(17,' Ayursparsh Recharging Therapy : 3 Days','17','7000,8500,7000,11050','Full body',0,0,'','3 days','This package includes Traditional whole body massage starting with a traditional ritual followed by a head massage, face massage and then the full body massage, Nasyam and Sirodhara- means dripping of luke warm traditionally prepared oil on the forehead in a rhythmic manner. It improves blood circulation to brain, soothes neurons, reduce tension, insomnia (Sleeplessness), blood pressure and calms mind and body. There are 3 types of Ayursparsh packages.',''),(18,' Ayursparsh Recharging Therapy : 7 Days','18','11000,14500,11000,18850','Full body',0,0,'','7 days ','',''),(19,' Ayursparsh Recharging Therapy : 14 Days','19','17000,24000,17000,31200','',0,0,'','','','Ayursparsh_L9AXjTo.jpg'),(20,'Rejuvination Package ( Rasayana) : 1 Day','20','3500,4250,3500,5550','Full body',0,0,'','1 day ','This treatment enhances sexual vigour by purifying and improving blood circulation to the genitals.  Special internal medicines and external oils are used for this purpose. It includes Abhyangam, Elakizhi, Njavarakizhi, steam, Vasthi, Pizhichil, and Sirodhara.',''),(21,'Rejuvination Package ( Rasayana): 14 Days','21','36200,46700,36200,60700','Full body',0,0,'','14 days ','',''),(22,'Rejuvination Package ( Rasayana): 21 Days','22','42000,57750,42000,75050','Full body',0,0,'','21 days ','',''),(23,'Rejuvination Package ( Rasayana): 28 Days','23','50000,71000,50000,92300','',0,0,'','','','rejuvination_U0qPoTT.jpg'),(24,'Slimming Package/ Obesity Package','24','1600,2200,1600,2850','',0,0,'','','This package mainly includes two types of massages Udwarthanam and Oil massage. It also includes Steam bath, course of medicines. Its duration depends on the body constitution and the decision of our doctor.','slimimng1_hP4u0Ds.jpg'),(25,'Brahmi Plus ( Memory boosting and Stress relieving  Package )       : 14 Days','25','21000,26600,21000,34550','Head and Shoulders',0,0,'','14 days ','Memory disorders can be attributed to many reasons. The degeneration of brain cells due to old age, Injuries, abuse and influence of drugs is a major one.  For this brahmi, Aswagandha etc used as internal medicines. It also includes head massage, Nasyam, Sirodhara and  Sirovasthi. There are 3 types of packages.',''),(26,'Brahmi Plus ( Memory boosting and Stress relieving  Package )       : 21 Days','26','31500,39900,31500,51850','Head and Shoulders',0,0,'','21 days ','',''),(27,'Brahmi Plus ( Memory boosting and Stress relieving  Package )       : 28 Days','27','42000,53200,42000,69150','Head and Shoulders',0,0,'','28 mins','',''),(28,'Club Ayurveda Special - Siro Abhyangam with Shoulders','28','500,700,500,1000','Head and Shoulders',0,0,'',' 30 mins','We proudly present this particular treatment for   youths and new Gen working peoples.  In this package head including shoulders are massaged with herbal oil.  It helps in reducing mental stress and increasing blood circulation. It cools the system and gives you sound sleep and rids you of headache.  If you undergo this treatment once in week, it will energize you more in your activities.',''),(29,'Club Ayurveda Special -Beauty Care ( Soundarya Chikitsa )','29','3750,4500,3750,5850','Full body',0,0,'','3days','This package starts with a gentle head massage  then Mukhalepanam, Thalapothichil, Ksheera dhoomam and body scrub with herbal scrubbers which peel out the dead skin, and the accompanied body massage improves blood circulation, complexion and the special herbal pack tones the skin and reduces ageing process.',''),(30,'Club ayurveda Special Rejuvenation and Shirodhara Packages for youths','30','5600,8000,5600,10500','Full body',0,0,'','7days','Rejuvenation  package  tones up the Muscles, increase blood circulation, eliminates toxins from the body by inducing profuse sweating, and refreshes you. In Shirodhara, the medicated oil is poured gently through forehead. It relaxes and rejuvenates your mind, revitalizes the nervous system, elevates the mood. It is best for hypertension, anxiety and depression.',''),(31,'Abhyangam with Herbal Facial                   ','31','1300,1700,1300,2200','Full body',0,0,'','60 mins ','',''),(32,'Abhyangam with Shirodhara','32','1600,2000,1600,2600','Full body',0,0,'','60 mins ','',''),(33,'Abhyangam with Udhwarthanam','33','1800,2200,1800,2850','Full body',0,0,'','60 mins ','',''),(34,'Abhyangam with Oushadha   snanam         ','34','1600,2000,1600,2600','Full body',0,0,'','60 mins ','',''),(35,'Abhyangam with Marma treatment ','35','2500,3000,2500,3900','Full body',0,0,'','60 mins ','',''),(36,'Abhyangam with Kizhi ','36','1700,2100,1700,2750','Full body',0,0,'','60 mins ','',''),(37,'Shirodhara with Herbal facial ','37','2000,2400,2000,3150','Head and Shoulders',0,0,'','60 mins ','',''),(38,'Shirodhara with Head, Face and Foot Massage','38','2200,2600,2200,3350','',0,0,'','60 mins ','',''),(39,'Shirodhara with Head and Face Massage ','39','1800,2200,1800,2850','Head and Shoulders',0,0,'','60 mins ','',''),(40,'Shirodhara Clubayurveda  special ','40','2500,3000,2500,3900','Head and Shoulders',0,0,'','45 mins','',''),(41,'Meditation','41','','',0,0,'','','',''),(42,'Yoga','42','','',0,0,'','','','');
/*!40000 ALTER TABLE `app_package` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_packagemask`
--

DROP TABLE IF EXISTS `app_packagemask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_packagemask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mask` varchar(500) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_packagemask`
--

LOCK TABLES `app_packagemask` WRITE;
/*!40000 ALTER TABLE `app_packagemask` DISABLE KEYS */;
INSERT INTO `app_packagemask` VALUES (1,'111111111111110000000000000000000000000',1),(2,'001111011100000000000000000000000000000',5);
/*!40000 ALTER TABLE `app_packagemask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_pendingprescription`
--

DROP TABLE IF EXISTS `app_pendingprescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_pendingprescription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_code` varchar(6) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `doctor_name` varchar(30) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  `consultation_fees` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_pendingprescription`
--

LOCK TABLES `app_pendingprescription` WRITE;
/*!40000 ALTER TABLE `app_pendingprescription` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_pendingprescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_pendingtreatment`
--

DROP TABLE IF EXISTS `app_pendingtreatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_pendingtreatment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_code` varchar(6) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `doctor_name` varchar(30) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  `consultation_fees` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_pendingtreatment`
--

LOCK TABLES `app_pendingtreatment` WRITE;
/*!40000 ALTER TABLE `app_pendingtreatment` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_pendingtreatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_prescription`
--

DROP TABLE IF EXISTS `app_prescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_prescription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pending_prescription_id` int(11) DEFAULT NULL,
  `pending_treatment_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_prescription_pending_prescription_5f4b73a6_fk_app_pendi` (`pending_prescription_id`),
  KEY `app_prescription_pending_treatment_id_dbf9ad9e_fk_app_pendi` (`pending_treatment_id`),
  CONSTRAINT `app_prescription_pending_prescription_5f4b73a6_fk_app_pendi` FOREIGN KEY (`pending_prescription_id`) REFERENCES `app_pendingprescription` (`id`),
  CONSTRAINT `app_prescription_pending_treatment_id_dbf9ad9e_fk_app_pendi` FOREIGN KEY (`pending_treatment_id`) REFERENCES `app_pendingtreatment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_prescription`
--

LOCK TABLES `app_prescription` WRITE;
/*!40000 ALTER TABLE `app_prescription` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_prescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_product`
--

DROP TABLE IF EXISTS `app_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(50) NOT NULL,
  `short_code` varchar(10) NOT NULL,
  `MRP` int(11) DEFAULT NULL,
  `SKU` varchar(15) NOT NULL,
  `tax_CGST` double NOT NULL,
  `tax_SGST` double NOT NULL,
  `category` varchar(30) NOT NULL,
  `remarks` varchar(200) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_product_item_name_franchise_code_e623e7cc_uniq` (`item_name`,`franchise_code`)
) ENGINE=InnoDB AUTO_INCREMENT=330 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_product`
--

LOCK TABLES `app_product` WRITE;
/*!40000 ALTER TABLE `app_product` DISABLE KEYS */;
INSERT INTO `app_product` VALUES (1,'Abhayarishtam  ','1',79,'450ml',0,0,'Arishtam','',0),(2,'Amrutharishtam ','2',83,'450ml',0,0,'Arishtam','',0),(3,'Aragwadharishtam ','3',88,'450ml',0,0,'Arishtam','',0),(4,'Aravindasavam ','4',88,'450ml',0,0,'Arishtam','',0),(5,'Asokarishtam  ','5',77,'450ml',0,0,'Arishtam','',0),(6,'Aswagandharishtam ','6',138,'450ml',0,0,'Arishtam','',0),(7,'Ayaskrity','7',99,'450ml',0,0,'Arishtam','',0),(8,'Balarishtam','8',88,'450ml',0,0,'Arishtam','',0),(9,'Chandanasavam','9',77,'450ml',0,0,'Arishtam','',0),(10,'Chitrakasavam','10',132,'450ml',0,0,'Arishtam','',0),(11,'Dasamoolarishtam','11',105,'450ml',0,0,'Arishtam','',0),(12,'Dhanwantararishtam','12',94,'450ml',0,0,'Arishtam','',0),(13,'Draksharishtam','13',110,'450ml',0,0,'Arishtam','',0),(14,'Duralabharishtam','14',88,'450ml',0,0,'Arishtam','',0),(15,'Jeerakarishtam','15',121,'450ml',0,0,'Arishtam','',0),(16,'Kanakasavam','16',77,'450ml',0,0,'Arishtam','',0),(17,'Khadirarishtam','17',110,'450ml',0,0,'Arishtam','',0),(18,'Kumaryasavam','18',94,'450ml',0,0,'Arishtam','',0),(19,'Kutajarishtam','19',94,'450ml',0,0,'Arishtam','',0),(20,'Lohasavam','20',88,'450ml',0,0,'Arishtam','',0),(21,'Mustarishtam','21',88,'450ml',0,0,'Arishtam','',0),(22,'Partharishtam','22',99,'450ml',0,0,'Arishtam','',0),(23,'Pippalyasavam','23',88,'450ml',0,0,'Arishtam','',0),(24,'Punarnavasam','24',80,'450ml',0,0,'Arishtam','',0),(25,'Saraswatarishtam','25',248,'450ml',0,0,'Arishtam','',0),(26,'Saribadyasavam','26',90,'450ml',0,0,'Arishtam','',0),(27,'Vasarishtam','27',116,'450ml',0,0,'Arishtam','',0),(28,'Anu Tailam','28',60,'10ml',0,0,'Tailams/Kuzhambus','',0),(29,'Asanaeladi Co. oil','29',205,'200ml',0,0,'Tailams/Kuzhambus','',0),(30,'Bala Tailam','30',106,'25ml',0,0,'Tailams/Kuzhambus','',0),(31,'Balaswagandhadi Tailam','31',202,'200ml',0,0,'Tailams/Kuzhambus','',0),(32,'Balaswagandhadi Kuzhambu','32',209,'200ml',0,0,'Tailams/Kuzhambus','',0),(33,'Chemparatyadi Co. oil','33',136,'200ml',0,0,'Tailams/Kuzhambus','',0),(34,'Chinchadi Tailam (S)','34',127,'200ml',0,0,'Tailams/Kuzhambus','',0),(35,'Dhanwantaram Tailam','35',204,'200ml',0,0,'Tailams/Kuzhambus','',0),(36,'Dhanwantaram Kuzhambu','36',170,'200ml',0,0,'Tailams/Kuzhambus','',0),(37,'Dhordhoorapatrati Co. oil','37',143,'200ml',0,0,'Tailams/Kuzhambus','',0),(38,'Eladi Co. oil','38',170,'200ml',0,0,'Tailams/Kuzhambus','',0),(39,'Gandha Tailam ','39',65,'10ml',0,0,'Tailams/Kuzhambus','',0),(40,'Gandharvahastadi Castor Oil','40',63,'50ml',0,0,'Tailams/Kuzhambus','',0),(41,'Karpasastyadi Tailam','41',152,'200ml',0,0,'Tailams/Kuzhambus','',0),(42,'Karpasastyadi Kuzhambu','42',148,'200ml',0,0,'Tailams/Kuzhambus','',0),(43,'Karpooradi Co. oil','43',125,'200ml',0,0,'Tailams/Kuzhambus','',0),(44,'Kayyanyadi Co. oil','44',158,'200ml',0,0,'Tailams/Kuzhambus','',0),(45,'Kottamchukkadi Tailam','45',138,'200ml',0,0,'Tailams/Kuzhambus','',0),(46,'Ksheerabala Tailam','46',166,'200ml',0,0,'Tailams/Kuzhambus','',0),(47,'Kumkumadi Tailam','47',326,'10ml',0,0,'Tailams/Kuzhambus','',0),(48,'Mahamasha Tailam','48',284,'200ml',0,0,'Tailams/Kuzhambus','',0),(49,'Maharajaprasarini Tailam','49',67,'10ml',0,0,'Tailams/Kuzhambus','',0),(50,'Malatyadi Co. oil','50',139,'200ml',0,0,'Tailams/Kuzhambus','',0),(51,'Marichadi Co. oil','51',120,'200ml',0,0,'Tailams/Kuzhambus','',0),(52,'Murivenna','52',184,'200ml',0,0,'Tailams/Kuzhambus','',0),(53,'Nalpamaradhi Co. oil','53',138,'200ml',0,0,'Tailams/Kuzhambus','',0),(54,'Narayana Tailam (B)','54',208,'200ml',0,0,'Tailams/Kuzhambus','',0),(55,'Neelibhringadi Co. oil','55',206,'200ml',0,0,'Tailams/Kuzhambus','',0),(56,'Pinda Tailam','56',138,'200ml',0,0,'Tailams/Kuzhambus','',0),(57,'Prabhanjanam Kuzhambu','57',162,'200ml',0,0,'Tailams/Kuzhambus','',0),(58,'Sahacharadi kuzhambu','58',176,'200ml',0,0,'Tailams/Kuzhambus','',0),(59,'Sahacharadi Tailam(B)','59',176,'200ml',0,0,'Tailams/Kuzhambus','',0),(60,'Amrutotaram Kashayam','60',100,'200ml',0,0,'Kashayam','',0),(61,'Aragwadhadi Kashayam','61',113,'200ml',0,0,'Kashayam','',0),(62,'Ashtavargam Kashayam','62',113,'200ml',0,0,'Kashayam','',0),(63,'Balaguluchyadi Kashayam','63',111,'200ml',0,0,'Kashayam','',0),(64,'Balajeerakadi Kashayam','64',109,'200ml',0,0,'Kashayam','',0),(65,'Bruhatyadi Kashayam','65',133,'200ml',0,0,'Kashayam','',0),(66,'Chirivilwadi Kashayam ','66',139,'200ml',0,0,'Kashayam','',0),(67,'Dasamoolam Kashayam','67',114,'200ml',0,0,'Kashayam','',0),(68,'Dasamoolakatutrayam Kashayam','68',121,'200ml',0,0,'Kashayam','',0),(69,'Dhanadanayanadi Kashayam','69',142,'200ml',0,0,'Kashayam','',0),(70,'Dhanwantaram Kashayam','70',133,'200ml',0,0,'Kashayam','',0),(71,'Drakshadi Kashayam','71',140,'200ml',0,0,'Kashayam','',0),(72,'Gandharvahastadi Kashayam','72',100,'200ml',0,0,'Kashayam','',0),(73,'Gulgulutiktakam Kashayam','73',176,'200ml',0,0,'Kashayam','',0),(74,'Guluchyadi Kashayam','74',151,'200ml',0,0,'Kashayam','',0),(75,'Indukantam Kashayam','75',124,'200ml',0,0,'Kashayam','',0),(76,'Katakakhadiradi Kashayam','76',108,'200ml',0,0,'Kashayam','',0),(77,'Karimbirubadi Kashayam','77',101,'200ml',0,0,'Kashayam','',0),(78,'Kokilakshakam Kashayam','78',101,'200ml',0,0,'Kashayam','',0),(79,'Kulathadi Kashayam','79',137,'200ml',0,0,'Kashayam','',0),(80,'Lasunairandadi Kashayam','80',136,'200ml',0,0,'Kashayam','',0),(81,'Maharasnadi Kashayam','81',161,'200ml',0,0,'Kashayam','',0),(82,'Mahatiktakam Kashayam','82',179,'200ml',0,0,'Kashayam','',0),(83,'Manjishtadi Kashayam','83',139,'200ml',0,0,'Kashayam','',0),(84,'Musaleekhadiradi Kashayam','84',101,'200ml',0,0,'Kashayam','',0),(85,'Nayopayam Kashayam','85',147,'200ml',0,0,'Kashayam','',0),(86,'Nimbadi Kashayam','86',107,'200ml',0,0,'Kashayam','',0),(87,'Pachanamrutam Kashayam','87',137,'200ml',0,0,'Kashayam','',0),(88,'Panchatiktakam Kashayam','88',163,'200ml',0,0,'Kashayam','',0),(89,'Pathyakshadhatryadi Kashayam','89',121,'200ml',0,0,'Kashayam','',0),(90,'Patolakaturohinyadi Kashayam','90',189,'200ml',0,0,'Kashayam','',0),(91,'Patolamooladi Kashayam','91',124,'200ml',0,0,'Kashayam','',0),(92,'Prasarinyadi Kashayam','92',126,'200ml',0,0,'Kashayam','',0),(93,'Punarnavadi Kashayam','93',102,'200ml',0,0,'Kashayam','',0),(94,'Rasonadi Kashayam','94',177,'200ml',0,0,'Kashayam','',0),(95,'Rasanadi Kashayam(S)','95',170,'200ml',0,0,'Kashayam','',0),(96,'Rasanadi kashayam(B)','96',182,'200ml',0,0,'Kashayam','',0),(97,'Rasnasaptakam Kashayam','97',108,'200ml',0,0,'Kashayam','',0),(98,'Sahacharadi Kashayam','98',100,'200ml',0,0,'Kashayam','',0),(99,'Saptasaram Kashayam','99',120,'200ml',0,0,'Kashayam','',0),(100,'Sonitamrutham Kashayam','100',139,'200ml',0,0,'Kashayam','',0),(101,'Sukumaram Kashayam','101',118,'200ml',0,0,'Kashayam','',0),(102,'Tiktakam Kashayam','102',142,'200ml',0,0,'Kashayam','',0),(103,'Trayantyadi Kashayam','103',144,'200ml',0,0,'Kashayam','',0),(104,'Vajrakam Kashayam','104',131,'200ml',0,0,'Kashayam','',0),(105,'Varanadi Kashayam','105',108,'200ml',0,0,'Kashayam','',0),(106,'Vasaguluchyadi Kashayam','106',126,'200ml',0,0,'Kashayam','',0),(107,'Vidaryadi Kashayam','107',126,'200ml',0,0,'Kashayam','',0),(108,'Vyaghryadi Kashayam','108',113,'200ml',0,0,'Kashayam','',0),(109,'Aragwadhadi Ghritam','109',240,'200ml',0,0,'Ghritam','',0),(110,'Brahmi Ghritam','110',240,'200ml',0,0,'Ghritam','',0),(111,'Dadimadi Ghritam','111',231,'200ml',0,0,'Ghritam','',0),(112,'Gulgulutiktakam Ghritam','112',293,'200ml',0,0,'Ghritam','',0),(113,'Indukantam Ghritam','113',232,'200ml',0,0,'Ghritam','',0),(114,'Mahakalyanaka Ghritam','114',317,'200ml',0,0,'Ghritam','',0),(115,'Mahatiktaka Ghritam','115',258,'200ml',0,0,'Ghritam','',0),(116,'Phalasarpis','116',245,'200ml',0,0,'Ghritam','',0),(117,'Saraswata Ghritam','117',255,'200ml',0,0,'Ghritam','',0),(118,'Sukumara Ghritam','118',315,'200ml',0,0,'Ghritam','',0),(119,'Tiktaka Ghritam','119',283,'200ml',0,0,'Ghritam','',0),(120,'Varanadi Ghritam','120',224,'200ml',0,0,'Ghritam','',0),(121,'Vidaryadi Ghritam','121',240,'200ml',0,0,'Ghritam','',0),(122,'Agastyarasayanam','122',120,'250gm',0,0,'Lehyam','',0),(123,'Aswagandhadi Lehyam','123',113,'250gm',0,0,'Lehyam','',0),(124,'Brahmarasayanam','124',161,'250gm',0,0,'Lehyam','',0),(125,'Chyavanaprasam','125',158,'250gm',0,0,'Lehyam','',0),(126,'Dasamoolahareetaki','126',113,'250gm',0,0,'Lehyam','',0),(127,'Dasamoolarasayanam','127',109,'100gm',0,0,'Lehyam','',0),(128,'Dasamoolarasayanam(30 Nos of 25Grams)','128',945,'I No',0,0,'Lehyam','',0),(129,'Gulardrakam','129',163,'250gm',0,0,'Lehyam','',0),(130,'Kalyanagulam ','130',143,'250gm',0,0,'Lehyam','',0),(131,'Kankayana Lehyam','131',163,'250gm',0,0,'Lehyam','',0),(132,'Koosmandarasayanam','132',139,'250gm',0,0,'Lehyam','',0),(133,'Madhusnuhi Rasayanam(B)','133',163,'250gm',0,0,'Lehyam','',0),(134,'Manibhadram Lehyam','134',152,'250gm',0,0,'Lehyam','',0),(135,'Narasimharasayanam','135',195,'250gm',0,0,'Lehyam','',0),(136,'Satavarigulam','136',163,'250gm',0,0,'Lehyam','',0),(137,'Sukumaram Lehyam','137',189,'250gm',0,0,'Lehyam','',0),(138,'Taleesapatra Vatakam','138',37,'50gms',0,0,'Lehyam','',0),(139,'Trivrith Lehyam','139',230,'250gm',0,0,'Lehyam','',0),(140,'Vilwadi Lehyam','140',120,'250gm',0,0,'Lehyam','',0),(141,'Vyoshadi Vatakam','141',32,'50gms',0,0,'Lehyam','',0),(142,'Ashta Choornam','142',60,'50gms',0,0,'Choornam','',0),(143,'Aswagandhadi Choornam','143',58,'50gms',0,0,'Choornam','',0),(144,'Avipathy Choornam','144',45,'50gms',0,0,'Choornam','',0),(145,'Dadimashtakam choornam','145',42,'50gms',0,0,'Choornam','',0),(146,'Dasanakanti Choornam','146',105,'50gms',0,0,'Choornam','',0),(147,'Eladi Choornam','147',91,'50gms',0,0,'Choornam','',0),(148,'Gokshura Choornam','148',42,'50gms',0,0,'Choornam','',0),(149,'Gulgulupanchapalam Choornam','149',68,'50gms',0,0,'Choornam','',0),(150,'Hinguvachadi Choornam','150',50,'50gms',0,0,'Choornam','',0),(151,'Jatamayadi Choornam','151',74,'50gms',0,0,'Choornam','',0),(152,'Kachoradi Choornam','152',69,'10gms',0,0,'Choornam','',0),(153,'Karpooradi Choornam(B)','153',59,'50gms',0,0,'Choornam','',0),(154,'Karpooradi Choornam(S)','154',54,'50gms',0,0,'Choornam','',0),(155,'Kolakulathadi Choornam','155',205,'500gms',0,0,'Choornam','',0),(156,'Kottamchukkadi Lepam','156',37,'50gms',0,0,'Choornam','',0),(157,'Mukhadooshikari Lepam','157',57,'50gms',0,0,'Choornam','',0),(158,'Nalpamara Choornam','158',42,'50gms',0,0,'Choornam','',0),(159,'Nimbadi Choornam','159',38,'50gms',0,0,'Choornam','',0),(160,'Pippali Rasayanam','160',57,'10gms',0,0,'Choornam','',0),(161,'Pushyanugam Choornam','161',60,'50gms',0,0,'Choornam','',0),(162,'Rajanyadi Choornam','162',51,'50gms',0,0,'Choornam','',0),(163,'Rasnadi Choornam','163',18,'7gms',0,0,'Choornam','',0),(164,'Shaddharana Choornam','164',83,'50gms',0,0,'Choornam','',0),(165,'Taleesapatradi Choornam','165',50,'50gms',0,0,'Choornam','',0),(166,'Triphaladi Choornam','166',35,'50gms',0,0,'Choornam','',0),(167,'Triphaladi Spl','167',57,'50gms',0,0,'Choornam','',0),(168,'Vaiswanara Choornam','168',48,'50gms',0,0,'Choornam','',0),(169,'Vilangatanduladi Choornam','169',65,'50gms',0,0,'Choornam','',0),(170,'Yogaraja Choornam','170',68,'50gms',0,0,'Choornam','',0),(171,'Elaneer Kuzhambu','171',48,'10ml',0,0,'Raskariya','',0),(172,'Aswagandhadi Choornam Tablet 90','172',81,'90 Nos',0,0,'Choornam Tablet','',0),(173,'Aswagandhadi Choornam Tablet 1000','173',765,'1000 Nos',0,0,'Choornam Tablet','',0),(174,'Taleesapatradi Choornam Tablet 90','174',86,'90 Nos',0,0,'Choornam Tablet','',0),(175,'Taleesapatradi Choornam Tablet 1000','175',808,'1000 Nos',0,0,'Choornam Tablet','',0),(176,'Triphaladi Choornam Tablet 100','176',85,'100 Nos',0,0,'Choornam Tablet','',0),(177,'Triphaladi Choornam Tablet 1000','177',723,'1000 Nos',0,0,'Choornam Tablet','',0),(178,'Amrutha Gulgulu','178',230,'90 Nos',0,0,'Gulikas','',0),(179,'Andhrakutharam(S)','179',338,'90 Nos',0,0,'Gulikas','',0),(180,'Chandraprabha','180',248,'90 Nos',0,0,'Gulikas','',0),(181,'Chukkumtippalyadi','181',330,'200 nos',0,0,'Gulikas','',0),(182,'Dhanwantharam Gulika','182',320,'200 Nos',0,0,'Gulikas','',0),(183,'Gokshuradi Gulgulu','183',338,'150 Nos',0,0,'Gulikas','',0),(184,'Gopichandanadi','184',330,'200 Nos',0,0,'Gulikas','',0),(185,'Gorochanadi Gulika','185',945,'200 Nos',0,0,'Gulikas','',0),(186,'Hinguvachadi Gulika','186',194,'90 Nos',0,0,'Gulikas','',0),(187,'Jeevaneeyavathi','187',440,'100 Nos',0,0,'Gulikas','',0),(188,'Kaisora Gulgulu','188',230,'90 Nos',0,0,'Gulikas','',0),(189,'Kanchanara Gulgulu','189',203,'90 Nos',0,0,'Gulikas','',0),(190,'Kankayana Vati','190',185,'90 Nos',0,0,'Gulikas','',0),(191,'Karutha Gulika','191',50,'10 Nos',0,0,'Gulikas','',0),(192,'Kastooryadi Gulika','192',510,'200 Nos',0,0,'Gulikas','',0),(193,'Kombanchadi Gulika','193',350,'200 Nos',0,0,'Gulikas','',0),(194,'Krimisodhini','194',175,'100 Nos',0,0,'Gulikas','',0),(195,'Lasunadi Vati','195',212,'90 Nos',0,0,'Gulikas','',0),(196,'Mahadhanwantaram Gulika','196',470,'200 Nos',0,0,'Gulikas','',0),(197,'Mahayogaraja Gulgulu','197',435,'100 Nos',0,0,'Gulikas','',0),(198,'Mandooravatakam','198',180,'90 Nos',0,0,'Gulikas','',0),(199,'Niruryadi Gulika','199',198,'90 Nos',0,0,'Gulikas','',0),(200,'Panchanimbadi Gulika ','200',315,'90 Nos',0,0,'Gulikas','',0),(201,'Punarnava  Mandooram','201',157,'90 Nos',0,0,'Gulikas','',0),(202,'Rajapravartini','202',198,'90 Nos',0,0,'Gulikas','',0),(203,'Shaddharana Tablet','203',221,'90 Nos',0,0,'Gulikas','',0),(204,'Sudarsana Tablet','204',383,'150 Nos',0,0,'Gulikas','',0),(205,'Trayodasasanga Gulgulu','205',212,'90 Nos',0,0,'Gulikas','',0),(206,'Triphala Gulgulu','206',194,'90 Nos',0,0,'Gulikas','',0),(207,'Vilwadi Gulika','207',230,'90 Nos',0,0,'Gulikas','',0),(208,'Yogaraja Gulgulu','208',239,'90 Nos',0,0,'Gulikas','',0),(209,'Amruta Gulgulu - 1000','209',2168,'1000 Nos',0,0,'Gulikas','',0),(210,'Andhrakutharam(S)  - 1000','210',3188,'1000 Nos',0,0,'Gulikas','',0),(211,'Chandraprabha  - 1000','211',2338,'1000 Nos',0,0,'Gulikas','',0),(212,'Chukkumtippalyadi  - 1000','212',1403,'1000 Nos',0,0,'Gulikas','',0),(213,'Dhanwantaram Gulika  - 1000','213',1360,'1000 Nos',0,0,'Gulikas','',0),(214,'Gokshuradi Gulgulu  - 1000','214',1913,'1000 Nos',0,0,'Gulikas','',0),(215,'Gopichandanadi 1000','215',1403,'1000 Nos',0,0,'Gulikas','',0),(216,'Gorochanadi Gulika 1000','216',4016,'1000 Nos',0,0,'Gulikas','',0),(217,'Hinguvachadi Gulika 1000','217',1828,'1000 Nos',0,0,'Gulikas','',0),(218,'Jeevaneeyavati 1000','218',3740,'1000 Nos',0,0,'Gulikas','',0),(219,'Kaisora Gulgulu 1000','219',2168,'1000 Nos',0,0,'Gulikas','',0),(220,'Kachanara Gulgulu 1000','220',1913,'1000 Nos',0,0,'Gulikas','',0),(221,'Kankayana Vati 1000','221',1743,'1000 Nos',0,0,'Gulikas','',0),(222,'Karutha Gulika 1000','222',4250,'1000 Nos',0,0,'Gulikas','',0),(223,'Kastooryadi Gulika 1000','223',2168,'1000 Nos',0,0,'Gulikas','',0),(224,'Kombanchadi Gulika 1000','224',1488,'1000 Nos',0,0,'Gulikas','',0),(225,'Krimisodhini 1000','225',1488,'1000 Nos',0,0,'Gulikas','',0),(226,'Lasunadi  vati 1000','226',1998,'1000 Nos',0,0,'Gulikas','',0),(227,'Mahadhanwantaram Gulika 1000','227',1998,'1000 Nos',0,0,'Gulikas','',0),(228,'Mahayogaraja Gulgulu 1000','228',3698,'1000 Nos',0,0,'Gulikas','',0),(229,'Mandooravatakam 1000','229',1700,'1000 Nos',0,0,'Gulikas','',0),(230,'Niruryadi Gulika 1000','230',1870,'1000 Nos',0,0,'Gulikas','',0),(231,'Panchanimbadi Gulika 1000','231',2975,'1000 Nos',0,0,'Gulikas','',0),(232,'Punarnava mandooram 1000','232',1488,'1000 Nos',0,0,'Gulikas','',0),(233,'Rajapravartini 1000','233',1870,'1000 Nos',0,0,'Gulikas','',0),(234,'Shaddharna Tablet 1000','234',2083,'1000 Nos',0,0,'Gulikas','',0),(235,'Sudarsana Tablet 1000','235',2168,'1000 Nos',0,0,'Gulikas','',0),(236,'Trayodasasanga Gulgulu 1000','236',1998,'1000 Nos',0,0,'Gulikas','',0),(237,'Triphala Gulgulu 1000','237',1828,'1000 Nos',0,0,'Gulikas','',0),(238,'Vilwadi Gulika 1000','238',2168,'1000 Nos',0,0,'Gulikas','',0),(239,'Yogaraja Gulgulu 1000','239',2253,'1000 Nos',0,0,'Gulikas','',0),(240,'Amruta Gulgulu -DS','240',380,'100 Nos',0,0,'Gulikas â€“ DS','',0),(241,'Chandraprabha DS','241',450,'100 Nos',0,0,'Gulikas â€“ DS','',0),(242,'Gokshuradi  Gulgulu - DS','242',355,'',0,0,'','',0),(243,'Hinguvachadi Gulika - DS','243',340,'',0,0,'','',0),(244,'Kaisora Gulgulu -DS','244',420,'100 Nos',0,0,'Gulikas â€“ DS','',0),(245,'Kanchanara Gulgulu -DS','245',370,'100 Nos',0,0,'Gulikas â€“ DS','',0),(246,'Kankayana Vati -DS','246',310,'100 Nos',0,0,'Gulikas â€“ DS','',0),(247,'Shaddhrana Tablet -DS','247',420,'100 Nos',0,0,'Gulikas â€“ DS','',0),(248,'Trayodasanga Gulgulu -DS','248',400,'100 Nos',0,0,'Gulikas â€“ DS','',0),(249,'Triphala Gulgulu - DS','249',390,'',0,0,'','',0),(250,'Yogaraja Gugulu - DS','250',425,'100 Nos',0,0,'Gulikas â€“ DS','',0),(251,'Amruta Gulgulu -DS - 1000','251',3230,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(252,'Chandraprabha -DS 1000','252',3825,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(253,'Gokshuradi Gulgulu -DS 1000','253',3018,'',0,0,'','',0),(254,'Hinguvachadi  Gulika -DS 1000','254',2890,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(255,'Kaisora  Gugulu -DS 1000','255',3570,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(256,'Kanchanara  Gulgulu -DS 1000','256',3145,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(257,'Kankayana Vati -DS 1000','257',2635,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(258,'Shaddhrana Tablet -DS 1000','258',3570,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(259,'Trayodasanga  Gulgulu -DS 1000','259',3400,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(260,'Triphala Gulgulu- DS 1000','260',3315,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(261,'Yogaraja Gulgulu -DS 1000','261',3613,'1000 Nos',0,0,'Gulikas â€“ DS','',0),(262,'Amrutotaram Kashayam Tablet','262',370,'100 Nos',0,0,'Kashayam Tablet','',0),(263,'Aragwadhadi Kashayam Tablet','263',440,'100 Nos',0,0,'Kashayam Tablet','',0),(264,'Ashtavargam Kashayam Tablet','264',380,'100 Nos',0,0,'Kashayam Tablet','',0),(265,'Balaguluchyadi Kashayam Tablet','265',440,'100 Nos',0,0,'Kashayam Tablet','',0),(266,'Bruhatyadi Kashayam Tablet','266',470,'100 Nos',0,0,'Kashayam Tablet','',0),(267,'Chirivilwadi Kashayam Tablet','267',470,'100 Nos',0,0,'Kashayam Tablet','',0),(268,'Dasamoolakatutrayam Kashayam Tablet','268',430,'100 Nos',0,0,'Kashayam Tablet','',0),(269,'Dasamoolam Kashayam Tablet','269',430,'100 Nos',0,0,'Kashayam Tablet','',0),(270,'Dhanadanayanadi Kashayam Tablet','270',470,'100 Nos',0,0,'Kashayam Tablet','',0),(271,'Dhanwantaram Kashayam Tablet ','271',460,'100 Nos',0,0,'Kashayam Tablet','',0),(272,'Drakshadi Kashayam Tablet','272',450,'100 Nos',0,0,'Kashayam Tablet','',0),(273,'Gandharvahastadi Kashayam Tablet','273',390,'100 Nos',0,0,'Kashayam Tablet','',0),(274,'Gulgulutiktakam Kashayam Tablet','274',600,'100 Nos',0,0,'Kashayam Tablet','',0),(275,'Guluchyadi Kashayam Tablet','275',430,'100 Nos',0,0,'Kashayam Tablet','',0),(276,'Indukantam Kashayam Tablet','276',400,'100 Nos',0,0,'Kashayam Tablet','',0),(277,'Karimbirubadi Kashayam Tablet','277',380,'100 Nos',0,0,'Kashayam Tablet','',0),(278,'Maharasnadi Kashayam Tablet','278',560,'100 Nos',0,0,'Kashayam Tablet','',0),(279,'Mahatiktakam Kashayam Tablet','279',575,'100 Nos',0,0,'Kashayam Tablet','',0),(280,'Manjishtadi Kashayam Tablet','280',470,'100 Nos',0,0,'Kashayam Tablet','',0),(281,'Nimbadi Kashayam Tablet','281',415,'100 Nos',0,0,'Kashayam Tablet','',0),(282,'Pathyakshadatryadi Kashayam Tablet','282',450,'100 Nos',0,0,'Kashayam Tablet','',0),(283,'Patolakaturohinyadi Kashayam Tablet','283',650,'100 Nos',0,0,'Kashayam Tablet','',0),(284,'Patolamooladi Kashayam Tablet','284',470,'100 Nos',0,0,'Kashayam Tablet','',0),(285,'Prasarinyadi Kashayam Tablet','285',380,'100 Nos',0,0,'Kashayam Tablet','',0),(286,'Punarnavadi Kashayam Tablet','286',360,'100 Nos',0,0,'Kashayam Tablet','',0),(287,'Rasanadi (S) Kashayam Tablet','287',575,'100 Nos',0,0,'Kashayam Tablet','',0),(288,'Rasanaspatakam Kashayam Tablet','288',380,'100 Nos',0,0,'Kashayam Tablet','',0),(289,'Sahacharadi Kashayam Tablet','289',380,'100 Nos',0,0,'Kashayam Tablet','',0),(290,'Saptasaram Kashayam Tablet','290',410,'100 Nos',0,0,'Kashayam Tablet','',0),(291,'Sukumaram Kashayam Tablet','291',420,'100 Nos',0,0,'Kashayam Tablet','',0),(292,'Tiktakam Kashayam tablet','292',515,'100 Nos',0,0,'Kashayam Tablet','',0),(293,'Varanadi Kashayam Tablet','293',390,'100 Nos',0,0,'Kashayam Tablet','',0),(294,'Vasaguluchyadi Kashayam Tablet','294',525,'100 Nos',0,0,'Kashayam Tablet','',0),(295,'Amrutotaram Kashayam Tablet - 1000','295',3145,'1000 Nos',0,0,'Kashayam Tablet','',0),(296,'Aragwadhadi Kashayam Tablet 1000','296',3740,'1000 Nos',0,0,'Kashayam Tablet','',0),(297,'Ashtavargam Kashayam Tablet 1000','297',3230,'1000 Nos',0,0,'Kashayam Tablet','',0),(298,'Balaguluchyadi Kashayam Tablet 1000','298',3740,'1000 Nos',0,0,'Kashayam Tablet','',0),(299,'Bruhatyadi Kashayam Tablet 1000','299',3995,'1000 Nos',0,0,'Kashayam Tablet','',0),(300,'Chirivilwadi Kashayam Tablet 1000','300',3995,'1000 Nos',0,0,'Kashayam Tablet','',0),(301,'Dasamoolakatutrayam Kashayam Tablet 1000','301',3655,'1000 Nos',0,0,'Kashayam Tablet','',0),(302,'Dasamoolam Kashayam Tablet 1000','302',3655,'1000 Nos',0,0,'Kashayam Tablet','',0),(303,'Dhanadanayanadi Kashayam Tablet 1000','303',3995,'1000 Nos',0,0,'Kashayam Tablet','',0),(304,'Dhanwantaram Kashayam Tablet  - 1000','304',3910,'1000 Nos',0,0,'Kashayam Tablet','',0),(305,'Drakshadi Kashayam Tablet 1000','305',3825,'1000 Nos',0,0,'Kashayam Tablet','',0),(306,'Gandharvahastadi Kashayam Tablet 1000','306',3315,'1000 Nos',0,0,'Kashayam Tablet','',0),(307,'Gulgulutiktakam Kashayam Tablet 1000','307',5100,'1000 Nos',0,0,'Kashayam Tablet','',0),(308,'Guluchyadi Kashayam Tablet 1000','308',3655,'1000 Nos',0,0,'Kashayam Tablet','',0),(309,'Indukantam Kashayam Tablet 1000','309',3400,'1000 Nos',0,0,'Kashayam Tablet','',0),(310,'Karimbirubadi Kashayam Tablet 1000','310',3230,'1000 Nos',0,0,'Kashayam Tablet','',0),(311,'Maharasnadi Kashayam Tablet 1000','311',4760,'1000 Nos',0,0,'Kashayam Tablet','',0),(312,'Mahatiktakam Kashayam Tablet 1000','312',4888,'1000 Nos',0,0,'Kashayam Tablet','',0),(313,'Manjishtadi Kashayam Tablet 1000','313',3995,'1000 Nos',0,0,'Kashayam Tablet','',0),(314,'Nimbadi Kashayam Tablet 1000','314',3528,'1000 Nos',0,0,'Kashayam Tablet','',0),(315,'Pathyakshadatryadi Kashayam Tablet 1000','315',3825,'1000 Nos',0,0,'Kashayam Tablet','',0),(316,'Patolakaturohinyadi Kashayam Tablet 1000','316',5525,'1000 Nos',0,0,'Kashayam Tablet','',0),(317,'Patolamooladi Kashayam Tablet 1000','317',3995,'1000 Nos',0,0,'Kashayam Tablet','',0),(318,'Prasarinyadi Kashayam Tablet 1000','318',3230,'1000 Nos',0,0,'Kashayam Tablet','',0),(319,'Punarnavadi Kashayam Tablet 1000','319',3060,'1000 Nos',0,0,'Kashayam Tablet','',0),(320,'Rasanadi (S) Kashayam Tablet 1000','320',4888,'1000 Nos',0,0,'Kashayam Tablet','',0),(321,'Rasanaspatakam Kashayam Tablet 1000','321',3230,'1000 Nos',0,0,'Kashayam Tablet','',0),(322,'Sahacharadi Kashayam Tablet 1000','322',3230,'1000 Nos',0,0,'Kashayam Tablet','',0),(323,'Saptasaram Kashayam Tablet 1000','323',3485,'1000 Nos',0,0,'Kashayam Tablet','',0),(324,'Sukumaram Kashayam Tablet 1000','324',3570,'1000 Nos',0,0,'Kashayam Tablet','',0),(325,'Tiktakam Kashayam tablet 1000','325',4378,'1000 Nos',0,0,'Kashayam Tablet','',0),(326,'Varanadi Kashayam Tablet 1000','326',3315,'1000 Nos',0,0,'Kashayam Tablet','',0),(327,'Vasaguluchyadi Kashayam Tablet 1000','327',4463,'1000 Nos',0,0,'Kashayam Tablet','',0),(329,'Randomness','RND',100,'ml',5,5,'Arishtam','',1);
/*!40000 ALTER TABLE `app_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_profile`
--

DROP TABLE IF EXISTS `app_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `role` varchar(50) NOT NULL,
  `organisation` varchar(100) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  `phoneno` varchar(15) NOT NULL,
  `user_id` int(11) NOT NULL,
  `regid` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `app_profile_user_id_87d292a0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_profile`
--

LOCK TABLES `app_profile` WRITE;
/*!40000 ALTER TABLE `app_profile` DISABLE KEYS */;
INSERT INTO `app_profile` VALUES (1,'George','Admin','Main Office',0,'8129054175',3,'0'),(2,'Sreejith','Admin','My Medical Store',1,'8129054175',4,'0'),(8,'Doctor1','Doctor','My Medical Store',1,'8129054175',12,'1'),(9,'Distributor1','Distributor','Main Office',0,'8129054175',14,'0'),(13,'Joy','Admin','Calicut Medical Centre',5,'8129054175',18,'0'),(16,'Mathew','Admin','Main Office',0,'8129054175',21,'0'),(17,'Dre','Admin','My New Franchisee',6,'9676455647',22,'0'),(18,'distributor2','Distributor','Main Office',0,'412341325',23,'0'),(19,'Club Ayurveda','Admin','Main Office',0,'8129054175',24,'0');
/*!40000 ALTER TABLE `app_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_salesreport`
--

DROP TABLE IF EXISTS `app_salesreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_salesreport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(80) NOT NULL,
  `quantity` int(11) NOT NULL,
  `sale_rate` double NOT NULL,
  `sales_base_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_salesreport_sales_base_id_a0550891_fk_app_salesreportbase_id` (`sales_base_id`),
  CONSTRAINT `app_salesreport_sales_base_id_a0550891_fk_app_salesreportbase_id` FOREIGN KEY (`sales_base_id`) REFERENCES `app_salesreportbase` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=340 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_salesreport`
--

LOCK TABLES `app_salesreport` WRITE;
/*!40000 ALTER TABLE `app_salesreport` DISABLE KEYS */;
INSERT INTO `app_salesreport` VALUES (1,'Aragwadharishtam ',1,88,5),(2,'Vasarishtam',1,116,5),(4,'Anu Tailam',2,60,7),(5,'Amrutha Gulgulu',1,230,7),(6,'Consultation fee',1,100,7),(7,'Abhayarishtam  ',1,79,8),(8,'Ashta Choornam',1,60,9),(9,'Ashta Choornam',1,60,10),(10,'Head Massage',1,100,11),(11,'Abhyangam',1,750,11),(12,'Abhayarishtam  ',1,79,12),(13,'Amrutharishtam ',1,83,12),(14,'Siro Abhyanagam',1,200,13),(15,'Abhyangam',1,750,13),(16,'Herbal Henna ',1,700,15),(17,'Shirodhara with Coconut Milk ',1,950,19),(18,'Thalam',1,400,20),(19,'Head Massage',1,6.66666666666667,21),(20,'Head Massage',1,100,22),(35,'Amrutharishtam ',1,83,35),(36,'Amrutharishtam ',1,83,36),(37,'Amrutharishtam ',1,83,37),(38,'Amrutharishtam ',1,83,38),(39,'Amrutharishtam ',1,83,39),(41,'Dasamoolarasayanam',1,109,41),(42,'Dasamoolarasayanam',1,109,42),(43,'Agastyarasayanam',1,120,43),(44,'Head Massage',1,400,44),(45,'Head Massage',1,400,45),(46,'Head Massage',1,400,46),(47,'Head Massage',1,500,47),(48,'Ashtavargam Kashayam Tablet',1,380,48),(49,'Ayaskrity',1,99,49),(50,'Dasamoolahareetaki',1,113,50),(51,'Gulardrakam',1,163,50),(52,'Dasamoolahareetaki',1,113,51),(53,'Gulardrakam',1,163,51),(54,'Brahmarasayanam',1,161,52),(55,'Chyavanaprasam',1,158,52),(56,'Abhayarishtam  ',1,79,53),(57,'Aswagandharishtam ',1,138,53),(58,'Amrutharishtam ',1,83,54),(59,'Asokarishtam  ',1,77,54),(60,'Amrutharishtam ',1,83,55),(61,'Asokarishtam  ',1,77,55),(62,'Amrutharishtam ',1,83,56),(63,'Asokarishtam  ',1,77,56),(64,'Amrutharishtam ',1,83,57),(65,'Asokarishtam  ',1,77,57),(66,'Ayaskrity',1,99,57),(67,'Balarishtam',1,88,57),(68,'Anu Tailam',1,60,58),(72,'Draksharishtam',1,110,61),(73,'Aragwadharishtam ',1,88,62),(74,'Aragwadharishtam ',1,88,63),(75,'Bala Tailam',1,106,64),(76,'Consultation fee',1,100,64),(77,'Abhayarishtam  ',1,79,65),(78,'Abhayarishtam  ',1,79,66),(79,'Abhayarishtam  ',1,79,67),(80,'Abhayarishtam  ',1,79,68),(81,'Anu Tailam',1,60,69),(82,'Anu Tailam',1,60,70),(83,'Anu Tailam',1,60,71),(84,'Anu Tailam',1,60,72),(85,'Anu Tailam',1,60,73),(86,'Anu Tailam',1,60,74),(87,'Bala Tailam',1,106,75),(88,'Anu Tailam',1,60,75),(89,'Balaswagandhadi Tailam',1,202,75),(90,'Bala Tailam',1,106,76),(91,'Anu Tailam',1,60,76),(92,'Balaswagandhadi Tailam',1,202,76),(93,'Bala Tailam',1,106,77),(94,'Anu Tailam',1,60,77),(95,'Balaswagandhadi Tailam',1,202,77),(96,'Vasarishtam',1,116,77),(97,'Ela Kizhi',1,750,78),(98,'Uzhichil',1,850,78),(99,'Ela Kizhi',1,750,79),(100,'Uzhichil',1,850,79),(101,'Ela Kizhi',1,750,80),(102,'Uzhichil',1,850,80),(103,'Ela Kizhi',1,750,81),(104,'Uzhichil',1,850,81),(105,'Ela Kizhi',1,750,82),(106,'Uzhichil',1,850,82),(107,'Ela Kizhi',1,750,83),(108,'Uzhichil',1,850,83),(109,'Ela Kizhi',1,750,84),(110,'Uzhichil',1,850,84),(111,'Partharishtam',1,99,85),(112,'Anu Tailam',1,60,85),(113,'Asanaeladi Co. oil',1,205,85),(114,'Chirivilwadi Kashayam ',1,139,87),(115,'Aswagandhadi Choornam Tablet 1000',1,765,89),(118,'Treatment 3',1,400,91),(119,'Treatment 3',1,600,92),(120,'Treatment 3',1,600,93),(121,'Treatment 3',1,700,94),(122,'Sukhachikitsa ( wellness package) - 7 days ',1,12000,95),(123,'Extra Charges',1,50,95),(124,'Sukhachikitsa ( wellness package) - 7 days ',1,12000,96),(125,'Room Rent',1,90,96),(126,'Anu Tailam',1,60,97),(127,'Anu Tailam',1,60,98),(128,'Uzhichil',1,850,99),(129,'Abhayarishtam  ',1,79,100),(130,'Ashta Choornam',1,60,100),(131,'Amrutha Gulgulu',1,230,100),(132,'Siro Abhyanagam',1,200,101),(133,'Ela Kizhi',1,750,101),(134,'Siro Abhyanagam',1,200,102),(135,'Ela Kizhi',1,750,102),(136,'Uzhichil',1,850,102),(137,'Stationary',2,1000,103),(138,'Stationary',2,1000,104),(139,'Stationary',2,1000,105),(140,'Stationary',3,1000,106),(141,'Ashta Choornam',1,60,107),(142,'Stationary',1,1000,108),(143,'Banner',1,2000,108),(144,'Stationary',1,1000,109),(145,'Banner',1,2000,109),(146,'Stationary',1,1000,110),(147,'Banner',1,2000,110),(148,'Stationary',1,1000,111),(149,'Banner',1,2000,111),(150,'Stationary',1,1000,112),(151,'Banner',1,2000,112),(152,'Stationary',1,1000,113),(153,'Banner',1,2000,113),(154,'Stationary',1,1000,114),(155,'Banner',1,2000,114),(156,'Stationary',1,1000,115),(157,'Banner',1,2000,115),(158,'Stationary',1,1000,116),(159,'Banner',1,2000,116),(160,'Stationary',1,1000,117),(161,'Banner',1,2000,117),(162,'Stationary',1,1000,118),(163,'Banner',1,2000,118),(164,'Stationary',1,1000,119),(165,'Banner',1,2000,119),(166,'Stationary',1,1000,120),(167,'Banner',1,2000,120),(168,'Stationary',1,1000,121),(169,'Banner',1,2000,121),(170,'Stationary',1,1000,122),(171,'Banner',1,2000,122),(172,'Stationary',1,1000,123),(173,'Banner',1,2000,123),(174,'Stationary',1,1000,124),(175,'Banner',1,2000,124),(176,'Stationary',1,1000,125),(177,'Banner',1,2000,125),(178,'Stationary',2,1000,126),(179,'Sukhachikitsa ( wellness package) - 7 days ',1,12000,127),(180,'Chikitsathirummu',1,850,128),(181,'Kati Vasthi',1,300,128),(182,'Chikitsathirummu',1,850,129),(183,'Kati Vasthi',1,300,129),(184,'Chikitsathirummu',1,850,130),(185,'Kati Vasthi',1,300,130),(186,'Ela Kizhi',1,750,131),(187,'Elakkithirummu',1,850,131),(188,'Ela Kizhi',1,750,132),(189,'Elakkithirummu',1,850,132),(190,'Kati Vasthi',1,300,132),(191,'Dadimashtakam choornam',1,42,133),(192,'Ashtavargam Kashayam Tablet',1,380,133),(193,'Dadimashtakam choornam',1,42,134),(194,'Ashtavargam Kashayam Tablet',1,380,134),(195,'Consultation Fee',1,100,135),(196,'Foods &amp; Beverages',1,500,135),(197,'Consultation Fee',1,100,136),(198,'Extra Charges',1,100,136),(199,'Abhayarishtam  ',1,79,137),(200,'Amrutharishtam ',1,83,137),(201,'Ayaskrity',1,99,138),(202,'Balarishtam',1,88,138),(203,'Aravindasavam ',1,88,140),(204,'Consultation fee',1,123,140),(205,'Asanaeladi Co. oil',1,205,142),(206,'Abhayarishtam  ',1,79,143),(207,'Abhyangam with Kizhi  - 60mins ',1,1700,144),(208,'Consultation fee',1,200,144),(209,'Abhyangam with Kizhi  - 60mins ',1,1700,145),(210,'Consultation fee',1,200,145),(211,'Abhyangam with Kizhi  - 60mins ',1,1700,146),(212,'Consultation fee',1,200,146),(213,'Aravindasavam ',1,88,147),(214,'Aravindasavam ',1,88,148),(215,'Abhyangam with Shirodhara',1,1600,150),(216,'Yoga',1,500,151),(217,'Asanaeladi Co. oil',1,205,152),(218,'Abhayarishtam  ',1,79,152),(219,'Asanaeladi Co. oil',2,205,153),(220,'Abhayarishtam  ',1,79,153),(221,'Banner',1,2000,154),(222,'Abhayarishtam  ',1,79,155),(223,'Agastyarasayanam',2,120,156),(224,'Abhayarishtam  ',1,79,156),(225,'Amrutharishtam ',4,83,156),(226,'Amruta Gulgulu - 1000',3,2168,156),(227,'Abhayarishtam  ',2,79,157),(229,'New item',1,100,159),(230,'New Item',1,100,160),(231,'Banner',1,2000,161),(232,'Stationary',1,1000,161),(233,'Banner',1,2000,162),(234,'Stationary',1,1000,162),(235,'Randomness',2,100,163),(236,'Randomness',2,100,164),(237,'Mustarishtam',1,88,164),(238,'Abhayarishtam  ',1,79,165),(239,'Amrutharishtam ',1,83,165),(240,'Abhayarishtam  ',1,79,166),(241,'Randomness',1,100,166),(242,'Abhayarishtam  ',1,79,167),(243,'Randomness',1,100,167),(252,'Aravindasavam ',1,88,175),(253,'Asokarishtam  ',1,77,175),(254,'Balarishtam',1,88,175),(255,'Chukkumtippalyadi',1,330,175),(256,'Dhanwantharam Gulika',1,320,175),(257,'Ashtavargam Kashayam Tablet',1,380,175),(258,'Balaguluchyadi Kashayam Tablet',1,440,175),(259,'Siro Abhyanagam   ',1,200,176),(260,'Abhyangam',1,750,176),(261,'Lumbar Disc prolapse',1,120,176),(262,'Lumbar Disc prolapse',1,120,177),(263,'Lumbar Disc prolapse',1,120,178),(264,'Tendonitis',1,200,178),(265,'Lumbar Disc prolapse',1,120,179),(266,'Tendonitis',1,200,179),(267,'Lumbar Disc prolapse',1,120,180),(268,'Tendonitis',1,200,180),(269,'Abhyangam',1,750,180),(270,'Lumbar Disc prolapse',1,120,181),(271,'Tendonitis',1,200,181),(272,'Abhyangam',1,750,181),(273,'Siro Abhyanagam   ',1,200,182),(274,'Ela Kizhi',1,750,183),(275,'Ela Kizhi',1,750,184),(276,'Ela Kizhi',1,750,185),(277,'Ela Kizhi',1,750,186),(278,'Lumbar Disc prolapse',1,120,186),(279,'Tendonitis',1,200,186),(280,' Sukhachikitsa ( wellness package) : 14 Days',1,23000,186),(281,'Ashta Choornam',1,60,187),(282,'Aswagandhadi Choornam Tablet 90',1,81,187),(283,'Indukantam Ghritam',1,232,187),(284,'Balarishtam',1,88,187),(285,'Dasamoolarasayanam',1,109,187),(286,'Asanaeladi Co. oil',1,205,187),(287,'Siro Abhyanagam   ',1,200,188),(288,'Tendonitis',1,200,188),(289,'Panchakarma/Detoxification packages : 7 Days',1,13000,188),(290,'Lumbar Disc prolapse',1,120,188),(291,'Siro Abhyanagam   ',1,200,189),(292,'Tendonitis',1,200,189),(293,'Panchakarma/Detoxification packages : 7 Days',1,13000,189),(294,'Lumbar Disc prolapse',1,120,189),(295,'Siro Abhyanagam   ',1,200,190),(296,'Tendonitis',1,200,190),(297,'Panchakarma/Detoxification packages : 7 Days',1,13000,190),(298,'Lumbar Disc prolapse',1,120,190),(299,'Siro Abhyanagam   ',1,200,191),(300,'Tendonitis',1,200,191),(301,'Panchakarma/Detoxification packages : 7 Days',1,13000,191),(302,'Lumbar Disc prolapse',1,120,191),(303,'Aravindasavam ',1,88,192),(304,'Aragwadharishtam ',1,88,192),(305,'Amrutharishtam ',1,83,192),(306,'Aswagandhadi Choornam Tablet 90',1,81,192),(307,'Aravindasavam ',1,88,193),(308,'Asokarishtam  ',1,77,193),(309,'Aswagandharishtam ',1,138,193),(310,'Siro Abhyanagam   ',1,200,194),(311,'Consultation Fee',1,100,194),(312,'Club Ayurveda Special - Siro Abhyangam with Shoulders',1,500,196),(313,'Extra Charges',1,200,196),(314,'Extra Charges',1,200,197),(315,'Abhyangam with Kizhi ',1,1700,197),(316,'Extra Charges',1,200,198),(317,'Lumbar Disc prolapse',1,240,198),(318,'Foods &amp; Beverages',1,150,198),(319,'Extra Charges',1,200,199),(320,'Lumbar Disc prolapse',1,240,199),(321,'Foods &amp; Beverages',1,150,199),(322,'Abhayarishtam  ',1,79,200),(323,'Aragwadharishtam ',1,88,200),(324,'Ayaskrity',1,99,201),(325,'Balarishtam',1,88,201),(326,'Ayaskrity',1,99,202),(327,'Balarishtam',1,88,202),(328,'Aswagandhadi Choornam Tablet 90',1,81,203),(329,'Dasamoolarasayanam',1,109,203),(330,'Aswagandhadi Choornam Tablet 90',1,81,204),(331,'Dasamoolarasayanam',1,109,204),(332,'Aswagandhadi Choornam Tablet 90',1,81,205),(333,'Dasamoolarasayanam',1,109,205),(334,'Stationary',1,1000,206),(335,'Stationary',1,1000,207),(336,'Banner',1,2000,208),(337,'Banner',1,2000,209),(338,'Abhayarishtam  ',1,79,210),(339,'Banner',1,2000,211);
/*!40000 ALTER TABLE `app_salesreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_salesreportbase`
--

DROP TABLE IF EXISTS `app_salesreportbase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_salesreportbase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `franchise_code` int(11) NOT NULL,
  `bill_type` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_salesreportbase_customer_id_40682ee4_fk_app_customer_id` (`customer_id`),
  CONSTRAINT `app_salesreportbase_customer_id_40682ee4_fk_app_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `app_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=212 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_salesreportbase`
--

LOCK TABLES `app_salesreportbase` WRITE;
/*!40000 ALTER TABLE `app_salesreportbase` DISABLE KEYS */;
INSERT INTO `app_salesreportbase` VALUES (5,'2017-11-18 20:27:57.988268',NULL,1,'Pharmacy'),(7,'2017-11-21 05:45:27.174404',NULL,1,'Pharmacy'),(8,'2017-11-21 05:55:12.751631',NULL,1,'Pharmacy'),(9,'2017-11-21 06:24:07.832856',NULL,1,'Pharmacy'),(10,'2017-11-21 06:26:42.703676',NULL,1,'Pharmacy'),(11,'2017-12-07 09:49:44.743387',NULL,1,'Pharmacy'),(12,'2017-12-07 09:51:49.406859',NULL,1,'Pharmacy'),(13,'2017-12-07 09:53:06.671762',NULL,1,'Pharmacy'),(14,'2017-12-07 09:55:11.329417',NULL,1,'Pharmacy'),(15,'2017-12-07 09:55:21.367010',NULL,1,'Pharmacy'),(16,'2017-12-07 10:24:22.795947',NULL,1,'Pharmacy'),(17,'2017-12-07 13:35:42.277502',NULL,1,'Pharmacy'),(18,'2017-12-07 13:37:48.214058',NULL,1,'Pharmacy'),(19,'2017-12-07 13:39:15.763904',NULL,1,'Invoice'),(20,'2017-12-07 13:49:00.853190',NULL,1,'Invoice'),(21,'2017-12-07 14:05:28.842390',NULL,1,'Invoice'),(22,'2017-12-07 14:07:26.430607',NULL,1,'Invoice'),(35,'2017-12-28 06:34:07.392905',NULL,1,'Pharmacy'),(36,'2017-12-28 06:41:02.136766',NULL,1,'Pharmacy'),(37,'2017-12-28 06:45:36.401190',NULL,1,'Pharmacy'),(38,'2017-12-28 06:47:38.664696',NULL,1,'Pharmacy'),(39,'2017-12-28 06:49:43.128843',NULL,1,'Pharmacy'),(41,'2017-12-28 06:53:58.895511',NULL,1,'Pharmacy'),(42,'2017-12-28 06:55:20.045688',NULL,1,'Pharmacy'),(43,'2017-12-28 06:55:47.089755',NULL,1,'Pharmacy'),(44,'2017-12-28 07:01:23.034050',NULL,1,'Invoice'),(45,'2017-12-28 07:01:38.618755',NULL,1,'Invoice'),(46,'2017-12-28 07:01:48.756898',NULL,1,'Invoice'),(47,'2017-12-28 07:01:58.929525',NULL,1,'Invoice'),(48,'2017-12-31 05:16:51.783556',NULL,5,'Pharmacy'),(49,'2017-12-31 07:16:28.273117',NULL,5,'Pharmacy'),(50,'2017-12-31 07:17:57.370518',NULL,5,'Pharmacy'),(51,'2017-12-31 09:08:28.157556',NULL,5,'Pharmacy'),(52,'2017-12-31 09:11:18.227874',NULL,5,'Pharmacy'),(53,'2018-01-01 22:49:05.567746',NULL,5,'Pharmacy'),(54,'2018-01-01 22:50:10.698985',NULL,5,'Pharmacy'),(55,'2018-01-01 22:51:21.245541',NULL,5,'Pharmacy'),(56,'2018-01-01 22:51:45.958808',NULL,5,'Pharmacy'),(57,'2018-01-01 22:52:10.345336',NULL,5,'Pharmacy'),(58,'2018-01-01 22:53:18.683274',NULL,5,'Pharmacy'),(61,'2018-01-01 23:03:58.900370',NULL,5,'Pharmacy'),(62,'2018-01-01 23:05:43.625232',NULL,5,'Pharmacy'),(63,'2018-01-01 23:06:13.824747',NULL,5,'Pharmacy'),(64,'2018-01-02 02:35:45.017749',NULL,5,'Pharmacy'),(65,'2018-01-10 23:39:54.901965',NULL,1,'Pharmacy'),(66,'2018-01-10 23:41:12.207213',NULL,1,'Pharmacy'),(67,'2018-01-10 23:43:23.375698',NULL,1,'Pharmacy'),(68,'2018-01-10 23:44:00.722087',NULL,1,'Pharmacy'),(69,'2018-01-10 23:45:03.690491',NULL,1,'Pharmacy'),(70,'2018-01-10 23:46:04.100585',NULL,1,'Pharmacy'),(71,'2018-01-10 23:46:45.346061',NULL,1,'Pharmacy'),(72,'2018-01-10 23:51:31.447232',NULL,1,'Pharmacy'),(73,'2018-01-10 23:54:33.367547',NULL,1,'Pharmacy'),(74,'2018-01-10 23:57:03.346077',NULL,1,'Pharmacy'),(75,'2018-01-10 23:58:20.191899',NULL,1,'Pharmacy'),(76,'2018-01-10 23:58:44.502826',NULL,1,'Pharmacy'),(77,'2018-01-11 00:13:41.857847',NULL,1,'Pharmacy'),(78,'2018-01-11 00:14:39.560422',NULL,1,'Invoice'),(79,'2018-01-11 00:15:48.244047',NULL,1,'Invoice'),(80,'2018-01-11 00:16:12.923469',NULL,1,'Invoice'),(81,'2018-01-11 00:16:23.451093',NULL,1,'Invoice'),(82,'2018-01-11 00:17:23.668616',NULL,1,'Invoice'),(83,'2018-01-11 00:19:14.480275',NULL,1,'Invoice'),(84,'2018-01-11 00:20:52.619322',NULL,1,'Invoice'),(85,'2018-01-11 00:23:14.248028',NULL,1,'Pharmacy'),(86,'2018-01-11 00:24:35.533578',NULL,1,'Pharmacy'),(87,'2018-01-11 00:24:48.274517',NULL,1,'Pharmacy'),(88,'2018-01-13 01:11:05.596102',NULL,1,'Pharmacy'),(89,'2018-01-13 01:20:49.838426',NULL,1,'Pharmacy'),(91,'2018-01-13 07:00:26.294595',NULL,1,'Invoice'),(92,'2018-01-13 07:01:42.435160',NULL,1,'Invoice'),(93,'2018-01-13 07:02:10.568308',NULL,1,'Invoice'),(94,'2018-01-13 07:03:22.205673',NULL,1,'Invoice'),(95,'2018-01-13 07:04:43.141771',NULL,1,'Invoice'),(96,'2018-01-13 07:09:03.212672',NULL,1,'Invoice'),(97,'2018-01-13 07:09:55.370883',NULL,1,'Pharmacy'),(98,'2018-01-13 07:12:03.457448',NULL,1,'Pharmacy'),(99,'2018-01-13 07:13:21.051610',NULL,1,'Invoice'),(100,'2018-01-13 07:16:21.269610',NULL,1,'Pharmacy'),(101,'2018-01-13 07:18:42.256963',NULL,1,'Invoice'),(102,'2018-01-13 07:19:20.687337',NULL,1,'Invoice'),(103,'2018-01-28 10:54:15.321769',NULL,0,'Pharmacy'),(104,'2018-01-28 10:55:34.193960',NULL,0,'Pharmacy'),(105,'2018-01-28 10:57:21.778230',NULL,0,'Pharmacy'),(106,'2018-01-28 11:01:01.469433',NULL,0,'Pharmacy'),(107,'2018-01-28 11:02:07.311987',NULL,1,'Pharmacy'),(108,'2018-01-28 13:37:19.243421',NULL,0,'Pharmacy'),(109,'2018-01-28 13:37:52.798135',NULL,0,'Pharmacy'),(110,'2018-01-28 13:40:19.248404',NULL,0,'Pharmacy'),(111,'2018-01-28 13:41:05.077728',NULL,0,'Pharmacy'),(112,'2018-01-28 13:41:59.229954',NULL,0,'Pharmacy'),(113,'2018-01-28 13:42:32.304229',NULL,0,'Pharmacy'),(114,'2018-01-28 13:42:51.907844',NULL,0,'Pharmacy'),(115,'2018-01-28 13:43:21.322377',NULL,0,'Pharmacy'),(116,'2018-01-28 13:43:52.339000',NULL,0,'Pharmacy'),(117,'2018-01-28 13:44:22.810481',NULL,0,'Pharmacy'),(118,'2018-01-28 13:44:30.751527',NULL,0,'Pharmacy'),(119,'2018-01-28 13:44:44.297996',NULL,0,'Pharmacy'),(120,'2018-01-28 13:44:59.566794',NULL,0,'Pharmacy'),(121,'2018-01-28 13:45:23.705250',NULL,0,'Pharmacy'),(122,'2018-01-28 13:45:46.748912',NULL,0,'Pharmacy'),(123,'2018-01-28 13:46:21.065087',NULL,0,'Pharmacy'),(124,'2018-01-28 13:46:32.721556',NULL,0,'Pharmacy'),(125,'2018-01-28 13:47:29.621749',NULL,0,'Pharmacy'),(126,'2018-01-28 13:48:19.232955',NULL,0,'Pharmacy'),(127,'2018-01-28 13:49:30.259639',NULL,1,'Invoice'),(128,'2018-01-28 13:50:07.521761',NULL,1,'Invoice'),(129,'2018-01-28 13:55:46.666975',NULL,1,'Invoice'),(130,'2018-01-28 13:55:50.907169',NULL,1,'Invoice'),(131,'2018-01-28 13:57:23.528939',NULL,1,'Invoice'),(132,'2018-01-28 13:58:48.850207',NULL,1,'Invoice'),(133,'2018-01-28 14:00:26.581717',NULL,1,'Pharmacy'),(134,'2018-01-28 14:00:51.078000',NULL,1,'Pharmacy'),(135,'2018-01-28 14:06:20.851044',NULL,1,'Pharmacy'),(136,'2018-01-28 14:07:28.733391',NULL,1,'Pharmacy'),(137,'2018-01-28 15:05:39.003262',NULL,1,'Pharmacy'),(138,'2018-01-28 15:08:07.921060',NULL,1,'Pharmacy'),(139,'2018-01-30 09:49:00.154364',NULL,1,'Pharmacy'),(140,'2018-01-30 09:50:45.681101',NULL,1,'Pharmacy'),(141,'2018-01-30 10:31:23.990380',NULL,1,'Pharmacy'),(142,'2018-01-30 10:38:24.801537',NULL,1,'Pharmacy'),(143,'2018-01-31 05:06:39.176521',NULL,1,'Pharmacy'),(144,'2018-01-31 05:16:18.518657',NULL,1,'Invoice'),(145,'2018-01-31 06:25:11.816287',NULL,1,'Invoice'),(146,'2018-01-31 06:26:12.894330',NULL,1,'Invoice'),(147,'2018-01-31 06:28:06.198427',NULL,1,'Pharmacy'),(148,'2018-01-31 06:30:13.470729',NULL,1,'Pharmacy'),(149,'2018-01-31 06:56:52.485778',NULL,1,'Pharmacy'),(150,'2018-02-08 02:15:38.485480',NULL,1,'Invoice'),(151,'2018-02-10 05:18:14.052206',NULL,1,'Invoice'),(152,'2018-02-11 12:52:52.483058',NULL,1,'Pharmacy'),(153,'2018-02-11 18:29:41.810841',NULL,1,'Pharmacy'),(154,'2018-02-11 19:02:02.048755',NULL,0,'Pharmacy'),(155,'2018-02-13 09:20:49.918155',NULL,1,'Pharmacy'),(156,'2018-02-13 09:35:20.674880',NULL,1,'Pharmacy'),(157,'2018-02-13 09:38:19.116965',NULL,1,'Pharmacy'),(159,'2018-02-13 18:29:44.923403',NULL,1,'Pharmacy'),(160,'2018-02-13 18:33:19.000188',NULL,1,'Pharmacy'),(161,'2018-02-17 10:47:36.438692',NULL,0,'Pharmacy'),(162,'2018-02-17 10:48:15.135142',NULL,0,'Pharmacy'),(163,'2018-02-20 17:08:50.389260',NULL,1,'Pharmacy'),(164,'2018-02-20 17:09:16.297154',NULL,1,'Pharmacy'),(165,'2018-02-20 17:15:04.319105',NULL,5,'Pharmacy'),(166,'2018-02-20 17:16:20.444202',NULL,1,'Pharmacy'),(167,'2018-02-20 17:17:19.784054',NULL,1,'Pharmacy'),(175,'2018-03-01 04:51:00.733598',NULL,1,'Pharmacy'),(176,'2018-03-01 04:51:27.104628',NULL,1,'Invoice'),(177,'2018-03-01 05:02:42.896199',NULL,1,'Invoice'),(178,'2018-03-01 05:25:17.107119',NULL,1,'Invoice'),(179,'2018-03-01 05:47:34.934630',NULL,1,'Invoice'),(180,'2018-03-01 06:05:33.704341',NULL,1,'Invoice'),(181,'2018-03-01 06:30:36.737047',NULL,1,'Invoice'),(182,'2018-03-01 06:33:49.646505',NULL,1,'Invoice'),(183,'2018-03-01 06:40:35.391841',NULL,1,'Invoice'),(184,'2018-03-01 06:45:02.078508',NULL,1,'Invoice'),(185,'2018-03-01 06:45:18.188042',NULL,1,'Invoice'),(186,'2018-03-01 06:45:31.377177',NULL,1,'Invoice'),(187,'2018-03-01 06:48:15.916440',NULL,1,'Pharmacy'),(188,'2018-03-01 06:48:59.768066',NULL,1,'Invoice'),(189,'2018-03-01 06:53:50.713680',NULL,1,'Invoice'),(190,'2018-03-01 06:55:56.831050',NULL,1,'Invoice'),(191,'2018-03-01 07:00:06.627549',NULL,1,'Invoice'),(192,'2018-03-03 13:53:30.994602',NULL,1,'Pharmacy'),(193,'2018-03-03 13:54:41.569904',NULL,5,'Pharmacy'),(194,'2018-03-03 13:58:56.619821',NULL,1,'Invoice'),(195,'2018-03-03 13:59:46.266643',NULL,1,'Pharmacy'),(196,'2018-03-03 14:02:26.716136',NULL,1,'Invoice'),(197,'2018-03-03 14:02:56.983147',NULL,1,'Invoice'),(198,'2018-03-03 14:03:53.264278',NULL,1,'Invoice'),(199,'2018-03-03 14:23:24.269045',NULL,1,'Invoice'),(200,'2018-03-05 09:58:43.336762',NULL,1,'Pharmacy'),(201,'2018-03-05 14:58:32.594802',NULL,1,'Pharmacy'),(202,'2018-03-05 15:06:37.780267',NULL,1,'Pharmacy'),(203,'2018-03-05 16:27:23.454060',NULL,1,'Pharmacy'),(204,'2018-03-05 16:28:33.481893',NULL,1,'Pharmacy'),(205,'2018-03-05 16:30:08.074092',NULL,1,'Pharmacy'),(206,'2018-03-06 03:10:58.228902',NULL,0,'Pharmacy'),(207,'2018-03-06 03:12:58.242671',NULL,0,'Pharmacy'),(208,'2018-03-08 17:50:35.923270',NULL,0,'Pharmacy'),(209,'2018-03-08 18:06:06.546871',NULL,0,'Pharmacy'),(210,'2018-03-10 17:40:06.914595',11,1,'Pharmacy'),(211,'2018-03-11 13:48:00.411346',NULL,0,'Pharmacy');
/*!40000 ALTER TABLE `app_salesreportbase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_savedbill`
--

DROP TABLE IF EXISTS `app_savedbill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_savedbill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_code` varchar(10) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  `productlist` varchar(200) NOT NULL,
  `ratelist` varchar(200) NOT NULL,
  `durationlist` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_savedbill`
--

LOCK TABLES `app_savedbill` WRITE;
/*!40000 ALTER TABLE `app_savedbill` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_savedbill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_scan`
--

DROP TABLE IF EXISTS `app_scan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_scan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `patient_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_scan_patient_id_0f934b9b_fk_app_customer_id` (`patient_id`),
  CONSTRAINT `app_scan_patient_id_0f934b9b_fk_app_customer_id` FOREIGN KEY (`patient_id`) REFERENCES `app_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_scan`
--

LOCK TABLES `app_scan` WRITE;
/*!40000 ALTER TABLE `app_scan` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_scan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_service`
--

DROP TABLE IF EXISTS `app_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `service_code` varchar(20) NOT NULL,
  `rates` varchar(30) NOT NULL,
  `body_part` varchar(30) DEFAULT NULL,
  `tax_CGST` double DEFAULT NULL,
  `tax_SGST` double DEFAULT NULL,
  `remarks` varchar(200) DEFAULT NULL,
  `duration` varchar(20) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_service_service_code_061db423_uniq` (`service_code`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_service`
--

LOCK TABLES `app_service` WRITE;
/*!40000 ALTER TABLE `app_service` DISABLE KEYS */;
INSERT INTO `app_service` VALUES (1,'Siro Abhyanagam   ','1','200,250,200,325','',0,0,'','','','Shiro-abhyangam_cXuAY60.jpg'),(2,'Abhyangam','2','750,1000,750,1300','',0,0,'','','This massage is performed using suitable oil all over body in seven postures mainly concentrating to head, ears, palms, and feet. This promotes complete effect of Abhyangam','abhyangam_jyQ0Kbv.jpg'),(3,'Chikitsathirummu','3','850,1100,850,1350','',0,0,'','','This special massage helps to get relief from back pains, sprains, shoulder pains, joint pains and stiffness etc.','Chikitsa_thirummu.jpg'),(4,'Ela Kizhi','4','750,1000,750,1300','',0,0,'','','Sudation done by using herbal leaves- The leaves of certain herbs are made into a bolus form in a cotton cloth and are pummelled on the affected part after therapeutic massage with suitable medicated oil.','elakizhi_cYdyp7f.jpg'),(5,'Elakkithirummu','5','850,1100,850,1350','',0,0,'','','This is a special massage which has its origin from the traditional martial arts of Kerala. This massage gives relief from all the muscular pains of the body. It also helps to reduce inflammation resulting from falls, accidents and sprains etcâ€¦','Elakki_Thirummal_uoZSa7N.jpg'),(6,'Kati Vasthi','6','300,400,300,550','',0,0,'','','Its especially for Sciatica, Osteoarthritis of hip and lower back. A small receptacle of dough is made on the affected region to which luke-warm medicated oil is poured and kept for some time.','Kati-Basti-for-Low-Back-ache_KBN7Zc0.jpg'),(7,'Mukha Lepam','7','400,500,400,650','',0,0,'','','This facial can be used for all types of skins. Herbal medicines are using for face packs, scrubbing, steaming and face massages. This gives a clearer and fairer appearance for the face.','mukalepam_rZ0tvgD.jpg'),(8,'Nasyam ( Nasal Medicine)','8','250,300,250,400','',0,0,'','','Nasyam is a therapeutic treatment for the nose, throat Sinuses and head. As it is a good purification therapy for the parts above shoulder, it helps to improve clarity of sense organ.','Nasyam_GfdjsHV.jpg'),(9,'Njavara Kizhi (Bolus ssage)','9','600,750,600,1000','Full body',0,0,'','60 mins','It is an effective treatment for rheumatism, joint pain, nerve weakness and emaciated limbs etc.. The body is gently massaged with linen bags filled with Njavara rice paste that has been cooked well in milk and herbal decoction.',''),(10,'Oushada Snanam','10','650,850,650,1100','',0,0,'','','This is one of the herbal treatments which were prevalent in the erstwhile royal families in Kerala to maintain radiant and vibrant beauty to their women folk. A combination of herbs is applied to the body, a simple massage is given, a special bath follows using a special herbal decoction.  This beauty therapy helps to exfoliate the dead skin and gives a soft and fragrant skin.','Oushada-Snanam_aoCdTTX.jpg'),(11,'Pizhichil ( Medicated  Oil Bath)','11','650,850,650,1100','',0,0,'','','This is a process traditionally followed once a year to keep the body fit & healthy and prevent ageing of cells & tissues, tones up muscle, increase blood circulation, and cleanse the body from toxins. It is also effective for sexual weakness and general disability','pizhichil_qW7xIid.jpg'),(12,'Paadha Abhyangam ( Foot massage)','12','300,400,300,550','',0,0,'','','This is one of the massages to sharpen the legs and arms by reducing excess fat and toning up the muscles.','padha-abhyangam_aGoFhfS.jpg'),(13,'Podi Kizhi','13','600,800,600,1050','',0,0,'','','Sudation done by using herbal Powder- This procedure is the same as Ela Kizhi. Instead of herbal leaves herbal powders are using in the form of boluses. Both of these Kizhi treatments are very good in treating of sciatica, Sprains, frozen shoulders, lumbago & stiffness of joints, muscular pains, and inflammations. Taking of KIZHI treatments once in a year is very good for health. It has five types of packages.','Podikizhi_iK1KAKj.jpg'),(14,'Sirodhara with Oil','14','600,800,600,1050','',0,0,'','','This is specialty of Keraleeya Ayurvedic treatment, in which herbal oil is poured in a rhythmic manner on the forehead of the person lying on his back.  Itâ€™s extremely beneficial for headaches, insomnia and relaxes the entire nervous system. It has five types of packages.','shirodhara_sduMBo2.jpg'),(15,'Skin Nourishing Therapy (Twak  Paricharanam)','15','950,1150,950,1500','',0,0,'','','It helps to protect and maintain our skin with shine.  It also cures problems like black spots, wrinkles, stretch marks, acne, pimples & reducing the dryness, roughness etcâ€¦ it includes Abhyangam with aloe Vera juice and medicated oil, Steam bath and face massage.','skin_nourishing_therapy_XDfKjQN.jpg'),(16,'Uzhichil','16','850,1000,850,1300','',0,0,'','','This is recommended for general fitness of the body. It tones up the muscles, increase blood circulation, relaxes joints and stimulates the nervous system and is good for sense organs, especially beneficial for diabetes. It has three types of packageâ€™s.','Uzhichil_uMWy3GC.jpg'),(17,'Udhwarthanam','17','800,950,800,1250','Full body',0,0,'','60 mins','This is for obesity related problems. It increases blood circulation, up the body and melts subcutaneous fat. The massage is done with levitated herbal powder followed by medicated warm water bath. It has five types of packages.',''),(18,'Shirodhara with Curd','18','600,800,600,1050','Head',0,0,'','45 mins ','',''),(19,'Shiro dhara with Milk','19','600,800,600,1050','Head',0,0,'','45 mins','',''),(20,'Shirodhara with Coconut Milk ','20','950,1150,950,1500','Head',0,0,'','45 mins ','',''),(21,'Steam Bath      ','21','350,450,350,600','Full body',0,0,'','30 mins ','',''),(22,'Kashaya Vasthi ( Normal)','22','450,550,450,700','',0,0,'','30 mins','',''),(23,'Njavara Theppu','23','600,700,600,950','Full body',0,0,'','40 mins ','',''),(24,'Thalapothichil','24','1200,1350,1200,1750','Head',0,0,'','45 mins','',''),(25,'Herbal Henna ','25','700,800,700,1050','Hair',0,0,'','30 mins','',''),(26,'Shirovasthy','26','800,1000,800,1300','Head',0,0,'','30 mins','',''),(27,'Keshadhoopanam','27','400,500,400,650','Hair',0,0,'','25 mins','',''),(28,'Keshakanthi massage      ','28','250,350,250,450','Head',0,0,'','20 mins   ','',''),(29,'Thalam','29','400,500,400,650','Head',0,0,'','20 mins','',''),(30,'Hot oil Massage ','30','500,700,500,950','Full body',0,0,'','30 mins','','');
/*!40000 ALTER TABLE `app_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_servicemask`
--

DROP TABLE IF EXISTS `app_servicemask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_servicemask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mask` varchar(500) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_servicemask`
--

LOCK TABLES `app_servicemask` WRITE;
/*!40000 ALTER TABLE `app_servicemask` DISABLE KEYS */;
INSERT INTO `app_servicemask` VALUES (1,'110000000000000000000000000011',1),(2,'011111000000000000000000000000',5);
/*!40000 ALTER TABLE `app_servicemask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_skulist`
--

DROP TABLE IF EXISTS `app_skulist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_skulist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `unit` varchar(30) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_skulist`
--

LOCK TABLES `app_skulist` WRITE;
/*!40000 ALTER TABLE `app_skulist` DISABLE KEYS */;
INSERT INTO `app_skulist` VALUES (1,'Quantity','ml',0),(2,'Quantity','grams',0),(3,'Number','nos',0);
/*!40000 ALTER TABLE `app_skulist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_stock`
--

DROP TABLE IF EXISTS `app_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(30) NOT NULL,
  `stock_quantity` int(11) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  `batch_no` varchar(20) NOT NULL,
  `expiry_date` date NOT NULL,
  `address` varchar(100) NOT NULL,
  `gst_no` varchar(30) NOT NULL,
  `vendor` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_stock`
--

LOCK TABLES `app_stock` WRITE;
/*!40000 ALTER TABLE `app_stock` DISABLE KEYS */;
INSERT INTO `app_stock` VALUES (1,'Abhayarishtam  ',0,1,'2/445','2018-04-12','','',''),(2,'Agastyarasayanam',100,0,'1/141/5','2018-09-12','','',''),(3,'Agastyarasayanam',10,1,'1/1323/21','2018-12-31','','1236721','');
/*!40000 ALTER TABLE `app_stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_stockreport`
--

DROP TABLE IF EXISTS `app_stockreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_stockreport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_code` varchar(30) NOT NULL,
  `item_name` varchar(30) NOT NULL,
  `stock` int(11) NOT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_stockreport`
--

LOCK TABLES `app_stockreport` WRITE;
/*!40000 ALTER TABLE `app_stockreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_stockreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_stocktransfer`
--

DROP TABLE IF EXISTS `app_stocktransfer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_stocktransfer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(30) NOT NULL,
  `stock_amount` varchar(20) NOT NULL,
  `franchise_name` varchar(30) NOT NULL,
  `discount` int(11) DEFAULT NULL,
  `expiry_date` date NOT NULL,
  `franchise_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_stocktransfer`
--

LOCK TABLES `app_stocktransfer` WRITE;
/*!40000 ALTER TABLE `app_stocktransfer` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_stocktransfer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_timestampdb`
--

DROP TABLE IF EXISTS `app_timestampdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_timestampdb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `table_name` varchar(50) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_timestampdb`
--

LOCK TABLES `app_timestampdb` WRITE;
/*!40000 ALTER TABLE `app_timestampdb` DISABLE KEYS */;
INSERT INTO `app_timestampdb` VALUES (1,'Franchise','2018-03-12 18:40:20.066651'),(2,'Service','2018-02-20 01:33:28.176624'),(3,'PackageMask','2018-01-06 01:44:35.000000'),(4,'Package','2018-02-20 01:29:13.921380'),(5,'ServiceMask','2018-01-06 01:44:56.000000'),(6,'Discount','2018-03-03 13:58:37.683226'),(7,'Enquiry','2018-03-08 18:24:23.460020'),(8,'TimestampDB','2018-01-06 01:49:24.000000');
/*!40000 ALTER TABLE `app_timestampdb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_treatment`
--

DROP TABLE IF EXISTS `app_treatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_treatment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rate` double NOT NULL,
  `tax_CGST` double DEFAULT NULL,
  `tax_SGST` double DEFAULT NULL,
  `franchise_code` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_treatment`
--

LOCK TABLES `app_treatment` WRITE;
/*!40000 ALTER TABLE `app_treatment` DISABLE KEYS */;
INSERT INTO `app_treatment` VALUES (1,120,5,5,1,'Lumbar Disc prolapse'),(2,200,10,10,1,'Tendonitis');
/*!40000 ALTER TABLE `app_treatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_treatmentmaster`
--

DROP TABLE IF EXISTS `app_treatmentmaster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_treatmentmaster` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `remarks` varchar(200) NOT NULL,
  `duration` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_treatmentmaster`
--

LOCK TABLES `app_treatmentmaster` WRITE;
/*!40000 ALTER TABLE `app_treatmentmaster` DISABLE KEYS */;
INSERT INTO `app_treatmentmaster` VALUES (1,'Lumbar Disc prolapse','',60),(2,'Rheumatoid Arthritis ( Vata Sonitha/ Vata Raktha)','',60),(3,'Osteo Arthritis( Sandhigata Vata) of Knee','',60),(4,'Gouty Arthritis ( Paitrika Vata Sonitha)','',60),(5,'Systemic Lupus Erythematosus (SLE)','',60),(6,'Lumbar Spondylosis ( Low back pain) Kateegraha','',60),(7,'Cervical Spondylosis( Neck Pain)','',60),(8,'Ankylosing Spondylitis( Bamboo spine)','',60),(9,'Spinal Injuries','',60),(10,'Sciatica ( Grudhrasi)','',60),(11,'Spinal canal stenosis','',60),(12,'Calcaneal spur ( Vata Kantakam)','',60),(13,'Plantar Fascitis','',60),(14,'Ligment and Tendom injuries/ Sports injuries','',60),(15,'Tendonitis','',60),(16,'Frozen shoulder/ Peri Arthritis of shoulder (Amsa sandhi soolam)','',60),(17,'Poly Myalgia','',60),(18,'Peripheral Neuritis','',60),(19,'Recurrent dis location of joints','',60),(20,'Eczema( Vicharchika)','',60),(21,'Allergic skin disease','',60),(22,'Psoriasis(Sidhma)','',60),(23,'Gastritis','',60),(24,'Treatment for Bronchial Asthma','',60),(25,'Hyper Acidity','',60),(26,'Treatment for Nervous disability (Hemiplegia, Paraplegia)','',60),(27,'Treatment for Obesity','',60),(28,'Treatment for Heel pain','',60),(29,'Treatment for Uric acid problem','',60),(30,'Treatment to Subside ageing and ailments','',60),(31,'Weight Loss Program','',60),(32,'Stress & Strain relief','',60),(33,'Head ache & Migraine','',60),(34,'Sinusitis','',60),(35,'Irritable Bowl Syndrome ( IBS)','',60),(36,'Diabetes','',60),(37,'De-Addiction & Rehabilitation','',60),(38,'Reflux Esophagitis','',60),(39,'Trigeminal neuralgia/ Facial neuralgia','',60),(40,'Stroke','',60),(41,'Multiple Sclerosis','',60),(42,'Muscular Dystrophy','',60),(43,'Neuro Muscular diseases','',60),(44,'Hyper  Lipidaemia','',60),(45,'Auto immune Disorders','',60),(46,'Post Traumatic Brain Injury Syndrome(PTBIS)','',60),(47,'Respiratory  Allergy','',60),(48,'Poly Cystic Ovarian Syndrome','',60),(49,'Male & Female Infertility','',60),(50,'Menopausal Syndrome ','',60),(51,'Endometriosis','',60),(52,'Uterine Fibroids','',60),(53,'Rehabilitation of Cancer','',60),(54,'Preventive treatment for Lifestyle disorders','',60),(55,'Varicose veins treatment ','',60),(56,'Heart Blockage Treatment','',60),(57,'Idopathic Thrombocytopenic purpura( ITP)','',60),(58,'Cronic Kidney Disease treatment','',60),(59,'Hair loss treatment','',60);
/*!40000 ALTER TABLE `app_treatmentmaster` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add stock report',7,'add_stockreport'),(20,'Can change stock report',7,'change_stockreport'),(21,'Can delete stock report',7,'delete_stockreport'),(22,'Can add appointment',8,'add_appointment'),(23,'Can change appointment',8,'change_appointment'),(24,'Can delete appointment',8,'delete_appointment'),(25,'Can add package',9,'add_package'),(26,'Can change package',9,'change_package'),(27,'Can delete package',9,'delete_package'),(28,'Can add franchise',10,'add_franchise'),(29,'Can change franchise',10,'change_franchise'),(30,'Can delete franchise',10,'delete_franchise'),(31,'Can add customer',11,'add_customer'),(32,'Can change customer',11,'change_customer'),(33,'Can delete customer',11,'delete_customer'),(34,'Can add sales report',12,'add_salesreport'),(35,'Can change sales report',12,'change_salesreport'),(36,'Can delete sales report',12,'delete_salesreport'),(37,'Can add country',13,'add_country'),(38,'Can change country',13,'change_country'),(39,'Can delete country',13,'delete_country'),(40,'Can add service',14,'add_service'),(41,'Can change service',14,'change_service'),(42,'Can delete service',14,'delete_service'),(43,'Can add treatment',15,'add_treatment'),(44,'Can change treatment',15,'change_treatment'),(45,'Can delete treatment',15,'delete_treatment'),(46,'Can add pending prescription',16,'add_pendingprescription'),(47,'Can change pending prescription',16,'change_pendingprescription'),(48,'Can delete pending prescription',16,'delete_pendingprescription'),(49,'Can add product',17,'add_product'),(50,'Can change product',17,'change_product'),(51,'Can delete product',17,'delete_product'),(52,'Can add discount',18,'add_discount'),(53,'Can change discount',18,'change_discount'),(54,'Can delete discount',18,'delete_discount'),(55,'Can add sku list',19,'add_skulist'),(56,'Can change sku list',19,'change_skulist'),(57,'Can delete sku list',19,'delete_skulist'),(58,'Can add stock transfer',20,'add_stocktransfer'),(59,'Can change stock transfer',20,'change_stocktransfer'),(60,'Can delete stock transfer',20,'delete_stocktransfer'),(61,'Can add category',21,'add_category'),(62,'Can change category',21,'change_category'),(63,'Can delete category',21,'delete_category'),(64,'Can add stock',22,'add_stock'),(65,'Can change stock',22,'change_stock'),(66,'Can delete stock',22,'delete_stock'),(67,'Can add saved bill',23,'add_savedbill'),(68,'Can change saved bill',23,'change_savedbill'),(69,'Can delete saved bill',23,'delete_savedbill'),(70,'Can add audit report',24,'add_auditreport'),(71,'Can change audit report',24,'change_auditreport'),(72,'Can delete audit report',24,'delete_auditreport'),(73,'Can add profile',25,'add_profile'),(74,'Can change profile',25,'change_profile'),(75,'Can delete profile',25,'delete_profile'),(76,'Can set discount - Granularity:Item',25,'itemwise_discount'),(77,'Can set discount - Granularity:Category',25,'categorywise_discount'),(78,'Can set price wise discount',25,'price_discount'),(79,'Can set percentage wise discount',25,'percentage_discount'),(80,'Can view doctor details',25,'viewdoctor'),(81,'Can view patient details',25,'viewpatient'),(82,'Can prescribe medicine',25,'prescribe'),(83,'Can add bill',25,'addbill'),(84,'Can edit bill',25,'viewbill'),(85,'Can add user',25,'adduser'),(86,'Can modify user',25,'modifyuser'),(87,'Can add package mask',26,'add_packagemask'),(88,'Can change package mask',26,'change_packagemask'),(89,'Can delete package mask',26,'delete_packagemask'),(90,'Can add service mask',27,'add_servicemask'),(91,'Can change service mask',27,'change_servicemask'),(92,'Can delete service mask',27,'delete_servicemask'),(93,'Can add treatment master',28,'add_treatmentmaster'),(94,'Can change treatment master',28,'change_treatmentmaster'),(95,'Can delete treatment master',28,'delete_treatmentmaster'),(96,'Can add pending treatment',29,'add_pendingtreatment'),(97,'Can change pending treatment',29,'change_pendingtreatment'),(98,'Can delete pending treatment',29,'delete_pendingtreatment'),(99,'Can add sales report base',30,'add_salesreportbase'),(100,'Can change sales report base',30,'change_salesreportbase'),(101,'Can delete sales report base',30,'delete_salesreportbase'),(102,'Can add implementation',31,'add_implementation'),(103,'Can change implementation',31,'change_implementation'),(104,'Can delete implementation',31,'delete_implementation'),(105,'Can add inspection',32,'add_inspection'),(106,'Can change inspection',32,'change_inspection'),(107,'Can delete inspection',32,'delete_inspection'),(108,'Is a distributor',25,'distributor'),(109,'Can add enquiry',33,'add_enquiry'),(110,'Can change enquiry',33,'change_enquiry'),(111,'Can delete enquiry',33,'delete_enquiry'),(112,'Can add note',34,'add_note'),(113,'Can change note',34,'change_note'),(114,'Can delete note',34,'delete_note'),(115,'Can add notes',34,'add_notes'),(116,'Can change notes',34,'change_notes'),(117,'Can delete notes',34,'delete_notes'),(118,'Can add note',35,'add_note'),(119,'Can change note',35,'change_note'),(120,'Can delete note',35,'delete_note'),(121,'Can add timestamp db',36,'add_timestampdb'),(122,'Can change timestamp db',36,'change_timestampdb'),(123,'Can delete timestamp db',36,'delete_timestampdb'),(124,'Can add prescription',37,'add_prescription'),(125,'Can change prescription',37,'change_prescription'),(126,'Can delete prescription',37,'delete_prescription'),(127,'Can add ho product',38,'add_hoproduct'),(128,'Can change ho product',38,'change_hoproduct'),(129,'Can delete ho product',38,'delete_hoproduct'),(130,'Can add scan',39,'add_scan'),(131,'Can change scan',39,'change_scan'),(132,'Can delete scan',39,'delete_scan');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$jdVcWghcqpUX$bubdKQfWUsaTblBoBlAfDvobOsNoo36KTEgJSCn2hRI=','2017-11-02 05:10:01.000000',1,'root','','','dennispetergeorge@gmail.com',1,1,'2017-11-02 05:09:31.000000'),(2,'pbkdf2_sha256$36000$0JoHwwW2mycs$rHJtPhMkkifPx1t/7iF9FoXGlCLmgSM0lqXo/WAa4Xw=','2018-03-12 05:58:42.112715',1,'Dennis','Dennis','George','dennispetergeorge@gmail.com',1,1,'2017-11-02 05:12:53.000000'),(3,'pbkdf2_sha256$36000$t2tN7M0CtoQ5$GbVDzA/Jpu0CAmtPOzBGGh/67dJF6wHQ6GDikSHEgxk=','2018-03-11 13:47:46.901315',1,'George','','','dennispetergeorge@gmail.com',1,1,'2017-11-02 05:16:14.000000'),(4,'pbkdf2_sha256$36000$v1Gk3n78ufUm$ytsJqwvzw6CAyCOV16ln/uEXC8NdBW6Pwg0r31hDQZg=','2018-03-10 15:39:33.412212',0,'Sreejith','','','dennispetergeorge@gmail.com',0,1,'2017-11-02 05:44:16.000000'),(12,'pbkdf2_sha256$36000$rCfbn6ES6G2o$MRGyPgtwNxHB6yGhMIw3OMYXZojLTZ+xbp9Mj7ORl64=','2018-03-07 04:35:55.225975',0,'doctor','','','dennispetergeorge@gmail.com',0,1,'2017-11-21 05:25:58.000000'),(14,'pbkdf2_sha256$36000$yJaqfP2uxMfD$9IWGagzCOfqduecrsgp3QXliixXpIbQO/hzhNE36Xmo=','2018-02-10 05:36:57.972505',0,'distributor1','','','dennispetergeorge@gmail.com',0,1,'2017-12-03 04:09:44.000000'),(18,'pbkdf2_sha256$36000$WAtyDqBlDwby$JqTuzkesZRx3H0I//eGsW3RoqUn52eGk2OH8gQ6BzO8=','2018-03-03 13:54:31.690555',0,'joy','','','dennispetergeorge@gmail.com',0,1,'2017-12-31 04:29:53.000000'),(21,'pbkdf2_sha256$36000$XeIsX7LZRe97$w1NCfNKFSqdH/15az6+vFfdTfVBREJRXof1ce37IMUc=',NULL,0,'mathew','','','dennispetergeorge@gmail.com',0,1,'2017-12-31 04:44:16.575285'),(22,'pbkdf2_sha256$36000$YRsLbYdZUFtH$bc68sp7S/pxcEXIW0irZFhev0pLhG5Po1Gr92FSrp7Y=',NULL,0,'dre','dre','','dennispetergeorge@gmail.com',0,1,'2018-01-08 02:20:14.000000'),(23,'pbkdf2_sha256$36000$hWxvhXx1UVYM$LQjAMB82AeLxAHVPPrndblL7JACYMEj5vsn5EwilkRY=','2018-02-10 05:23:39.730999',0,'distributor2','','','dennispetergeorge@gmail.com',0,1,'2018-01-12 23:46:57.364674'),(24,'pbkdf2_sha256$36000$QCLt8BvGNBLS$C5VUr8VZ9SWd5lgjy4xWKhn93lUwmpOvHR8eWWJR7XY=','2018-02-08 03:03:00.518880',0,'Club Ayurveda','','','dennispetergeorge@gmail.com',0,1,'2018-02-08 03:01:53.201678');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=810 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,2,6),(7,2,7),(8,2,8),(9,2,9),(10,2,10),(11,2,11),(12,2,12),(13,2,13),(14,2,14),(15,2,15),(16,2,16),(17,2,17),(18,2,18),(19,2,19),(20,2,20),(21,2,21),(22,2,22),(23,2,23),(24,2,24),(25,2,25),(26,2,26),(27,2,27),(28,2,28),(29,2,29),(30,2,30),(31,2,31),(32,2,32),(33,2,33),(34,2,34),(35,2,35),(36,2,36),(37,2,37),(38,2,38),(39,2,39),(40,2,40),(41,2,41),(42,2,42),(43,2,43),(44,2,44),(45,2,45),(46,2,46),(47,2,47),(48,2,48),(49,2,49),(50,2,50),(51,2,51),(52,2,52),(53,2,53),(54,2,54),(55,2,55),(56,2,56),(57,2,57),(58,2,58),(59,2,59),(60,2,60),(61,2,61),(62,2,62),(63,2,63),(64,2,64),(65,2,65),(66,2,66),(67,2,67),(68,2,68),(69,2,69),(70,2,70),(71,2,71),(72,2,72),(73,2,73),(74,2,74),(75,2,75),(76,2,76),(77,2,77),(78,2,78),(79,2,79),(80,2,80),(81,2,81),(82,2,82),(83,2,83),(84,2,84),(85,2,85),(86,2,86),(449,3,1),(450,3,2),(451,3,3),(175,3,4),(176,3,5),(177,3,6),(178,3,7),(179,3,8),(180,3,9),(181,3,10),(182,3,11),(183,3,12),(453,3,13),(454,3,14),(455,3,15),(456,3,16),(457,3,17),(458,3,18),(118,3,19),(119,3,20),(120,3,21),(184,3,22),(185,3,23),(186,3,24),(99,3,25),(100,3,26),(101,3,27),(87,3,28),(88,3,29),(89,3,30),(187,3,31),(188,3,32),(189,3,33),(115,3,34),(116,3,35),(117,3,36),(190,3,37),(191,3,38),(192,3,39),(102,3,40),(103,3,41),(104,3,42),(193,3,43),(194,3,44),(195,3,45),(196,3,46),(197,3,47),(198,3,48),(96,3,49),(97,3,50),(98,3,51),(199,3,52),(200,3,53),(201,3,54),(95,3,55),(93,3,56),(94,3,57),(108,3,58),(109,3,59),(110,3,60),(90,3,61),(91,3,62),(92,3,63),(105,3,64),(106,3,65),(107,3,66),(202,3,67),(203,3,68),(204,3,69),(122,3,70),(123,3,71),(121,3,72),(205,3,73),(206,3,74),(207,3,75),(111,3,76),(112,3,77),(113,3,78),(114,3,79),(128,3,80),(129,3,81),(130,3,82),(126,3,83),(127,3,84),(124,3,85),(125,3,86),(208,3,87),(209,3,88),(210,3,89),(211,3,90),(212,3,91),(213,3,92),(214,3,93),(215,3,94),(216,3,95),(425,3,96),(426,3,97),(427,3,98),(428,3,99),(429,3,100),(430,3,101),(431,3,102),(432,3,103),(433,3,104),(434,3,105),(435,3,106),(436,3,107),(162,4,19),(163,4,20),(164,4,21),(752,4,31),(750,4,32),(751,4,33),(159,4,34),(160,4,35),(161,4,36),(146,4,43),(147,4,44),(148,4,45),(137,4,49),(138,4,50),(139,4,51),(136,4,55),(134,4,56),(135,4,57),(152,4,58),(153,4,59),(154,4,60),(131,4,61),(132,4,62),(133,4,63),(149,4,64),(150,4,65),(151,4,66),(166,4,70),(167,4,71),(165,4,72),(155,4,76),(156,4,77),(157,4,78),(158,4,79),(168,4,80),(169,4,81),(170,4,82),(173,4,83),(174,4,84),(171,4,85),(172,4,86),(142,4,87),(140,4,88),(141,4,89),(143,4,90),(144,4,91),(145,4,92),(423,12,81),(424,12,82),(441,14,19),(442,14,20),(443,14,21),(438,14,34),(439,14,35),(440,14,36),(445,14,70),(446,14,71),(444,14,72),(448,14,103),(447,14,106),(437,14,108),(622,18,19),(623,18,20),(624,18,21),(689,18,22),(690,18,23),(691,18,24),(692,18,31),(687,18,32),(688,18,33),(619,18,34),(620,18,35),(621,18,36),(606,18,43),(607,18,44),(608,18,45),(597,18,49),(598,18,50),(599,18,51),(596,18,55),(594,18,56),(595,18,57),(612,18,58),(613,18,59),(614,18,60),(591,18,61),(592,18,62),(593,18,63),(609,18,64),(610,18,65),(611,18,66),(626,18,70),(627,18,71),(625,18,72),(615,18,76),(616,18,77),(617,18,78),(618,18,79),(628,18,80),(629,18,81),(630,18,82),(633,18,83),(634,18,84),(631,18,85),(632,18,86),(602,18,87),(600,18,88),(601,18,89),(603,18,90),(604,18,91),(605,18,92),(672,21,19),(673,21,20),(674,21,21),(653,21,25),(654,21,26),(655,21,27),(641,21,28),(642,21,29),(643,21,30),(669,21,34),(670,21,35),(671,21,36),(656,21,40),(657,21,41),(658,21,42),(650,21,49),(651,21,50),(652,21,51),(649,21,55),(647,21,56),(648,21,57),(662,21,58),(663,21,59),(664,21,60),(644,21,61),(645,21,62),(646,21,63),(659,21,64),(660,21,65),(661,21,66),(676,21,70),(677,21,71),(675,21,72),(665,21,76),(666,21,77),(667,21,78),(668,21,79),(682,21,80),(683,21,81),(684,21,82),(680,21,83),(681,21,84),(678,21,85),(679,21,86),(685,21,103),(686,21,106),(724,22,19),(725,22,20),(726,22,21),(755,22,31),(753,22,32),(754,22,33),(721,22,34),(722,22,35),(723,22,36),(708,22,43),(709,22,44),(710,22,45),(699,22,49),(700,22,50),(701,22,51),(698,22,55),(696,22,56),(697,22,57),(714,22,58),(715,22,59),(716,22,60),(693,22,61),(694,22,62),(695,22,63),(711,22,64),(712,22,65),(713,22,66),(728,22,70),(729,22,71),(727,22,72),(717,22,76),(718,22,77),(719,22,78),(720,22,79),(730,22,80),(731,22,81),(732,22,82),(735,22,83),(736,22,84),(733,22,85),(734,22,86),(704,22,87),(702,22,88),(703,22,89),(705,22,90),(706,22,91),(707,22,92),(741,23,19),(742,23,20),(743,23,21),(738,23,34),(739,23,35),(740,23,36),(745,23,70),(746,23,71),(744,23,72),(748,23,103),(749,23,106),(737,23,108),(747,23,111),(787,24,19),(788,24,20),(789,24,21),(799,24,22),(800,24,23),(798,24,24),(768,24,25),(769,24,26),(770,24,27),(756,24,28),(757,24,29),(758,24,30),(803,24,31),(801,24,32),(802,24,33),(784,24,34),(785,24,35),(786,24,36),(771,24,40),(772,24,41),(773,24,42),(765,24,49),(766,24,50),(767,24,51),(764,24,55),(762,24,56),(763,24,57),(777,24,58),(778,24,59),(779,24,60),(759,24,61),(760,24,62),(761,24,63),(774,24,64),(775,24,65),(776,24,66),(791,24,70),(792,24,71),(790,24,72),(780,24,76),(781,24,77),(782,24,78),(783,24,79),(805,24,80),(806,24,81),(807,24,82),(796,24,83),(797,24,84),(794,24,85),(795,24,86),(808,24,103),(809,24,106),(804,24,110),(793,24,111);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-11-02 05:12:53.221854','2','George',1,'[{\"added\": {}}]',4,1),(2,'2017-11-02 05:13:55.071831','2','George',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]',4,1),(3,'2017-11-02 05:14:26.415564','1','root',2,'[{\"changed\": {\"fields\": [\"username\"]}}]',4,1),(4,'2017-11-02 05:14:51.234117','2','Dennis',2,'[{\"changed\": {\"fields\": [\"username\", \"first_name\", \"last_name\", \"is_staff\", \"is_superuser\"]}}]',4,1),(5,'2017-11-02 08:01:08.022028','3','George',2,'[]',4,2),(6,'2017-11-02 08:12:43.649631','4','Sreejith',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,2),(7,'2017-11-04 05:46:58.493200','3','George',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,2),(8,'2017-11-04 06:48:36.552700','5','random',3,'',4,2),(9,'2017-11-04 06:57:54.555630','8','Random',3,'',4,2),(10,'2017-11-21 05:29:05.879642','12','doctor',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,2),(11,'2017-11-30 04:10:56.758064','3','George',2,'[]',4,2),(12,'2017-12-03 04:09:03.408725','13','distributor1',3,'',4,2),(13,'2017-12-03 04:41:11.651116','14','distributor1',2,'[]',4,2),(14,'2017-12-03 04:49:24.932105','3','George',2,'[]',4,2),(15,'2017-12-03 04:49:35.339872','3','George',2,'[{\"changed\": {\"fields\": [\"is_staff\", \"is_superuser\"]}}]',4,2),(16,'2017-12-07 09:20:50.326329','2','Treatment object',3,'',15,2),(17,'2017-12-27 04:54:24.262847','2','Profile object',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',25,2),(18,'2017-12-27 05:23:50.785939','12','doctor',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,2),(19,'2017-12-28 23:20:01.617896','1','Enquiry object',1,'[{\"added\": {}}]',33,2),(20,'2017-12-29 00:16:42.821745','2','Enquiry object',3,'',33,2),(21,'2017-12-29 00:16:56.916048','3','Enquiry object',3,'',33,2),(22,'2017-12-29 00:17:45.507386','4','Enquiry object',3,'',33,2),(23,'2017-12-29 00:19:12.738911','6','Enquiry object',3,'',33,2),(24,'2017-12-29 00:35:11.720628','5','Enquiry object',3,'',33,2),(25,'2017-12-29 00:44:42.207847','1','Enquiry object',3,'',33,2),(26,'2017-12-31 04:39:36.995894','19','joy_doctor',3,'',4,2),(27,'2018-01-01 22:48:27.786408','18','joy',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,2),(28,'2018-01-02 00:00:48.114851','18','joy',2,'[]',4,2),(29,'2018-01-02 02:30:19.993959','20','joy_doctor',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,2),(30,'2018-01-02 02:51:26.065579','3','George',2,'[]',4,2),(31,'2018-01-05 03:07:19.297207','1','Note object',1,'[{\"added\": {}}]',35,2),(32,'2018-01-05 03:20:46.104325','1','Note object',3,'',35,2),(33,'2018-01-05 03:22:01.437856','2','Note object',1,'[{\"added\": {}}]',35,2),(34,'2018-01-06 01:42:38.204119','1','TimestampDB object',1,'[{\"added\": {}}]',36,2),(35,'2018-01-06 01:43:30.211361','2','TimestampDB object',1,'[{\"added\": {}}]',36,2),(36,'2018-01-06 01:44:37.384967','3','TimestampDB object',1,'[{\"added\": {}}]',36,2),(37,'2018-01-06 01:44:45.424173','4','TimestampDB object',1,'[{\"added\": {}}]',36,2),(38,'2018-01-06 01:44:57.791014','5','TimestampDB object',1,'[{\"added\": {}}]',36,2),(39,'2018-01-06 01:46:29.345168','6','TimestampDB object',1,'[{\"added\": {}}]',36,2),(40,'2018-01-06 01:48:54.505912','7','TimestampDB object',1,'[{\"added\": {}}]',36,2),(41,'2018-01-06 01:49:25.286948','8','TimestampDB object',1,'[{\"added\": {}}]',36,2),(42,'2018-01-06 02:00:23.146032','5','Customer object',3,'',11,2),(43,'2018-01-06 02:00:29.546168','4','Customer object',3,'',11,2),(44,'2018-01-06 02:04:21.013067','6','Customer object',3,'',11,2),(45,'2018-01-06 02:06:01.873531','7','Customer object',3,'',11,2),(46,'2018-01-06 02:11:04.547220','8','Customer object',3,'',11,2),(47,'2018-01-12 23:59:52.577248','7','Franchise object',3,'',10,2),(48,'2018-01-13 00:02:06.068087','8','Franchise object',3,'',10,2),(49,'2018-01-13 00:53:09.539516','4','Sreejith',2,'[]',4,3),(50,'2018-01-13 00:53:25.335293','22','dre',2,'[]',4,3),(51,'2018-01-28 13:27:43.376019','3','SKUList object',2,'[{\"changed\": {\"fields\": [\"unit\"]}}]',19,2),(52,'2018-02-10 04:38:05.689961','12','doctor',2,'[]',4,2),(53,'2018-02-17 04:21:22.114308','26','john2',3,'',4,2),(54,'2018-02-17 04:21:22.216756','25','john',3,'',4,2),(55,'2018-02-17 04:25:24.548039','9','Franchise object',3,'',10,2),(56,'2018-02-17 04:25:28.984023','7','Franchise object',3,'',10,2),(57,'2018-02-17 04:28:14.400454','10','Franchise object',3,'',10,2),(58,'2018-02-20 03:14:37.069140','28','john',3,'',4,2),(59,'2018-02-20 03:50:25.851333','20','joy_doctor',3,'',4,2),(60,'2018-02-20 03:50:26.034694','9','Random',3,'',4,2),(61,'2018-02-20 03:50:26.079372','10','random2',3,'',4,2),(62,'2018-02-20 03:50:26.124063','11','random3',3,'',4,2),(63,'2018-02-21 13:18:55.955711','2','Enquiry object',3,'',33,2),(64,'2018-02-21 13:19:08.122999','1','Enquiry object',3,'',33,2),(65,'2018-02-21 13:19:43.629671','4','Enquiry object',3,'',33,2),(66,'2018-02-21 13:19:43.708044','3','Enquiry object',3,'',33,2),(67,'2018-02-21 13:35:17.022602','5','Enquiry object',3,'',33,2),(68,'2018-02-22 10:49:16.639535','11','Customer object',3,'',11,2),(69,'2018-02-22 17:27:22.292030','11','Customer object',3,'',11,2),(70,'2018-02-22 18:05:51.323020','12','Customer object',3,'',11,2),(71,'2018-02-25 07:04:05.430159','13','Customer object',3,'',11,2),(72,'2018-02-26 01:38:14.248068','7','Franchise object',3,'',10,2),(73,'2018-03-12 05:58:59.253293','22','dre',2,'[{\"changed\": {\"fields\": [\"first_name\"]}}]',4,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'app','appointment'),(24,'app','auditreport'),(21,'app','category'),(13,'app','country'),(11,'app','customer'),(18,'app','discount'),(33,'app','enquiry'),(10,'app','franchise'),(38,'app','hoproduct'),(31,'app','implementation'),(32,'app','inspection'),(35,'app','note'),(34,'app','notes'),(9,'app','package'),(26,'app','packagemask'),(16,'app','pendingprescription'),(29,'app','pendingtreatment'),(37,'app','prescription'),(17,'app','product'),(25,'app','profile'),(12,'app','salesreport'),(30,'app','salesreportbase'),(23,'app','savedbill'),(39,'app','scan'),(14,'app','service'),(27,'app','servicemask'),(19,'app','skulist'),(22,'app','stock'),(7,'app','stockreport'),(20,'app','stocktransfer'),(36,'app','timestampdb'),(15,'app','treatment'),(28,'app','treatmentmaster'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-11-02 05:06:18.860971'),(2,'auth','0001_initial','2017-11-02 05:06:31.960008'),(3,'admin','0001_initial','2017-11-02 05:06:34.732048'),(4,'admin','0002_logentry_remove_auto_add','2017-11-02 05:06:34.889285'),(5,'app','0001_initial','2017-11-02 05:06:49.347155'),(6,'contenttypes','0002_remove_content_type_name','2017-11-02 05:06:51.477016'),(7,'auth','0002_alter_permission_name_max_length','2017-11-02 05:06:51.774255'),(8,'auth','0003_alter_user_email_max_length','2017-11-02 05:06:51.991081'),(9,'auth','0004_alter_user_username_opts','2017-11-02 05:06:52.058859'),(10,'auth','0005_alter_user_last_login_null','2017-11-02 05:06:53.163776'),(11,'auth','0006_require_contenttypes_0002','2017-11-02 05:06:53.252186'),(12,'auth','0007_alter_validators_add_error_messages','2017-11-02 05:06:53.327186'),(13,'auth','0008_alter_user_username_max_length','2017-11-02 05:06:54.021020'),(14,'sessions','0001_initial','2017-11-02 05:06:54.923956'),(15,'app','0002_packagemask_servicemask_treatmentmaster','2017-11-02 05:40:34.421495'),(16,'app','0003_franchise_active','2017-11-02 05:54:39.964980'),(17,'app','0004_auto_20171102_0736','2017-11-02 07:36:24.512480'),(18,'app','0005_auto_20171102_0746','2017-11-02 07:46:19.542114'),(19,'app','0006_auto_20171102_0808','2017-11-02 08:09:16.986157'),(20,'app','0007_auto_20171102_0907','2017-11-02 09:07:15.446328'),(21,'app','0008_auto_20171102_1104','2017-11-02 11:10:21.451732'),(22,'app','0009_auto_20171102_1110','2017-11-02 11:10:22.060270'),(23,'app','0010_auto_20171104_0605','2017-11-04 06:05:57.368040'),(24,'app','0011_pendingtreatment','2017-11-10 05:38:16.308377'),(25,'app','0012_auto_20171110_2341','2017-11-10 23:41:30.832484'),(26,'app','0013_profile_regid','2017-11-11 01:44:32.621168'),(27,'app','0014_customer_phoneno_sec','2017-11-11 01:49:18.417286'),(28,'app','0015_country_district_code','2017-11-11 02:02:41.412583'),(29,'app','0016_auto_20171111_0234','2017-11-11 02:34:12.727568'),(30,'app','0017_auto_20171118_1644','2017-11-18 16:44:48.165651'),(31,'app','0018_remove_salesreport_franchise_code','2017-11-18 16:44:49.254035'),(32,'app','0019_auto_20171118_1647','2017-11-18 16:47:19.841256'),(33,'app','0020_auto_20171118_2019','2017-11-18 20:19:29.968163'),(34,'app','0021_auto_20171118_2024','2017-11-18 20:24:06.129595'),(35,'app','0022_customer_franchise_code','2017-11-23 07:17:59.996246'),(36,'app','0023_implementation','2017-11-26 14:17:23.933793'),(37,'app','0024_inspection','2017-11-26 14:18:36.567421'),(38,'app','0025_auto_20171203_0409','2017-12-03 04:09:28.898722'),(39,'app','0026_auto_20171203_0947','2017-12-03 09:47:57.182308'),(40,'app','0027_inspection_comments','2017-12-03 18:49:40.681821'),(41,'app','0028_implementation_date_mou','2017-12-03 18:50:54.740106'),(42,'app','0029_auto_20171203_1851','2017-12-03 18:51:07.419429'),(43,'app','0030_inspection_v7','2017-12-03 19:06:33.711264'),(44,'app','0031_franchise_website','2017-12-04 05:49:21.771742'),(45,'app','0032_customer_company_name','2017-12-07 08:53:51.542840'),(46,'app','0033_auto_20171207_1031','2017-12-07 13:35:37.146191'),(47,'app','0034_auto_20171227_0509','2017-12-27 05:10:06.483997'),(48,'app','0035_auto_20171227_0602','2017-12-27 06:02:34.369298'),(49,'app','0036_auto_20171227_1141','2017-12-27 11:41:32.128390'),(50,'app','0037_auto_20171228_0743','2017-12-28 07:44:06.526861'),(51,'app','0038_note','2017-12-28 08:53:51.124664'),(52,'app','0039_auto_20171228_0859','2017-12-28 09:00:05.265738'),(53,'app','0040_auto_20171228_0904','2017-12-28 09:04:30.638917'),(54,'app','0041_auto_20171228_0906','2017-12-28 09:06:35.605986'),(55,'app','0042_auto_20171228_0911','2017-12-28 09:11:39.509653'),(56,'app','0043_delete_note','2017-12-28 09:14:05.987077'),(57,'app','0044_note','2017-12-28 09:15:22.148466'),(58,'app','0045_auto_20171228_0923','2017-12-28 09:23:46.967174'),(59,'app','0046_delete_notes','2017-12-28 09:28:15.175264'),(60,'app','0047_note','2017-12-28 09:29:00.138350'),(61,'app','0048_auto_20171228_2301','2017-12-28 23:17:29.803731'),(62,'app','0049_auto_20171228_2317','2017-12-28 23:17:33.767557'),(63,'app','0050_auto_20171228_2325','2017-12-28 23:25:59.291218'),(64,'app','0051_auto_20171229_0004','2017-12-29 00:04:45.737004'),(65,'app','0052_auto_20171229_0014','2017-12-29 00:14:42.090869'),(66,'app','0053_auto_20171229_0014','2017-12-29 00:15:00.342518'),(67,'app','0054_remove_enquiry_date','2017-12-29 00:18:36.420386'),(68,'app','0055_auto_20171229_0041','2017-12-29 00:41:42.637871'),(69,'app','0056_auto_20171229_0042','2017-12-29 00:42:27.507185'),(70,'app','0057_auto_20171229_0046','2017-12-29 00:46:28.113723'),(71,'app','0058_auto_20171230_1520','2017-12-30 15:20:22.261467'),(72,'app','0059_auto_20171231_0658','2017-12-31 06:58:48.552206'),(73,'app','0060_franchise_customers_today','2017-12-31 09:07:35.430535'),(74,'app','0061_franchise_new_customers','2017-12-31 09:16:36.656294'),(75,'app','0062_enquiry_timestamp','2017-12-31 09:21:20.257549'),(76,'app','0063_remove_enquiry_timestamp','2017-12-31 09:22:04.509207'),(77,'app','0064_enquiry_timestamp','2017-12-31 09:22:50.645234'),(78,'app','0065_auto_20180101_0953','2018-01-01 09:59:46.340519'),(79,'app','0066_timestampdb','2018-01-01 09:59:46.904694'),(80,'app','0067_auto_20180101_2259','2018-01-01 23:00:03.010439'),(81,'app','0068_enquiry_lastchanged','2018-01-02 00:28:54.343484'),(82,'app','0069_auto_20180102_0829','2018-01-02 02:59:52.404861'),(83,'app','0070_note_pic','2018-01-05 02:45:03.774598'),(84,'app','0071_auto_20180105_1028','2018-01-05 04:58:32.849704'),(85,'app','0072_prescription','2018-01-05 10:16:39.136426'),(86,'app','0073_auto_20180105_1557','2018-01-05 10:27:34.088188'),(87,'app','0074_auto_20180110_0750','2018-01-10 02:21:01.987304'),(88,'app','0075_discount_franchise_name','2018-01-10 02:28:09.865170'),(89,'app','0076_auto_20180111_0610','2018-01-11 00:40:32.629250'),(90,'app','0077_auto_20180113_0650','2018-01-13 01:20:45.548874'),(91,'app','0078_enquiry_confirmed_time','2018-01-19 07:08:08.880049'),(92,'app','0079_hoproduct','2018-01-22 09:00:33.042110'),(93,'app','0080_auto_20180128_1626','2018-01-28 10:56:34.904877'),(94,'app','0081_auto_20180128_1904','2018-01-28 13:34:32.101286'),(95,'app','0082_remove_treatmentmaster_body_part','2018-02-10 05:39:30.653828'),(96,'app','0083_scan','2018-02-13 12:27:12.833493'),(97,'app','0084_auto_20180214_0029','2018-02-13 18:59:21.228316'),(98,'app','0085_customer_gender','2018-02-14 03:46:20.597766'),(99,'app','0086_auto_20180217_0939','2018-02-17 04:09:15.605573'),(100,'app','0087_auto_20180217_0947','2018-02-17 04:17:13.596682'),(101,'app','0088_auto_20180220_0848','2018-02-20 03:18:29.487753'),(102,'app','0002_appointment','2018-02-21 02:01:39.469961'),(103,'app','0003_remove_enquiry_time','2018-02-21 13:12:17.850725'),(104,'app','0004_enquiry_requested_time','2018-02-21 13:15:28.292806'),(105,'app','0005_auto_20180221_1847','2018-02-21 13:17:04.826455'),(106,'app','0006_appointment_request','2018-02-22 18:13:46.974630'),(107,'app','0007_auto_20180301_1029','2018-03-01 04:59:59.901614'),(108,'app','0008_auto_20180301_1032','2018-03-01 05:02:14.362618'),(109,'app','0009_auto_20180303_1931','2018-03-03 14:01:58.662366'),(110,'app','0010_auto_20180306_1122','2018-03-06 05:53:10.161156'),(111,'app','0011_franchise_bankname','2018-03-07 05:34:08.963515'),(112,'app','0012_franchise_town','2018-03-07 07:02:08.512743'),(113,'app','0013_franchise_gstno','2018-03-10 15:52:28.018394');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('05i3le74mzblwyvuhvffiu0kj3iv71ao','OWZiZjUyNzE0OWRiMjU3NWM3YjE2YzY1ZTNiMThkYjlmYTk1ZWRhZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzNDUxM2I1Y2NiZTZmNWQ1YjQ2Y2E5ZDNjZTM4NjNmODRhMTY1ZDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-01-16 04:05:48.132899'),('2g33azwb8fam95u2sofyjrycr4j5j1m1','OWU4MTliYThhMjcwZDMzYzU1ZGYxYjgzMjE2YzMxZTYwYTZmYjhlOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyNzdlOWEyY2U2NDAxMTRkM2MxOTZjZmUyNmU3MWFiNTY4Y2YwZGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2018-02-03 10:22:14.397864'),('2gt7ho3aabr5qp9crpu659kkfzlahg7c','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-02-11 10:54:45.119272'),('32tgypkm3t9u56g75pmejn6i4pabamen','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-03-26 05:58:42.314112'),('54itao22vvijjvv8v2m4pgmzs21zhx42','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-03-07 13:17:43.324384'),('5d278bcudc8fvbg4xnyuyz9z02ffbxsq','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-01-11 23:16:43.400089'),('9306tbs6cp5tpuwh7hpdkjscilyw86rc','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-12-21 08:57:31.152203'),('99tnunrz9qx6ql8t09joec02i7yr5ye4','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-02-13 09:44:57.781473'),('9lt93pnn2k9fwwsldccloxuhoqrvd73a','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-02-13 10:24:56.706095'),('a48gq2blw2i971t0hgxbm3kwb7g79wrv','OWZiZjUyNzE0OWRiMjU3NWM3YjE2YzY1ZTNiMThkYjlmYTk1ZWRhZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzNDUxM2I1Y2NiZTZmNWQ1YjQ2Y2E5ZDNjZTM4NjNmODRhMTY1ZDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2017-12-07 06:51:14.916406'),('agtdiaztw3u1jburwntdemgppi4kumar','MDQ1NjE3NTM5YTY4OGYxZTBjZGQ4ZjZiNmFjMzJkZDM5MmM5NTc0Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2YzE2OTcxNWEzMDJkZDc2YzcyMjVhNmRmMTdlODQ1NDQzMGM0ZWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyMyJ9','2018-01-27 00:12:05.350653'),('ax9ygf2docphl25flm2ldac2o648u4o3','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-03-07 04:06:36.322836'),('bl1xixtuoutlntinrznez19oj3ij7224','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-01-16 02:50:11.307112'),('chutgiuqzafe7j9hcsvh1uekzc0kpo0c','OTY1MWJkYzFhZjUyMWM1NzYxNmJkZWE1YmQ0YmFlNzA3NDNkMzc3Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjcyNWMzODkzMDgzNzc3NjEyOGFjYjUzNjUxMWU2MDA3NjA0OWM3NGYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-02-24 05:38:21.455687'),('dacb0nsf20zk8in9rel45evl03f6otdt','N2ZmMGEwMTczYTkxYjRjNWI2MDBhZjYxZTFiNjQ1NjcwNDNmYzk3Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjM0ZmI2ZmNiYzU4MWNjODlmNWNkOWE2YzY1ZjJjYWViYmJjMDJlZDIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9','2018-01-15 08:44:26.329704'),('e31bsdq61s0vyn0a4l8hjiulsqoaaqcv','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-03-06 03:10:54.315608'),('ecnza6kn365grdvh2dgaqaic6m4z3g5g','OWZiZjUyNzE0OWRiMjU3NWM3YjE2YzY1ZTNiMThkYjlmYTk1ZWRhZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzNDUxM2I1Y2NiZTZmNWQ1YjQ2Y2E5ZDNjZTM4NjNmODRhMTY1ZDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-02-07 08:12:21.938563'),('eqfpih62fdhqgn4ji1tfbg2m6px076b6','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-01-11 06:41:23.181849'),('f71frnrqo3cl0bck2jn7x3ogn6zkbhqt','MjBhMmZiMTkyYWI3Zjc1NDFjNmQ5ZDAwZTFlNWJmYTQwZGYxMDZkMzp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-11-16 08:12:44.073253'),('figqjkmyztw57s28zhkvb8hn0a0yj9v3','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-03-11 04:13:52.357802'),('fs2x3lyqtn9f81yu8opg0em53senpjn2','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2017-12-05 05:29:19.984357'),('h6tdg8wqc4ypeo0ggkyyyjvfqwptaxgb','NWExMTU3MTlhNTQzN2Y0ZTFhNjlkYjk3OWJiMjQ0Mjk1YjhhODEwYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjRlZTgxZjRjZWQyYzdhNjZkODhhOWJmNmRjNjVhMDI3MjZiM2FlMzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2018-03-24 15:48:46.679159'),('hc0ouhoc5k8qljdvjndm5sjiwify5xbw','OWU4MTliYThhMjcwZDMzYzU1ZGYxYjgzMjE2YzMxZTYwYTZmYjhlOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyNzdlOWEyY2U2NDAxMTRkM2MxOTZjZmUyNmU3MWFiNTY4Y2YwZGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2018-01-25 00:18:13.479392'),('hqcqr70curqjvrzpb02y8cgyuo10ah91','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-03-03 04:20:55.356334'),('iuqgkiszbpxhqakgvkbwjg1fgkhah8r5','OTY1MWJkYzFhZjUyMWM1NzYxNmJkZWE1YmQ0YmFlNzA3NDNkMzc3Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjcyNWMzODkzMDgzNzc3NjEyOGFjYjUzNjUxMWU2MDA3NjA0OWM3NGYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-02-27 09:15:43.527659'),('krizv5o8mcgarwgnrjrv2npxq44reodl','ODdkMDI2ODI4NjMyMzI1MDBmZTk2MDU4ZDY2Njg4Mjg5NWEzMWNlZDp7Il9hdXRoX3VzZXJfaGFzaCI6ImEzYjZkYmRlNTA4ZmQ5MjNkMjA5MTA5MGQzODllMDA0ZTYzZjZmOTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9','2018-01-20 04:07:50.546463'),('kt1fik02vm060b7335uy4ft2cpvvscgg','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-03-12 01:38:04.750280'),('kxhgvwyhfr5jlnc6dpnbwyu3ncvq4li4','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-03-09 09:37:02.662304'),('mlmvd0tq2eu52q0wx8bzldsl1l9zagjf','OTY1MWJkYzFhZjUyMWM1NzYxNmJkZWE1YmQ0YmFlNzA3NDNkMzc3Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjcyNWMzODkzMDgzNzc3NjEyOGFjYjUzNjUxMWU2MDA3NjA0OWM3NGYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-03-11 15:42:45.593285'),('n3nyfm1v4kvikopi44i8th10ombeje72','OWZiZjUyNzE0OWRiMjU3NWM3YjE2YzY1ZTNiMThkYjlmYTk1ZWRhZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzNDUxM2I1Y2NiZTZmNWQ1YjQ2Y2E5ZDNjZTM4NjNmODRhMTY1ZDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-01-02 05:59:23.166796'),('n5sa8vbcvci2vb5detctom5jsya4xi1c','OTY1MWJkYzFhZjUyMWM1NzYxNmJkZWE1YmQ0YmFlNzA3NDNkMzc3Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjcyNWMzODkzMDgzNzc3NjEyOGFjYjUzNjUxMWU2MDA3NjA0OWM3NGYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-03-07 01:53:48.078343'),('nzcmia99fg8g8u35uw4me7yujf27zl81','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-12-14 04:10:22.845583'),('pce8s1tx7xj7xdgdg4su2kbmfuepyo20','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-01-24 09:26:01.125118'),('pggc7dxeg8ri46i25teva1rjb48vsera','OWZiZjUyNzE0OWRiMjU3NWM3YjE2YzY1ZTNiMThkYjlmYTk1ZWRhZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzNDUxM2I1Y2NiZTZmNWQ1YjQ2Y2E5ZDNjZTM4NjNmODRhMTY1ZDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2017-12-02 20:09:52.128203'),('q4kjlshge9l80zyoblg59y63bb2lqpu6','OWU4MTliYThhMjcwZDMzYzU1ZGYxYjgzMjE2YzMxZTYwYTZmYjhlOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyNzdlOWEyY2U2NDAxMTRkM2MxOTZjZmUyNmU3MWFiNTY4Y2YwZGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2018-02-04 03:59:34.638927'),('q5dw6od4l37ykce25emi1xxgu8pkbvko','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-02-25 12:54:21.099462'),('qai95waknh5l7r1qfrqak3molws4bpq4','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-03-08 18:27:16.648648'),('qn67eo6r6cwlzctjbexz5kglecy4yort','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-01-02 06:03:07.155284'),('rfzqjmfxr5ktpjn6vct3csevmtqq88le','OTY1MWJkYzFhZjUyMWM1NzYxNmJkZWE1YmQ0YmFlNzA3NDNkMzc3Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjcyNWMzODkzMDgzNzc3NjEyOGFjYjUzNjUxMWU2MDA3NjA0OWM3NGYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-03-12 02:00:58.729937'),('tu7c256l0hdtqpcgyt28655xwopgepin','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2017-11-18 06:48:18.787366'),('u1ctzkfbo404pnysmpmpvokvhjgl2ced','N2ZmMGEwMTczYTkxYjRjNWI2MDBhZjYxZTFiNjQ1NjcwNDNmYzk3Yzp7Il9hdXRoX3VzZXJfaGFzaCI6IjM0ZmI2ZmNiYzU4MWNjODlmNWNkOWE2YzY1ZjJjYWViYmJjMDJlZDIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9','2018-01-14 04:39:59.756698'),('udged4zbruk0l0zqax1l6w88n5retmzw','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-01-10 04:47:58.385154'),('uj2yhowox05aj6wisxceg968myk602ea','OWU4MTliYThhMjcwZDMzYzU1ZGYxYjgzMjE2YzMxZTYwYTZmYjhlOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjAyNzdlOWEyY2U2NDAxMTRkM2MxOTZjZmUyNmU3MWFiNTY4Y2YwZGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2017-12-17 04:49:46.301603'),('v8bm40vzo9li863j6ofoo442h8a9wahp','ZWZkN2IwMmE4ZmViYjdjYjNkNTMwOTYwOTRkMTdhMWQyNzAzNTlhZjp7Il9hdXRoX3VzZXJfaGFzaCI6ImI3ZTNhZDQ1NzFiNjc5NzYwOTJmZDE1ZGFiYWZkODIwMmFjMDE3MjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2018-01-11 02:53:57.895327'),('vkloif1049rzhxdpid78800c21lywfrp','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-02-21 02:32:19.429188'),('vohiw8lsd1la0k2o8d33cbfigq7tmtdz','Yzc3MjhmM2UzYjJmNmE3ZTU2YmEwMTJhNDM0YjgxN2RiNWQ1OTE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImEyMDhkM2FkY2Q1NzBhNWVkNDU0NTA0ZDk3NmE4MDg2NmRhYWQzYWIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-03-08 10:45:51.212402'),('wnsiq71whvwzw2ncvh3zc7yyywcuudsd','NWExMTU3MTlhNTQzN2Y0ZTFhNjlkYjk3OWJiMjQ0Mjk1YjhhODEwYzp7Il9hdXRoX3VzZXJfaGFzaCI6IjRlZTgxZjRjZWQyYzdhNjZkODhhOWJmNmRjNjVhMDI3MjZiM2FlMzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2018-03-25 13:47:47.086185'),('xjokd1qiplcpxl0c6pcqdgy8o7rp40rk','OTY1MWJkYzFhZjUyMWM1NzYxNmJkZWE1YmQ0YmFlNzA3NDNkMzc3Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjcyNWMzODkzMDgzNzc3NjEyOGFjYjUzNjUxMWU2MDA3NjA0OWM3NGYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2018-03-07 03:17:48.163689'),('yirtfmxrwvr8v91w3cla8wus5p71bael','OWZiZjUyNzE0OWRiMjU3NWM3YjE2YzY1ZTNiMThkYjlmYTk1ZWRhZTp7Il9hdXRoX3VzZXJfaGFzaCI6ImMzNDUxM2I1Y2NiZTZmNWQ1YjQ2Y2E5ZDNjZTM4NjNmODRhMTY1ZDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=','2017-12-25 06:41:48.754818'),('zpx5ibgpjtf2pjmorv9yu3th72wpchh1','NmIwOTQzODBkNjI1YzkyZWU4ZjM0Mjk2OTA2YzhiMGI5MGVmZTBiNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjVhMzljYTExZTIxYmNjZTEyYzgzM2NjYTE5N2Q5MjE1MDQ5NWEzMzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2018-03-21 05:01:37.731414');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-13  8:17:33
