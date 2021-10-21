function check() {
    let arr = [
        '"http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg", width: "240", height: "160"',
        '"http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg", width: "320", height: "195"',
        '"http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg", width: "500", height: "343"'

    ];

    let ran = Math.floor(Math.random() * arr.length)
    document.getElementById('inner').innerHTML = ` <img src=${arr[ran]}></img>` 

    
}