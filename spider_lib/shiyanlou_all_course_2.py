import requests
import re
from bs4 import BeautifulSoup

host_url = "http://www.shiyanlou.com{}"
html = '''<body>







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
                        <li><a class="" href="/courses/">全部课程</a></li>
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


					<li class=""><a href="/teacher">我的课程</a></li>


            </ul>


            <ul class="nav navbar-nav navbar-right header-user">





                        <li><a class="btn btn-primary" id="header-continue-lab" href="/courses/running">继续实验</a></li>


                <li data-v-07a2dd56="" class="header-message"><a data-v-07a2dd56="" href="/user/message"><i data-v-07a2dd56="" class="fa fa-bell-o"></i> <div data-v-07a2dd56="" class="mark"></div></a> <!----></li>


                <li data-v-815c5224="" class="header-userbox dropdown"><a data-v-815c5224="" data-toggle="dropdown" class="dropdown-toggle"><img data-v-815c5224="" src="https://dn-simplecloud.shiyanlou.com/gravatarNTY0MzE5MDc1OTIx.png?v=1467272233337&amp;imageView2/1/w/200/h/200" class="header-avatar"> <img data-v-815c5224="" src="https://static.shiyanlou.com/img/icon-vip.png" class="vip-icon"> <span data-v-815c5224="" class="caret"></span></a> <ul data-v-815c5224="" class="dropdown-menu"><li data-v-815c5224=""><a data-v-815c5224="" href="/user/63246/">我的主页</a></li> <li data-v-815c5224=""><a data-v-815c5224="" href="/user/profile">个人设置</a></li> <li data-v-815c5224=""><a data-v-815c5224="" href="/logout">安全退出</a></li></ul></li>
            </ul>


            <form class="navbar-form navbar-right" action="/search" method="get" role="search">
                <div class="form-group">
                    <label><i class="fa fa-search"></i></label>
                    <input class="form-control" name="search" autocomplete="off" placeholder="搜索 课程/问答" type="text">
                </div>
            </form>
        </div>
    </div>
</nav>









    <div class="layout-margin-top">


    </div>

    <div class="layout-margin-top">



<div class="container layout layout-margin-top">

<ol class="breadcrumb">
    <li><a href="/courses/">全部课程</a></li>

    <li>

    <a href="/courses/?tag=Web">Web</a>，

    <a href="/courses/?tag=HTML5">HTML5</a>

    </li>

    <li class="active">
        <a href="/courses/361">
        基于HTML5 Canvas实现小游戏
        </a>
    </li>
</ol>

    <div class="row">
        <div class="col-md-9 layout-body">






















    <div class="side-image side-image-mobile">
        <img src="https://dn-simplecloud.shiyanlou.com/ncn361.jpg?imageView2/0/h/300">
    </div>
    <div class="content course-infobox">
        <div class="clearfix course-infobox-header">
            <h4 class="pull-left course-infobox-title">

                <span>基于HTML5 Canvas实现小游戏</span>

            </h4>
            <div class="pull-right course-infobox-follow" data-follow-url="/courses/361/follow" data-unfollow-url="/courses/361/unfollow">
                <span class="course-infobox-followers">157</span>
                <span>人关注</span>

                <i class="fa fa-star-o"></i>

            </div>
        </div>
        <div class="clearfix course-infobox-body">
            <div class="course-infobox-content">
            <p>本课程基于 HTML5 的 canvas 实现了一个小游戏，着重介绍了 HTML5 游戏开发的流程及游戏开发中需要处理的东西。对 Web 游戏开发感兴趣的同学可以通过这个项目实践 HTML5 及 JavaScript 基础知识。</p>

            </div>

            <div class="course-infobox-progress">

                    <div class="course-progress-finished"></div>



                <span>（1/1）</span>
            </div>





                <div class="pull-right course-infobox-price">

                </div>

        </div>

        <div class="clearfix course-infobox-footer">

            <div class="pull-right course-infobox-learned">3728 人学过</div>
        </div>

    </div>
	<div class="content">
        <ul class="nav nav-tabs" role="tablist">

            <li role="presentation" class="active">
                <a href="#labs" aria-controls="labs" role="tab" data-toggle="tab">实验列表</a>
            </li>

		</ul>
		<div class="tab-content">

            <div role="tabpanel" class="tab-pane active" id="labs">





    <div class="lab-item ">
    <div class="lab-item-status">

            <img src="https://static.shiyanlou.com/img/lab-ok.png">

    </div>
    <div class="lab-item-index">第1节</div>
    <div class="lab-item-title" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="HTML5 Canvas小游戏">HTML5 Canvas小游戏</div>
    <div class="pull-right lab-item-ctrl">














                         <a class="btn btn-default" href="/courses/361/labs/1158/document" target="_blank">查看文档</a>



                        <a class="btn btn-primary  member-vm lab-item-start-newlab" data-mobile-url="/courses/document/1158" href="#" data-url="/courses/start/1158" data-labid="1158" data-next="/courses/running">开始实验</a>






    </div>
</div>


            </div>
		</div>
	</div>
    <div class="content">
        <ul class="nav nav-tabs" role="tablist">
            <li role="presentation" class="active">
                <a href="#comments" class="stat-event" aria-controls="comments" role="tab" data-stat="course_comment" data-toggle="tab">课程评论(8)</a>
            </li>
            <li role="presentation">
                <a href="#reports" class="stat-event" data-stat="course_report" aria-controls="reports" role="tab" data-toggle="tab">实验报告(3)</a>
            </li>
            <li role="presentation">
                <a href="#questions" class="stat-event" data-stat="course_question" aria-controls="questions" role="tab" data-toggle="tab">实验问答(5)</a>
            </li>
        </ul>
        <div class="tab-content">
            <div role="tabpanel" class="tab-pane course-comment active" id="comments">
                <div class="comment-box">
                    <div class="comment-form">

                            <textarea class="comment-form-content" placeholder="输入您想说的话..."></textarea>
                            <button class="pull-right btn btn-primary comment-form-add">发表评论</button>
                            <button class="pull-right btn btn-primary comment-form-reset">清除评论</button>

                    </div>
                    <div class="comment-title">最新评论</div>
                    <div class="comment-list"><div class="row comment-list-item"><div class="col-md-1">
        <div class="user-avatar ">
            <a class="avatar" href="/user/319811/" target="_blank">
                <img src="https://dn-simplecloud.shiyanlou.com/gravatarEDL2VAMF5C8S.jpg?imageView2/1/w/200/h/200">
            </a>

            <a class="member-icon" href="/vip" target="_blank">
                <img src="https://static.shiyanlou.com/img/vip-icon.png">
            </a>
        </div></div><div class="col-md-11 comment-item-body">
        <div class="user-username">
            <a class="username" href="/user/319811/" target="_blank">
                Lilliput_
            </a>
            <span class="user-level">L61</span>
        </div><div class="comment-item-content markdown-box"><p>good</p>
</div><div class="comment-item-date">3月前</div><div class="comment-item-lab">来自：HTML5 Canvas小游戏</div><div class="comment-item-reply" data-pid="9054"><i class="fa fa-share"></i>回复</div></div></div><div class="row comment-list-item"><div class="col-md-1">
        <div class="user-avatar ">
            <a class="avatar" href="/user/312917/" target="_blank">
                <img src="https://dn-simplecloud.shiyanlou.com/gravatarY4TU3H9VJDN8.jpg?imageView2/1/w/200/h/200">
            </a>

        </div></div><div class="col-md-11 comment-item-body">
        <div class="user-username">
            <a class="username" href="/user/312917/" target="_blank">
                zpyzpy
            </a>
            <span class="user-level">L4</span>
        </div><div class="comment-item-content markdown-box"><p>会卡</p>
</div><div class="comment-item-date">3月前</div><div class="comment-item-lab">来自：HTML5 Canvas小游戏</div><div class="comment-item-reply" data-pid="8566"><i class="fa fa-share"></i>回复</div></div></div><div class="row comment-list-item"><div class="col-md-1">
        <div class="user-avatar ">
            <a class="avatar" href="/user/166939/" target="_blank">
                <img src="https://dn-simplecloud.shiyanlou.com/gravatarMQVVJLCVCQ4Q.jpg?imageView2/1/w/200/h/200">
            </a>

        </div></div><div class="col-md-11 comment-item-body">
        <div class="user-username">
            <a class="username" href="/user/166939/" target="_blank">
                tonylinx
            </a>
            <span class="user-level">L1</span>
        </div><div class="comment-item-content markdown-box"><p>good!</p>
</div><div class="comment-item-date">5月前</div><div class="comment-item-reply" data-pid="5271"><i class="fa fa-share"></i>回复</div></div></div><div class="row comment-list-item"><div class="col-md-1">
        <div class="user-avatar ">
            <a class="avatar" href="/user/250563/" target="_blank">
                <img src="https://dn-simplecloud.shiyanlou.com/gravatar7RMGKTWMHFGM.jpg?imageView2/1/w/200/h/200">
            </a>

        </div></div><div class="col-md-11 comment-item-body">
        <div class="user-username">
            <a class="username" href="/user/250563/" target="_blank">
                璎珞桐
            </a>
            <span class="user-level">L21</span>
        </div><div class="comment-item-content markdown-box"><p>在reset（）函数里面加入if else通过monstersCaught的值来判断，就可以实现将hero在捕捉到monster的时候让hero就停留在捕获的位置</p>
</div><div class="comment-item-date">5月前</div><div class="comment-item-reply" data-pid="5264"><i class="fa fa-share"></i>回复</div></div></div><div class="row comment-list-item"><div class="col-md-1">
        <div class="user-avatar ">
            <a class="avatar" href="/user/255202/" target="_blank">
                <img src="https://dn-simplecloud.shiyanlou.com/gravatarZHSTPGKMYA73.jpg?imageView2/1/w/200/h/200">
            </a>

        </div></div><div class="col-md-11 comment-item-body">
        <div class="user-username">
            <a class="username" href="/user/255202/" target="_blank">
                MrFu
            </a>
            <span class="user-level">L9</span>
        </div><div class="comment-item-content markdown-box"><p>写完发现不行呀</p>
</div><div class="comment-item-date">5月前</div><div class="comment-item-reply" data-pid="5167"><i class="fa fa-share"></i>回复</div></div></div><div class="row comment-list-item"><div class="col-md-1">
        <div class="user-avatar ">
            <a class="avatar" href="/user/164325/" target="_blank">
                <img src="https://dn-simplecloud.shiyanlou.com/gravatarP3ZRZF74FE9X.jpg?imageView2/1/w/200/h/200">
            </a>

        </div></div><div class="col-md-11 comment-item-body">
        <div class="user-username">
            <a class="username" href="/user/164325/" target="_blank">
                CherryUI
            </a>
            <span class="user-level">L35</span>
        </div><div class="comment-item-content markdown-box"><p>nice</p>
</div><div class="comment-item-date">1年前</div><div class="comment-item-reply" data-pid="3400"><i class="fa fa-share"></i>回复</div></div></div></div>
                    <div class="pagination-container"></div>
                </div>
            </div>
            <div role="tabpanel" class="tab-pane" id="reports">
				<span class="lab-id active" data-lab-id="None">全部</span>

				<span class="lab-id" data-lab-id="1158">第1节</span>

                <div class="report-owner">
                    <span class="owner-list" data-user-id="63246">我的报告</span> / <span class="owner-list active" data-user-id="None">所有报告</span>
                </div>
                <div class="row report-items"></div>
                <div class="pagination-container"></div>
            </div>
            <div role="tabpanel" class="tab-pane" id="questions">
                <a class="btn btn-success" data-toggle="modal" href="#askquestion">我要提问</a>
                <hr>
                <ul class="row question-items"></ul>
                <div class="pagination-container"></div>
            </div>
        </div>
    </div>


        </div>
        <div class="col-md-3 layout-side">

    <div class="side-image side-image-pc">
        <img src="https://dn-simplecloud.shiyanlou.com/ncn361.jpg?imageView2/0/h/300">
    </div>









<div class="sidebox mooc-teacher">
    <div class="sidebox-header mooc-header">
        <h4 class="sidebox-title">课程教师</h4>
    </div>
    <div class="sidebox-body mooc-content">
        <a href="/user/7682/" target="_blank">
            <img src="https://dn-simplecloud.shiyanlou.com/gravatar57aeee35c98205091e18d1140e9f38cf.png
?imageView2/1/w/100/h/100">
        </a>
        <div class="mooc-info">
            <div class="name"><strong>JellyBool</strong> </div>

            <div class="courses">共发布过<strong>8</strong>门课程</div>
        </div>
        <div class="mooc-extra-info">
            <div class="word long-paragraph">

            </div>
        </div>
    </div>
    <div class="sidebox-footer mooc-footer">
        <a href="/teacher/7682" target="_blank">查看老师的所有课程 &gt;</a>
    </div>
</div>




    <div class="side-image">
    <a href="/vip" target="_blank">
        <img src="https://static.shiyanlou.com/img/banner-vip.png">
    </a>
</div>




    <div class="sidebox pre-course">
        <div class="sidebox-header">
            <h4 class="sidebox-title">前置课程</h4>
        </div>
        <div class="sidebox-body course-content">

            <a href="/courses/21">Javascript基础（新版）</a>

        </div>
    </div>



    <div class="sidebox adv-course">
        <div class="sidebox-header">
            <h4 class="sidebox-title">进阶课程</h4>
        </div>
        <div class="sideobx-body course-content">

            <a href="/courses/144">网页版扫雷</a>

            <a href="/courses/161">网页版拼图游戏</a>

        </div>
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

					<div class="form-label">
                        分享专属链接给好友，或粘贴到QQ群/微博/论坛，好友注册后，您和好友将分别获赠3个实验豆！
                    </div>
					<input id="bstext" class="form-invite" value="https://www.shiyanlou.com/register?inviter=NTY0MzE5MDc1OTIx" type="text">

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




<div class="modal fade askquestion-modal" id="askquestion" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
                <h4 class="modal-title">发帖</h4>
            </div>
            <div class="modal-body words-ctrl">
                <form class="form-horizontal" action="/questions/">
                    <input name="_csrf_token" value="1488029393##1d0f890f80bff194a1a7ab38c06640b612ed334f" type="hidden">
                    <div class="form-group">
                        <label class="col-md-2 control-label">标题</label>
                        <div class="col-md-10">
                            <input name="title" min="5" max="100" class="form-control" placeholder="至少输入5个字" value="" type="text">
                            <span class="help-block"></span>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-2 control-label">描述</label>
                        <div class="col-md-10">



<div class="tabpanel mkeditor">
    <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active">
            <a href="#mkeditor-editor" role="tab" data-toggle="tab">编辑</a>
        </li>
        <li role="presentation">
            <a class="mkeditor-btn-view" href="#mkeditor-viewer" role="tab" data-toggle="tab">预览</a>
        </li>
    </ul>
    <div class="tab-content">
        <div class="tab-pane active mkeditor-editor" id="mkeditor-editor" role="tabpanel">

            <div class="btn-group" role="group">

                <button type="button" class="btn btn-default mkeditor-btn-bold">
                    <i class="fa fa-bold"></i>
                </button>
                <button type="button" class="btn btn-default mkeditor-btn-italic">
                    <i class="fa fa-italic"></i>
                </button>
                <button type="button" class="btn btn-default mkeditor-btn-link">
                    <i class="fa fa-link"></i>
                </button>
                <button type="button" class="btn btn-default mkeditor-btn-quote">
                    <i class="fa fa-quote-left"></i>
                </button>
                <button type="button" class="btn btn-default mkeditor-btn-code">
                    <i class="fa fa-code"></i>
                </button>
                <button id="mkeditor-pickfile" type="button" class="btn btn-default mkeditor-btn-img" style="z-index: 1;">
                    <i class="fa fa-image"></i>
                </button>

                <button type="button" class="btn btn-default mkeditor-btn-listol">
                    <i class="fa fa-list-ol"></i>
                </button>
                <button type="button" class="btn btn-default mkeditor-btn-listul">
                    <i class="fa fa-list-ul"></i>
                </button>
            <div id="html5_1b9o50bt61s81q6s1gj11cuaqs53_container" class="moxie-shim moxie-shim-html5" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px; overflow: hidden; z-index: 0;"><input id="html5_1b9o50bt61s81q6s1gj11cuaqs53" style="font-size: 999px; opacity: 0; position: absolute; top: 0px; left: 0px; width: 100%; height: 100%;" multiple="" accept="" type="file"></div></div>
            <div class="btn-group pull-right" role="group">
                <a style="font-size:12px; color:#666; text-decoration:underline;" href="/questions/764" target="_blank">
                    <i class="fa fa-question-circle"></i>Markdown 语法
                </a>
            </div>
            <textarea name="content" class="content" min="0" max="20000" placeholder="推荐使用 Markdown 语法，至少输入 5 个字"></textarea>
            <div class="help-block"></div>
        </div>
        <div class="tab-pane mkeditor-viewer markdown-body" id="mkeditor-viewer" role="tabpanel">
            <div></div>
        </div>
    </div>
</div>

                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-2 control-label">板块</label>
                        <div class="col-md-10">
                            <div class="q-types" data-type="">
                            </div>
                        </div>
                    </div>


                </form>
            </div>
            <div class="modal-footer">
                <a type="button" class="submit-question btn btn-primary" href="/vip" target="_blank" style="background:#FFFFFF;color:#00CC99;border:none;float:left;padding-left:0;"><img src="https://static.shiyanlou.com/img/icon-vip-advance.png" alt=""> 加入高级会员获得助教答疑</a>
                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                <button type="button" class="submit-question btn btn-primary">提交</button>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="start-newlab">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                <h3>开始新实验</h3>
			</div>
			<div class="modal-body" style="text-align:center">
                <p> 一个实验正在进行，是否停止它，开始新实验？</p>

			</div>
			<div class="modal-footer" style="margin-top:0px">

                    <button class="btn" data-dismiss="modal" aria-hidden="true">关闭</button>
                    <a class="btn btn-primary start-newlab-confirm">确定</a>

			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
</div>
<div class="modal fade" id="start-evaluation-course">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                <h3>开始评估课实验</h3>
			</div>
			<div class="modal-body">
                <div>
                    <p>为了让评估结果更加准确，请注意以下操作：</p>
                    <ul>
                        <li>完成实验后点击「停止实验」按钮</li>
                        <li>将代码提交到代码库</li>
                        <li>尽可能详尽的撰写实验报告</li>
                        <li>尽可能在实验操作的关键步骤截图</li>
                        <li>尽可能减少无用操作</li>
                        <li>尽可能高效的利用内存/CPU资源</li>
                    </ul>
                    <p>评估课还在不断完善中，我们真挚希望你能通过我们提供的这个平台，找到更好的发展机会。</p>
                </div>
                <br>
                <div class="start-newlab"></div>
			</div>
			<div class="modal-footer">
                <button class="btn" data-dismiss="modal" aria-hidden="true">关闭</button>
                <a class="btn btn-primary start-confirm">确定</a>
			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
</div>
<div class="modal fade" id="vip-startlab-modal">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                <h3>开始实验</h3>
			</div>
			<div class="modal-body">
                <div class="start-newlab"></div>
                <br>
                <div class="text-center vip-vm">
                    <a class="btn btn-default btn-lg newvm">创建新环境</a>

					&nbsp;&nbsp;or&nbsp;&nbsp;
                    <a class="btn btn-primary btn-lg oldvm">使用已保存的环境</a>

                </div>
                <br>
			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
</div>
<div class="modal fade" id="bean-course-modal" tabindex="-1" role="dialog" aria-hidden="true">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
                <h4 class="modal-title">激活项目课：基于HTML5 Canvas实现小游戏</h4>
			</div>
			<div class="modal-body">
				<div style="font-size:14px; font-weight:thin;">
					本课程基于 HTML5 的 canvas 实现了一个小游戏，着重介绍了 HTML5 游戏开发的流程及游戏开发中需要处理的东西。对 Web 游戏开发感兴趣的同学可以通过这个项目实践 HTML5 及 JavaScript 基础知识。
				</div>
				<div style="margin:36px 0 18px; font-size:16px; font-weight:bold;">
                    您有 <span style="color:#f66;"><strong>24</strong></span> 个实验豆，激活本课程需要消耗 <span style="color:#f66;"><strong>0</strong></span> 个实验豆！
				</div>
                <div style="color:#84B61A; font-size:14px; font-weight:bold;">激活后可不限次数学习本课。<a href="/faq#shiyandou" style="font-weight:normal;" target="_blank">如何获得实验豆？</a></div>
			</div>
			<div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>

                <button type="button" class="btn btn-primary bean-course-confirm" data-dismiss="modal">永久激活</button>

			</div>
		</div>
	</div>
</div>


<div class="modal fade" id="charge-course-modal" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>
                <h4 class="modal-title">课程报名</h4>
            </div>
            <div class="modal-body">
                <form class="row form-horizontal">
                     <input name="_csrf_token" value="1488029393##1d0f890f80bff194a1a7ab38c06640b612ed334f" type="hidden">
                    <div class="form-group">
                        <label class="col-md-2 control-label">邮箱</label>
                        <div class="col-md-10">
                            <input class="form-control" name="email" value="1121031509@qq.com" type="email">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-2 control-label">手机号码</label>
                        <div class="col-md-10">
                            <div class="input-group">
                                <input class="form-control" name="phone_no" type="text">
                                <span class="input-group-btn">
                                    <button class="btn btn-default charge-course-phone-code" type="button" style="padding:7px 12px;">获取验证码</button>
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-2 control-label">验证码</label>
                        <div class="col-md-10">
                            <input class="form-control" name="verify_code" type="text">
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                <button type="button" class="btn btn-primary charge-course-confirm">确定</button>
            </div>
        </div>
    </div>
</div>



<div class="modal fade" id="paid-modal" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title" style="text-align:center;">支付确认</h4>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class="col-md-6">
                        <button class="btn btn-primary paid-confirm" type="button">支付成功</button>
                    </div>
                    <div class="col-md-6">
                        <button class="btn btn-primary paid-method" type="button" style="background:none; color:#0c9">选择支付方式</button>
                    </div>
                </div>
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
                                    <input name="login" class="form-control" placeholder="请输入邮箱" type="email">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="input-group">
                                    <div class="input-group-addon">
                                        <i class="fa fa-lock" style="margin:0;"></i>
                                    </div>
                                    <input name="password" class="form-control" placeholder="请输入密码" type="password">
                                </div>
                            </div>
                            <div class="form-inline verify-code-item" style="display:none;">
                                <div class="form-group">
                                    <div class="input-group">
                                        <input name="captcha_v" class="form-control" placeholder="请输入验证码" type="text">
                                    </div>
                                </div>
                                <img class="verify-code" src="" source="/captcha.gif">
                            </div>
                            <div class="form-group remember-login">
                                <input name="remember" value="y" type="checkbox"> 下次自动登录
                                <a class="pull-right" href="/reset_password">忘记密码？</a>
                            </div>
                            <div class="form-group">
                                <input class="btn btn-primary" name="submit" value="进入实验楼" type="submit">
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
                                    <input name="email" class="form-control" placeholder="请输入邮箱" type="email">
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="input-group">
                                    <div class="input-group-addon">
                                        <i class="fa fa-lock" style="margin:0;"></i>
                                    </div>
                                    <input name="password" class="form-control" placeholder="请输入密码" type="password">
                                </div>
                            </div>
                            <div class="form-inline">
                                <div class="form-group">
                                    <div class="input-group">
                                        <input name="captcha_v" class="form-control" placeholder="请输入验证码" type="text">
                                    </div>
                                </div>
                                <img class="verify-code" src="" source="/captcha.gif">
                            </div>
                            <div class="form-group">
                                <input class="btn btn-primary" name="submit" value="注册" type="submit">
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


    <div id="base-data" data-flash="false" data-is-login="true" data-jwt-token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzaGl5YW5sb3U6d2ViOmFwcCIsInVuYW1lIjoiXHU1ZTAzXHU1NTY2XHU4YzQ2IiwidWlkIjoiNjMyNDYiLCJleHAiOjE0ODgwMjkzOTMsImlhdCI6MTQ4Nzk0Mjk5M30.FqK40clE_h9Vxqkk_QVSDgZmbG726HiIQ_tvOVHGL8U" data-user-id="63246" data-is-jwt="true" data-socket-url="wss://comet.shiyanlou.com" data-msg-user="" data-msg-system=""></div>

    <!-- 不带 CSS 的库 -->
    <script async="" src="https://www.google-analytics.com/analytics.js"></script><script src="https://static.shiyanlou.com/static/babel-polyfill/6.20.0/polyfill.min.js"></script>
    <script src="/app/dist/js/manifest.js?=201702222257"></script>
    <script src="/app/dist/js/vendor.js?=201702222257"></script>

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


<div id="jinja-data" data-userlab-id="3109382" data-course-id="361" data-is-authenticated="true" data-user-joined="true" data-user-logined="true" data-show-student-info-modal="false" data-login-url="/login?next=%2Fcourses%2F361" data-start-newlab-url="/courses/clear" data-faq="/faq" data-comment-post="/courses/361/comments" data-loginurl="/login?next=%2Fcourses%2F361" data-site-type="0" data-report-post="/courses/361/reports" data-recomment-img="https://static.shiyanlou.com/img/recommentReport.png" data-charge-course-phone-code="/user/sms/code" data-join-private-course="/courses/join" data-current-user-id="63246" data-vip-icon="https://static.shiyanlou.com/img/icon-vip.png" data-vip-index="/vip" data-get-question-url="/courses/361/questions" data-real-price="" data-query-bill="/purchase/bill/query" data-question-form="/questions/meta" data-qiniu-token-url="/api/qiniu/token"></div>
<script src="/app/dist/js/course/labs.js?=201702222257"></script><div style="display: none; position: fixed; top: 0px; left: 0px; right: 0px; bottom: 0px; background: rgba(0, 0, 0, 0.5) none repeat scroll 0% 0%; text-align: center; z-index: 1600;"><i class="fa fa-spinner fa-pulse" style="margin-top: 244.4px; color: rgb(255, 255, 255); font-size: 35px;"></i></div><div id="global-zeroclipboard-html-bridge" class="global-zeroclipboard-container" style="position: absolute; left: 0px; top: -9999px; width: 1px; height: 1px; z-index: 999999999;"><object id="global-zeroclipboard-flash-bridge" name="global-zeroclipboard-flash-bridge" type="application/x-shockwave-flash" data="https://static.shiyanlou.com/static/zeroclipboard/2.3.0/ZeroClipboard.swf?noCache=1487942987732" height="100%" width="100%"><param name="allowScriptAccess" value="always"><param name="allowNetworking" value="all"><param name="menu" value="false"><param name="wmode" value="transparent"><param name="flashvars" value="trustedOrigins=www.shiyanlou.com%2C%2F%2Fwww.shiyanlou.com%2Chttps%3A%2F%2Fwww.shiyanlou.com&amp;swfObjectId=global-zeroclipboard-flash-bridge&amp;jsVersion=2.3.0"><div id="global-zeroclipboard-flash-bridge_fallbackContent">&nbsp;</div></object></div>






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
def parse_content(url, title, tag, study_num):
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text, 'lxml')
    soup = BeautifulSoup(html, 'lxml')
    type_list = soup.select('ol[class=breadcrumb] > li > a')
    types = []
    for i in type_list:
        if type_list.index(i)!=0 and type_list.index(i)!=len(type_list)-1:
            types.append(i.get_text())
    print(types)

def get_course_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    course = soup.find_all('div', {'class': 'col-md-4', 'class': 'col-sm-6', 'class': 'course'})
    for i in course:
        href = i.find('a',{'class':'course-box'}).get('href')
        title = i.find('span', {'class': 'course-title'}).get_text()
        study_people = i.find('span', {'class': 'course-per-num', 'class': 'pull-left'}).get_text()
        study_people = re.sub("\D", "", study_people)  # 数字这里有太多的空格和回车，清理一下
        study_num  = study_num + int(study_people)
        try:
            tag = i.find('span', {'class': 'course-per-num', 'class': 'pull-right'}).get_text()
        except:
            tag = "课程"
        # print("{}    学习人数:{}    {}   课程链接:{}\n".format(tag, study_people, title,host_url.format(href) ))

def main():
    res = requests.get('https://www.shiyanlou.com/courses/')
    soup = BeautifulSoup(res.text, 'lxml')
    course_link = "https://www.shiyanlou.com/courses/?course_type=all&tag=all&fee=all&page={}"
    page = soup.find_all('ul',{'class':'pagination'})
    if len(page)<1:
        print('未获得全部页面')
        return None
    li_num = page[0].find_all('li')
    page_num = 0
    for i in li_num:
        try:
            li_num = int(i.find('a').get_text())
        except:
            li_num = 0
        if li_num > page_num:
            page_num = li_num
    for i in range(1,page_num+1):
        get_course_link(course_link.format(i))


if __name__ == "__main__":
    # main()
    parse_content('www.demo.com','title','course','12138')
