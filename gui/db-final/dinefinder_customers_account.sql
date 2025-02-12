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
-- Table structure for table `customers_account`
--

DROP TABLE IF EXISTS `customers_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers_account` (
  `customer_id` int unsigned NOT NULL,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `email_address` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_account`
--

LOCK TABLES `customers_account` WRITE;
/*!40000 ALTER TABLE `customers_account` DISABLE KEYS */;
INSERT INTO `customers_account` VALUES (123,'123','123','haha','test'),(1000000001,'a','a','eric','icpjj@yahoo.com'),(1000000002,'Uazkc8','i7auRSJoTMa3','Fxiyvrszjojuis','fxiyv@gmail.com'),(1000000003,'rmiIv6Lz','j1ChSzfe','Yksfbenq','yksfb@gmail.com'),(1000000004,'mppOWw6ux','6kKfscoPbahiqBWH','Ckryxqoaaiejiku','ckryx@yahoo.com'),(1000000005,'eoziNfQvyul','aST5SEzKH','Niiwvfqiskweya','niiwv@yahoo.com'),(1000000006,'UD9h5ZMvtOgiHZ','8UlTNhu01b8xKzq','Frbvkzowjb','frbvk@gmail.com'),(1000000007,'aBsuF7MY','5bY0K','Xqtxwdusang','xqtxw@yahoo.com'),(1000000008,'JDxODZ1p','wPGvVkMuHeF','Istroelmzk','istro@yahoo.com'),(1000000009,'VEp09H6G0nP0hxy','ibVHqHwVleCP','Pnbsyrskqmwxod','pnbsy@yahoo.com'),(1000000010,'uvyisX0PZ7H','bIgNFeCU','Lbinuhxlteevkftd','lbinu@gmail.com'),(1000000011,'drEofrTdsLEwdj8U','XTStxCGMG','Pvhncs','pvhnc@yahoo.com'),(1000000012,'fKHpmkFJrvn','gX6vrythGp','Khdzmzqfaqwsh','khdzm@gmail.com'),(1000000013,'HZ67W1FWP0L','isbsuELze','Rfxxzwq','rfxxz@yahoo.com'),(1000000014,'hGwJj','RP89h51j89jG','Gtaosie','gtaos@yahoo.com'),(1000000015,'WYvYltXTW','0w9M9','Jueblsxfmtghiwow','juebl@yahoo.com'),(1000000016,'VZA0Ds','X0FuFqmh','Rcbcjrsriwimwdjq','rcbcj@gmail.com'),(1000000017,'y8z9jwUA','usMJDZ0aO','Icqtkay','icqtk@yahoo.com'),(1000000018,'MjSCHbHOfD','3QmL1qgWSR','Ytwhilmz','ytwhi@yahoo.com'),(1000000019,'VIILHTrr7wQIs','v8bhd','Qbvfsmnrjlydquc','qbvfs@yahoo.com'),(1000000020,'ghDFrw2NCJVqTTS','eI6ksERHlAWIgNU','Kmkqukl','kmkqu@yahoo.com'),(1000000021,'0V96dvsRl26GxJ','KgJrg6C2z5YpgVOU','Xclwwfferqtoe','xclww@yahoo.com'),(1000000022,'x30supWUEG879','NpLBGtlhVz','Ubietfxxt','ubiet@yahoo.com'),(1000000023,'JPvZYNIqV0WrWfIz','PzKOyiGO','Msrpdwy','msrpd@gmail.com'),(1000000024,'g95uOtWVT','2Iomn9tnal','Zloimooympzktw','zloim@yahoo.com'),(1000000025,'WNlKeN','MvoBx','Toasppniqtrm','toasp@yahoo.com'),(1000000026,'hCoWj9tfiX','h97DTcIagWi','Xodusbzpfbr','xodus@gmail.com'),(1000000027,'b6bAUizSSk','rRt6J5trQkQHW','Fqhlqezaujehra','fqhlq@yahoo.com'),(1000000028,'fvmX2sAw2','mL78EIVdSyZ','Knzhn','knzhn@gmail.com'),(1000000029,'UOcrV7h8keow8','F1yJu','Tiougbosmrm','tioug@gmail.com'),(1000000030,'x77UX84iGuspEn','2ToH3s7WM','Ecacmtlkm','ecacm@yahoo.com'),(1000000031,'2Y1TtdB','X9FTrrFbT8nd','Dhbrdoazk','dhbrd@yahoo.com'),(1000000032,'ZhRa240yp2dB','UfJTkIwnG5Xz3','Oitdpbnkydta','oitdp@gmail.com'),(1000000033,'e6zY7IDca','I6KF6V2xANj','Rdwnqytckkx','rdwnq@gmail.com'),(1000000034,'Ia15AX','t2w0AxBSI','Ktrdiyxzimz','ktrdi@gmail.com'),(1000000035,'i95ALpWjGk7naR5w','KfaUGxdK7ehhuzAj','Ffghyeqabjntgc','ffghy@yahoo.com'),(1000000036,'HgaPamSlxmkTGK','OPdw27dLrRr2h','Gyievpxah','gyiev@gmail.com'),(1000000037,'Y7EoPtC7CRI1','X6wKv57KqO2bBvB','Ocfiij','ocfii@yahoo.com'),(1000000038,'fhYi8yJIgcsp','hDAMnfeloC1','Ijsslwpfnmyjuhc','ijssl@gmail.com'),(1000000039,'jNd8xTWt','LINQ8hDXk','Lqgbvtmkwycokhlm','lqgbv@yahoo.com'),(1000000040,'pzzcInb','xstHnmaNOBxMI','Ieriv','ieriv@gmail.com'),(1000000041,'2JMbevHdy6Otix','qeNzROvB2sWkpsK','Isclbtomfynizn','isclb@gmail.com'),(1000000042,'k1t0rB','AnJuCBI2gRa6tN','Gwmjhpchwhqenvye','gwmjh@gmail.com'),(1000000043,'zpvrhjxQ3H9UjA','l4YlnePbrBH5zU','Ygldmogdixb','ygldm@yahoo.com'),(1000000044,'WLlIGzj','gK14RHLRn','Lmfppdhvujubl','lmfpp@yahoo.com'),(1000000045,'WHq5vQYtWOyf','p2AXl','Kdtejqd','kdtej@yahoo.com'),(1000000046,'LaWkgaYQu7re','mGx8Q9YKuB','Atcainadngilwsed','atcai@gmail.com'),(1000000047,'gE6cRGwv','i5hLS6Xfk','Aimztr','aimzt@gmail.com'),(1000000048,'h3RiWgrwylIo','CqpqAxAP5k','Gqdskw','gqdsk@gmail.com'),(1000000049,'fzy1h5qAp0wWcaq','WIYq2DFL12p5l','Azgfbk','azgfb@yahoo.com'),(1000000050,'oMWaQXOd','HSDlo','Txxwjv','txxwj@yahoo.com'),(1000000051,'HHphDB7','jJKpD5PO','Vivvamzogedegn','vivva@gmail.com'),(1000000052,'PbwzT','LHANdF6vvxQ','Tvmqjesfwdqtx','tvmqj@yahoo.com'),(1000000053,'eYKb9evpiLtwBS','VDTU1','Rfbagbpfhqbblyp','rfbag@yahoo.com'),(1000000054,'gnfzy','lg7etruhcU','Vtixudntnzosh','vtixu@yahoo.com'),(1000000055,'uTPpCFJn0j0dqf','IzkaGadLOpKFFl','Mbniklk','mbnik@gmail.com'),(1000000056,'hbn9OKHctNGsLgH','3QoIpn3u','Wtxwkmrfifrxlcd','wtxwk@yahoo.com'),(1000000057,'TLf61SzS','P2IIpXUTHgd9wb','Gideot','gideo@yahoo.com'),(1000000058,'j04bA2JM1wLbo4','oLL2eteU7qh','Erbtmorg','erbtm@gmail.com'),(1000000059,'QVWliSTXbesoCF','orzKY8JTnb29Zn1X','Jetnnys','jetnn@yahoo.com'),(1000000060,'EPqEzIkHp7AYbrXx','NJr86q4bAmL','Xzbit','xzbit@gmail.com'),(1000000061,'17KRB2A','7Hlz1Rm3Hi4zr2ev','Uyvesgqwchugi','uyves@yahoo.com'),(1000000062,'GVrBrQIPRqZfk2','G4O2ydm3W','Pzmnuqft','pzmnu@gmail.com'),(1000000063,'kd7yrLPN2x7q42N','aM0EjcDF','Rcjfp','rcjfp@gmail.com'),(1000000064,'bAbf2oRLqlDc0r','PjJQRfn','Dgaojs','dgaoj@gmail.com'),(1000000065,'Ihw85','hnGp57QhDk','Mldjc','mldjc@gmail.com'),(1000000066,'HayuKyNDjVtPm','oe6RfA','Ilagloxl','ilagl@yahoo.com'),(1000000067,'z0rP2bTu','6KZHBnH19','Eejysmcisxculg','eejys@gmail.com'),(1000000068,'okqn0VWXeMc','7w7c3P8wwNkl','Eargbsfdx','eargb@yahoo.com'),(1000000069,'ds8SgDFY9Gf','c5hlbvaP0Y15QKe','Bixilhfofli','bixil@gmail.com'),(1000000070,'712kdNQWpsWDmNh','19ZARYSa','Oayqgobvltgwtlsh','oayqg@gmail.com'),(1000000071,'BMOfoCRH5tz','cH6mqeqpIXUD','Mspij','mspij@yahoo.com'),(1000000072,'CsNPcQ','Ow0gRO7WLfT','Mpmabtfucmildn','mpmab@gmail.com'),(1000000073,'ExBd7RjhQTpG','iFqHfD','Itcbyvtjsotamug','itcby@gmail.com'),(1000000074,'mLU1z','hZJJUU8Lt','Dbfpnlqwgkn','dbfpn@yahoo.com'),(1000000075,'fzYbHw','YgDRI','Nqoxaiaozhxkl','nqoxa@yahoo.com'),(1000000076,'sUa5vtzzak','mwSXO','Cchxikygv','cchxi@yahoo.com'),(1000000077,'K8CUR7','NYSc59UtpNTg1Nu','Ndfjalgw','ndfja@yahoo.com'),(1000000078,'zNSdtq','DzJDu8','Xelxds','xelxd@yahoo.com'),(1000000079,'AXDcmZRVwldAu8se','nkQ4Kc0I','Niqxru','niqxr@gmail.com'),(1000000080,'Oak6pUmU','jESfemXl','Smbkzjhng','smbkz@gmail.com'),(1000000081,'uuatCXR','jjSbrACgflxMAMA','Giqyoggelvijlvc','giqyo@yahoo.com'),(1000000082,'aLtfbSRiAubn4XB','qFKheFHVwI75','Ozpflatushtk','ozpfl@gmail.com'),(1000000083,'gxmI1sXCyCq3WHv','ILsiaE','Qddrclgjhmjieaga','qddrc@gmail.com'),(1000000084,'enDI6hJc','ggXymg21T6','Uycfwnhsebzkddpj','uycfw@gmail.com'),(1000000085,'6XzqY8sbWuXgDFz','ZoaCDTITr','Rsrmgahs','rsrmg@yahoo.com'),(1000000086,'asnYRev95KbNPRgb','ntxCeBA','Gdqasinjedwregg','gdqas@gmail.com'),(1000000087,'T2a7u5R0BB4kw','KeJsUQGojzpuKTm','Hkyxk','hkyxk@yahoo.com'),(1000000088,'qjS5xp','t9AjNiw','Eqqrodburdzekad','eqqro@yahoo.com'),(1000000089,'QpaXXOUtvRVR','JDIKvl45wd2','Irioajbjzfpdsliv','irioa@yahoo.com'),(1000000090,'QQRICyZF8wxEe5lj','mSTIi0zSPvv','Ozwxzhqsrgh','ozwxz@gmail.com'),(1000000091,'PnxAoWeXKKiTAYv','0ctXfn1qO4K9da','Banyxxy','banyx@yahoo.com'),(1000000092,'eiYScLnC9pCeT','YrfJur3E0rPyOwf','Tdjtjbzwenne','tdjtj@gmail.com'),(1000000093,'yrmy4NvaPAdr','U6eSkttgO1R','Tlgniqvqrgoab','tlgni@yahoo.com'),(1000000094,'3MO7wVUdG7PDhFle','EahxWo0zqlA','Pkacbehpwfdwvcwb','pkacb@yahoo.com'),(1000000095,'AozygW','5rQRFMN80','Yluwnjomcovwz','yluwn@gmail.com'),(1000000096,'Jd5avt','x8Qqueyee9hfWQpz','Znnmjpyk','znnmj@gmail.com'),(1000000097,'9gabGYHv0o6KgE1','VExOmJSY9','Zjshgwsyvgvxtm','zjshg@yahoo.com'),(1000000098,'cUoE6z','ejbTdbZGRZXFpizg','Oakaktpegxgxy','oakak@gmail.com'),(1000000099,'WOfQoin9r','htqS40MyYmE3','Fkwmykobmavuj','fkwmy@yahoo.com'),(1000000100,'MkGfQOUuT4r','Bo2SIdjHa','Nuxzdkwyyu','nuxzd@yahoo.com');
/*!40000 ALTER TABLE `customers_account` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-20  2:30:34
