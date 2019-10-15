// pages/jiaru.js
var app = getApp()
var that=this; 
Page({

  /**
   * 页面的初始数据
   */
  
  data: {
    id: '',
    card: "",
  },
  onLoad: function () {
    var that = this;
    wx.showLoading({
      title: '加载中',
    })
    setTimeout(function () {
      that.setData({
        id:app.globalData.id,
        card: app.globalData.card,
      })
      wx.hideLoading()
    }, 1000)
  },
  jumpPage: function () {
    wx.navigateTo({
    //  url: '/pages/fapai'
    })
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