0x18. Webstack monitoring
=========================

Background Context
------------------

"You cannot fix or improve what you cannot measure" is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

-   Application monitoring: getting data about your running software and making sure it is behaving as expected
-   Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)


Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/HjJQMilktjdS5BksAfLY0Q "explain to anyone"), **without the help of Google**:

### General

-   Why is monitoring needed
-   What are the 2 main area of monitoring
-   What are access logs for a web server (such as Nginx)
-   What are error logs for a web server (such as Nginx)

Your servers
------------

| Name | Username | IP | State |  |
| --- | --- | --- | --- | --- |
| 764-web-01 | `ubuntu` | `104.196.1.139` | running | [Soft reboot]
| 764-web-02 | `ubuntu` | `35.227.123.185` | running | [Soft reboot]
| 764-lb-01 | `ubuntu` | `35.237.31.57` | running | [Soft reboot]

* * * * *

Tasks
-----

#### 0\. Sign up for Datadog and install datadog-agent mandatory

For this task head to [https://www.datadoghq.com/](https://intranet.hbtn.io/rltoken/Uho9kxbX9KHCSYAQ-Zl1AQ "https://www.datadoghq.com/") and sign up for a free `Datadog` account. When signing up, you'll have the option of selecting statistics from your current stack that `Datadog` can monitor for you. Once you have an account set up, follow the instructions given on the website to install the `Datadog` agent.


#### 1\. Monitor some metrics mandatory

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some `monitors` within the `Datadog` dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check](https://intranet.hbtn.io/rltoken/naY47nur2yPJNw8tdACnzQ "System Check").

-   Set up a monitor that checks the number of read requests issued to the device per second.
-   Set up a monitor that checks the number of write requests issued to the device per second.


#### 2\. Create a dashboard mandatory

Now create a dashboard with different metrics displayed in order to get a few different visualizations.

-   Create a new `dashboard`
-   Add at least 4 `widgets` to your dashboard. They can be of any type and monitor whatever you'd like
-   Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. **Note**: in order to get the id of your dashboard, you may need to use [Datadog's API](https://intranet.hbtn.io/rltoken/VrzQP39UUFMmAKZx0IZLuw "Datadog's API")
