# QQ_zone
QQ空间爬虫，一小时20万数据

<h1>环境要求</h1>
<ul>
<li>python3</li>
<li>requests</li>
<li>selenium</li>
<li>configparser</li>
<li>xlwt</li>


</ul>

<h1>安装环境</h1>
  可使用pip或者easy_install安装<br>
  安装格式为：<br>
  pip install ...<br>
  easy_install ...<br>

<h1>运行项目</h2>
<ul>
<li>打开userinfo.ini,填入你的qq_number,qq_password</li><br>
<li>进入项目根目录下打开cmd 或终端 运行命令python qq_spider，一段时间后，数据存储在项目里frends,mood_detail文件夹里</li><br>
<li>好友qq_number存储在frends文件夹中的json文件中</li><br>
  
<li>说说mood存储在mood_detail中的excel文件夹中</li><br>
<li>文件data_analys.py中可选择将数据存入mysql中</li>
</ul>

<h1>数据分析</h1>

<ul>
<li>可参考此篇博客</li><br>
  <a href="https://my.oschina.net/u/3264690/blog/1498751">抓取60000+QQ空间说说做一次数据分析
</a>

</ul>
