# Udacity Log Analysis Project In Full Stack Course

This is the one of the fullstack project in udacity

By Doing this project i learned how to print particular data from the database using python(2.7)
and also postgreswl

##Step 1: The Installation of required files
1.Vagrant:---->https://www.vagrantup.com/ 
2.VirtualBox:--->https://www.virtualbox.org/ <br>
3.Download the file from github(this is the vm repository of fullstack):-->
https://github.com/udacity/fullstack-nanodegree-vm</br>
4.And Yayy!! We got a file called newsdata.sql into vagrant directory</br>

##Step 2:Running 
1.We have to change our directory to vagrant<br>
2.**commands**
    **vagrant up** -->run the vagrant <br>
    **vagrant ssh**--> to login into vm<br>
3. Now type this command in vagrant directory **psql -d news -f newsdata.sql** to load database<br>
            **\c** --connect to database<br>
            **\dt** --see the tables in database<br>
            **\dv** -- see the views in database<br>
            **\q** -- quit the database<br>
4. This  **python log.py** to run the programm<br>

I have created views to retrieve the data<br>
These are the queries i used to create views<br>
##Articles_View<br>
articles_view = '''create or replace view atriclesdata as select title,
             count(title) as views from articles, log where articles.slug =
             replace(log.path,'/article/','')
             group by title order by views desc limit 3;'''<br>
##Author_View<br>
pop_auth = '''create view pop_auth as SELECT authors.name, count(*) AS views
            FROM articles, log
            WHERE log.path = concat('/article/', articles.slug)
            GROUP BY authors.name ORDER BY views desc LIMIT 3;'''<br>
            
##These are views for generating the data of errors by day which are greater than 1%<br>
dataset = '''create view rqst as select count(status) as errorstatus,date(time) as errortime
          from log where status!='200 OK' group by date(time) order by errorstatus;'''
dataset2= '''create view total_r as select count(status) as currentstatus,date(time)
          as currenttime from log group by date(time) order by currentstatus;'''
dataset3 = '''create view finalresult as select  errortime,((100.00*errorstatus)/currentstatus) as percent from rqst
         natural join total_r where total_r.currenttime=rqst.errortime group by errortime,percent order
         by percent;'''
