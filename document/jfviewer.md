# log in jiufeng yingxiang zhongxin web site

nanchang: www.1yingxiang.com/dist/
aliyun: https://v2.jfhealthcare.cn/v2/rmis/dist/


[account]: zny 
[passwd]: 123
==========
## account: sy passwd: 123
lwx 1
----------

UID repeat err 
occured two different dcm file
20180511072721-342751

[label]:(http://47.100.41.69:8090/v2/rmis/dist/)

[tb-check-platform](http://47.100.43.165:8090/v2/rmis/dist/)
lwx, 1
jcys, 1 ====>>>> request platform

[jicenyiyuan](http://47.100.43.165:8090/v2/rmis/dist/)
[account]: jcys
[passwd]:1

[jf-tb-label](http://101.132.45.197:8685/v2/rmis/dist/#/)
[account]:lwx
[passwd]: 1

[mysql](rm-uf60965662rf7p9lwwo.mysql.rds.aliyuncs.com) 
# NOTE:(主实例，尽量不用)
[mysql](rr-uf649b219tyye23vkgo.mysql.rds.aliyuncs.com)
Port: 3306
account: rmis_ro
passwd: jf@12345
database: rmis_db
* connect database:$ mysql -urmis_ro -p -hrm-uf60965662rf7p9lwwo.mysql.rds.aliyuncs.com -P3306
* $ mysql -urmis_ro -p -h101.132.225.195
```mysql
select
	bci.REPORT_TIME,bci.check_num,bci.REFUSE_NAME,ri.IMG_PAGE,bci.APPLY_HOSP,bci.APPLY_DOC,bci.PARTS
from
	(
		select
      ACCESSION_NUM,
			REFUSE_NAME,
			check_num,
			REPORT_TIME,
			APPLY_HOSP,
	    APPLY_DOC,
      PARTS
		from
			busin_checklist_index
		where
			STATUS_CODE = '3555'
		and
			REFUSE_NAME is not null
		and REFUSE_NAME NOT REGEXP '测试'
	) bci LEFT JOIN rep_record rer on rer.ACCESSION_NUM = bci.accession_num
LEFT JOIN rep_image ri on ri.REP_UID = rer.REP_UID
where bci.REPORT_TIME > '2018-07-05 00:00:00'
```
