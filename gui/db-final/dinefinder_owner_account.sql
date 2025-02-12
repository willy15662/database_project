-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: dinefinder
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `owner_account`
--

DROP TABLE IF EXISTS `owner_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owner_account` (
  `owner_id` int unsigned NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `have_restaurant` int unsigned DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `email_address` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner_account`
--

LOCK TABLES `owner_account` WRITE;
/*!40000 ALTER TABLE `owner_account` DISABLE KEYS */;
INSERT INTO `owner_account` VALUES (1234,'1234','1234',NULL,NULL,NULL),(2000000001,'K1jiu','bWpQYfb6Y79Nr4E',1,'0970472898','k1jiu@gmail.com'),(2000000002,'eI0YOzRs','YVEouoYfTJ6Iwbk',1,'0984336742','ei0yo@yahoo.com'),(2000000003,'z34brd2','pn6T1h',1,'0927768884','z34br@gmail.com'),(2000000004,'qvJjwzDSmq1','xbbaow972SIxP',1,'0942934405','qvjjw@gmail.com'),(2000000005,'scRwNhIuPbf3Ywe1','IGIJS3X1KcnR',1,'0968446655','scrwn@yahoo.com'),(2000000006,'zkdBU00qk','sOT6TUthB9H21RN',1,'0941901239','zkdbu@gmail.com'),(2000000007,'YorssNuXCrbTJQJW','AbQva',1,'0988930114','yorss@gmail.com'),(2000000008,'Y6oVTqR','9IweaNBAR8fW',1,'0910944840','y6ovt@yahoo.com'),(2000000009,'uuuH4AN3fEO5','bFbjHjCWYI',1,'0930673816','uuuh4@yahoo.com'),(2000000010,'XqUwImb2HKQ8J5x','OGYux5J',1,'0982747304','xquwi@gmail.com'),(2000000011,'RFaeTXKiuH74f','IpSIJ',1,'0999373251','rfaet@gmail.com'),(2000000012,'LSlQpvJB','PODJPoMs7KWM6',1,'0979421947','lslqp@gmail.com'),(2000000013,'eoLatL','I1yjeHF1s4eT371F',1,'0904983562','eolat@yahoo.com'),(2000000014,'SCxUl5k','QoY8siqYg7SDnK',1,'0913253447','scxul@yahoo.com'),(2000000015,'NHpSBu1spf','fXm9DQmc',1,'0973859821','nhpsb@gmail.com'),(2000000016,'Q3ylb7thQ','6QoaVFer0',1,'0977263269','q3ylb@yahoo.com'),(2000000017,'WdKSJd3nc68w','gruPaFz',1,'0941302326','wdksj@yahoo.com'),(2000000018,'FylN4XtU6AGA','QQyCz4qdHPVyYYx',1,'0965316275','fyln4@yahoo.com'),(2000000019,'qAhSLULEfZlodF','udd1KJBq7U',1,'0911792938','qahsl@gmail.com'),(2000000020,'ttJJbF4Lpvs','PkgQ0xp',1,'0954573342','ttjjb@yahoo.com'),(2000000021,'ijTKn8CSG430','WeG8RTVJ603yg',1,'0981479024','ijtkn@gmail.com'),(2000000022,'x60LXc','iWPRyuMy1yeSsEc',1,'0906990908','x60lx@yahoo.com'),(2000000023,'KTIFuJupD6KdbSnQ','zId44aCqOgGo',1,'0951959978','ktifu@yahoo.com'),(2000000024,'LU3yvLMUV6QlnbQU','pkbEhOPs96v4',1,'0938684490','lu3yv@yahoo.com'),(2000000025,'BoRHbD','QK125JEXG',1,'0929463640','borhb@gmail.com'),(2000000026,'lRMZv7k9nDo','u9TSLfjO2eAZj',1,'0927893709','lrmzv@gmail.com'),(2000000027,'qJ4VyS','MLIKBzbkA5FgaXz',1,'0918759502','qj4vy@gmail.com'),(2000000028,'zJiG4n','09SBCd62bk5tJJ7',1,'0997655998','zjig4@yahoo.com'),(2000000029,'v36Ph','yasTtPATK',1,'0985446885','v36ph@gmail.com'),(2000000030,'BmusdUE','wndyr7gK',1,'0935933802','bmusd@gmail.com'),(2000000031,'iUvBb','Ivn0F7XDR3t02m',1,'0966712570','iuvbb@gmail.com'),(2000000032,'oSqCjF0pi4VuU','YXVDkuza',1,'0909141058','osqcj@gmail.com'),(2000000033,'qUQiq','wRnWGUKaZBL',1,'0941207505','quqiq@gmail.com'),(2000000034,'h780LehKxpBLOUlw','7veX057RRx',1,'0977771213','h780l@yahoo.com'),(2000000035,'6wZMQRIX4','nkZ332',1,'0945506832','6wzmq@gmail.com'),(2000000036,'GEA0h20E','U4ZNfAkPE443aC',1,'0975707976','gea0h@gmail.com'),(2000000037,'MKefN','oZ2b9Bmayli',1,'0919164103','mkefn@yahoo.com'),(2000000038,'unCQqy','iuY2PIy6rwCycs7',1,'0933258151','uncqq@yahoo.com'),(2000000039,'FiRLaGsPfO2QKk','HB1UhY5gN',1,'0917858057','firla@yahoo.com'),(2000000040,'To5HLQJY','WPUt9SZkAoj',1,'0930650396','to5hl@yahoo.com'),(2000000041,'rBdnYTT7','RBBmjfpSPdlcLx',1,'0914343426','rbdny@yahoo.com'),(2000000042,'Zachg5bSBy','cIkO7HOY33tWti',1,'0924103690','zachg@gmail.com'),(2000000043,'UwufdqGq','eCGk9JmcJ1v',1,'0993129277','uwufd@yahoo.com'),(2000000044,'FCFRSCyBhMX','2W5jX9amwK1ieCk',1,'0910963745','fcfrs@yahoo.com'),(2000000045,'3jJGYwPIOaawYipo','TkCM3Q9sTFydDTU',1,'0941843720','3jjgy@yahoo.com'),(2000000046,'d4MLoTJ6rQ','FP04r',1,'0936178667','d4mlo@yahoo.com'),(2000000047,'RJZok','VpLvVO1',1,'0990767984','rjzok@yahoo.com'),(2000000048,'BBJP2G','H7CjB',1,'0980797145','bbjp2@yahoo.com'),(2000000049,'qDQArhJ','zfr2CQRxX4Ff',1,'0950352333','qdqar@yahoo.com'),(2000000050,'otVTOO25tHBhc3','GBePgLoUFvEZFH5',1,'0986666121','otvto@gmail.com'),(2000000051,'RIvSl86w5','RNyMFYKMKeH',1,'0954793769','rivsl@gmail.com'),(2000000052,'3dMeGEdn','JMd6bRpqRWr',1,'0905281486','3dmeg@gmail.com'),(2000000053,'Qn1o0I5DKtDXf','lXyUn9oFATMl',1,'0953419714','qn1o0@gmail.com'),(2000000054,'RVqgcy45uc','OgKJ3Pcd5',1,'0988641968','rvqgc@gmail.com'),(2000000055,'C9v5ERCU','A7aYxaJDkkdfxAue',1,'0900849768','c9v5e@gmail.com'),(2000000056,'q3RgZKMV','Iwt5aUI0SQtt4',1,'0986519200','q3rgz@gmail.com'),(2000000057,'S7p8nM3SeB','zNB6zfmT',1,'0928735528','s7p8n@yahoo.com'),(2000000058,'5B7hc','3SnRHaUBr3abG5',1,'0936957476','5b7hc@yahoo.com'),(2000000059,'ZMa3JOgL6HddBg7','4HQk6RXm92hc3I',1,'0918694612','zma3j@gmail.com'),(2000000060,'7Z06oigdEDp','RwWYtcdT',1,'0936398980','7z06o@gmail.com'),(2000000061,'IvT0HPZMEeHE','yRIEkzE6',1,'0968510161','ivt0h@gmail.com'),(2000000062,'jXhJ6DA','RDj9AQ',1,'0928897777','jxhj6@yahoo.com'),(2000000063,'JUANT','h8vrN2VANrcJCM',1,'0948783229','juant@yahoo.com'),(2000000064,'bEtGDzwo25rn','IiqCuaKPwL0pJW',1,'0983597176','betgd@yahoo.com'),(2000000065,'Eeuu3RibnxaqwWC','fROlxLjfy9',1,'0906885860','eeuu3@yahoo.com'),(2000000066,'V82l6sRRUyDHDCWF','D3iEF8LcIgI',1,'0922423773','v82l6@yahoo.com'),(2000000067,'bq2x4s4gDnaTcpji','DekgyrFJI1kN2K',1,'0921394010','bq2x4@yahoo.com'),(2000000068,'9zr7QcCDS','fy7VTuC',1,'0987341592','9zr7q@yahoo.com'),(2000000069,'eFo5w8A49qf6mcr','UcEfbgbYmTNPXKZZ',1,'0965409687','efo5w@gmail.com'),(2000000070,'DqqdtN88Ciz','7LdljZl',1,'0944752254','dqqdt@yahoo.com'),(2000000071,'e1auCFXRoqKImu1','KBbh3DZ',1,'0914577968','e1auc@gmail.com'),(2000000072,'J5VU411ZEY3cj','w3FtSk352GwCD8YP',1,'0923181233','j5vu4@yahoo.com'),(2000000073,'bPLPr00nH','Kq2zXVSKRu2fky',1,'0933251770','bplpr@yahoo.com'),(2000000074,'Mo4bT','1m45Zo',1,'0949994386','mo4bt@gmail.com'),(2000000075,'rhH0js83F','miJc0',1,'0994637064','rhh0j@gmail.com'),(2000000076,'zWCzK6','Lj763',1,'0900895843','zwczk@yahoo.com'),(2000000077,'sWENGXH3va2D56','7CQjKWhBIOXs7EXR',1,'0928973705','sweng@yahoo.com'),(2000000078,'G9U6TxAu','N498xNvv',1,'0983630301','g9u6t@gmail.com'),(2000000079,'1xy3dwQ','6eGMmBVTGDh',1,'0900605067','1xy3d@yahoo.com'),(2000000080,'4F6uNzAJJLq','xDTPU73dp8V',1,'0996289066','4f6un@gmail.com'),(2000000081,'ikrP8Qjk0nx5OKjH','L9N768fZt5jw',1,'0948960220','ikrp8@yahoo.com'),(2000000082,'aAuEJpFFtbfQBcNk','E8HpX19Ljly',1,'0978076054','aauej@yahoo.com'),(2000000083,'JRBO3FXNP','hKMVndBrDM6',1,'0974787472','jrbo3@gmail.com'),(2000000084,'vR44m','y5TObL9NE',1,'0909889853','vr44m@yahoo.com'),(2000000085,'8Q3tWE','dGLM9',1,'0910370382','8q3tw@gmail.com'),(2000000086,'PgCssz','U0ZF3',1,'0941905774','pgcss@gmail.com'),(2000000087,'6AAuWYDJ','MaCNghAw7J0',1,'0953250032','6aauw@gmail.com'),(2000000088,'CIAllezg','NZzbmaih',1,'0943239351','ciall@gmail.com'),(2000000089,'Yns7BsPpwRQgTsM','28PJux7UT',1,'0977293336','yns7b@yahoo.com'),(2000000090,'xlhYeHKbt3AJuW','a5NxEnkYOb4eV',1,'0911128945','xlhye@yahoo.com'),(2000000091,'g5LUFKbgRC','lTJlfyK',1,'0911930795','g5luf@gmail.com'),(2000000092,'FXLcS6sFDm08oY4','apgRMC2slr8',1,'0988435234','fxlcs@yahoo.com'),(2000000093,'TrdK611Zk2','rLiPw4',1,'0968932186','trdk6@yahoo.com'),(2000000094,'IyuTicHx5Qhic2','2oF4exf',1,'0913991794','iyuti@yahoo.com'),(2000000095,'W5Pbv','NaIRsx',1,'0901304912','w5pbv@yahoo.com'),(2000000096,'C8uY3NFnPU','TTjv76H4vmVC4BC',1,'0967396295','c8uy3@yahoo.com'),(2000000097,'uAMewE8zzAenV','08WtAfcOzp',1,'0925366832','uamew@yahoo.com'),(2000000098,'J7zWG4G86','TuR9toL',1,'0998506824','j7zwg@yahoo.com'),(2000000099,'ScIump','FdeWcnMIjXMiue',1,'0990316209','scium@yahoo.com'),(2000000100,'gNbAMsz39asTK3','Z9ojjMZhKExR',1,'0907864964','gnbam@yahoo.com');
/*!40000 ALTER TABLE `owner_account` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-20  2:30:33
