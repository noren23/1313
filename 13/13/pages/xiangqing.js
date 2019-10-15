// pages/xiangqing.js
var app = getApp();
var that; 
Page({

  /**
   * 页面的初始数据
   */
  data: {
   id:'',
  },
  /**
   * 生命周期函数--监听页面加载
   */
  jumpPage1: function (options) {
    that = this;
    wx.request({
      url: 'https://api.shisanshui.rtxux.xyz/history/'+this.data.id,
      data: {
        "id": this.data.id,
      },
      method: "GET",
      header: {
        //请求头和ajax写法一样
        'content-type': 'application/json',
        'X-Auth-Token': app.globalData.token
      },
      success: function (res) {
        //app.globalData.token = res.data.data.token;
        // app.globalData.username=this.data.username;
       // console.log(res.data);
        app.globalData.status = res.data.status;
        if (app.globalData.status == 5000)
        {
          wx.showToast({
            title: '错误',
            icon: 'none',
            duration: 2000//持续的时间
          })
        }
        else if (app.globalData.status==3001)
        {
          wx.showToast({
            title: '战局不存在或未结束',
            icon: 'none',
            duration: 2000//持续的时间
          })
        }
        else{
        app.globalData.resid= res.data.data.id;
        app.globalData.timestamp = res.data.data.timestamp;
        app.globalData.detail = res.data.data.detail;
        console.log(app.globalData.detail);
        wx.navigateTo({
          url: '/pages/jieguo2'
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
  idInput: function (e) {
    this.setData({
      id: e.detail.value
    })
  },
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