
function MSubPage() {
	var mCurPage = sessionStorage.getItem('mPage');
	if(mCurPage==null){
		mCurPage = 0;
	}
	mCurPage--;
	if(mCurPage<=0){
		mCurPage = 0;
	}
	sessionStorage.setItem('mPage', mCurPage);
}


function MAddPage() {
	var mCurPage = sessionStorage.getItem('mPage');
	if(mCurPage==null){
		mCurPage = 0;
	}
	mCurPage++;
	sessionStorage.setItem('mPage', mCurPage);
}

function MGetPage() {
	var mCurPage = sessionStorage.getItem('mPage');
	if(mCurPage==null){
		mCurPage = 0;
	}
	return mCurPage;
}




function MSetShowPage(val) {
	sessionStorage.setItem('mPage', val);
	sessionStorage.setItem('mShowPage', val);
}

function MGetShowPage() {
	var mCurPage = sessionStorage.getItem('mShowPage');
	return mCurPage;
}


function MGetLongPressSwitchBool(val) {
	mLongPressSwitch=val
	if(mLongPressSwitch==null){
		mLongPressSwitch = 1;
	}
	if (mLongPressSwitch==0) {
		mLongPressSwitch=1;
	}else{
		mLongPressSwitch=0
	}
	return mLongPressSwitch
}

function MLongPressSwitch() {
	var mLongPressSwitch = sessionStorage.getItem('mLongPressSwitch');

	mLongPressSwitch=MGetLongPressSwitchBool(mLongPressSwitch)
	sessionStorage.setItem('mLongPressSwitch', mLongPressSwitch);

	var isOpen = mLongPressSwitch == 1 ? true: false;
	return isOpen
}


function MGetLongPressSwitch() {
	var mLongPressSwitch = sessionStorage.getItem('mLongPressSwitch');
	mLongPressSwitch=MGetLongPressSwitchBool(mLongPressSwitch)
	return mLongPressSwitch;
}


function scrollToEle(ele){
	if(ele){
		var oTop = ele.offsetTop;
		console.log(oTop)
		window.scrollTo(0,oTop);
	}
	
}

// h1ContentWithTag为h1标签 包含<h1></h1>
// oc会调用这个函数
function scrollToH1WithContent(h1ContentWithTag){
	var element_arr = document.getElementsByTagName('h1');
	for (var i = 0; i < element_arr.length; i++) {
		var element = element_arr[i]


		var ori = element.outerHTML;
		if(ori == h1ContentWithTag){
			scrollToEle(element)
			break;
		}

	}
}

function GetReadH1() {
	var h1_arr = new Array();
	var htmlContent = document.getElementsByTagName('html')[0].outerHTML;
	var result_arr = htmlContent.match(/<h1>看完此文章需理解<\/h1>[\s\S]*?<\/ul>/)
	if(result_arr){
		result = result_arr[0]
		var li_arr = result.match(/<li>[\s\S]*?<\/li>/g)
		for (var i = 0; i < li_arr.length; i++) {
			var li = li_arr[i]
			var h1_from_li = li.replace("<li>","<h1>").replace("</li>", "</h1>")
			h1_arr[i] = h1_from_li
		}
	}
	return h1_arr
}	

function AutoJump2Next() {
	h1_read_arr = GetReadH1()

    var documentScrollTop = document.documentElement.scrollTop

    var element_arr = document.getElementsByTagName('h1');
    var succ = 0

	for (var i = 0; i < element_arr.length; i++) {
		var element = element_arr[i]


		var ori = element.outerHTML;
		var oTop = element.offsetTop;

		succ = 0

		if(documentScrollTop < oTop){
			for (var j = 0; j < h1_read_arr.length; j++) {
				var h1_tag_content = h1_read_arr[j]
				if(ori == h1_tag_content){
					scrollToEle(element)
					succ = 1
					break;
				}
			}
		}

		if(succ == 1){
			break
		}
		
	}
}

//页面加载完毕
document.onreadystatechange = function(){
    if(document.readyState == 'complete'){
        // 页面加载完毕

        document.onkeydown = function (event) {
			switch(event.keyCode){
				case 13 :  // Enter（回车键）
        			AutoJump2Next()
	                break;
			}
		}
    }
}


// var timer1 = setTimeout(function(){
// 	var h1ContentWithTag = "<h1>Bloom全屏泛光代码实现</h1>"
// 	scrollToH1WithContent(h1ContentWithTag)
// },1000);