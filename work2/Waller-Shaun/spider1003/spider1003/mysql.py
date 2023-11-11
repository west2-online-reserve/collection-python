import pymysql
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='040426',
    database='spider',
)

cursor = conn.cursor()
create_table_query = '''
drop table if exists `FZU_edu_jxtz`;

create table `FZU_edu_jxtz`(
	`project_id` int unsigned auto_increment comment '编号',
	`creator` varchar(50) not null comment '通知人',
	`title` varchar(500) not null comment '标题',
	`time` varchar(50) not null comment '时间',
	`link` Nvarchar(255) not null comment '详情链接',
	`annex_title` varchar(5000) default '' comment '附件名',
	`annex_link` varchar(5000) default '' comment '附件链接',
	`annex_download_times` varchar(5000) default '' comment '附件下载次数',
	primary key(`project_id`)
	) engine = innodb comment='西二Q1';
'''
conn.commit()
cursor.close()
conn.close()