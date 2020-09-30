
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


