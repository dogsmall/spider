var page = require("webpage").create();
var fs = require('fs')

// page.setting('javascriptEnabled',true)
page.settings = {
    javascriptEnabled: true,
    loadImages: false,
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
};
// phantom.injectJs('md5.js')
phantom.addCookie({
    'name': 'CNZZDATA1259612802',   /* required property */
    'value': '1387150528-1482821646-%7C1482827046',  /* required property */
    'domain': 'www.toutiao.com',
    'path': '/',                /* required property */
    'httponly': false,
    'secure': false,
    // 'expires': (new Date()).getTime() + (1000 * 60 * 60 * 24 * 15)   /* <-- expires in 1 hour */
});
page.onConsoleMessage = function (msg) {
    console.log('Page title is ' + msg);
};
// console.log(CryptoJS.MD5(list[i].split(',')[0]))
var url = 'http://www.toutiao.com/gossip/'
console.log(url)
page.open(url, function (status) {
    if (status !== "success") {
        console.log("open fail!");
    }
    page.scrollPosition = { top: 0, lefT: 0 }
    setTimeout(function () {
        page.scrollPosition = {
            top: 10000,
            left: 0
        };
        var s = page.evaluate(function () {
            window.scrollTop(0,100000);
            return document.body.scrollHeight
        });
        console.log(s)
        page.render('google_1.jpeg');
        phantom.exit()
    }, 5000)
    // page.onResourceReceived = function (response) {
    //     console.log(response)
    //     // console.log('Response (#' + response.id + ', stage "' + response.stage + '"): ' + JSON.stringify(response));
    // };



});



