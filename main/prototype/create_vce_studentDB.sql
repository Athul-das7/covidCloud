SET SQL_SAFE_UPDATES = 0;

DROP DATABASE IF EXISTS vce_db;
CREATE DATABASE vce_db;
USE vce_db;

create table student_list (
	roll_no varchar(15) primary key,
    student_name varchar(30) not null,
    branch varchar(5) not null,
    section char not null,
    img_path varchar(28) not null
);


INSERT INTO student_list(roll_no,student_name,branch,section,img_path) VALUE
("1602-19-735-001","KONKATI ABHISHEK","ECE","A","media/19/1.jpg"),
("1602-19-735-002","M ACHYUTHA SAI SHREE","ECE","A","media/19/2.jpg"),
("1602-19-735-003","BONU AKHILA","ECE","A","media/19/3.jpg"),
("1602-19-735-004","N ANAGHA","ECE","A","media/19/4.jpg"),
("1602-19-735-005","GANDU BHASKER","ECE","A","media/19/5.jpg"),
("1602-19-735-006","DIKSHA K","ECE","A","media/19/6.jpg"),
("1602-19-735-007","GURIJALA GURIJALA DINESH REDDY","ECE","A","media/19/7.jpg"),
("1602-19-735-008","M GANESH","ECE","A","media/19/8.jpg"),
("1602-19-735-009","GOPI UDAYA BHANU","ECE","A","media/19/9.jpg"),
("1602-19-735-010","GANTALA GOPINATH MONIESH","ECE","A","media/19/10.jpg"),
("1602-19-735-011","KUSUMA HARANATH JASWANTH","ECE","A","media/19/11.jpg"),
("1602-19-735-012","HARI PRIYA REDDY M.","ECE","A","media/19/12.jpg"),
("1602-19-735-013","YARLANKI HEMANTH","ECE","A","media/19/13.jpg"),
("1602-19-735-014","SADINENI HIMAJA","ECE","A","media/19/14.jpg"),
("1602-19-735-015","SUDI REDDY KEERTHI","ECE","A","media/19/15.jpg"),
("1602-19-735-016","KOLLI KETHAN","ECE","A","media/19/16.jpg"),
("1602-19-735-017","CHORAGUDI KRISHNA CHAITANYA","ECE","A","media/19/17.jpg"),
("1602-19-735-018","ANUMANDLA MANIDATTA","ECE","A","media/19/18.jpg"),
("1602-19-735-019","KORIKANA MANOHAR","ECE","A","media/19/19.png"),
("1602-19-735-020","CHIMMULA MANOJ KUMAR","ECE","A","media/19/20.jpg"),
("1602-19-735-021","KAKI MUKESH","ECE","A","media/19/21.jpg"),
("1602-19-735-022","CHILUWARI NAVEEN KUMAR","ECE","A","media/19/22.jpg"),
("1602-19-735-023","JUVERIA NISHATH","ECE","A","media/19/23.jpg"),
("1602-19-735-024","PAVAN KALYAN TADAKA","ECE","A","media/19/24.jpg"),
("1602-19-735-025","PRAKSHAL LOHADE","ECE","A","media/19/25.jpg"),
("1602-19-735-026","CILVERI PRANEETH KUMAR","ECE","A","media/19/26.jpg"),
("1602-19-735-027","KANCHARAKUNTLA PRATHIBHA","ECE","A","media/19/27.jpg"),
("1602-19-735-028","VALLAMKONDA RAHUL","ECE","A","media/19/28.jpg"),
("1602-19-735-029","DAMMANNAGARI RAJA SHEKAR REDDY","ECE","A","media/19/29.jpg"),
("1602-19-735-030","N RICHIKA REDDY","ECE","A","media/19/30.jpg"),
("1602-19-735-031","SUNCHU ROHITH VARMA","ECE","A","media/19/31.jpg"),
("1602-19-735-032","BUTTI RUPA SHREE","ECE","A","media/19/32.jpg"),
("1602-19-735-033","KATAKAM SAI CHARAN","ECE","A","media/19/33.jpg"),
("1602-19-735-034","P.E. SAI GANESH RAO","ECE","A","media/19/34.jpg"),
("1602-19-735-035","JONNALAGADDA SAI KRISHNA RAJU","ECE","A","media/19/35.jpg"),
("1602-19-735-036","MALYALA SAI SIDDESHWAR","ECE","A","media/19/36.jpg"),
("1602-19-735-037","CHANDA SAI SREEJA","ECE","A","media/19/37.jpg"),
("1602-19-735-038","GAJJELA SAMANTH GOUD","ECE","A","media/19/38.jpg"),
("1602-19-735-039","YADAVALLI SAMUEL II","ECE","A","media/19/39.jpg"),
("1602-19-735-040","MADHAVANENI SANNITH","ECE","A","media/19/40.jpg"),
("1602-19-735-041","BILLAKANTI SATHVIK RAO","ECE","A","media/19/41.jpg"),
("1602-19-735-042","SHAIK ARIF","ECE","A","media/19/42.jpg"),
("1602-19-735-043","MASNA SHIVA PRASAD","ECE","A","media/19/43.jpg"),
("1602-19-735-044","KOTTE SHIVA SAI","ECE","A","media/19/44.jpg"),
("1602-19-735-045","KAKKIRENI SHIVA TEJA","ECE","A","media/19/45.jpg"),
("1602-19-735-046","ANEMI SHRAVANI","ECE","A","media/19/46.jpg"),
("1602-19-735-047","MALOTHU SNEHA","ECE","A","media/19/47.jpg"),
("1602-19-735-048","TADAKANTI SREEJA","ECE","A","media/19/48.jpg"),
("1602-19-735-049","SRI KRISHNA KIRTHI","ECE","A","media/19/49.jpg"),
("1602-19-735-050","THEPPANI SRIKANTH","ECE","A","media/19/50.jpg"),
("1602-19-735-051","SAMA SRINIJA","ECE","A","media/19/51.jpg"),
("1602-19-735-052","TIRUVAIPATI SRIPAD","ECE","A","media/19/52.jpg"),
("1602-19-735-053","PATHA SRUJANA","ECE","A","media/19/53.jpg"),
("1602-19-735-054","V SUMANASREE LAKSHMI","ECE","A","media/19/54.jpg"),
("1602-19-735-055","KOPPULA SUSHRUTH","ECE","A","media/19/55.jpg"),
("1602-19-735-056","KOKKILIGADDA TANUJA","ECE","A","media/19/56.jpg"),
("1602-19-735-057","KARRI VAMSI","ECE","A","media/19/57.jpg"),
("1602-19-735-058","K VAMSI","ECE","A","media/19/58.jpg"),
("1602-19-735-059","NAGAM VENKATESH","ECE","A","media/19/59.jpg"),
("1602-19-735-060","MUTTANA VINAY KUMAR REDDY","ECE","A","media/19/60.jpg"),
("1602-19-735-061","NOMULA AARTHI SAI","ECE","B","media/19/61.jpg"),
("1602-19-735-062","JAJALA ABHINAV REDDY","ECE","B","media/19/62.jpg"),
("1602-19-735-063","GUNDETI ADI DEV","ECE","B","media/19/63.jpg"),
("1602-19-735-064","CHILUKURI ADITYA","ECE","B","media/19/64.jpg"),
("1602-19-735-065","AHMED SALAHUDDIN SUHAIB","ECE","B","media/19/65.jpg"),
("1602-19-735-066","ANUGU AKASH REDDY","ECE","B","media/19/66.jpg"),
("1602-19-735-067","MERUGU AMARNATH","ECE","B","media/19/67.jpg"),
("1602-19-735-068","PEDDI AMOKH","ECE","B","media/19/68.jpg"),
("1602-19-735-069","JALAGAM ARAVIND","ECE","B","media/19/69.jpg"),
("1602-19-735-070","SHEELAM ARUN KUMAR","ECE","B","media/19/70.jpg"),
("1602-19-735-071","KUMARANKANDATH ATHUL DAS","ECE","B","media/19/71.jpg"),
("1602-19-735-072","CHAKKA AVINASH","ECE","B","media/19/72.jpg"),
("1602-19-735-073","TULA DURGA PRASAD","ECE","B","media/19/73.jpg"),
("1602-19-735-074","ALLAMPALLY ESHWAR","ECE","B","media/19/74.jpg"),
("1602-19-735-075","CHINNAM GEETHIKA","ECE","B","media/19/75.jpg"),
("1602-19-735-076","REDAPANGU GRACE","ECE","B","media/19/76.jpg"),
("1602-19-735-077","ROLLA HYNDAVI","ECE","B","media/19/77.jpg"),
("1602-19-735-078","METTARI JASHWANTH","ECE","B","media/19/78.jpg"),
("1602-19-735-079","KRISHNA SRIYA EMANI","ECE","B","media/19/79.jpg"),
("1602-19-735-080","KANURI KANURI KRISHNA VYAS","ECE","B","media/19/80.jpg"),
("1602-19-735-081","P LAKSHMI NARAYANA","ECE","B","media/19/81.jpg"),
("1602-19-735-082","SATHINENI LAXMA REDDY","ECE","B","media/19/82.jpg"),
("1602-19-735-083","POTHULA MAHALAXMEE","ECE","B","media/19/83.jpg"),
("1602-19-735-084","MERUVA MANIKANTA MANOJ","ECE","B","media/19/84.jpg"),
("1602-19-735-085","THUMULA MANISH RAO","ECE","B","media/19/85.jpg"),
("1602-19-735-086","BATHINI MEGHANA","ECE","B","media/19/86.jpg"),
("1602-19-735-087","MIHIR DESHPANDE","ECE","B","media/19/87.jpg"),
("1602-19-735-088","MOHAMMAD ABDUL AZEEZ","ECE","B","media/19/88.jpg"),
("1602-19-735-089","MOHAMMAD AMEER SOHAIL","ECE","B","media/19/89.jpg"),
("1602-19-735-090","MOHD SHOEB AQTAR","ECE","B","media/19/90.jpg"),
("1602-19-735-091","SEELAM MOUNIKA","ECE","B","media/19/91.jpg"),
("1602-19-735-092","KATASANI NAVYA SREE","ECE","B","media/19/92.jpg"),
("1602-19-735-093","PALSA NISHANK NISHANK PALSA","ECE","B","media/19/93.jpg"),
("1602-19-735-094","MANDA NITHIN MANDA NITHIN","ECE","B","media/19/94.jpg"),
("1602-19-735-095","PRAJA SAMATHA JADE","ECE","B","media/19/95.jpg"),
("1602-19-735-096","PRIYANKA DARSHANAM","ECE","B","media/19/96.jpg"),
("1602-19-735-097","MALLEMPATI RAJESH","ECE","B","media/19/97.jpg"),
("1602-19-735-098","CHEEPU RISHITHA","ECE","B","media/19/98.jpg"),
("1602-19-735-099","PONNURU SAHITHYA DEVI","ECE","B","media/19/99.jpg"),
("1602-19-735-100","RACHAKONDA SAI KIRAN","ECE","B","media/19/100.jpg"),
("1602-19-735-101","B SAI PRABHAT","ECE","B","media/19/101.jpg"),
("1602-19-735-102","SANDHYA PODILA","ECE","B","media/19/102.jpg"),
("1602-19-735-103","ODDAMAAN SANKEERTAN","ECE","B","media/19/103.jpg"),
("1602-19-735-104","GOURISHETTY SATHWIK","ECE","B","media/19/104.jpg"),
("1602-19-735-105","AKULA SATHWIKA","ECE","B","media/19/105.jpg"),
("1602-19-735-106","RAMIREDDY SATYA SAITEJA","ECE","B","media/19/106.jpg"),
("1602-19-735-107","BALDA SHAINY","ECE","B","media/19/107.jpg"),
("1602-19-735-108","SATLA SHASHANK","ECE","B","media/19/108.jpg"),
("1602-19-735-109","SHASHI TEJA GALI","ECE","B","media/19/109.jpg"),
("1602-19-735-110","SHIVA HEMANTH NAIK DEVAVAT","ECE","B","media/19/110.jpg"),
("1602-19-735-111","LEKKALA SHRAVAN KUMAR","ECE","B","media/19/111.jpg"),
("1602-19-735-112","RAMASANI SOWMITH","ECE","B","media/19/112.jpg"),
("1602-19-735-113","VAZIR SREEJA","ECE","B","media/19/113.jpg"),
("1602-19-735-114","NUKALA SRI VAISHNAVI KIRAN","ECE","B","media/19/114.jpg"),
("1602-19-735-115","SWARGAM SRIKAR","ECE","B","media/19/115.jpg"),
("1602-19-735-116","SRIVIDYA BATTULA","ECE","B","media/19/116.jpg"),
("1602-19-735-117","BOLISETTI SUSHANTH","ECE","B","media/19/117.jpg"),
("1602-19-735-118","GOSHAMAHAL UDAY KIRAN","ECE","B","media/19/118.jpg"),
("1602-19-735-119","NAKOD VENKATESH","ECE","B","media/19/119.jpg"),
("1602-19-735-120","CHAPPIDI VYSHNAVI","ECE","B","media/19/120.jpg"),
("1602-19-735-121","P ABHIGNA ","ECE","C","media/19/121.jpg"),
("1602-19-735-122","CHERUPALLI ADARSH","ECE","C","media/19/122.jpg"),
("1602-19-735-123","RAICHUR AKSHAYA","ECE","C","media/19/123.jpg"),
("1602-19-735-124","A ANUSH","ECE","C","media/19/124.jpg"),
("1602-19-735-125","BUSSA ANUSHA ANUSHA BUSSA","ECE","C","media/19/125.jpg"),
("1602-19-735-126","BACHHALI BHAVANI SUPRIYA ","ECE","C","media/19/126.jpg"),
("1602-19-735-127","KATEMONI CHARAN","ECE","C","media/19/127.jpg"),
("1602-19-735-128","KARAP CHETAN DAS","ECE","C","media/19/128.jpg"),
("1602-19-735-129","KUPPIREDDY DEEPAK REDDY","ECE","C","media/19/129.jpg"),
("1602-19-735-130","YAGANTI DINESH KUMAR REDDY","ECE","C","media/19/130.jpg"),
("1602-19-735-131","GREESHMANTH VARMA K","ECE","C","media/19/131.jpg"),
("1602-19-735-132","PRADYUMNA HARIKEERTHI","ECE","C","media/19/132.jpg"),
("1602-19-735-133","PABBA HARSHITH","ECE","C","media/19/133.jpg"),
("1602-19-735-134","PALLE HARSHITHA","ECE","C","media/19/134.jpg"),
("1602-19-735-135","DORNALA HEMACHARAN","ECE","C","media/19/135.jpg"),
("1602-19-735-136","GORRE JUGAL","ECE","C","media/19/136.jpg"),
("1602-19-735-137","SRI VENKATA SAI","ECE","C","media/19/137.jpg"),
("1602-19-735-138","KOWTHALAM LOKVIKAS","ECE","C","media/19/138.jpg"),
("1602-19-735-139","KADAM MAHESH","ECE","C","media/19/139.jpg"),
("1602-19-735-140","P MOHAMMAD REALA","ECE","C","media/19/140.jpg"),
("1602-19-735-141","MOHAMMED FEROZ","ECE","C","media/19/141.jpg"),
("1602-19-735-142","B NAGA SAI YASHWANTH","ECE","C","media/19/142.jpg"),
("1602-19-735-143","LUNAVATH NAVINDER","ECE","C","media/19/143.jpg"),
("1602-19-735-144","ARTHAM NAVYA","ECE","C","media/19/144.jpg"),
("1602-19-735-145","KODIMALA NAVYA","ECE","C","media/19/145.jpg"),
("1602-19-735-146","RAGIR NIKHIL YADAV","ECE","C","media/19/146.jpg"),
("1602-19-735-147","VADLA PAVAN CHARY","ECE","C","media/19/147.jpg"),
("1602-19-735-148","MYAKALA PRAMOD REDDY","ECE","C","media/19/148.jpg"),
("1602-19-735-149","KUMMARI PRANI SAHITH","ECE","C","media/19/149.jpg"),
("1602-19-735-150","POTHANA RAHUL","ECE","C","media/19/150.jpg"),
("1602-19-735-151","BETHI RISHI KUMAR","ECE","C","media/19/151.jpg"),
("1602-19-735-152","KOTHA RISHIKESH REDDY","ECE","C","media/19/152.jpg"),
("1602-19-735-153","GUNDA SAI AAKANKSHA","ECE","C","media/19/153.jpg"),
("1602-19-735-154","TEJAVATH SAI BALAJI","ECE","C","media/19/154.jpg"),
("1602-19-735-155","PECHANNAGARI SAI JYOTHI","ECE","C","media/19/155.jpg"),
("1602-19-735-156","KONDA SAI MADHAV","ECE","C","media/19/156.jpg"),
("1602-19-735-157","ADIKE SAI PRATHYUSH","ECE","C","media/19/157.jpg"),
("1602-19-735-158","CH SAI VAMSHI","ECE","C","media/19/158.jpg"),
("1602-19-735-159","GADDAM SAKETH REDDY","ECE","C","media/19/159.jpg"),
("1602-19-735-160","NENAVATH SANGEETHA","ECE","C","media/19/160.jpg"),
("1602-19-735-161","SHAIK NAFISA KOWSAR","ECE","C","media/19/161.jpg"),
("1602-19-735-162","NALLA SREEJA","ECE","C","media/19/162.jpg"),
("1602-19-735-163","V.SRI LEKHA ","ECE","C","media/19/163.jpg"),
("1602-19-735-164","CHENCHALA SRIHITHA","ECE","C","media/19/164.jpg"),
("1602-19-735-165","N SRIVIMALA VAISHNAVI","ECE","C","media/19/165.jpg"),
("1602-19-735-166","SASI KOUSHIK","ECE","C","media/19/166.jpg"),
("1602-19-735-167","GOVADA SURESH NITIN","ECE","C","media/19/167.jpg"),
("1602-19-735-168","BALIJA SUSHANTH","ECE","C","media/19/168.jpg"),
("1602-19-735-169","M TEJAVARDHAN REDDY","ECE","C","media/19/169.jpg"),
("1602-19-735-170","B THARUNKUMAR","ECE","C","media/19/170.jpg"),
("1602-19-735-171","VAISHNAVI KAGITA","ECE","C","media/19/171.jpg"),
("1602-19-735-172","VAMSHI CH","ECE","C","media/19/172.jpg"),
("1602-19-735-173","SRAVYA DEEPIKA","ECE","C","media/19/173.jpg"),
("1602-19-735-174","RANGA VIJAY GOWTHAM","ECE","C","media/19/174.jpg"),
("1602-19-735-175","NALLA VIJAY","ECE","C","media/19/175.jpg"),
("1602-19-735-176","MOLATOTI VIJAYA VIPIN","ECE","C","media/19/176.jpg"),
("1602-19-735-177","ITIKELA VINEESHA","ECE","C","media/19/177.jpg"),
("1602-19-735-178","PATLOLLA VINEETH REDDY","ECE","C","media/19/178.jpg"),
("1602-19-735-179","CHIRUVOLU VISHNU TEJA","ECE","C","media/19/179.jpg"),
("1602-19-735-180","NAGA VISHWANATH","ECE","C","media/19/180.jpg"),
("1602-18-735-001","BAJJURI.ACHUTA GOPI KRISHNA","ECE","A","media/18/1.jpg"),
("1602-18-735-002","P.AISHWARYA","ECE","A","media/18/2.jpg"),
("1602-18-735-003","ANNARAM.AKANKSHA","ECE","A","media/18/3.jpg"),
("1602-18-735-004","AKASH.PUJARI","ECE","A","media/18/4.jpg"),
("1602-18-735-005","MEDISHETTY.AKHILKUMAR","ECE","A","media/18/5.jpg"),
("1602-18-735-006","BANDI.ANUDEEP","ECE","A","media/18/6.jpg"),
("1602-18-735-007","ASMITA.D","ECE","A","media/18/7.jpg"),
("1602-18-735-008","MADAGONI.BHARADWAJ","ECE","A","media/18/8.jpg"),
("1602-18-735-009","B BHUVANA.CHANDRIKA","ECE","A","media/18/9.jpg"),
("1602-18-735-010","GANDAM.CHANDU","ECE","A","media/18/10.jpg"),
("1602-18-735-011","MEDURI.CHARAN","ECE","A","media/18/11.jpg"),
("1602-18-735-012","GANGAM.DINESH REDDY","ECE","A","media/18/12.jpg"),
("1602-18-735-013","RAJPUT.HANUMANTH SINGH","ECE","A","media/18/13.jpg"),
("1602-18-735-014","R.HARI KRISHNA","ECE","A","media/18/14.jpg"),
("1602-18-735-015","MODALA.HARIKRISHNA","ECE","A","media/18/15.jpg"),
("1602-18-735-016","LINGALA.HARSHA VARDHAN REDDY","ECE","A","media/18/16.jpg"),
("1602-18-735-017","HARSHITHA.CHALLA","ECE","A","media/18/17.jpg"),
("1602-18-735-018","YEDDULA.HARSHITHA","ECE","A","media/18/18.jpg"),
("1602-18-735-019","BOJJANNAGARI.JEEVAN REDDY","ECE","A","media/18/19.jpg"),
("1602-18-735-020","KEERTHANA.PUTTA","ECE","A","media/18/20.jpg"),
("1602-18-735-021","BHEEMI REDDY.LOHITH REDDY","ECE","A","media/18/21.jpg"),
("1602-18-735-022","G S V.MANEESH","ECE","A","media/18/22.jpg"),
("1602-18-735-023","KANDULA.MANOJ","ECE","A","media/18/23.jpg"),
("1602-18-735-024","ESLAVATH.MOHITH","ECE","A","media/18/24.jpg"),
("1602-18-735-025","NAGA SAI.TEJESH AVADANAM","ECE","A","media/18/25.jpg"),
("1602-18-735-026","BANDARU.POOJITHA","ECE","A","media/18/26.jpg"),
("1602-18-735-027","GOLLAPUDI.PRAVALIKA","ECE","A","media/18/27.jpg"),
("1602-18-735-028","GUDIKANDULA.PRIYANKA","ECE","A","media/18/28.jpg"),
("1602-18-735-029","ORUGANTI.RAHUL REDDY","ECE","A","media/18/29.jpg"),
("1602-18-735-030","M.RAKESH REDDY","ECE","A","media/18/30.jpg"),
("1602-18-735-031","LINGALA.ROHIT","ECE","A","media/18/31.jpg"),
("1602-18-735-032","THAKKALLAPALLY.SAI ABHINAV","ECE","A","media/18/32.jpg"),
("1602-18-735-033","BHONAGIRI.SAI DINESH","ECE","A","media/18/33.jpg"),
("1602-18-735-034","BRAHMADEVARA.SAI SHANMUK","ECE","A","media/18/34.jpg"),
("1602-18-735-035","ARUTLA.SAMARA SIMHA REDDY","ECE","A","media/18/35.jpg"),
("1602-18-735-036","G.SATHVIKA","ECE","A","media/18/36.jpg"),
("1602-18-735-037","THUMMALAPALLI.SATHWIKA","ECE","A","media/18/37.jpg"),
("1602-18-735-038","SATYA SIVA PAVAN KUMAR.KOTIPALLI","ECE","A","media/18/38.jpg"),
("1602-18-735-039","SHAIK.ARSHIYA ROOFI","ECE","A","media/18/39.jpg"),
("1602-18-735-040","ARAVAPALLI.SHANMUKHA NAADH","ECE","A","media/18/40.jpg"),
("1602-18-735-041","AJMEERA.SHEKAR","ECE","A","media/18/41.jpg"),
("1602-18-735-042","SHIVVA.REVANTH","ECE","A","media/18/42.jpg"),
("1602-18-735-043","BAROOR.SHRESHTA REDDY","ECE","A","media/18/43.jpg"),
("1602-18-735-044","AKARAPU.SIDDHARTHA","ECE","A","media/18/44.jpg"),
("1602-18-735-045","EMMIDI.SOWMYA","ECE","A","media/18/45.jpg"),
("1602-18-735-046","REGATTI.SPANDANA","ECE","A","media/18/46.jpg"),
("1602-18-735-047","PRODDATOORI.SRAVANTHI","ECE","A","media/18/47.jpg"),
("1602-18-735-048","A S R S.SRI HARSHA","ECE","A","media/18/48.jpg"),
("1602-18-735-049","PULLURU.SUMANTH","ECE","A","media/18/49.jpg"),
("1602-18-735-050","SUMAYA.SULTANA","ECE","A","media/18/50.jpg"),
("1602-18-735-051","SUMEK.AGARWAL","ECE","A","media/18/51.jpg"),
("1602-18-735-052","SYED.ADIL FYJAAN","ECE","A","media/18/52.jpg"),
("1602-18-735-053","PANUGANTI.TEJ KUMAR","ECE","A","media/18/53.jpg"),
("1602-18-735-054","YARAMADA.TEJASWI","ECE","A","media/18/54.jpg"),
("1602-18-735-055","BODA.THANUJ SAI","ECE","A","media/18/55.jpg"),
("1602-18-735-056","CHINTI REDDY.VARSHA","ECE","A","media/18/56.jpg"),
("1602-18-735-057","LANKA.VENKATA SUBHASH JAHNAV","ECE","A","media/18/57.jpg"),
("1602-18-735-058","PANDIRI.VISHISTA REDDY","ECE","A","media/18/58.jpg"),
("1602-18-735-059","MADDURI.VISHNU KAUSHIK","ECE","A","media/18/59.jpg"),
("1602-18-735-060","PALLIKONDA.VISHNU VARDHAN","ECE","A","media/18/60.jpg"),
("1602-18-735-061","GIRKALA.AISHWARYA","ECE","B","media/18/61.jpg"),
("1602-18-735-062","CHITTURI.AKHILA","ECE","B","media/18/62.jpg"),
("1602-18-735-063","THOTA.ALEKHYA","ECE","B","media/18/63.jpg"),
("1602-18-735-064","NAGIREDDYPALLI.AMRUTHREDDY","ECE","B","media/18/64.jpg"),
("1602-18-735-065","BHOGISETTI.ANISH SAI VARDHAN","ECE","B","media/18/65.jpg"),
("1602-18-735-066","PITTA.ASHIKA SHARON","ECE","B","media/18/66.jpg"),
("1602-18-735-067","KOTHA.ASHRITH","ECE","B","media/18/67.jpg"),
("1602-18-735-068","PASPULA.BHARATH KUMAR","ECE","B","media/18/68.jpg"),
("1602-18-735-069","KACHAM.CHAKRADHAR","ECE","B","media/18/69.jpg"),
("1602-18-735-070","MORAMPUDI.DHARANI","ECE","B","media/18/70.jpg"),
("1602-18-735-071","AVULA.HEMAVENKATA SAINATH","ECE","B","media/18/71.jpg"),
("1602-18-735-072","N.JAYA PRAKASH","ECE","B","media/18/72.jpg"),
("1602-18-735-073","KALAVENA.KARTHIK","ECE","B","media/18/73.jpg"),
("1602-18-735-074","PAKKIR.KEERTHIKA REDDY","ECE","B","media/18/74.jpg"),
("1602-18-735-075","KONDETI.KHYATHI","ECE","B","media/18/75.jpg"),
("1602-18-735-076","CHENCHALA.LAASYA","ECE","B","media/18/76.jpg"),
("1602-18-735-077","DUBASI.LAKSHMI SINDHURA","ECE","B","media/18/77.jpg"),
("1602-18-735-078","KARKADA.MAHALAKSHMI","ECE","B","media/18/78.jpg"),
("1602-18-735-079","PALURU.MANIKANTA","ECE","B","media/18/79.jpg"),
("1602-18-735-080",".NAZEEMA","ECE","B","media/18/80.jpg"),
("1602-18-735-081","CHERYALA.NEERAJ KUMAR","ECE","B","media/18/81.jpg"),
("1602-18-735-082","THALLA.NIKHIL KUMAR","ECE","B","media/18/82.jpg"),
("1602-18-735-083","MADAVANENI.NIKHIL","ECE","B","media/18/83.jpg"),
("1602-18-735-084","VELMA.PRABHAS REDDY","ECE","B","media/18/84.jpg"),
("1602-18-735-085","JUPAKA.PRABHATH","ECE","B","media/18/85.jpg"),
("1602-18-735-086","ANCHURI.PRANEETH","ECE","B","media/18/86.jpg"),
("1602-18-735-087","PRASHANTH.KEMSARAM","ECE","B","media/18/87.jpg"),
("1602-18-735-088","PRATHIMA.CHEEDELLA","ECE","B","media/18/88.jpg"),
("1602-18-735-089","CHINNA.PRAVALIKA","ECE","B","media/18/89.jpg"),
("1602-18-735-090","JILLALA.PRUDHVI RANJAN REDDY","ECE","B","media/18/90.jpg"),
("1602-18-735-091","PANYALA.ROHITH REDDY","ECE","B","media/18/91.jpg"),
("1602-18-735-092","SAHAJA.PULIGADDA","ECE","B","media/18/92.jpg"),
("1602-18-735-093","KATUKAM.SAI AKHIL","ECE","B","media/18/93.jpg"),
("1602-18-735-094","PALVAI.SAI CHARAN","ECE","B","media/18/94.jpg"),
("1602-18-735-095","C.SAI KISHORE REDDY","ECE","B","media/18/95.jpg"),
("1602-18-735-096","C.SAI SUJITH REDDY","ECE","B","media/18/96.jpg"),
("1602-18-735-097","ADDALA.SAI TEJA","ECE","B","media/18/97.jpg"),
("1602-18-735-098","JAGARAPU.SAIVAMSHI","ECE","B","media/18/98.jpg"),
("1602-18-735-099","PONNURU.SAI VINUTHNA","ECE","B","media/18/99.jpg"),
("1602-18-735-100","KOTHA.SAIVRUN","ECE","B","media/18/100.jpg"),
("1602-18-735-101","ALLISETTY.SHIRISHA","ECE","B","media/18/101.jpg"),
("1602-18-735-102","VADALI DGNANA.SHIVA SAI CHAITANYA","ECE","B","media/18/102.jpg"),
("1602-18-735-103","SHYAMALA.MARLAPUDI","ECE","B","media/18/103.jpg"),
("1602-18-735-104","JENNELA.SRAVYA SRI","ECE","B","media/18/104.jpg"),
("1602-18-735-105","GOLLA.SRI NEHA","ECE","B","media/18/105.jpg"),
("1602-18-735-106","PANYALA.SRILEKHA","ECE","B","media/18/106.jpg"),
("1602-18-735-107","PANNATI.SUCHITH","ECE","B","media/18/107.jpg"),
("1602-18-735-108","BOORLA.SUNANDA","ECE","B","media/18/108.jpg"),
("1602-18-735-109","ADUSUMALLI.SUPRAJA","ECE","B","media/18/109.jpg"),
("1602-18-735-110","MANNAVA.SUPRAJA","ECE","B","media/18/110.jpg"),
("1602-18-735-111","DHARAVATH.SUSHEEL NAIK","ECE","B","media/18/111.jpg"),
("1602-18-735-112","TATINENI.SWETHA SRI SAI","ECE","B","media/18/112.jpg"),
("1602-18-735-113","CHINTA.TEJA SAI","ECE","B","media/18/113.jpg"),
("1602-18-735-114","DODLA.THARUN REDDY","ECE","B","media/18/114.jpg"),
("1602-18-735-115","AWARU.VAMSHI SAI","ECE","B","media/18/115.jpg"),
("1602-18-735-116","MODELA.VARUN","ECE","B","media/18/116.jpg"),
("1602-18-735-117","JAJULA.VENKATA SAI AVINASH","ECE","B","media/18/117.jpg"),
("1602-18-735-118","SINGAM.VENKATA SAI SIDDARTHA","ECE","B","media/18/118.jpg"),
("1602-18-735-119","AVULA.VIKRAMADITHYA","ECE","B","media/18/119.jpg"),
("1602-18-735-120","SAMUGARI.VISHNU PRIYA","ECE","B","media/18/120.jpg"),
("1602-18-735-302","ANKURU. SAI TEJA","ECE","C","media/18/302.jpg"),
("1602-18-735-304","NAGARJUNAKONDA. BHARGAVI","ECE","C","media/18/304.jpg"),
("1602-18-735-309","AHSAN SHADAB. PATEL","ECE","C","media/18/309.jpg"),
("1602-18-735-312","KATHA. MUKESH","ECE","C","media/18/312.jpg"),
("1602-18-735-315","SRIPADI. SRIMANTH","ECE","C","media/18/315.jpg"),
("1602-18-735-318","GANGARAPU. KARTHIK","ECE","C","media/18/318.jpg");
