// pages/jieguo2.js
var app = getApp();
var that; 
Page({

  /**
   * 页面的初始数据
   */
  data: {
    timestamp:'',
    id:'',
    p1:"",
    p2:"",
    p3:"",
    p4:"",
    pi1:'',
    pi2: '',
    pi3: '',
    pi4: '',
    card11:"",
    card12: "",
    card13: "",
    card21: "",
    card22: "",
    card23:"",
    card31: "",
    card32: "",
    card33: "",
    score1:'',
    score2: '',
    score3: '',
    score4: '',

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
        timestamp: app.globalData.timestamp,
        id: app.globalData.resid,
        card1: app.globalData.detail[0].card,
       // card12: app.globalData.detail[0].card[1],
       // card13: app.globalData.detail[0].card[2],
        card2: app.globalData.detail[1].card,
       // card22: app.globalData.detail[1].card[1],
       // card23: app.globalData.detail[1].card[2],
        card3: app.globalData.detail[2].card,
       // card32: app.globalData.detail[2].card[1],
       // card33: app.globalData.detail[2].card[2],
        card4: app.globalData.detail[3].card,
        pi1: app.globalData.detail[0].player_id,
        pi2: app.globalData.detail[1].player_id,
        pi3: app.globalData.detail[2].player_id,
        pi4: app.globalData.detail[3].player_id,
        p1: app.globalData.detail[0].name,
        p2: app.globalData.detail[1].name,
        p3: app.globalData.detail[2].name,
        p4: app.globalData.detail[3].name,
        score1: app.globalData.detail[0].score,
        score2: app.globalData.detail[1].score,
        score3: app.globalData.detail[2].score,
        score4: app.globalData.detail[3].score,
      })
      wx.hideLoading()
    }, 10)
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