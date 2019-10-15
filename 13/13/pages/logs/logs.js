//logs.js
const util = require('../../utils/util.js');
var app = getApp();
var that; 
var Util = require('../../utils/util.js');
Page({
  data: {
    focus: false,
    password:"",
    username:"",
    token:"",
    user_id:0
  },
  onLoad:function(){
 //   app.globalData.token="";
   this.data.username="",
     this.data.password = ""
  },
  jumpPage1: function () {
   // app.grobalData.username=this.data.username;
   /* if (this.data.username == "20080525" && this.data.password == "20080525") {
       wx.showToast({
        title: '用户名或密码未填写',
        icon: 'none',
         duration: 2000//持续的时间
       })
    }
    else{  */
    that = this;
    wx.request({
      url: "https://api.shisanshui.rtxux.xyz/auth/login",
      method: "POST", 
      header: {
        //请求头和ajax写法一样
        'Content-Type': 'application/json'
      },
      data: JSON.stringify({
        "username": this.data.username,
        "password": this.data.password
      }),
      success: function (res) {
        app.globalData.token=res.data.data.token;
       // app.globalData.username=this.data.username;
       // console.log(app.globalData.token);
        if (app.globalData.token!=""){
        wx.navigateTo({
          url: '/pages/page1',
        })
       }
      },
      complete: function (res) {
        if (res == null || res.data == null) {
          console.error('网络请求失败');
          return;
        }
      },
      fail: function (error) {
        console.log("请求失败!");
      }
    })
    
  },
  userNameInput: function (e) {
    this.setData({
      username: e.detail.value
    })
  },
  passWdInput: function (e) {
    this.setData({
      password: e.detail.value
    })
  },
  bindReplaceInput: function (e) {
    var value = e.detail.value
    var pos = e.detail.cursor
    var left
    if (pos !== -1) {
      // 光标在中间
      left = e.detail.value.slice(0, pos)
      // 计算光标的位置
      pos = left.replace(/11/g, '2').length
    }

    // 直接返回对象，可以对输入进行过滤处理，同时可以控制光标的位置
    return {
      value: value.replace(/11/g, '2'),
      cursor: pos
    }

    // 或者直接返回字符串,光标在最后边
    // return value.replace(/11/g,'2'),
  },
  bindHideKeyboard: function (e) {
    if (e.detail.value === '123') {
      // 收起键盘
      wx.hideKeyboard()
    }
  },
  jumpPage: function(){
    wx.navigateTo({
      url:'/pages/zhuce',
    })
  },
})

