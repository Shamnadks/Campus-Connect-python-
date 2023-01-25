/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `project`;

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(10) NOT NULL AUTO_INCREMENT,
  `department_id` int(10) DEFAULT NULL,
  `course` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`department_id`,`course`) values (2,1,'bsc cs');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `department_id` int(10) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`department_id`,`department_name`) values (1,'Computer Science'),(2,'Computer Application'),(3,'commerce'),(4,'bba'),(6,'mca');

/*Table structure for table `doubts_and_reply` */

DROP TABLE IF EXISTS `doubts_and_reply`;

CREATE TABLE `doubts_and_reply` (
  `doubt_id` int(5) NOT NULL AUTO_INCREMENT,
  `doubt` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `d_date` varchar(10) DEFAULT NULL,
  `r_date` varchar(10) DEFAULT NULL,
  `user_id` int(5) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`doubt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `doubts_and_reply` */

insert  into `doubts_and_reply`(`doubt_id`,`doubt`,`reply`,`d_date`,`r_date`,`user_id`,`staff_id`) values (1,'sssss','sdfvdv','2022/02/02','2022-03-03',1,5);

/*Table structure for table `focus_area` */

DROP TABLE IF EXISTS `focus_area`;

CREATE TABLE `focus_area` (
  `focus_id` int(11) NOT NULL AUTO_INCREMENT,
  `fsuballoc_id` int(11) DEFAULT NULL,
  `syllabus` varchar(500) DEFAULT NULL,
  `note` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`focus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `focus_area` */

insert  into `focus_area`(`focus_id`,`fsuballoc_id`,`syllabus`,`note`) values (1,2,'edfxfxde','/static/focus_area/220303-000748.pdf');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `u_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`u_type`) values (1,'admin','admin','admin'),(2,'anu@gmail.com','544','staff'),(3,'anoop@gmail.com','300','staff'),(4,'sr@gmail.com','584','staff'),(5,'an@gmail.com','156','staff'),(6,'gfh','989','user'),(8,'moni@gmail.com','775','staff'),(9,'ai@gmail.com','877','staff');

/*Table structure for table `note` */

DROP TABLE IF EXISTS `note`;

CREATE TABLE `note` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) DEFAULT NULL,
  `note` varchar(1000) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `note` */

insert  into `note`(`note_id`,`subject_id`,`note`,`date`) values (1,4,'/static/notes/220302-233004.pdf','2022-03-02'),(2,2,'kjhbvvh ','0000-00-00');

/*Table structure for table `previous_questions` */

DROP TABLE IF EXISTS `previous_questions`;

CREATE TABLE `previous_questions` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) DEFAULT NULL,
  `question_paper` varchar(100) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `previous_questions` */

insert  into `previous_questions`(`question_id`,`year`,`question_paper`,`subject_id`) values (1,2015,'asdfytgh',1),(2,2014,'/static/pq/220303-101058.pdf',4);

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(5) NOT NULL AUTO_INCREMENT,
  `staff_id` int(5) DEFAULT NULL,
  `user_id` int(5) DEFAULT NULL,
  `rating` int(5) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`staff_id`,`user_id`,`rating`,`date`) values (1,5,1,4,'2022-02-28');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(10) DEFAULT NULL,
  `staff_name` varchar(25) DEFAULT NULL,
  `phone_no` int(11) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `email_id` varchar(40) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `adhaar_no` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`staff_name`,`phone_no`,`profile_pic`,`email_id`,`qualification`,`adhaar_no`) values (8,'monisha',786896,'/static/photo/220307-210814.jpg','moni@gmail.com','mca',54678),(9,'ainisha',76548989,'/static/photo/220307-213208.jpg','ai@gmail.com','mba',78787);

/*Table structure for table `suballoc` */

DROP TABLE IF EXISTS `suballoc`;

CREATE TABLE `suballoc` (
  `suballoc_id` int(5) NOT NULL AUTO_INCREMENT,
  `subject_id` int(5) DEFAULT NULL,
  `staff_id` int(5) DEFAULT NULL,
  PRIMARY KEY (`suballoc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `suballoc` */

insert  into `suballoc`(`suballoc_id`,`subject_id`,`staff_id`) values (1,0,0),(2,4,5),(3,4,4),(4,4,9);

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `semester` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`subject`,`course_id`,`semester`) values (1,'ejp',0,'5'),(2,'com',3,'5'),(3,'linux',0,'4'),(4,'ENGLISH',2,'1'),(6,'data mining',2,'SEM 4');

/*Table structure for table `suggestion` */

DROP TABLE IF EXISTS `suggestion`;

CREATE TABLE `suggestion` (
  `suggestion_id` int(100) NOT NULL,
  `suggestion` varchar(100) DEFAULT NULL,
  `user_id` int(5) DEFAULT NULL,
  PRIMARY KEY (`suggestion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `suggestion` */

insert  into `suggestion`(`suggestion_id`,`suggestion`,`user_id`) values (1,'voice',1);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(15) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `adhar_number` int(16) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `email_id` varchar(30) DEFAULT NULL,
  `phone_no` int(12) DEFAULT NULL,
  `course` varchar(20) DEFAULT NULL,
  `batch` varchar(10) DEFAULT NULL,
  `institution` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`username`,`adhar_number`,`profile_pic`,`email_id`,`phone_no`,`course`,`batch`,`institution`) values (1,'abc',845120,'mnb','abc@gmail.com',665,'sdfgh','Szdsffg','dfgg');

/*Table structure for table `video` */

DROP TABLE IF EXISTS `video`;

CREATE TABLE `video` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `vsuballoc_id` int(11) DEFAULT NULL,
  `video` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `video` */

insert  into `video`(`video_id`,`vsuballoc_id`,`video`,`date`) values (1,2,'/static/video/220303-093527.mp4','2022-03-03');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
