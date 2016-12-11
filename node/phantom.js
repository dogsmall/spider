var page = require("webpage").create();
var fs = require('fs')
// page.setting('javascriptEnabled',true)
page.settings = {
    javascriptEnabled: true,
    loadImages: false,
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
};
phantom.injectJs('md5.js')
phantom.addCookie({
    'name': 'CookieName',   /* required property */
    'value': 'SINAGLOBAL=3251250314579.1147.1470725256414; wvr=6; YF-Page-G0=00acf392ca0910c1098d285f7eb74a11; SCF=ArqiEfmQWLrAiMojWDMEzkoNs1VLm31c8bsa70mbNqaviYm8dT1Kq5cCrJSXqG5bL4aQoDrTaZoubFcx2zhJwMo.; SUB=_2A251T9O-DeRxGeRH6VYZ-C_LyzuIHXVWPUJ2rDV8PUNbmtBeLXPSkW98s7IUgPm4ZfGov6i5tQUoiPLGsg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5f8TiH-ew4DsiVdcFTyJ9K5JpX5KMhUgL.Foz4eoBR1h2NehM2dJLoI0qLxKqL1K-LBo5LxK-LBKBLB-2LxK-LBK-L1hMLxK.L1heLB-BLxKBLBonL1KqLxKBLB.eL1-qt; SUHB=0FQrCX2RFk4A0C; ALF=1512888172; SSOLoginState=1481352174; _s_tentry=login.sina.com.cn; UOR=book.51cto.com,widget.weibo.com,login.sina.com.cn; Apache=6492411931057.882.1481352183720; ULV=1481352183901:47:7:6:6492411931057.882.1481352183720:1481349339478',  /* required property */
    'domain': 'weibo.com',
    'path': '/',                /* required property */
    'httponly': false,
    'secure': false,
    'expires': (new Date()).getTime() + (1000 * 60 * 60 * 24 * 15)   /* <-- expires in 1 hour */
});
page.onConsoleMessage = function(msg) {
  console.log('Page title is ' + msg);
};
var file = fs.read('index.txt');
var list = file.split('\n')
// console.log(list)
for(var i = 0;i<list.length;i++){
    // console.log(CryptoJS.MD5(list[i].split(',')[0]))
    var url = 'http://weibo.com/p/100808' + CryptoJS.MD5(list[i].split(',')[0])
    console.log(url)
    page.open(url, function (status) {
        if (status !== "success") {
            console.log("open fail!");
        }
        setTimeout(function () {
            var apply = page.evaluate(function () {
                return document.getElementById("Pl_Core_T8CustomTriColumn__12").innerText + document.getElementById("Pl_Core_Ut2UserList__14").innerText;
            });
            console.log(apply.split('\n'));
            // fs.write("body.txt", apply, "a/+");
            phantom.exit();
        }, 5000);
    });
}


