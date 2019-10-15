// pages/jieguo1.js
var app = getApp();
var that; 
var index;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    ab:[],
    id:[],
    card:[],
    score: [],
    st: [],
    x:[],
    n:''
    },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    wx.showLoading({
      title: '加载中',
    })
    setTimeout(function () {
      that.setData({
        n: app.globalData.limit,
        id: app.globalData.x,
        card: app.globalData.c1,
        score: app.globalData.y,
        st: app.globalData.z,
        ab: app.globalData.aa,
      })
      wx.hideLoading()
    }, 100)
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