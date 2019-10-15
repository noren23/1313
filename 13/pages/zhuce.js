// pages/zhuce.js
var app = getApp();
var that;
Page({

  /**
   * 页面的初始数据
   */

  data: {
    username:"",
    password:""
  },
  jumpPage: function () {
    that = this;
    wx.request({
      url: "https://api.shisanshui.rtxux.xyz/auth/register",
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
        //app.globalData.token = res.data.data.token;
        // app.globalData.username=this.data.username;
       // console.log(username);
        if (res.data.status == 1001) {
          wx.showToast({
            title: '用户名已被使用',
            icon: 'none',
            duration: 2000//持续的时间
          })
        }
        if (res.data.status==0){
        wx.navigateTo({
          url: '/pages/zhucechenggong'
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
  /**
   * 生命周期函数--监听页面加载
   */

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})