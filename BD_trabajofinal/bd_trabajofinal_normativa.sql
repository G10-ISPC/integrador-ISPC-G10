-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: bd_trabajofinal
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `normativa`
--

DROP TABLE IF EXISTS `normativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `normativa` (
  `num_normativa` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `descripcion` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `organo_legislativo` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `palabra_clave` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_jurisdiccion` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_tipo_normativa` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_categoria` int DEFAULT NULL,
  PRIMARY KEY (`num_normativa`),
  KEY `normativa_ibfk_1` (`id_jurisdiccion`),
  KEY `normativa_ibfk_2` (`id_tipo_normativa`),
  KEY `normativa_ibfk_3` (`id_categoria`),
  CONSTRAINT `normativa_ibfk_1` FOREIGN KEY (`id_jurisdiccion`) REFERENCES `jurisdiccion` (`id_jurisdiccion`),
  CONSTRAINT `normativa_ibfk_2` FOREIGN KEY (`id_tipo_normativa`) REFERENCES `tipo_normativa` (`id_tipo_normativa`),
  CONSTRAINT `normativa_ibfk_3` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normativa`
--

LOCK TABLES `normativa` WRITE;
/*!40000 ALTER TABLE `normativa` DISABLE KEYS */;
INSERT INTO `normativa` VALUES (7642,'Ley de Ejercicio Profesional de la Informatica','Establece entre los profesionales de Ciencias Informáticas una comunidad de intereses e ideales éticos, normativos y profesionales.Cómo debe ser y a qué se considera ejercicio profesional.','2000-10-04','Legislatura de Córdoba','informaticos','2','1',1),(20744,'Ley de Contrato de Trabajo Nº 20.744','Es la norma legal que regula las relaciones laborales de los trabajadores que se encuentran bajo relación de dependencia. Determina derechos y obligaciones, establece condiciones de trabajo, entre otros aspectos.','1974-09-05','Congreso de la Nación','trabajador','1','1',1),(25326,'Ley de Proteccion de Datos','Contiene principios generales de protección de Datos, derechos, obligaciones de responsables y usuarios de Datos','2000-10-04','Congreso de la Nación','datos','1','1',2),(27555,'Ley de Teletrabajo','Regula los derechos y obligaciones de las partes cuando la relación laboral se desarrolla a distancia. Los derechos y obligaciones son las mismas que las personas que trabajan bajo la modalidad presencial.','2020-07-30','Congreso de la Nación','teletrabajo','1','1',1);
/*!40000 ALTER TABLE `normativa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-23 14:37:24
