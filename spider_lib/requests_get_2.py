import requests
import re
from bs4 import BeautifulSoup
res = requests.get('https://www.shiyanlou.com/courses/')
resptext = '''<body>
<nav class="navbar navbar-default navbar-fixed-top home-header">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#header-navbar-collapse" aria-expanded="false">
                <span class="sr-only">实验楼</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">
                <img src="https://static.shiyanlou.com/img/logo_02.png">
            </a>
        </div>

        <div class="collapse navbar-collapse" id="header-navbar-collapse">
            <ul class="nav navbar-nav">
                <li class="dropdown active">
                    <a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                        课程 <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="active" href="/courses/">全部课程</a></li>
                        <li><a class="" href="/courses/?status=preview">即将上线</a></li>
                        <li><a class="" href="/developer">开发者</a></li>
                    </ul>
                </li>
                <li class="">
                    <a href="/paths/">路径</a>
                </li>
                <li class="">
                    <a href="/questions/">讨论区</a>
                </li>
                <li class=" bootcamp new-nav logo-1111">
                    <a href="/bootcamp/">训练营</a>
                </li>
                <li class=" new-nav logo-1111">
                    <a href="/vip">会员</a>
                </li>

            </ul>


            <ul class="nav navbar-nav navbar-right header-sign">
                <li><a class="sign-in" data-sign="signin" href="#sign-modal" data-toggle="modal">登录</a></li>
                <li><a class="sign-up" data-sign="signup" href="#sign-modal" data-toggle="modal">注册</a></li>
            </ul>


            <form class="navbar-form navbar-right" action="/search" method="get" role="search">
                <div class="form-group">
                    <label><i class="fa fa-search"></i></label>
                    <input type="text" class="form-control" name="search" autocomplete="off" placeholder="搜索 课程/问答">
                </div>
            </form>
        </div>
    </div>
</nav>






    <div class="layout-margin-top">


    </div>

    <div class="layout-margin-top">



<div class="container layout layout-margin-top">


    <div class="row">
        <div class="col-md-9 layout-body">

    <div class="content">
        <div class="row course-cates">
            <div class="col-md-1 course-cates-title">类别：</div>
            <div class="col-md-11 course-cates-content">
                <a class="active" href="/courses/?course_type=all&amp;tag=all">全部</a>
                <a class="" href="/courses/?course_type=all&amp;tag=all&amp;fee=free">免费</a>
                <a class="" href="/courses/?course_type=all&amp;tag=all&amp;fee=limited">限免</a>
                <div class="course-cates-vip ">
                    <a target="_blank" href="/vip"><img src="https://static.shiyanlou.com/img/vip-icon.png"></a>
                    <a class="" href="/courses/?course_type=all&amp;tag=all&amp;fee=member">会员</a>
                </div>
            </div>
        </div>
        <div class="row course-cates">
            <div class="col-md-1 course-cates-title">标签：</div>
            <div class="col-md-11 course-cates-content">
                <a class="active" href="/courses/?course_type=all&amp;fee=all">全部</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Python&amp;fee=all">Python</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=C%2FC%2B%2B&amp;fee=all">C/C++</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Linux&amp;fee=all">Linux</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Web&amp;fee=all">Web</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8&amp;fee=all">信息安全</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=PHP&amp;fee=all">PHP</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Java&amp;fee=all">Java</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=NodeJS&amp;fee=all">NodeJS</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Android&amp;fee=all">Android</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=GO&amp;fee=all">GO</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Spark&amp;fee=all">Spark</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%B8%93%E4%B8%9A%E8%AF%BE&amp;fee=all">计算机专业课</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Hadoop&amp;fee=all">Hadoop</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=HTML5&amp;fee=all">HTML5</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Scala&amp;fee=all">Scala</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Ruby&amp;fee=all">Ruby</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=R&amp;fee=all">R</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=%E7%BD%91%E7%BB%9C&amp;fee=all">网络</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Git&amp;fee=all">Git</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=SQL&amp;fee=all">SQL</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=NoSQL&amp;fee=all">NoSQL</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=%E7%AE%97%E6%B3%95&amp;fee=all">算法</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Docker&amp;fee=all">Docker</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Swift&amp;fee=all">Swift</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=%E6%B1%87%E7%BC%96&amp;fee=all">汇编</a>

                    <a class="" href="/courses/?course_type=all&amp;tag=Windows&amp;fee=all">Windows</a>

            </div>
        </div>
    </div>
    <div class="content position-relative">
        <ul class="nav nav-tabs" role="tablist">
            <li class="active"><a href="/courses/?course_type=all&amp;tag=all&amp;fee=all">已上线</a></li>
            <li class=""><a href="/courses/?status=preview" class="stat-event" data-stat="preview_course">即将上线</a></li>
        </ul>
        <div class="clearfix"></div>
        <div class="courses-sort">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;order=latest">最新</a>
            /
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;order=hotest">最热</a>
        </div>
        <div class="search-result"></div>
        <div class="row">





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/63">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/63/follow" data-unfollow-url="/courses/63/unfollow" style="display: none;"></i>

        </div>
        <div class="course-img">

            <img alt="新手指南之玩转实验楼" src="https://dn-simplecloud.shiyanlou.com/ncn63.jpg">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="新手指南之玩转实验楼">新手指南之玩转实验楼</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                74213

			</span>



        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/1">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/1/follow" data-unfollow-url="/courses/1/unfollow" style="display: block;"></i>

        </div>
        <div class="course-img">

            <img alt="Linux 基础入门（新版）" src="https://dn-simplecloud.shiyanlou.com/ncn1.jpg">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Linux 基础入门（新版）">Linux 基础入门（新版）</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                92247

			</span>



        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/757">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/757/follow" data-unfollow-url="/courses/757/unfollow" style="display: none;"></i>

        </div>
        <div class="course-img">

            <img alt="Laravel 项目实战：仿新浪微博Web应用" src="https://dn-simplecloud.shiyanlou.com/1487669073080.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Laravel 项目实战：仿新浪微博Web应用">Laravel 项目实战：仿新浪微博Web应用</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                108

			</span>

                <span class="course-bootcamp pull-right">训练营</span>

        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/749">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/749/follow" data-unfollow-url="/courses/749/unfollow" style="display: none;"></i>

        </div>
        <div class="course-img">

            <img alt="3个C语言实例带你掌握递归方法论" src="https://dn-simplecloud.shiyanlou.com/1486541505613.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="3个C语言实例带你掌握递归方法论">3个C语言实例带你掌握递归方法论</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                67

			</span>



        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/745">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/745/follow" data-unfollow-url="/courses/745/unfollow" style="display: none;"></i>

        </div>
        <div class="course-img">

            <img alt="C++实现智能指针" src="https://dn-simplecloud.shiyanlou.com/1486431745968.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="C++实现智能指针">C++实现智能指针</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                110

			</span>



        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/743">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/743/follow" data-unfollow-url="/courses/743/unfollow" style="display: none;"></i>

        </div>
        <div class="course-img">

            <img alt="PHP 封装分页类" src="https://dn-simplecloud.shiyanlou.com/1484814157291.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="PHP 封装分页类">PHP 封装分页类</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                121

			</span>



        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/717">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/717/follow" data-unfollow-url="/courses/717/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="Kali 渗透测试 - Web 应用攻击实战" src="https://dn-simplecloud.shiyanlou.com/1480389165511.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Kali 渗透测试 - Web 应用攻击实战">Kali 渗透测试 - Web 应用攻击实战</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                139

			</span>

                <span class="course-bootcamp pull-right">训练营</span>

        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/741">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/741/follow" data-unfollow-url="/courses/741/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="Python 实现英文新闻摘要自动提取" src="https://dn-simplecloud.shiyanlou.com/1484188708361.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Python 实现英文新闻摘要自动提取">Python 实现英文新闻摘要自动提取</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                1610

			</span>


                <span class="course-money pull-right">会员</span>


        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/736">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/736/follow" data-unfollow-url="/courses/736/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="大数据带你挖掘打车的秘籍" src="https://dn-simplecloud.shiyanlou.com/1483667179293.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="大数据带你挖掘打车的秘籍">大数据带你挖掘打车的秘籍</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                1345

			</span>


                <span class="course-money pull-right">会员</span>


        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/680">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/680/follow" data-unfollow-url="/courses/680/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="由浅入深学网络" src="https://dn-simplecloud.shiyanlou.com/1478912239755.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="由浅入深学网络">由浅入深学网络</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                175

			</span>

                <span class="course-bootcamp pull-right">训练营</span>

        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/746">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/746/follow" data-unfollow-url="/courses/746/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="人机对战初体验:Python基于Pygame实现四子棋游戏" src="https://dn-simplecloud.shiyanlou.com/1484793020912.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="人机对战初体验:Python基于Pygame实现四子棋游戏">人机对战初体验:Python基于Pygame实现四子棋游戏</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                956

			</span>


                <span class="course-money pull-right">会员</span>


        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/729">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/729/follow" data-unfollow-url="/courses/729/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="使用 Python 解数学方程" src="https://dn-simplecloud.shiyanlou.com/1482807365470.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="使用 Python 解数学方程">使用 Python 解数学方程</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                1838

			</span>



        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/498">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/498/follow" data-unfollow-url="/courses/498/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="动手实战学Docker (15个实验+54个视频)" src="https://dn-simplecloud.shiyanlou.com/1478912280773.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="动手实战学Docker (15个实验+54个视频)">动手实战学Docker (15个实验+54个视频)</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                447

			</span>

                <span class="course-bootcamp pull-right">训练营</span>

        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/737">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/737/follow" data-unfollow-url="/courses/737/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="C语言实现LRU缓存" src="https://dn-simplecloud.shiyanlou.com/1484532035638.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="C语言实现LRU缓存">C语言实现LRU缓存</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                504

			</span>



        </div>
    </a>
</div>





<div class="col-md-4 col-sm-6  course">
    <a class="course-box" href="/courses/723">
        <div class="sign-box">



            <i class="fa fa-star-o course-follow pull-right" data-follow-url="/courses/723/follow" data-unfollow-url="/courses/723/unfollow" style="display:none"></i>

        </div>
        <div class="course-img">

            <img alt="PHP实现ECharts图表功能" src="https://dn-simplecloud.shiyanlou.com/1484552004144.png">

        </div>

        <div class="course-body">
            <span class="course-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="PHP实现ECharts图表功能">PHP实现ECharts图表功能</span>
        </div>
        <div class="course-footer">
			<span class="course-per-num pull-left">
                <i class="fa fa-users"></i>

                260

			</span>


                <span class="course-money pull-right">会员</span>


        </div>
    </a>
</div>




        </div>


<nav class="pagination-container">
    <ul class="pagination">

        <li class="disabled">
            <a href="#" aria-label="Previous">
                <span aria-hidden="true">上一页</span>
            </a>
        </li>



        <li class="active">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=1">1</a>
        </li>



        <li class="">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=2">2</a>
        </li>



        <li class="">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=3">3</a>
        </li>



        <li class="">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=4">4</a>
        </li>



        <li class="">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=5">5</a>
        </li>



        <li>
            <a href="#">...</a>
        </li>



        <li class="">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=24">24</a>
        </li>



        <li class="">
            <a href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=25">25</a>
        </li>



        <li class="">
            <a aria-label="Next" href="/courses/?course_type=all&amp;tag=all&amp;fee=all&amp;page=2">
                <span aria-hidden="true">下一页</span>
            </a>
        </li>

    </ul>
</nav>


    </div>

        </div>
        <div class="col-md-3 layout-side">





<div class="panel panel-default panel-userinfo">
    <div class="panel-body body-userinfo">
        <div class="media userinfo-header">
            <div class="media-left">
                <div class="user-avatar">

                     <a class="avatar" href="#sign-modal" data-toggle="modal" data-sign="signin">
                         <img class="circle" src="https://static.shiyanlou.com/img/logo-grey.png">
                     </a>

                </div>
             </div>
            <div class="media-body">

                 <span class="media-heading username">欢迎来到实验楼</span>
                 <p class="vip-remain">做实验，学编程</p>

            </div>
        </div>

        <div class="row userinfo-data">

            <hr>
            <div class="btn-group-lr">
            <a href="#sign-modal" type="button" class="btn btn-success col-md-5 col-xs-6 login-btn" data-toggle="modal" data-sign="signin">登录</a>
            <a href="#sign-modal" type="button" class="btn btn-success col-md-5 col-xs-6 col-md-offset-1 register-btn" data-toggle="modal" data-sign="signup">注册</a>
            </div>

        </div>

        <div class="userinfo-footer row">
            <div class="col-md-6 col-xs-6 pos-left">

                <a href="#sign-modal" data-toggle="modal" data-sign="signin"><span class="glyphicon glyphicon-bookmark"></span> 加入私有课</a>

            </div>
            <div class="col-md-6 col-xs-6 pos-right">
                <a href="/contribute" target="_blank"><span class="glyphicon glyphicon-send"></span> 我要投稿</a>
            </div>

            <div id="join-private-course" class="modal fade words-ctrl" tabindex="-1" role="dialog">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title">加入私有课</h4>
                        </div>
                        <div class="modal-body">
                            <div style="margin:15px 0; font:16px;">输入教师提供的私有课程码可以加入教师的私有课程。</div>
                            <form id="private-course-form" method="POST" action="/courses/join">
                                <div class="form-group">
                                    <label for="code">邀请码</label>
                                    <input class="form-control" id="code" name="code" type="text" value="">
                                    <input name="_csrf_token" type="hidden" value="1487847164##3974daa9b82ccd5cdbeab7a2169e1c2af47f0f9f">
                                </div>
                            </form>

                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                            <button type="button" class="btn btn-primary" onclick="document.getElementById('private-course-form').submit();">确定</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>


<div class="sidebox">

	<div class="sidebox-header">
		<h4 class="sidebox-title">最热路径</h4>
	</div>
	<div class="sidebox-body course-content side-list-body">
        <a href="/paths/python"><img style="width:25px;height:25px" src="https://dn-simplecloud.qbox.me/1471513769430.png"> Python 研发工程师</a>
        <a href="/paths/bigdata"><img style="width:25px;height:25px" src="https://dn-simplecloud.qbox.me/1471513926288.png"> 大数据工程师</a>
        <a href="/paths/cpp"><img style="width:25px;height:25px" src="https://dn-simplecloud.qbox.me/1471513793360.png"> C++ 研发工程师</a>
        <a href="/paths/security"><img style="width:25px;height:25px" src="https://dn-simplecloud.qbox.me/1471513867033.png"> 信息安全工程师</a>
        <a href="/paths/linuxsys"><img style="width:25px;height:25px" src="https://dn-simplecloud.qbox.me/1471514004752.png"> Linux 运维工程师</a>
	</div>

</div>

<div class="side-image side-qrcode">
    <img src="https://static.shiyanlou.com/img/ShiyanlouQRCode.png">
    <div class="side-image-text">关注公众号，手机看教程</div>
</div>

        </div>
    </div>
</div>

    </div>

	<div class="modal fade" id="invite-user" tabindex="-1" role="dialog" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                    <h4 class="modal-title">邀请好友，双方都可获赠实验豆！</h4>
				</div>
				<div class="modal-body">

                        <p></p><h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4><p></p>

					<div id="msg-modal"></div>
				</div>
			</div>
		</div>
	</div>

	<div class="modal fade" id="flash-message" tabindex="-1" role="dialog">
		<div class="modal-dialog" rolw="document">
		</div>
	</div>
	<div class="modal fade" id="modal-message" tabindex="-1" role="dialog" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                    <h4 class="modal-title">注意</h4>
				</div>
				<div class="modal-body">
				</div>
				<div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                    <button type="button" class="btn btn-primary confirm" data-dismiss="modal">确定</button>
				</div>
			</div>
		</div>
	</div>











    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
            <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <div class="modal-body">
                <ul class="nav nav-tabs" role="tablist">
                    <li role="presentation" class="active">
                        <a href="#signin-form" aria-controls="signin-form" role="tab" data-toggle="tab">登录</a>
                    </li>
                    <li role="presentation">
                        <a href="#signup-form" aria-controls="signup-form" role="tab" data-toggle="tab">注册</a>
                    </li>
                </ul>
                <div class="tab-content">
                    <div role="tabpanel" class="tab-pane active" id="signin-form">
                        <form action="/login" method="post">
                            <div class="form-group">
                                <div class="input-group">
                                    <div class="input-group-addon">
                                        <i class="fa fa-envelope" style="margin:0;"></i>
                                    </div>
                                    <input type="email" name="login" class="form-control" placeholder="请输入邮箱">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="input-group">
                                    <div class="input-group-addon">
                                        <i class="fa fa-lock" style="margin:0;"></i>
                                    </div>
                                    <input type="password" name="password" class="form-control" placeholder="请输入密码">
                                </div>
                            </div>
                            <div class="form-inline verify-code-item" style="display:none;">
                                <div class="form-group">
                                    <div class="input-group">
                                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
                                    </div>
                                </div>
                                <img class="verify-code" src="" source="/captcha.gif">
                            </div>
                            <div class="form-group remember-login">
                                <input name="remember" type="checkbox" value="y"> 下次自动登录
                                <a class="pull-right" href="/reset_password">忘记密码？</a>
                            </div>
                            <div class="form-group">
                                <input class="btn btn-primary" name="submit" type="submit" value="进入实验楼">
                            </div>
                            <div class="form-group widget-signin">
                                <span>快速登录</span>
                                <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                                <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                                <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                                <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                                <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                            </div>
                            <div class="form-group error-msg">
                                <div class="alert alert-danger" role="alert"></div>
                            </div>
                        </form>
                    </div>
                    <div role="tabpanel" class="tab-pane" id="signup-form">
                        <form action="/register" method="post">
                            <div class="form-group">
                                <div class="input-group">
                                    <div class="input-group-addon">
                                        <i class="fa fa-envelope" style="margin:0;"></i>
                                    </div>
                                    <input type="email" name="email" class="form-control" placeholder="请输入邮箱">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="input-group">
                                    <div class="input-group-addon">
                                        <i class="fa fa-lock" style="margin:0;"></i>
                                    </div>
                                    <input type="password" name="password" class="form-control" placeholder="请输入密码">
                                </div>
                            </div>
                            <div class="form-inline">
                                <div class="form-group">
                                    <div class="input-group">
                                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
                                    </div>
                                </div>
                                <img class="verify-code" src="" source="/captcha.gif">
                            </div>
                            <div class="form-group">
                                <input class="btn btn-primary" name="submit" type="submit" value="注册">
                            </div>
                            <div class="form-group agree-privacy">
                                注册表示您已经同意我们的<a href="/privacy" target="_blank">隐私条款</a>
                            </div>
                            <div class="form-group widget-signup">
                                <span>快速注册</span>
                                <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                                <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                                <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                                <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                                <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                            </div>
                            <div class="form-group error-msg">
                                <div class="alert alert-danger" role="alert"></div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>


    <div id="base-data" data-flash="false" data-is-login="false" data-is-jwt="true" data-socket-url="wss://comet.shiyanlou.com" data-msg-user="" data-msg-system=""></div>

    <!-- 不带 CSS 的库 -->
    <script async="" src="https://www.google-analytics.com/analytics.js"></script><script src="https://static.shiyanlou.com/static/babel-polyfill/6.20.0/polyfill.min.js"></script>
    <script src="/app/dist/js/manifest.js?=201702022062448"></script>
    <script src="/app/dist/js/vendor.js?=201702022062448"></script>

    <script src="https://static.shiyanlou.com/static/jquery/2.2.4/jquery.min.js"></script>
    <script src="https://static.shiyanlou.com/static/jquery.form/3.51/jquery.form.min.js"></script>
    <script src="https://static.shiyanlou.com/static/jquery.qrcode/1.0/jquery.qrcode.min.js"></script>
    <script src="https://static.shiyanlou.com/static/html2canvas/0.4.1/html2canvas.min.js"></script>
    <script src="https://static.shiyanlou.com/static/jspdf/1.3.2/jspdf.min.js"></script>
    <script src="https://static.shiyanlou.com/static/zeroclipboard/2.3.0/ZeroClipboard.min.js"></script>
    <script src="https://static.shiyanlou.com/static/aliyun/aliyun-oss-sdk-4.3.0.min.js"></script>
    <script src="https://static.shiyanlou.com/static/qiniu/qiniu.js"></script>
    <script src="https://static.shiyanlou.com/static/plupload/2.1.9/js/plupload.full.min.js"></script>
    <script src="https://static.shiyanlou.com/static/echarts/v3.3.2/echarts.min.js"></script>
    <!-- 不带 CSS 的库 end -->

    <!-- 带有 CSS 的库 -->
    <script src="https://static.shiyanlou.com/static/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://static.shiyanlou.com/static/bootstrap-switch/3.3.2/js/bootstrap-switch.min.js"></script>
    <script src="https://static.shiyanlou.com/static/bootstrap-tour/0.11.0/js/bootstrap-tour.min.js"></script>
    <script src="https://static.shiyanlou.com/static/bootstrap-table/1.11.0/bootstrap-table.min.js"></script>
    <script src="https://static.shiyanlou.com/static/bootstrap-table/1.11.0/locale/bootstrap-table-zh-CN.min.js"></script>
    <script src="https://static.shiyanlou.com/static/bootstrap-table/1.11.0/extensions/filter-control/bootstrap-table-filter-control.min.js"></script>

    <script src="https://static.shiyanlou.com/static/ace/1.2.5/ace.js"></script>
    <script src="https://static.shiyanlou.com/static/videojs/5.15.1/js/video.min.js"></script>
    <script src="https://static.shiyanlou.com/static/katex/0.7.1/katex.min.js"></script>
    <script src="https://static.shiyanlou.com/static/highlight.js/9.9.0/js/highlight.min.js"></script>
    <!-- 带有 CSS 的库 end -->

    <script src="https://static.shiyanlou.com/static/ravenjs/3.7.0/raven.min.js"></script>
    <script>
        Raven.config('https://bc3878b7ed0a4468a65390bd79e6e73f@sentry.shiyanlou.com/5', {
            release: '3.12.13'
        }).install();
    </script>






<div id="jinja-data" data-loginurl="/login" data-private-course-url="/courses/join" data-site-type="0"></div>

<script src="/app/dist/js/course/index.js?=201702022062448"></script><div style="display: none; position: fixed; top: 0px; left: 0px; right: 0px; bottom: 0px; text-align: center; z-index: 1600; background: rgba(0, 0, 0, 0.498039);"><i class="fa fa-spinner fa-pulse" style="margin-top: 224px; color: rgb(255, 255, 255); font-size: 35px;"></i></div>






<div class="footer">
    <div class="container">
        <div class="row">
            <div class="col-md-4 clearfix footer-col">
                <img src="https://static.shiyanlou.com/img/logo_03.png">
                <div class="footer-slogan">动手做实验，轻松学IT</div>
                <div class="col-xs-2">
                    <div class="social-item footer-weixin-item">
                        <i class="fa fa-weixin"></i>
                        <div class="footer-weixin">
                            <img src="https://static.shiyanlou.com/img/footer-weixin.png">
                        </div>
                    </div>
                </div>
                <div class="col-xs-2">
                    <div class="social-item footer-weibo-item">
                        <a href="http://weibo.com/shiyanlou2013" target="_blank">
                            <i class="fa fa-weibo"></i>
                        </a>
                    </div>
                </div>
            </div>
            <div class="col-xs-6 col-sm-3 col-md-2 footer-col">
                <div class="col-title">公司</div>
                <a href="/aboutus" target="_blank">关于我们</a><br>
                <a href="/contact" target="_blank">联系我们</a><br>
                <a href="http://www.simplecloud.cn/jobs.html" target="_blank">加入我们</a><br>
                <a href="https://blog.shiyanlou.com" target="_blank">技术博客</a><br>
            </div>
            <div class="col-xs-6 col-sm-3 col-md-2 footer-col">
                <div class="col-title">合作</div>
                <a href="/contribute" target="_blank">我要投稿</a><br>
                <a href="/labs" target="_blank">教师合作</a><br>
                <a href="/edu/" target="_blank">高校合作</a><br>
                <a href="/friends" target="_blank">友情链接</a>
            </div>
            <div class="col-xs-6 col-sm-3 col-md-2 footer-col">
                <div class="col-title">服务</div>
                <a href="/bootcamp/" target="_blank">实战训练营</a><br>
                <a href="/vip" target="_blank">会员服务</a><br>
                <a href="/courses/reports" target="_blank">实验报告</a><br>
                <a href="/questions/?tag=%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98" target="_blank">常见问题</a><br>
                <a href="/privacy" target="_blank">隐私条款</a>
            </div>
            <div class="col-xs-6 col-sm-3 col-md-2 footer-col">
                <div class="col-title">学习路径</div>
                <a href="/paths/python" target="_blank">Python学习路径</a><br>
                <a href="/paths/linuxdev" target="_blank">Linux学习路径</a><br>
                <a href="/paths/bigdata" target="_blank">大数据学习路径</a><br>
                <a href="/paths/java" target="_blank">Java学习路径</a><br>
                <a href="/paths/php" target="_blank">PHP学习路径</a><br>
                <a href="/paths/" ,="" target="_blank">全部</a>
            </div>
        </div>
    </div>
    <div class="text-center copyright">
        <span>Copyright @2013-2016 实验楼在线教育</span>
        <span class="ver-line"> | </span>
        <a href="http://www.miibeian.gov.cn/" target="_blank">蜀ICP备13019762号</a>
        <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
         (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
         m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
         })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
        ga('create', 'UA-89338452-1', 'auto');
        ga('send', 'pageview');
        </script>
    </div>
</div>






</body>'''
soup = BeautifulSoup(res.text, 'lxml')
soup = BeautifulSoup(resptext, 'lxml')
course = soup.find_all('div',{'class':'col-md-4','class':'col-sm-6','class':'course'})
for i in course:
    title = i.find('span',{'class':'course-title'}).get_text()
    study_people = i.find('span',{'class':'course-per-num','class':'pull-left'}).get_text()
    study_people = re.sub("\D", "", study_people)# 数字这里有太多的空格和回车，清理一下
    try:
        tag = i.find('span',{'class':'course-per-num','class':'pull-right'}).get_text()
    except:
        tag="课程"
    print("{}    学习人数:{}    {}\n".format(tag, study_people, title,))