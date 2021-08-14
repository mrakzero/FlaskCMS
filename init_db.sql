-- Init db
-- add default permiation data

INSERT INTO T_ROLE (code, name,description) VALUES ('administrator','管理员', '管理员拥有全部权限');
INSERT INTO T_ROLE (code, name,description) VALUES ('editor', '编辑','可以对文章、标签、分类、页面、友情链接、评论进行管理');
INSERT INTO T_ROLE (code, name,description) VALUES ('author', '作者', '所发表的文章无需管理员审核即可显示，还可以编辑已通过审核的文章，并且拥有媒体库的使用权限');
INSERT INTO T_ROLE (code, name,description) VALUES ('contributor', '投稿者', '可以发表或删除自己的文章，但所发文章需经管理员审核后才能在博客上显示');
INSERT INTO T_ROLE (code, name,description) VALUES ('subscriber', '订阅者', '只允许修改自己的个人资料，例如昵称、联系方式、密码等等');

INSERT INTO T_USER (username, nickname,password_hash,email,roleid,status) VALUES ('admin','管理员', 'bd92ff7cffc281d94e657b5dd707a7721e62124cd01537f0944a4e5329fcab57','admin@flaskcms.com',1,TRUE);

INSERT INTO T_CATEGORY(name,slug,parentid,description) VALUES ('未分类','default',null,'未分类')