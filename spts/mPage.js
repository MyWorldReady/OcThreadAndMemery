
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
		mCurPage = 6;
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
