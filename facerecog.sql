select * from facerecog.student;
drop table facerecog.student;

create table `facerecog`.`student` (
	`Dep` varchar(45) null,
    `course` varchar(45) null,
    `Year` varchar(45) null,
    `Semester` varchar(45) null,
    `Student_id` varchar(45) null,
    `Name` varchar(45) null,
	`Division` varchar(45) null,
	`Roll` varchar(45) null,
    `Gender` varchar(45) null,
    `Dob` varchar(45) null,
    `Email` varchar(45) null,
    `Phone` varchar(45) null,
	`Address` varchar(45) null,
	`Teacher` varchar(45) null,
	`PhotoSample` varchar(45) null,
    Primary Key (`Student_id`)
);
select * from student;

