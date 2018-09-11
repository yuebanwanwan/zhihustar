from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="zh" data-theme="light">
<head>
<meta charset="utf-8">
<title>vczh - 知乎</title>
<meta name="viewport"
	content="width=device-width,initial-scale=1,maximum-scale=1">
<meta name="renderer" content="webkit">
<meta name="force-rendering" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="google-site-verification"
	content="FTeR0c8arOPKh8c5DYh_9uu98_zJbaWw53J-Sch9MTg">
<title>知乎 - 有问题上知乎</title>
<meta name="description"
	content="有问题，上知乎。知乎是中文互联网知名知识分享平台，以「知识连接一切」为愿景，致力于构建一个人人都可以便捷接入的知识分享网络，让人们便捷地与世界分享知识、经验和见解，发现更大的世界。">
<link data-react-helmet="true" rel="prefetch"
	href="https://pic2.zhimg.com/80/v2-67b965aa94a92ed49b1a4205145b5cf4_r.jpg">
<link rel="shortcut icon" type="image/x-icon"
	href="https://static.zhihu.com/static/favicon.ico">
<link rel="search" type="application/opensearchdescription+xml"
	href="https://static.zhihu.com/static/search.xml" title="知乎">
<link rel="dns-prefetch" href="//static.zhimg.com">
<link rel="dns-prefetch" href="//pic1.zhimg.com">
<link rel="dns-prefetch" href="//pic2.zhimg.com">
<link rel="dns-prefetch" href="//pic3.zhimg.com">
<link rel="dns-prefetch" href="//pic4.zhimg.com">
<link
	href="https://static.zhihu.com/heifetz/main.app.a1ee5be883336a42315f.css"
	rel="stylesheet">
<script type="text/javascript" charset="utf-8" async=""
	src="https://static.zhihu.com/heifetz/main.modals.5fe5951b47e6abd38853.js"></script>
<script type="text/javascript" charset="utf-8" async=""
	src="https://static.zhihu.com/heifetz/main.signflow.1028b283e165d4f4b269.js"></script>
<style type="text/css">
.CloseIcon-icon-2xww {
	transition: opacity .3s ease-out
}

.CloseIcon-icon-2xww:hover {
	opacity: .8
}
</style>
<style type="text/css">
.animations-fadeIn-1aFv {
	animation: animations-fadeIn-1aFv .3s ease-out both
}

@
keyframes animations-fadeIn-1aFv { 0%{
	opacity: 0
}

to {
	opacity: 1
}

}
.animations-fadeOut-3XSQ {
	animation: animations-fadeOut-3XSQ .3s ease-out both
}

@
keyframes animations-fadeOut-3XSQ { 0%{
	opacity: 1
}

to {
	opacity: 0
}

}
.animations-fadeInUp-3KKK {
	animation: animations-fadeInUp-3KKK .3s cubic-bezier(.25, .1, .35, 1)
		both
}

@
keyframes animations-fadeInUp-3KKK { 0%{
	opacity: 0;
	transform: translateY(20px)
}

to {
	opacity: 1;
	transform: translateY(0)
}

}
.animations-fadeOutDown-r_A_ {
	animation: animations-fadeOutDown-r_A_ .3s cubic-bezier(.25, .1, .35, 1)
		both
}

@
keyframes animations-fadeOutDown-r_A_ { 0%{
	transform: translateY(0)
}

to {
	opacity: 0;
	transform: translateY(20px)
}
}
</style>
<style type="text/css">
.Modal-backdrop-2ksh {
	background-color: rgba(0, 0, 0, .65)
}

.Modal-backdrop-2ksh, .Modal-modalWrapper-56Mq {
	position: fixed;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	z-index: 10010
}

.Modal-modalWrapper-56Mq {
	display: -ms-flexbox;
	display: flex;
	-ms-flex-align: center;
	align-items: center;
	-ms-flex-pack: center;
	justify-content: center
}

.Modal-modal-wf58 {
	position: relative;
	z-index: 10011;
	background: #fff;
	border-radius: 2px
}

.Modal-content-3JxL {
	width: 588px;
	max-height: calc(100vh - 24px * 2);
	overflow-x: hidden;
	overflow-y: auto;
	-webkit-overflow-scrolling: touch
}

.Modal-closeButton-3JkR {
	position: absolute;
	top: 4px;
	right: -44px;
	padding: 12px;
	width: 40px;
	height: 40px;
	cursor: pointer;
	box-sizing: border-box;
	background: none;
	outline: none;
	border: none
}
</style>
<style type="text/css">
.FeedbackButton-button-3waL {
	position: fixed;
	z-index: 10000;
	bottom: 40px;
	right: 40px;
	width: 40px;
	height: 40px;
	cursor: pointer;
	border-radius: 50%;
	background-color: #fff;
	border: none;
	outline: none;
	box-shadow: 0 0 10px rgba(0, 0, 0, .15);
	font-weight: 700;
	line-height: normal
}

.FeedbackButton-icon-1Rgw {
	display: inline-block;
	vertical-align: middle;
	width: 18px;
	height: 18px;
	background-image:
		url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCAzNSAzNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+R3JvdXAgNjwvdGl0bGU+PGcgZmlsbD0iIzAwOEZFQiIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNMTMgMTguM2MwLS40IDAtLjcuNC0xIC4yLS4yLjUtLjMuOC0uMy40IDAgLjcgMCAxIC40LjIuMi4zLjUuMyAxIDAgLjIgMCAuNS0uNC43IDAgLjQtLjQuNS0uOC41LS4zIDAtLjYgMC0uOC0uNC0uMyAwLS40LS40LS40LS43ek0xMCAxMC43di0xYy40LTEgMS41LTIuNyA0LjItMi43IDIgMCAzLjggMS40IDMuOCAzcy0xLjQgMi43LTIgMy4zYy0uOC42LTEgMS0xLjIgMS43LS4yLjYtLjYgMS0xLjMgMS0uMy0uMi0uNi0uMy0uNy0uNXYtLjhjMC0uMiAwLS43LjMtMS4ybDEuNC0xLjVjMS40LTEuMiAxLjYtMiAuOC0yLjgtLjUtLjQtMS42LS41LTIuMiAwLS44LjQtMSAxLTEuMiAxLjMtLjIuNS0uMyAxLTEuMyAxLS4zLS4yLS40LS40LS41LS44eiIvPjxwYXRoIGQ9Ik0yOS44IDEwLjJ2M2MxLjQgMS44IDIuMyA0IDIuMyA2LjMgMCAzLjgtMi4yIDctNS41IDl2My44bC0zLjctMi41LTMgLjNjLTIuOCAwLTQuMy0uOC02LjQtMi4yaC0zLjFDMTMgMzAuNCAxNS42IDMyIDIwIDMyYy44IDAgMS43IDAgMi42LS4ybDYgNHYtNi40YzMuNS0yLjQgNS43LTYgNS43LTEwIDAtMy42LTEuNy03LTQuNS05LjJ6TTE0LjQgMjUuNmM4IDAgMTMuMi02IDEzLjItMTNTMjEgMCAxNC40IDBDNi40IDAgMCA1LjcgMCAxMi43YzAgNCAxLjUgNy41IDQuNCAxMFYyOWw2LjMtMy42IDMuNy4yek0xNC4yIDJjNi41IDAgMTEuNSA1LjMgMTEuNSAxMUMyNS43IDE5IDIxIDI0IDE0LjQgMjRjLTEgMC0zLjYtLjMtNC41LS41TDYgMjUuN3YtNGMtMi43LTIuMi00LTUtNC04LjZDMiA3IDcgMiAxNCAyeiIvPjwvZz48L3N2Zz4=);
	background-repeat: no-repeat;
	background-size: contain
}

.FeedbackButton-button-3waL:hover .FeedbackButton-icon-1Rgw {
	background-image:
		url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzUiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCAzNSAzNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+R3JvdXAgMTE8L3RpdGxlPjxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+PHBhdGggZD0iTTI5LjQgMTNjMCAyLS4zIDguMi01IDExLjQtNC4zIDMtOSAzLjMtMTEuMyAzLjNoLTNjMi44IDIuNyA2LjYgNC44IDEyLjIgNCAxIDAgNi4zIDQgNi4zIDRWMjljMy41LTIuMyA1LjMtNS4yIDUuNi05LjUuMy0zLjctMS42LTctNC41LTkuNXYzem0tMTUgMTIuNmM4IDAgMTMuMi02IDEzLjItMTNTMjEgMCAxNC40IDBDNi40IDAgMCA1LjcgMCAxMi43YzAgNCAxLjUgNy41IDQuNCAxMFYyOWw2LjMtMy42IDMuNy4zeiIgZmlsbD0iIzAwOEZFQiIvPjxwYXRoIGQ9Ik0xMyAxOC4zYzAtLjQgMC0uNy40LTFzLjUtLjMuOC0uM2MuNCAwIC43IDAgMSAuNC4yLjIuMy41LjMgMSAwIC4yIDAgLjUtLjQuNyAwIC40LS40LjUtLjguNS0uMyAwLS42IDAtLjgtLjQtLjMgMC0uNC0uNC0uNC0uN3ptLTMtNy42di0xYy40LTEgMS40LTIuNyA0LjItMi43IDIgMCAzLjggMS40IDMuOCAzcy0xLjQgMi43LTIgMy4zYy0uOC42LTEgMS0xLjIgMS43LS4yLjYtLjYgMS0xLjMgMS0uMy0uMi0uNi0uMy0uNy0uNXYtLjhjMC0uMiAwLS43LjMtMS4ybDEuNC0xLjVjMS40LTEuMiAxLjYtMiAuOC0yLjgtLjUtLjQtMS42LS41LTIuMiAwLS44LjQtMSAxLTEuMiAxLjMtLjIuNS0uMyAxLTEuMyAxLS4zLS4yLS40LS40LS41LS44eiIgZmlsbD0iI0ZGRiIvPjwvZz48L3N2Zz4=)
}
</style>
<style type="text/css">
.DrawingExample-svg-30WA {
	position: absolute;
	top: 30px;
	right: 0;
	left: 0;
	margin: auto;
	transform: rotate(-44deg)
}

.DrawingExample-ellipse-26bv {
	stroke-dasharray: 520;
	transform-origin: center;
	animation: DrawingExample-drawingExample-3Bm3 .6s linear both
}

@
keyframes DrawingExample-drawingExample-3Bm3 { 0%{
	stroke-dashoffset: 520
}

50%{
stroke-dashoffset
:
1000;opacity
:
1
}
to {
	stroke-dashoffset: 1000;
	opacity: 0
}
}
</style>
<style type="text/css">
.Spinner-spinner-2PGn {
	position: absolute;
	width: 30px;
	height: 30px;
	top: 50%;
	left: 50%;
	margin: -15px 0 0 -15px;
	animation: Spinner-rotate-RMMJ .8s linear infinite
}

.Spinner-spinner-2PGn .Spinner-circle-teFy {
	stroke: #4197ff;
	stroke-dasharray: 187;
	stroke-dashoffset: 46.75;
	transform-origin: center
}

@
keyframes Spinner-rotate-RMMJ { 0%{
	transform: rotate(0deg)
}

to {
	transform: rotate(1turn)
}
}
</style>
<style type="text/css">
.FeedbackForm-form-1uUg {
	padding: 40px 24px 32px;
	width: 100%;
	font-size: 14px;
	line-height: 1.5;
	font-family: HelveticaNeue-Light, Helvetica, PingFangSC-Light,
		Hiragino Sans GB, Microsoft YaHei, Arial, sans-serif;
	color: #404040;
	box-sizing: border-box
}

.FeedbackForm-header-3hQI {
	margin-bottom: 26px;
	text-align: center
}

.FeedbackForm-title-2uCC {
	font-size: 24px;
	font-weight: 500;
	line-height: 33px;
	font-family: Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei,
		Arial, sans-serif
}

.FeedbackForm-inputBox-15yJ {
	display: block;
	padding: 12px;
	width: 100%;
	height: auto;
	font-size: 15px;
	border: 1px solid #e7eaf1;
	border-radius: 3px;
	box-sizing: border-box;
	resize: none;
	outline: none;
	color: inherit;
	transition: box-shadow .15s ease-out;
	overflow: auto
}

.FeedbackForm-inputBox-15yJ::-webkit-input-placeholder {
	color: #9aaabf;
	transition: color .15s ease-out
}

.FeedbackForm-inputBox-15yJ:-ms-input-placeholder {
	color: #9aaabf;
	transition: color .15s ease-out
}

.FeedbackForm-inputBox-15yJ::placeholder {
	color: #9aaabf;
	transition: color .15s ease-out
}

.FeedbackForm-inputBox-15yJ:hover::-webkit-input-placeholder {
	color: rgba(154, 170, 191, .8)
}

.FeedbackForm-inputBox-15yJ:hover:-ms-input-placeholder {
	color: rgba(154, 170, 191, .8)
}

.FeedbackForm-inputBox-15yJ:hover::placeholder {
	color: rgba(154, 170, 191, .8)
}

.FeedbackForm-inputBox-15yJ:focus {
	box-shadow: 0 0 5px #e7eaf1
}

.FeedbackForm-inputBox-15yJ:focus::-webkit-input-placeholder {
	color: rgba(154, 170, 191, .8)
}

.FeedbackForm-inputBox-15yJ:focus:-ms-input-placeholder {
	color: rgba(154, 170, 191, .8)
}

.FeedbackForm-inputBox-15yJ:focus::placeholder {
	color: rgba(154, 170, 191, .8)
}

.FeedbackForm-inputBox-15yJ.FeedbackForm-isWarning-2ds- {
	border-color: #f75659
}

.FeedbackForm-inputBox-15yJ.FeedbackForm-isWarning-2ds-::-webkit-input-placeholder
	{
	color: #f75659
}

.FeedbackForm-inputBox-15yJ.FeedbackForm-isWarning-2ds-:-ms-input-placeholder
	{
	color: #f75659
}

.FeedbackForm-inputBox-15yJ.FeedbackForm-isWarning-2ds-::placeholder {
	color: #f75659
}

.FeedbackForm-inputBox-15yJ.FeedbackForm-isWarning-2ds-:focus {
	box-shadow: none
}

.FeedbackForm-screenShot--Gsn {
	overflow: hidden;
	box-sizing: border-box;
	transition: max-height .3s ease, opacity .3s ease
}

.FeedbackForm-screenShotLabel-2Sgh {
	padding-top: 22px;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

.FeedbackForm-canvasContainer-mrde {
	margin-top: 8px;
	position: relative;
	background-color: #f6f7f9
}

.FeedbackForm-canvas-tSGI {
	display: block;
	max-width: 100%;
	cursor:
		url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAABGdBTUEAALGPC/xhBQAAARpJREFUOBGdkr1KA0EUhTcxEkSQQIpAihQWPoedD2BnIVsZQiBVEkiR7SwtBDsJqXwBLQwEgoWNjY2FjYUQ38Ei5Oc7sBeGLTKze+Djzsyecxh2N4ryq0zkHpYQQ2H1SW5TNsxukaZzQsewACvTvIBg3eFUaABHMEv3OruBIN3icm8wZl+FZ3iBQ/AqweGW2FrlKlChV0McFsxOvaegm/T2lLzzTC/dqzaO7A1s/8GzE28Dhhj0f1jQnZ+c18CrKxxrcMO2/uK87m3AcAkrsKA7vzlvQJAmuNywrX84bwY1YBrBATyCFWj+QguCJKNCU1DZQ7r/Y55CsK5x2i2eWFcggTPIJd3Eiv5Zd3KlU3OJOQd9lVd4A5Xl1g4YG2GGhwRfegAAAABJRU5ErkJggg==)
		0 17, default;
	cursor: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAABGdBTUEAALGPC/xhBQAAARpJREFUOBGdkr1KA0EUhTcxEkSQQIpAihQWPoedD2BnIVsZQiBVEkiR7SwtBDsJqXwBLQwEgoWNjY2FjYUQ38Ei5Oc7sBeGLTKze+Djzsyecxh2N4ryq0zkHpYQQ2H1SW5TNsxukaZzQsewACvTvIBg3eFUaABHMEv3OruBIN3icm8wZl+FZ3iBQ/AqweGW2FrlKlChV0McFsxOvaegm/T2lLzzTC/dqzaO7A1s/8GzE28Dhhj0f1jQnZ+c18CrKxxrcMO2/uK87m3AcAkrsKA7vzlvQJAmuNywrX84bwY1YBrBATyCFWj+QguCJKNCU1DZQ7r/Y55CsK5x2i2eWFcggTPIJd3Eiv5Zd3KlU3OJOQd9lVd4A5Xl1g4YG2GGhwRfegAAAABJRU5ErkJggg==)
		1x,
		url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAABGdBTUEAALGPC/xhBQAAAn9JREFUWAnFlz1IV2EUxs2+ixCCrCCrIaiGGnLIRdBacqkhtCEbqqVaoqmacpIma6rFHHITh1pKMKFaInATkb4hKChKIwj7rt8D74XDy3tfKM69Hng4zz3nvc9zfH3/93//DQ31xWqsBsEnMAU6wILFSpwnwB+Db/BDoPZYjuMYsMMU/Af1nron2o7hh5KBNNhP0AtqjV24vQPFzsT5F70jVU7UiPhNcNyY7IC/AfEwxfUsvcVmvRtdhNIQkNFvcAoUsQ3yGhRDxLmpWOiZryUMzxqDrfCXiTXjZo0bvZIwKnbhvHHZBH9q1s7Am03fhV42BsUQcb5knDbAp8EzsNHUXWgfKrF52XW/cVwH1265xgXUyszL6gOuExixc/8xjIZ8C9YbHRd6GpWyHcjV33PfTpcJjMgJuJ4xOeNU7yP37DY6LvQoKnrUpwxzNb12tLpMYES64foyzBmnep+5p83ouNCDqHwHKcNc7Qv3tLtMYEQOwPVClTNO9ea5Z7/RcaH7UJFwyjBX0x/Q5TKBEdFWa8tzxqme3gTdX0/3IqrDmDLM1XTodfhdYw9qcyBnnOrpcdDrOglienDpAZYyzNX0oDwJ3GMUxZxxWe+M+yRBcBX53j8OpS9Z9ziM4tKguoJ8B5Tthq1fDPe4p+co3gbLgrLyLWDNY94X1rqnFmN8F64dUiwBIyAeRNd6Za0sjqFsTXWGdJYU+q00DGz/qhpVxg3EraH4Q7AmmDaSB4Hq10Ot0vQimMVDPaLeFJz1A1DvQsqVxmbU40Hs9ST9tZVOYMT1r+gw1zF9ReEx2BI3qrrWp6jTiH+FPwD6pI2BJ6DW0HkYBzNAQ9wH82DB4i/kUnkzGX+skQAAAABJRU5ErkJggg==)
		2x) 0 17, default
}

.FeedbackForm-canvas-tSGI.FeedbackForm-isCapturing-3UFp {
	display: none
}

.FeedbackForm-checkLabelWrapper-3B7w {
	margin-top: 12px
}

.FeedbackForm-checkLabel-2VTb {
	cursor: pointer;
	color: #9aaabf;
	transition: color .15s ease-out;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

.FeedbackForm-checkLabel-2VTb:hover {
	color: rgba(154, 170, 191, .8)
}

.FeedbackForm-checkLabel-2VTb input {
	margin-right: .5em;
	vertical-align: 1px
}

.FeedbackForm-actions-dJ87 {
	margin-top: 40px;
	text-align: center
}

.FeedbackForm-submitButton-1oKQ {
	display: inline-block;
	min-width: 220px;
	padding: 8px 1em;
	background-color: #0f88eb;
	border: 1px solid #0f88eb;
	border-radius: 3px;
	font: inherit;
	color: #fff;
	transition: background-color .15s ease-out, opacity .15s ease-out;
	cursor: pointer;
	outline: none
}

.FeedbackForm-submitButton-1oKQ[disabled] {
	opacity: .8;
	cursor: default
}

.FeedbackForm-submitButton-1oKQ:hover {
	background-color: #0d79d1
}

.FeedbackForm-submitButton-1oKQ:active {
	opacity: .8
}

.FeedbackForm-successMask-34go {
	display: -ms-flexbox;
	display: flex;
	-ms-flex-pack: center;
	justify-content: center;
	-ms-flex-align: center;
	align-items: center;
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: #fff
}

.FeedbackForm-successTitle-1Y6p {
	font-size: 24px;
	font-weight: 500;
	line-height: 33px;
	font-family: Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei,
		Arial, sans-serif;
	text-align: center
}

.FeedbackForm-successSubtitle-A_aP {
	margin-top: 10px;
	font-size: 18px;
	line-height: 33px;
	text-align: center
}
</style>
</head>
<body class="Entry-body">
	<div id="root">
		<div data-zop-usertoken="{}">
			<div class="LoadingBar"></div>
			<div>
				<header role="banner" class="Sticky AppHeader"
					data-za-module="TopNavBar">
					<div class="AppHeader-inner">
						<a href="//www.zhihu.com" aria-label="知乎"><svg
								viewBox="0 0 200 91"
								class="Icon ZhihuLogo ZhihuLogo--blue Icon--logo" width="64"
								height="30" aria-hidden="true"
								style="height: 30px; width: 64px;">
								<title></title><g>
								<path
									d="M53.29 80.035l7.32.002 2.41 8.24 13.128-8.24h15.477v-67.98H53.29v67.978zm7.79-60.598h22.756v53.22h-8.73l-8.718 5.473-1.587-5.46-3.72-.012v-53.22zM46.818 43.162h-16.35c.545-8.467.687-16.12.687-22.955h15.987s.615-7.05-2.68-6.97H16.807c1.09-4.1 2.46-8.332 4.1-12.708 0 0-7.523 0-10.085 6.74-1.06 2.78-4.128 13.48-9.592 24.41 1.84-.2 7.927-.37 11.512-6.94.66-1.84.785-2.08 1.605-4.54h9.02c0 3.28-.374 20.9-.526 22.95H6.51c-3.67 0-4.863 7.38-4.863 7.38H22.14C20.765 66.11 13.385 79.24 0 89.62c6.403 1.828 12.784-.29 15.937-3.094 0 0 7.182-6.53 11.12-21.64L43.92 85.18s2.473-8.402-.388-12.496c-2.37-2.788-8.768-10.33-11.496-13.064l-4.57 3.627c1.363-4.368 2.183-8.61 2.46-12.71H49.19s-.027-7.38-2.372-7.38zm128.752-.502c6.51-8.013 14.054-18.302 14.054-18.302s-5.827-4.625-8.556-1.27c-1.874 2.548-11.51 15.063-11.51 15.063l6.012 4.51zm-46.903-18.462c-2.814-2.577-8.096.667-8.096.667s12.35 17.2 12.85 17.953l6.08-4.29s-8.02-11.752-10.83-14.33zM199.99 46.5c-6.18 0-40.908.292-40.953.292v-31.56c1.503 0 3.882-.124 7.14-.376 12.773-.753 21.914-1.25 27.427-1.504 0 0 3.817-8.496-.185-10.45-.96-.37-7.24 1.43-7.24 1.43s-51.63 5.153-72.61 5.64c.5 2.756 2.38 5.336 4.93 6.11 4.16 1.087 7.09.53 15.36.277 7.76-.5 13.65-.76 17.66-.76v31.19h-41.71s.88 6.97 7.97 7.14h33.73v22.16c0 4.364-3.498 6.87-7.65 6.6-4.4.034-8.15-.36-13.027-.566.623 1.24 1.977 4.496 6.035 6.824 3.087 1.502 5.054 2.053 8.13 2.053 9.237 0 14.27-5.4 14.027-14.16V53.93h38.235c3.026 0 2.72-7.432 2.72-7.432z"
									fill-rule="evenodd"></path></g></svg></a>
						<nav role="navigation" class="AppHeader-nav">
							<a class="AppHeader-navItem" href="//www.zhihu.com/"
								data-za-not-track-link="true">首页</a><a class="AppHeader-navItem"
								href="//www.zhihu.com/explore" data-za-not-track-link="true">发现</a><a
								href="//www.zhihu.com/topic" class="AppHeader-navItem"
								data-za-not-track-link="true">话题</a>
						</nav>
						<div class="SearchBar" role="search"
							data-za-module="PresetWordItem">
							<div class="SearchBar-toolWrapper">
								<form class="SearchBar-tool">
									<div>
										<div class="Popover">
											<div
												class="SearchBar-input Input-wrapper Input-wrapper--grey">
												<input type="text" maxlength="100" autocomplete="off"
													role="combobox" aria-expanded="false"
													aria-autocomplete="list"
													aria-activedescendant="AutoComplete2--1"
													id="Popover1-toggle" aria-haspopup="true"
													aria-owns="Popover1-content" class="Input"
													placeholder="男生秋季穿搭" value="">
												<div class="Input-after">
													<button aria-label="搜索" type="button"
														class="Button SearchBar-searchIcon Button--primary">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Search" fill="currentColor"
																viewBox="0 0 24 24" width="18" height="18">
																<path
																	d="M17.068 15.58a8.377 8.377 0 0 0 1.774-5.159 8.421 8.421 0 1 0-8.42 8.421 8.38 8.38 0 0 0 5.158-1.774l3.879 3.88c.957.573 2.131-.464 1.488-1.49l-3.879-3.878zm-6.647 1.157a6.323 6.323 0 0 1-6.316-6.316 6.323 6.323 0 0 1 6.316-6.316 6.323 6.323 0 0 1 6.316 6.316 6.323 6.323 0 0 1-6.316 6.316z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
											</div>
										</div>
									</div>
								</form>
							</div>
						</div>
						<div class="AppHeader-userInfo">
							<div class="AppHeader-profile">
								<div>
									<button type="button"
										class="Button AppHeader-login Button--blue">登录</button>
									<button type="button"
										class="Button Button--primary Button--blue">加入知乎</button>
								</div>
							</div>
						</div>
					</div>
					<div class="PageHeader">
						<div class="ProfileMain-header">
							<div class="ProfileMain-avatar">
								<img class="Avatar" width="38" height="38"
									src="https://pic3.zhimg.com/v2-1bea18837914ab5a40537d515ed3219c_xs.jpg"
									srcset="https://pic3.zhimg.com/v2-1bea18837914ab5a40537d515ed3219c_l.jpg 2x">
							</div>
							<ul role="tablist" class="Tabs ProfileMain-tabs">
								<li role="tab" class="Tabs-item Tabs-item--noMeta"
									aria-controls="Profile-activities"><a
									class="Tabs-link is-active"
									href="/people/excited-vczh/activities">动态</a></li>
								<li role="tab" class="Tabs-item" aria-controls="Profile-answers"><a
									class="Tabs-link" href="/people/excited-vczh/answers">回答<span
										class="Tabs-meta">20,437</span></a></li>
								<li role="tab" class="Tabs-item" aria-controls="Profile-asks"><a
									class="Tabs-link" href="/people/excited-vczh/asks">提问<span
										class="Tabs-meta">544</span></a></li>
								<li role="tab" class="Tabs-item" aria-controls="Profile-posts"><a
									class="Tabs-link" href="/people/excited-vczh/posts">文章<span
										class="Tabs-meta">119</span></a></li>
								<li role="tab" class="Tabs-item" aria-controls="Profile-columns"><a
									class="Tabs-link" href="/people/excited-vczh/columns">专栏<span
										class="Tabs-meta">5</span></a></li>
								<li role="tab" class="Tabs-item" aria-controls="Profile-pins"><a
									meta="1,956" class="Tabs-link" href="/people/excited-vczh/pins">想法<span
										class="Tabs-meta">1956</span></a></li>
								<li role="tab" class="Tabs-item Tabs-item--noMeta"><div
										class="Popover Tabs-link">
										<button type="button" id="Popover22-toggle"
											aria-haspopup="true" aria-expanded="false"
											aria-owns="Popover22-content"
											class="Button ProfileMain-menuToggler Button--plain">
											更多
											<svg viewBox="0 0 10 6"
												class="Icon ProfileMain-tabIcon Icon--arrow" width="10"
												height="16" aria-hidden="true"
												style="height: 16px; width: 10px;">
												<title></title><g>
												<path
													d="M8.716.217L5.002 4 1.285.218C.99-.072.514-.072.22.218c-.294.29-.294.76 0 1.052l4.25 4.512c.292.29.77.29 1.063 0L9.78 1.27c.293-.29.293-.76 0-1.052-.295-.29-.77-.29-1.063 0z"></path></g></svg>
										</button>
									</div></li>
							</ul>
							<div
								class="MemberButtonGroup ProfileButtonGroup ProfileMain-buttons">
								<button type="button"
									class="Button FollowButton Button--primary Button--blue">
									<span style="display: inline-flex; align-items: center;">​<svg
											class="Zi Zi--Plus FollowButton-icon" fill="currentColor"
											viewBox="0 0 24 24" width="1.2em" height="1.2em">
											<path
												d="M13.491 10.488s-.012-5.387 0-5.998c-.037-1.987-3.035-1.987-2.997 0-.038 1.912 0 5.998 0 5.998H4.499c-1.999.01-1.999 3.009 0 3.009s5.995-.01 5.995-.01v5.999c0 2.019 3.006 2.019 2.997 0-.01-2.019 0-5.998 0-5.998s3.996.009 6.004.009c2.008 0 2.008-3-.01-3.009h-5.994z"
												fill-rule="evenodd"></path></svg></span>关注他
								</button>
								<button type="button"
									class="Button Button--grey Button--withIcon Button--withLabel">
									<span style="display: inline-flex; align-items: center;">​<svg
											class="Zi Zi--Comments Button-zi" fill="currentColor"
											viewBox="0 0 24 24" width="1.2em" height="1.2em">
											<path
												d="M11 2c5.571 0 9 4.335 9 8 0 6-6.475 9.764-11.481 8.022-.315-.07-.379-.124-.78.078-1.455.54-2.413.921-3.525 1.122-.483.087-.916-.25-.588-.581 0 0 .677-.417.842-1.904.064-.351-.14-.879-.454-1.171A8.833 8.833 0 0 1 2 10c0-3.87 3.394-8 9-8zm10.14 9.628c.758.988.86 2.009.86 3.15 0 1.195-.619 3.11-1.368 3.938-.209.23-.354.467-.308.722.12 1.073.614 1.501.614 1.501.237.239-.188.562-.537.5-.803-.146-1.495-.42-2.546-.811-.29-.146-.336-.106-.563-.057-2.043.711-4.398.475-6.083-.927 5.965-.524 8.727-3.03 9.93-8.016z"
												fill-rule="evenodd"></path></svg></span>发私信
								</button>
							</div>
						</div>
					</div>
				</header>
			</div>
			<main role="main" class="App-main">
			<div itemprop="people" itemtype="http://schema.org/Person"
				itemscope="">
				<meta itemprop="url"
					content="https://www.zhihu.com/people/excited-vczh">
				<meta itemprop="gender" content="Male">
				<meta itemprop="image"
					content="https://pic3.zhimg.com/v2-1bea18837914ab5a40537d515ed3219c_is.jpg">
				<meta itemprop="zhihu:voteupCount" content="2320099">
				<meta itemprop="zhihu:thankedCount" content="251575">
				<meta itemprop="zhihu:followerCount" content="756129">
				<meta itemprop="zhihu:answerCount" content="20437">
				<meta itemprop="zhihu:articlesCount" content="119">
				<div id="ProfileHeader" class="ProfileHeader">
					<div class="Card">
						<div class="ProfileHeader-userCover">
							<div class="UserCover">
								<img class="UserCover-image"
									src="https://pic2.zhimg.com/80/v2-67b965aa94a92ed49b1a4205145b5cf4_r.jpg"
									alt="用户封面">
							</div>
						</div>
						<div class="ProfileHeader-wrapper">
							<div class="ProfileHeader-main">
								<div class="UserAvatar ProfileHeader-avatar" style="top: -25px;">
									<img class="Avatar Avatar--large UserAvatar-inner" width="160"
										height="160"
										src="https://pic3.zhimg.com/v2-1bea18837914ab5a40537d515ed3219c_xl.jpg"
										srcset="https://pic3.zhimg.com/v2-1bea18837914ab5a40537d515ed3219c_xll.jpg 2x">
								</div>
								<div class="ProfileHeader-content">
									<div class="ProfileHeader-contentHead">
										<h1 class="ProfileHeader-title">
											<span class="ProfileHeader-name">vczh</span><span
												class="RichText ztext ProfileHeader-headline">专业造轮子，拉黑抢前排。<a
												href="https://link.zhihu.com/?target=http%3A//gaclib.net"
												class=" external" target="_blank" rel="nofollow noreferrer"
												data-za-detail-view-id="1043"><span class="invisible">http://</span><span
													class="visible">gaclib.net</span><span class="invisible"></span></a></span>
										</h1>
									</div>
									<div class="ProfileHeader-contentBody"
										style="overflow: hidden; transition: height 300ms ease-out; -webkit-transition: height 300ms ease-out; height: 50px;">
										<div>
											<div class="ProfileHeader-info">
												<div class="ProfileHeader-infoItem">
													<div class="ProfileHeader-iconWrapper">
														<svg viewBox="0 0 20 18" class="Icon Icon--company"
															width="13" height="16" aria-hidden="true"
															style="height: 16px; width: 13px;">
															<title></title><g>
															<path
																d="M15 3.998v-2C14.86.89 13.98 0 13 0H7C5.822 0 5.016.89 5 2v2l-3.02-.002c-1.098 0-1.97.89-1.97 2L0 16c0 1.11.882 2 1.98 2h16.033c1.1 0 1.98-.89 1.987-2V6c-.007-1.113-.884-2.002-1.982-2.002H15zM7 4V2.5s-.004-.5.5-.5h5c.5 0 .5.5.5.5V4H7z"></path></g></svg>
													</div>
													计算机软件
													<div class="ProfileHeader-divider"></div>
													Microsoft Office
													<div class="ProfileHeader-divider"></div>
													Developer
												</div>
												<div class="ProfileHeader-infoItem">
													<div class="ProfileHeader-iconWrapper">
														<svg viewBox="0 0 22 16" class="Icon Icon--education"
															width="16" height="16" aria-hidden="true"
															style="height: 16px; width: 16px;">
															<title></title><g>
															<path
																d="M11 0L0 3.94v.588l4.153 2.73v5.166C4.158 12.758 7.028 16 11 16c3.972 0 6.808-3.116 6.85-3.576l.006-5.163 4.13-2.732.014-.586L11 0z"></path></g></svg>
													</div>
													华南理工大学
													<div class="ProfileHeader-divider"></div>
													软件学院
													<div class="ProfileHeader-divider"></div>
													<div class="ProfileHeader-iconWrapper">
														<svg width="14" height="16" viewBox="0 0 14 14"
															class="Icon Icon--male" aria-hidden="true"
															style="height: 16px; width: 14px;">
															<title></title><g>
															<path
																d="M3.025 10.64c-1.367-1.366-1.367-3.582 0-4.95 1.367-1.366 3.583-1.366 4.95 0 1.367 1.368 1.367 3.584 0 4.95-1.367 1.368-3.583 1.368-4.95 0zm10.122-9.368c-.002-.414-.34-.75-.753-.753L8.322 0c-.413-.002-.746.33-.744.744.002.413.338.75.75.752l2.128.313c-.95.953-1.832 1.828-1.832 1.828-2.14-1.482-5.104-1.27-7.013.64-2.147 2.147-2.147 5.63 0 7.777 2.15 2.148 5.63 2.148 7.78 0 1.908-1.91 2.12-4.873.636-7.016l1.842-1.82.303 2.116c.003.414.34.75.753.753.413.002.746-.332.744-.745l-.52-4.073z"
																fill-rule="evenodd"></path></g></svg>
													</div>
												</div>
											</div>
										</div>
									</div>
									<div class="ProfileHeader-contentFooter">
										<button type="button"
											class="Button ProfileHeader-expandButton Button--plain">
											<svg viewBox="0 0 10 6"
												class="Icon ProfileHeader-arrowIcon Icon--arrow" width="10"
												height="16" aria-hidden="true"
												style="height: 16px; width: 10px;">
												<title></title><g>
												<path
													d="M8.716.217L5.002 4 1.285.218C.99-.072.514-.072.22.218c-.294.29-.294.76 0 1.052l4.25 4.512c.292.29.77.29 1.063 0L9.78 1.27c.293-.29.293-.76 0-1.052-.295-.29-.77-.29-1.063 0z"></path></g></svg>
											查看详细资料
										</button>
										<div
											class="MemberButtonGroup ProfileButtonGroup ProfileHeader-buttons">
											<button type="button"
												class="Button FollowButton Button--primary Button--blue">
												<span style="display: inline-flex; align-items: center;">​<svg
														class="Zi Zi--Plus FollowButton-icon" fill="currentColor"
														viewBox="0 0 24 24" width="1.2em" height="1.2em">
														<path
															d="M13.491 10.488s-.012-5.387 0-5.998c-.037-1.987-3.035-1.987-2.997 0-.038 1.912 0 5.998 0 5.998H4.499c-1.999.01-1.999 3.009 0 3.009s5.995-.01 5.995-.01v5.999c0 2.019 3.006 2.019 2.997 0-.01-2.019 0-5.998 0-5.998s3.996.009 6.004.009c2.008 0 2.008-3-.01-3.009h-5.994z"
															fill-rule="evenodd"></path></svg></span>关注他
											</button>
											<button type="button"
												class="Button Button--grey Button--withIcon Button--withLabel">
												<span style="display: inline-flex; align-items: center;">​<svg
														class="Zi Zi--Comments Button-zi" fill="currentColor"
														viewBox="0 0 24 24" width="1.2em" height="1.2em">
														<path
															d="M11 2c5.571 0 9 4.335 9 8 0 6-6.475 9.764-11.481 8.022-.315-.07-.379-.124-.78.078-1.455.54-2.413.921-3.525 1.122-.483.087-.916-.25-.588-.581 0 0 .677-.417.842-1.904.064-.351-.14-.879-.454-1.171A8.833 8.833 0 0 1 2 10c0-3.87 3.394-8 9-8zm10.14 9.628c.758.988.86 2.009.86 3.15 0 1.195-.619 3.11-1.368 3.938-.209.23-.354.467-.308.722.12 1.073.614 1.501.614 1.501.237.239-.188.562-.537.5-.803-.146-1.495-.42-2.546-.811-.29-.146-.336-.106-.563-.057-2.043.711-4.398.475-6.083-.927 5.965-.524 8.727-3.03 9.93-8.016z"
															fill-rule="evenodd"></path></svg></span>发私信
											</button>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="Profile-main">
					<div class="Profile-mainColumn">
						<div class="Card ProfileMain" id="ProfileMain">
							<div class="ProfileMain-header">
								<ul role="tablist" class="Tabs ProfileMain-tabs">
									<li role="tab" class="Tabs-item Tabs-item--noMeta"
										aria-controls="Profile-activities"><a
										class="Tabs-link is-active"
										href="/people/excited-vczh/activities">动态</a></li>
									<li role="tab" class="Tabs-item"
										aria-controls="Profile-answers"><a class="Tabs-link"
										href="/people/excited-vczh/answers">回答<span
											class="Tabs-meta">20,437</span></a></li>
									<li role="tab" class="Tabs-item" aria-controls="Profile-asks"><a
										class="Tabs-link" href="/people/excited-vczh/asks">提问<span
											class="Tabs-meta">544</span></a></li>
									<li role="tab" class="Tabs-item" aria-controls="Profile-posts"><a
										class="Tabs-link" href="/people/excited-vczh/posts">文章<span
											class="Tabs-meta">119</span></a></li>
									<li role="tab" class="Tabs-item"
										aria-controls="Profile-columns"><a class="Tabs-link"
										href="/people/excited-vczh/columns">专栏<span
											class="Tabs-meta">5</span></a></li>
									<li role="tab" class="Tabs-item" aria-controls="Profile-pins"><a
										meta="1,956" class="Tabs-link"
										href="/people/excited-vczh/pins">想法<span class="Tabs-meta">1956</span></a></li>
									<li role="tab" class="Tabs-item Tabs-item--noMeta"><div
											class="Popover Tabs-link">
											<button type="button" id="Popover3-toggle"
												aria-haspopup="true" aria-expanded="false"
												aria-owns="Popover3-content"
												class="Button ProfileMain-menuToggler Button--plain">
												更多
												<svg viewBox="0 0 10 6"
													class="Icon ProfileMain-tabIcon Icon--arrow" width="10"
													height="16" aria-hidden="true"
													style="height: 16px; width: 10px;">
													<title></title><g>
													<path
														d="M8.716.217L5.002 4 1.285.218C.99-.072.514-.072.22.218c-.294.29-.294.76 0 1.052l4.25 4.512c.292.29.77.29 1.063 0L9.78 1.27c.293-.29.293-.76 0-1.052-.295-.29-.77-.29-1.063 0z"></path></g></svg>
											</button>
										</div></li>
								</ul>
							</div>
							<div>
								<div>
									<div class="Sticky"></div>
								</div>
							</div>
							<div class="List ProfileActivities" id="Profile-activities"
								data-zop-feedlistfather="1">
								<div class="List-header">
									<h4 class="List-headerText">
										<span>他的动态</span>
									</h4>
									<div class="List-headerOptions"></div>
								</div>
								<div class="">
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">关注了问题</span><span>10
													分钟前</span>
											</div>
										</div>
										<div class="ContentItem">
											<h2 class="ContentItem-title">
												<div class="QuestionItem-title">
													<a href="/question/278924100" target="_blank"
														data-za-detail-view-name="Title">fgo氪多少可以被定义为“无氪”，“微氪”“中氪”“重氪”？</a>
												</div>
											</h2>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>1
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;弗兰切斯卡&quot;,&quot;itemId&quot;:474823126,&quot;title&quot;:&quot;fsn中fate线红A与海克力士一战为何仅杀六命后战死？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="474823126" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/291333347">
													<meta itemprop="name"
														content="fsn中fate线红A与海克力士一战为何仅杀六命后战死？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/291333347/answer/474823126">fsn中fate线红A与海克力士一战为何仅杀六命后战死？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="弗兰切斯卡">
													<meta itemprop="image"
														content="https://pic3.zhimg.com/50/v2-2c1eb78513c7cdd404da4f7593c5b47e_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/jia-hao-yang-24">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover4-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover4-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/jia-hao-yang-24"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic3.zhimg.com/50/v2-2c1eb78513c7cdd404da4f7593c5b47e_xs.jpg"
																	srcset="https://pic3.zhimg.com/50/v2-2c1eb78513c7cdd404da4f7593c5b47e_l.jpg 2x"
																	alt="弗兰切斯卡"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover5-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover5-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/jia-hao-yang-24">弗兰切斯卡</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">那个吉尔居然也成了英灵
																	还是caster 都是我的错</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">60 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="60">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/291333347/answer/474823126">
											<meta itemprop="dateCreated"
												content="2018-08-21T17:09:30.000Z">
											<meta itemprop="dateModified"
												content="2018-08-22T08:53:24.000Z">
											<meta itemprop="commentCount" content="215">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">分条回答你的问题 1.赫拉克勒斯的十二试炼宝具
														实际上可以无效化等级B以下的攻击 王之宝库作为英灵宝具的原典与出处 其中有很多B与B级以上的宝具并没有问题
														反而是无限剑制 其中的宝具等级比原版低一级 到底有多少B级及以上宝具还有待考虑
														2.士郎在UBW线中通过无限剑制战胜闪闪 实际上是武技的胜利 闪闪因为王之宝库与天之锁…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 60
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>215 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover6-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover6-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;Respirology&quot;,&quot;itemId&quot;:114302355,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="114302355" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/114302355">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="Respirology">
													<meta itemprop="image"
														content="https://pic1.zhimg.com/50/v2-c6200b9b1763efa924a4f642d8c7ad6f_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/respirology-46">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover7-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover7-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/respirology-46"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic1.zhimg.com/50/v2-c6200b9b1763efa924a4f642d8c7ad6f_xs.jpg"
																	srcset="https://pic1.zhimg.com/50/v2-c6200b9b1763efa924a4f642d8c7ad6f_l.jpg 2x"
																	alt="Respirology"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover8-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover8-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/respirology-46">Respirology</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">医学博士（网上不看病）</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">63 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="63">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/114302355">
											<meta itemprop="dateCreated"
												content="2016-08-01T00:17:17.000Z">
											<meta itemprop="dateModified"
												content="2016-08-01T00:17:17.000Z">
											<meta itemprop="commentCount" content="20">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">必须有泰国菜“冬阴功”啊～
														听起来是不是有很费精力又要熬好久好久的感觉？ 实际呢，这是个音译，“冬阴”是泰国的一种酸辣调料，“功”是虾的意思。
														翻译成酸辣虾汤是不是瞬间就没有逼格了～ 我记得还有个泰国功夫片也叫“冬阴功”，简直莫名其妙～…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 63
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>20 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover9-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover9-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;Lea Liu&quot;,&quot;itemId&quot;:487507865,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="487507865" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/487507865">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="Lea Liu">
													<meta itemprop="image"
														content="https://pic2.zhimg.com/50/120639e58ddf09991f4901416fc67350_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/lea-liu-23">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover10-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover10-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/lea-liu-23"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic2.zhimg.com/50/120639e58ddf09991f4901416fc67350_xs.jpg"
																	srcset="https://pic2.zhimg.com/50/120639e58ddf09991f4901416fc67350_l.jpg 2x"
																	alt="Lea Liu"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover11-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover11-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/lea-liu-23">Lea Liu</a>
																	</div>
																</div>
																<a class="UserLink-badge" data-tooltip="优秀回答者"
																href="https://www.zhihu.com/question/48509984"
																target="_blank"><svg viewBox="0 0 20 20"
																		class="Icon Icon--badgeGlorious" width="16"
																		height="16" aria-hidden="true"
																		style="height: 16px; width: 16px;">
																		<title>用户标识</title><g>
																		<g fill="none" fill-rule="evenodd">     <path
																			d="M.64 11.39c1.068.895 1.808 2.733 1.66 4.113l.022-.196c-.147 1.384.856 2.4 2.24 2.278l-.198.016c1.387-.12 3.21.656 4.083 1.735l-.125-.154c.876 1.085 2.304 1.093 3.195.028l-.127.152c.895-1.068 2.733-1.808 4.113-1.66l-.198-.022c1.386.147 2.402-.856 2.28-2.238l.016.197c-.12-1.388.656-3.212 1.735-4.084l-.154.125c1.084-.876 1.093-2.304.028-3.195l.152.127c-1.068-.895-1.808-2.732-1.66-4.113l-.022.198c.147-1.386-.856-2.4-2.24-2.28l.198-.016c-1.387.122-3.21-.655-4.083-1.734l.125.153C10.802-.265 9.374-.274 8.483.79L8.61.64c-.895 1.068-2.733 1.808-4.113 1.662l.198.02c-1.386-.147-2.4.857-2.28 2.24L2.4 4.363c.12 1.387-.656 3.21-1.735 4.084l.154-.126C-.265 9.2-.274 10.626.79 11.517L.64 11.39z"
																			fill="#FF9500"></path>     <path
																			d="M10.034 12.96L7.38 14.58c-.47.286-.747.09-.618-.45l.72-3.024-2.36-2.024c-.418-.357-.318-.68.235-.725l3.1-.25 1.195-2.87c.21-.508.55-.513.763 0l1.195 2.87 3.1.25c.547.043.657.365.236.725l-2.362 2.024.72 3.025c.13.535-.143.74-.616.45l-2.654-1.62z"
																			fill="#FFF"></path>   </g></g></svg></a></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">美术狗（狸？），NYU
																	Game Center，萌系女汉子。</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">136 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image"
												content="https://pic3.zhimg.com/50/v2-3d70a6ce5a79f26573908a023282e1f0_200x112.jpg">
											<meta itemprop="upvoteCount" content="136">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/487507865">
											<meta itemprop="dateCreated"
												content="2018-09-07T19:43:11.000Z">
											<meta itemprop="dateModified"
												content="2018-09-09T15:38:40.000Z">
											<meta itemprop="commentCount" content="33">
											<div class="RichContent is-collapsed">
												<div class="RichContent-cover">
													<div class="RichContent-cover-inner">
														<div class="VagueImage"
															data-src="https://pic3.zhimg.com/50/v2-3d70a6ce5a79f26573908a023282e1f0_400x224.jpg">
															<div class="VagueImage-mask is-active"></div>
														</div>
													</div>
												</div>
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">阿多比 Adobe，就是设计师都爱的Photoshop，
														Illustrator他们公司。虽说这家的中文译名也没多好听，但Adobe直译是土砖，泥胚,，砖胚的意思。提醒我们这些设计师，不要总觉得自己是…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 136
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>33 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover12-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover12-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;郑星宇&quot;,&quot;itemId&quot;:51032007,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="51032007" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/51032007">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="郑星宇">
													<meta itemprop="image"
														content="https://pic4.zhimg.com/50/e2820a875a67eb28c91dbc35c0ea4a0d_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/zheng-xing-yu-29">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover13-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover13-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/zheng-xing-yu-29"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic4.zhimg.com/50/e2820a875a67eb28c91dbc35c0ea4a0d_xs.jpg"
																	srcset="https://pic4.zhimg.com/50/e2820a875a67eb28c91dbc35c0ea4a0d_l.jpg 2x"
																	alt="郑星宇"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover14-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover14-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/zheng-xing-yu-29">郑星宇</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">Lonely
																	God/肉月饼运输机/职业地陪/INTJ</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">72 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="72">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/51032007">
											<meta itemprop="dateCreated"
												content="2015-06-11T15:37:22.000Z">
											<meta itemprop="dateModified"
												content="2015-06-12T16:32:44.000Z">
											<meta itemprop="commentCount" content="49">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">可能有些文不对题源自网络，侵删 欢迎补充，欢迎改正
														我表示大陆的翻译跟台湾的品牌名翻译比简直小巫见大巫 heads&amp;shoulders=海飞丝 =海伦仙度丝
														Rejoic=飘柔 =飞柔 GE=通用电气 =奇异公司 :-I Sony=骚尼(误)…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 72
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>49 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover15-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover15-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;博眼&quot;,&quot;itemId&quot;:51015230,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="51015230" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/51015230">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="博眼">
													<meta itemprop="image"
														content="https://pic3.zhimg.com/50/42c17f980bf7e6a9994e72f39571c567_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/bo-yan-37">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover16-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover16-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/bo-yan-37"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic3.zhimg.com/50/42c17f980bf7e6a9994e72f39571c567_xs.jpg"
																	srcset="https://pic3.zhimg.com/50/42c17f980bf7e6a9994e72f39571c567_l.jpg 2x"
																	alt="博眼"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover17-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover17-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/bo-yan-37">博眼</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">overlanding
																	爱好者</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">64 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="64">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/51015230">
											<meta itemprop="dateCreated"
												content="2015-06-11T13:18:06.000Z">
											<meta itemprop="dateModified"
												content="2016-08-01T04:24:13.000Z">
											<meta itemprop="commentCount" content="27">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">不行了我要搬运澳洲商场的名字了 请大家带好字典和避雷针。
														在澳洲，我们有如下商场： The Coles Dick smith JB HiFi 等等 基本离不开脐下三寸
														不行了我去笑一会儿 谢谢评论补充： 房地产连锁： LJ Hooker…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 64
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>27 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover18-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover18-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;晴明&quot;,&quot;itemId&quot;:487784890,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="487784890" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/487784890">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="晴明">
													<meta itemprop="image"
														content="https://pic3.zhimg.com/50/v2-7bc0b0197a08c2e4e8adc930028b76c4_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/Fenix-9">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover19-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover19-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/Fenix-9"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic3.zhimg.com/50/v2-7bc0b0197a08c2e4e8adc930028b76c4_xs.jpg"
																	srcset="https://pic3.zhimg.com/50/v2-7bc0b0197a08c2e4e8adc930028b76c4_l.jpg 2x"
																	alt="晴明"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover20-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover20-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank" href="//www.zhihu.com/people/Fenix-9">晴明</a>
																	</div>
																</div>
																<a class="UserLink-badge" data-tooltip="优秀回答者"
																href="https://www.zhihu.com/question/48509984"
																target="_blank"><svg viewBox="0 0 20 20"
																		class="Icon Icon--badgeGlorious" width="16"
																		height="16" aria-hidden="true"
																		style="height: 16px; width: 16px;">
																		<title>用户标识</title><g>
																		<g fill="none" fill-rule="evenodd">     <path
																			d="M.64 11.39c1.068.895 1.808 2.733 1.66 4.113l.022-.196c-.147 1.384.856 2.4 2.24 2.278l-.198.016c1.387-.12 3.21.656 4.083 1.735l-.125-.154c.876 1.085 2.304 1.093 3.195.028l-.127.152c.895-1.068 2.733-1.808 4.113-1.66l-.198-.022c1.386.147 2.402-.856 2.28-2.238l.016.197c-.12-1.388.656-3.212 1.735-4.084l-.154.125c1.084-.876 1.093-2.304.028-3.195l.152.127c-1.068-.895-1.808-2.732-1.66-4.113l-.022.198c.147-1.386-.856-2.4-2.24-2.28l.198-.016c-1.387.122-3.21-.655-4.083-1.734l.125.153C10.802-.265 9.374-.274 8.483.79L8.61.64c-.895 1.068-2.733 1.808-4.113 1.662l.198.02c-1.386-.147-2.4.857-2.28 2.24L2.4 4.363c.12 1.387-.656 3.21-1.735 4.084l.154-.126C-.265 9.2-.274 10.626.79 11.517L.64 11.39z"
																			fill="#FF9500"></path>     <path
																			d="M10.034 12.96L7.38 14.58c-.47.286-.747.09-.618-.45l.72-3.024-2.36-2.024c-.418-.357-.318-.68.235-.725l3.1-.25 1.195-2.87c.21-.508.55-.513.763 0l1.195 2.87 3.1.25c.547.043.657.365.236.725l-2.362 2.024.72 3.025c.13.535-.143.74-.616.45l-2.654-1.62z"
																			fill="#FFF"></path>   </g></g></svg></a></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">他说你不能就这样过完一生</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">170 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="170">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/487784890">
											<meta itemprop="dateCreated"
												content="2018-09-08T08:49:55.000Z">
											<meta itemprop="dateModified"
												content="2018-09-08T08:49:55.000Z">
											<meta itemprop="commentCount" content="30">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">HSBC…大家都知道，汇丰银行。 但是很少有人知道，HSBC的全称：
														「the Hongkong and Shanghai Banking Corporation」
														有一次翻客户的银行水单时，看到这个名字差点没认出来，以为是哪里的野鸡银行……</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 170
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>30 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover21-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover21-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;苏黎世贝勒爷&quot;,&quot;itemId&quot;:190485296,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="190485296" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/190485296">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="苏黎世贝勒爷">
													<meta itemprop="image"
														content="https://pic2.zhimg.com/50/46907dbb770aacfb8ac194b08518ddbc_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/sulishibeileye">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover23-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover23-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/sulishibeileye"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic2.zhimg.com/50/46907dbb770aacfb8ac194b08518ddbc_xs.jpg"
																	srcset="https://pic2.zhimg.com/50/46907dbb770aacfb8ac194b08518ddbc_l.jpg 2x"
																	alt="苏黎世贝勒爷"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover24-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover24-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/sulishibeileye">苏黎世贝勒爷</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">Control
																	system/Automotive Engineer</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">87 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="87">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/190485296">
											<meta itemprop="dateCreated"
												content="2017-06-28T06:22:05.000Z">
											<meta itemprop="dateModified"
												content="2017-06-28T06:35:09.000Z">
											<meta itemprop="commentCount" content="16">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">汽车方面，我赞同，宝马的BMW（Bayerische Motoren
														Werke）巴伐利亚发动机工厂当然是首当其冲。 不过不知道这些会点儿德语，知道BMW直译是发动机工厂的学没学过历史？
														梅赛德斯-奔驰是不是看起来非常地高大上，豪华大气？至少听起来比什么宝马的破逼发动机工厂强多了。
														可是你知不知道梅赛德斯-奔驰是两家公司在1…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 87
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>16 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover25-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover25-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;匿名用户&quot;,&quot;itemId&quot;:51004441,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="51004441" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/51004441">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="匿名用户">
													<meta itemprop="image"
														content="https://pic4.zhimg.com/aadd7b895_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><img
														class="Avatar AuthorInfo-avatar" width="38" height="38"
														src="https://pic4.zhimg.com/aadd7b895_xs.jpg"
														srcset="https://pic4.zhimg.com/aadd7b895_l.jpg 2x"
														alt="匿名用户"></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name">匿名用户</span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge"></div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">115 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="115">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/51004441">
											<meta itemprop="dateCreated"
												content="2015-06-11T11:27:42.000Z">
											<meta itemprop="dateModified"
												content="2015-06-11T11:27:42.000Z">
											<meta itemprop="commentCount" content="20">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">Schwarzkopf 译名：施华蔻 实名： 黑头…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 115
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>20 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover26-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover26-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;豌豆先生&quot;,&quot;itemId&quot;:50982189,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="50982189" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/50982189">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="豌豆先生">
													<meta itemprop="image"
														content="https://pic1.zhimg.com/50/41f775eac40759f8065564760b33c65e_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/wandouxiansheng">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover27-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover27-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/wandouxiansheng"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic1.zhimg.com/50/41f775eac40759f8065564760b33c65e_xs.jpg"
																	srcset="https://pic1.zhimg.com/50/41f775eac40759f8065564760b33c65e_l.jpg 2x"
																	alt="豌豆先生"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover28-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover28-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/wandouxiansheng">豌豆先生</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">休、生、傷、杜、景、
																	死、驚、開</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">165 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="165">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/50982189">
											<meta itemprop="dateCreated"
												content="2015-06-11T08:25:29.000Z">
											<meta itemprop="dateModified"
												content="2015-06-11T08:25:29.000Z">
											<meta itemprop="commentCount" content="36">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">谢邀 英文的一时没想起来 法语的目前想到有几个： 多乐之日-Tous
														les jours-每天 巴黎贝甜-Paris Baguettes-巴黎法棍 家乐福-Carrefour-交叉路口…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 165
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>36 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover29-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover29-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;荻野幸&quot;,&quot;itemId&quot;:51069866,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="51069866" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/51069866">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="荻野幸">
													<meta itemprop="image"
														content="https://pic2.zhimg.com/50/v2-07a94f4414b6a83f59d5e18e96240f26_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/di-ye-xing">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover30-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover30-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/di-ye-xing"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic2.zhimg.com/50/v2-07a94f4414b6a83f59d5e18e96240f26_xs.jpg"
																	srcset="https://pic2.zhimg.com/50/v2-07a94f4414b6a83f59d5e18e96240f26_l.jpg 2x"
																	alt="荻野幸"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover31-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover31-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/di-ye-xing">荻野幸</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">矗立于那道光之下</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">602 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="602">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/51069866">
											<meta itemprop="dateCreated"
												content="2015-06-12T02:40:17.000Z">
											<meta itemprop="dateModified"
												content="2015-06-21T04:30:16.000Z">
											<meta itemprop="commentCount" content="105">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">德语狗第一时间就想到了：绝逼是宝马(BMW). BMW=
														Bayerische Motoren Werke,
														直译过来就是巴伐利亚发动机工厂。结果这个中文译名简直。。。屌丝被包装成了高富帅。
														至于人民牌汽车（Volkswagen)啊，黑头( Schwarzkopf) 啊也是。还有一个，BASF
														（巴登苯胺苏打厂） 德语区的…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 602
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>105 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover32-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover32-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;匿名用户&quot;,&quot;itemId&quot;:50993139,&quot;title&quot;:&quot;有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="50993139" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/31200332">
													<meta itemprop="name"
														content="有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/31200332/answer/50993139">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="匿名用户">
													<meta itemprop="image"
														content="https://pic4.zhimg.com/aadd7b895_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><img
														class="Avatar AuthorInfo-avatar" width="38" height="38"
														src="https://pic4.zhimg.com/aadd7b895_xs.jpg"
														srcset="https://pic4.zhimg.com/aadd7b895_l.jpg 2x"
														alt="匿名用户"></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name">匿名用户</span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge"></div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">1,462 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="1462">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/31200332/answer/50993139">
											<meta itemprop="dateCreated"
												content="2015-06-11T09:43:11.000Z">
											<meta itemprop="dateModified"
												content="2015-06-11T15:04:03.000Z">
											<meta itemprop="commentCount" content="128">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">你就想想那些以人名命名的公司。 Morgan Stanley
														摩根士丹利 Roland Berger 罗兰贝格 Dr. Ing h. c. F. Porsche 保时捷
														Lockheed Martin 洛克希德马丁 Merriam Webster 韦氏 American
														Shengdiyage 阿妹你看上帝压狗 你再想想 徐福记 王麻子…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 1.5K
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>128 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover33-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover33-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">关注了问题</span><span>2
													小时前</span>
											</div>
										</div>
										<div class="ContentItem">
											<h2 class="ContentItem-title">
												<div class="QuestionItem-title">
													<a href="/question/31200332" target="_blank"
														data-za-detail-view-name="Title">有哪些名字译成中文看起来很高大上，其实原意特别土的国外品牌？</a>
												</div>
											</h2>
										</div>
									</div>
									<div class="List-item">
										<div class="List-itemMeta">
											<div class="ActivityItem-meta">
												<span class="ActivityItem-metaTitle">赞同了回答</span><span>3
													小时前</span>
											</div>
										</div>
										<div class="ContentItem AnswerItem"
											data-zop="{&quot;authorName&quot;:&quot;兰斯洛特&quot;,&quot;itemId&quot;:488015583,&quot;title&quot;:&quot;fate系列有哪些实力被高估的从者？&quot;,&quot;type&quot;:&quot;answer&quot;}"
											name="488015583" itemprop="answer"
											itemtype="http://schema.org/Answer" itemscope="">
											<h2 class="ContentItem-title">
												<div itemprop="zhihu:question"
													itemtype="http://schema.org/Question" itemscope="">
													<meta itemprop="url"
														content="https://www.zhihu.com/question/293736216">
													<meta itemprop="name" content="fate系列有哪些实力被高估的从者？">
													<a target="_blank" data-za-detail-view-element_name="Title"
														href="/question/293736216/answer/488015583">fate系列有哪些实力被高估的从者？</a>
												</div>
											</h2>
											<div class="ContentItem-meta">
												<div class="AuthorInfo AnswerItem-authorInfo"
													itemprop="author" itemscope=""
													itemtype="http://schema.org/Person">
													<meta itemprop="name" content="兰斯洛特">
													<meta itemprop="image"
														content="https://pic4.zhimg.com/50/v2-146ad246e9763b1adc4b3c3fe63d9020_s.jpg">
													<meta itemprop="url"
														content="https://www.zhihu.com/people/kui-xing-shi">
													<meta itemprop="zhihu:followerCount">
													<span class="UserLink AuthorInfo-avatarWrapper"><div
															class="Popover">
															<div id="Popover34-toggle" aria-haspopup="true"
																aria-expanded="false" aria-owns="Popover34-content">
																<a class="UserLink-link"
																	data-za-detail-view-element_name="User" target="_blank"
																	href="//www.zhihu.com/people/kui-xing-shi"><img
																	class="Avatar AuthorInfo-avatar" width="38" height="38"
																	src="https://pic4.zhimg.com/50/v2-146ad246e9763b1adc4b3c3fe63d9020_xs.jpg"
																	srcset="https://pic4.zhimg.com/50/v2-146ad246e9763b1adc4b3c3fe63d9020_l.jpg 2x"
																	alt="兰斯洛特"></a>
															</div>
														</div></span>
													<div class="AuthorInfo-content">
														<div class="AuthorInfo-head">
															<span class="UserLink AuthorInfo-name"><div
																	class="Popover">
																	<div id="Popover35-toggle" aria-haspopup="true"
																		aria-expanded="false" aria-owns="Popover35-content">
																		<a class="UserLink-link"
																			data-za-detail-view-element_name="User"
																			target="_blank"
																			href="//www.zhihu.com/people/kui-xing-shi">兰斯洛特</a>
																	</div>
																</div></span>
														</div>
														<div class="AuthorInfo-detail">
															<div class="AuthorInfo-badge">
																<div class="RichText ztext AuthorInfo-badgeText">学生</div>
															</div>
														</div>
													</div>
												</div>
												<div class="AnswerItem-extraInfo">
													<span class="Voters"><button type="button"
															class="Button Button--plain">93 人赞同了该回答</button></span>
												</div>
											</div>
											<meta itemprop="image" content="">
											<meta itemprop="upvoteCount" content="93">
											<meta itemprop="url"
												content="https://www.zhihu.com/question/293736216/answer/488015583">
											<meta itemprop="dateCreated"
												content="2018-09-08T16:24:21.000Z">
											<meta itemprop="dateModified"
												content="2018-09-08T16:24:21.000Z">
											<meta itemprop="commentCount" content="33">
											<div class="RichContent is-collapsed">
												<div class="RichContent-inner">
													<span class="RichText ztext CopyrightRichText-richText"
														itemprop="text">全部， 你们生前不是很牛逼吗？ 现在连只螃蟹都打不过 丢人…</span>
													<button type="button"
														class="Button ContentItem-more Button--plain">
														阅读全文<span
															style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--ArrowDown ContentItem-arrowIcon"
																fill="currentColor" viewBox="0 0 24 24" width="24"
																height="24">
																<path
																	d="M12 13L8.285 9.218a.758.758 0 0 0-1.064 0 .738.738 0 0 0 0 1.052l4.249 4.512a.758.758 0 0 0 1.064 0l4.246-4.512a.738.738 0 0 0 0-1.052.757.757 0 0 0-1.063 0L12.002 13z"
																	fill-rule="evenodd"></path></svg></span>
													</button>
												</div>
												<div class="ContentItem-actions">
													<span><button aria-label="赞同" type="button"
															class="Button VoteButton VoteButton--up">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleUp VoteButton-TriangleUp"
																	fill="currentColor" viewBox="0 0 24 24" width="10"
																	height="10">
																	<path
																		d="M2 18.242c0-.326.088-.532.237-.896l7.98-13.203C10.572 3.57 11.086 3 12 3c.915 0 1.429.571 1.784 1.143l7.98 13.203c.15.364.236.57.236.896 0 1.386-.875 1.9-1.955 1.9H3.955c-1.08 0-1.955-.517-1.955-1.9z"
																		fill-rule="evenodd"></path></svg></span>赞同 93
														</button>
														<button aria-label="反对" type="button"
															class="Button VoteButton VoteButton--down">
															<span style="display: inline-flex; align-items: center;">​<svg
																	class="Zi Zi--TriangleDown" fill="currentColor"
																	viewBox="0 0 24 24" width="10" height="10">
																	<path
																		d="M20.044 3H3.956C2.876 3 2 3.517 2 4.9c0 .326.087.533.236.896L10.216 19c.355.571.87 1.143 1.784 1.143s1.429-.572 1.784-1.143l7.98-13.204c.149-.363.236-.57.236-.896 0-1.386-.876-1.9-1.956-1.9z"
																		fill-rule="evenodd"></path></svg></span>
														</button></span>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Comment Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M10.241 19.313a.97.97 0 0 0-.77.2 7.908 7.908 0 0 1-3.772 1.482.409.409 0 0 1-.38-.637 5.825 5.825 0 0 0 1.11-2.237.605.605 0 0 0-.227-.59A7.935 7.935 0 0 1 3 11.25C3 6.7 7.03 3 12 3s9 3.7 9 8.25-4.373 9.108-10.759 8.063z"
																	fill-rule="evenodd"></path></svg></span>33 条评论
													</button>
													<div class="Popover ShareMenu ContentItem-action">
														<div class="" id="Popover36-toggle" aria-haspopup="true"
															aria-expanded="false" aria-owns="Popover36-content">
															<button type="button"
																class="Button Button--plain Button--withIcon Button--withLabel">
																<span style="display: inline-flex; align-items: center;">​<svg
																		class="Zi Zi--Share Button-zi" fill="currentColor"
																		viewBox="0 0 24 24" width="1.2em" height="1.2em">
																		<path
																			d="M2.931 7.89c-1.067.24-1.275 1.669-.318 2.207l5.277 2.908 8.168-4.776c.25-.127.477.198.273.39L9.05 14.66l.927 5.953c.18 1.084 1.593 1.376 2.182.456l9.644-15.242c.584-.892-.212-2.029-1.234-1.796L2.93 7.89z"
																			fill-rule="evenodd"></path></svg></span>分享
															</button>
														</div>
													</div>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Star Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z"
																	fill-rule="evenodd"></path></svg></span>收藏
													</button>
													<button type="button"
														class="Button ContentItem-action Button--plain Button--withIcon Button--withLabel">
														<span style="display: inline-flex; align-items: center;">​<svg
																class="Zi Zi--Heart Button-zi" fill="currentColor"
																viewBox="0 0 24 24" width="1.2em" height="1.2em">
																<path
																	d="M2 8.437C2 5.505 4.294 3.094 7.207 3 9.243 3 11.092 4.19 12 6c.823-1.758 2.649-3 4.651-3C19.545 3 22 5.507 22 8.432 22 16.24 13.842 21 12 21 10.158 21 2 16.24 2 8.437z"
																	fill-rule="evenodd"></path></svg></span>感谢
													</button>
												</div>
											</div>
										</div>
									</div>
									<div></div>
								</div>
							</div>
						</div>
					</div>
					<div class="Profile-sideColumn" data-za-module="RightSideBar">
						<div class="Card">
							<div class="Card-header Profile-sideColumnTitle">
								<div class="Card-headerText">个人成就</div>
							</div>
							<div class="Profile-sideColumnItems">
								<div class="Profile-sideColumnItem">
									<div class="IconGraf">
										<div class="IconGraf-iconWrapper">
											<svg viewBox="0 0 14 16"
												class="Icon IconGraf-icon Icon--marked" width="16"
												height="14" aria-hidden="true"
												style="height: 14px; width: 16px;">
												<title></title><g>
												<path
													d="M0 1.505C0 .675.666 0 1.5 0H3v6l.59-.59c.778-.778 2.043-.777 2.82 0L7 6V0h5.498C13.328 0 14 .667 14 1.505v12.99c0 .83-.675 1.505-1.498 1.505H1.498C.67 16 0 15.333 0 14.495V1.505z"
													fill-rule="evenodd"></path></g></svg>
										</div>
										<span>知乎收录</span><a class="Profile-sideColumnItemLink"
											href="/people/excited-vczh/answers/included"> 4 个回答</a><a
											class="Profile-sideColumnItemLink"
											href="/people/excited-vczh/posts/included"> 2 篇文章</a>
									</div>
									<div class="Profile-sideColumnItemValue">编辑推荐收录</div>
								</div>
								<div class="Profile-sideColumnItem">
									<div class="IconGraf">
										<div class="IconGraf-iconWrapper">
											<svg viewBox="0 0 20 18" xmlns="http://www.w3.org/2000/svg"
												class="Icon IconGraf-icon Icon--like" width="16" height="16"
												aria-hidden="true" style="height: 16px; width: 16px;">
												<title></title><g>
												<path
													d="M.718 7.024c-.718 0-.718.63-.718.63l.996 9.693c0 .703.718.65.718.65h1.45c.916 0 .847-.65.847-.65V7.793c-.09-.88-.853-.79-.846-.79l-2.446.02zm11.727-.05S13.2 5.396 13.6 2.89C13.765.03 11.55-.6 10.565.53c-1.014 1.232 0 2.056-4.45 5.83C5.336 6.965 5 8.01 5 8.997v6.998c-.016 1.104.49 2 1.99 2h7.586c2.097 0 2.86-1.416 2.86-1.416s2.178-5.402 2.346-5.91c1.047-3.516-1.95-3.704-1.95-3.704l-5.387.007z"></path></g></svg>
										</div>
										获得 2,320,099 次赞同
									</div>
									<div class="Profile-sideColumnItemValue">获得 251,575 次感谢 ，
										346,245 次收藏</div>
								</div>
								<div class="Profile-sideColumnItem">
									<div class="IconGraf">
										<div class="IconGraf-iconWrapper">
											<svg width="16" height="16" viewBox="0 0 16 16"
												class="Icon IconGraf-icon Icon--commonEdit"
												aria-hidden="true" style="height: 16px; width: 16px;">
												<title></title><g>
												<path
													d="M8 15.5C3.858 15.5.5 12.142.5 8 .5 3.858 3.858.5 8 .5c4.142 0 7.5 3.358 7.5 7.5 0 4.142-3.358 7.5-7.5 7.5zm3.032-11.643c-.22-.214-.574-.208-.79.013L5.1 9.173 6.778 10.8l5.142-5.303c.215-.222.21-.575-.01-.79l-.878-.85zm-6.77 7.107L4 12l1.028-.293.955-.27L4.503 10l-.242.964z"
													fill-rule="evenodd"></path></g></svg>
										</div>
										<a class="Profile-sideColumnItemLink"
											href="/people/excited-vczh/logs" target="_blank">参与 2,737
											次公共编辑</a>
									</div>
									<div class="Profile-sideColumnItemValue"></div>
								</div>
							</div>
						</div>
						<div class="Card FollowshipCard">
							<div
								class="NumberBoard FollowshipCard-counts NumberBoard--divider">
								<a type="button" class="Button NumberBoard-item Button--plain"
									href="/people/excited-vczh/following"><div
										class="NumberBoard-itemInner">
										<div class="NumberBoard-itemName">关注了</div>
										<strong class="NumberBoard-itemValue" title="2917">2,917</strong>
									</div></a><a type="button" class="Button NumberBoard-item Button--plain"
									href="/people/excited-vczh/followers"><div
										class="NumberBoard-itemInner">
										<div class="NumberBoard-itemName">关注者</div>
										<strong class="NumberBoard-itemValue" title="756129">756,129</strong>
									</div></a>
							</div>
						</div>
						<div class="Profile-lightList">
							<a class="Profile-lightItem" target="_blank"
								href="/lives/users/0970f947b898ecc0ec035f9126dd4e08"><span
								class="Profile-lightItemName">赞助的 Live ⚡️</span><span
								class="Profile-lightItemValue">10</span></a><a
								class="Profile-lightItem"
								href="/people/excited-vczh/following/topics"><span
								class="Profile-lightItemName">关注的话题</span><span
								class="Profile-lightItemValue">41</span></a><a
								class="Profile-lightItem"
								href="/people/excited-vczh/following/columns"><span
								class="Profile-lightItemName">关注的专栏</span><span
								class="Profile-lightItemValue">93</span></a><a
								class="Profile-lightItem"
								href="/people/excited-vczh/following/questions"><span
								class="Profile-lightItemName">关注的问题</span><span
								class="Profile-lightItemValue">34,533</span></a><a
								class="Profile-lightItem"
								href="/people/excited-vczh/following/collections"><span
								class="Profile-lightItemName">关注的收藏夹</span><span
								class="Profile-lightItemValue">15</span></a>
						</div>
						<footer class="Footer">
							<a class="Footer-item" target="_blank" rel="noopener noreferrer"
								href="//liukanshan.zhihu.com/">刘看山</a><span class="Footer-dot"></span><a
								class="Footer-item" target="_blank" rel="noopener noreferrer"
								href="/question/19581624">知乎指南</a><span class="Footer-dot"></span><a
								class="Footer-item" target="_blank" rel="noopener noreferrer"
								href="/terms">知乎协议</a><span class="Footer-dot"></span><a
								class="Footer-item" target="_blank" rel="noopener noreferrer"
								href="/terms/privacy">隐私政策</a><br>
							<a class="Footer-item" target="_blank" href="/app">应用</a><span
								class="Footer-dot"></span><a class="Footer-item" target="_blank"
								rel="noopener noreferrer"
								href="https://app.mokahr.com/apply/zhihu">工作</a><span
								class="Footer-dot"></span>
							<button type="button" class="Button OrgCreateButton">申请开通知乎机构号</button>
							<br>
							<a class="Footer-item" target="_blank" rel="noopener noreferrer"
								href="https://zhuanlan.zhihu.com/p/28561671">侵权举报</a><span
								class="Footer-dot"></span><a class="Footer-item" target="_blank"
								rel="noopener noreferrer" href="http://www.12377.cn">网上有害信息举报专区</a><br>
							<span class="Footer-item">违法和不良信息举报：010-82716601</span><br>
							<a class="Footer-item" target="_blank" href="/jubao">儿童色情信息举报专区</a><br>
							<a class="Footer-item" target="_blank" rel="noopener noreferrer"
								href="https://zhstatic.zhihu.com/assets/zhihu/certificates/certificate-ICP.png">电信与服务业务经营许可证</a><br>
							<a class="Footer-item" target="_blank" rel="noopener noreferrer"
								href="https://zhstatic.zhihu.com/assets/zhihu/certificates/certificate-1.jpeg">网络文化经营许可证</a><br>
							<a class="Footer-item" target="_blank" href="/contact">联系我们</a><span>
								© 2018 知乎</span>
						</footer>
					</div>
				</div>
			</div>
			</main>
			<div class="CornerButtons">
				<div class="CornerAnimayedFlex">
					<button data-tooltip="建议反馈" data-tooltip-position="left"
						data-tooltip-will-hide-on-click="true" aria-label="建议反馈"
						type="button" class="Button CornerButton Button--plain">
						<svg class="Zi Zi--Feedback" title="建议反馈" fill="currentColor"
							viewBox="0 0 24 24" width="24" height="24">
							<path
								d="M19.99 6.99L18 5s-1-1-2-1H8C7 4 6 5 6 5L4 7S3 8 3 9v9s0 2 2.002 2H19c2 0 2-2 2-2V9c0-1-1.01-2.01-1.01-2.01zM16.5 5.5L19 8H5l2.5-2.5h9zm-2 5.5s.5 0 .5.5-.5.5-.5.5h-5s-.5 0-.5-.5.5-.5.5-.5h5z"></path></svg>
					</button>
				</div>
				<div class="CornerAnimayedFlex CornerAnimayedFlex--hidden">
					<button data-tooltip="回到顶部" data-tooltip-position="left"
						data-tooltip-will-hide-on-click="true" aria-label="回到顶部"
						type="button" class="Button CornerButton Button--plain">
						<svg class="Zi Zi--BackToTop" title="回到顶部" fill="currentColor"
							viewBox="0 0 24 24" width="24" height="24">
							<path
								d="M16.036 19.59a1 1 0 0 1-.997.995H9.032a.996.996 0 0 1-.997-.996v-7.005H5.03c-1.1 0-1.36-.633-.578-1.416L11.33 4.29a1.003 1.003 0 0 1 1.412 0l6.878 6.88c.782.78.523 1.415-.58 1.415h-3.004v7.005z"></path></svg>
					</button>
				</div>
			</div>
		</div>
	</div>
	<div id="data" style="display: none"
		data-useragent="{&quot;os&quot;:{&quot;name&quot;:&quot;Linux&quot;,&quot;version&quot;:&quot;x86_64&quot;},&quot;browser&quot;:{&quot;name&quot;:&quot;Safari&quot;,&quot;version&quot;:&quot;9.0&quot;,&quot;major&quot;:&quot;9&quot;}}"></div>
	<script
		src="https://static.zhihu.com/heifetz/vendor.995451a211dcf23e7059.js"></script>
	<script
		src="https://static.zhihu.com/heifetz/main.raven.dbf2c158f8ce2e862c9d.js"
		defer=""></script>
	<script
		src="https://static.zhihu.com/heifetz/main.app.5155fa44900359980de6.js"></script>
	<script
		src="https://static.zhihu.com/heifetz/main.people-routes.d1e78656bfff860152e8.js"></script>
	<div>
		<div style="display: none;">想来知乎工作？请发送邮件到 jobs@zhihu.com</div>
	</div>
	<div>
		<div>
			<span></span>
		</div>
	</div>
	<span><div></div></span>
</body>
</html>
'''
import re

html = etree.HTML(text)
res = html.xpath('//strong[@class="NumberBoard-itemValue"]')
res1 = res[1].xpath('./text()')
print(res)
print(res1)
str = res1[0].replace(',','')
if int(str) > 10000:
    print(int(str))
    print('666')


