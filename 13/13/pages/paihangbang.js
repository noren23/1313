// pages/paihangbang.js
var app = getApp();
var that; 
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name1: "",
    name2: "",
    name3: "",
    name4: "",
    name5: "",
    playerId1: '',
    playerId2: '',
    playerId3: '',
    playerId4: '',
    playerId5: '',
    score1: '',
    score2: '',
    score3: '',
    score4: '',
    score5: '',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    that = this;
    wx.request({
      url: "https://api.shisanshui.rtxux.xyz/rank",
      method: "GET",
      success: function (res) {
        // app.globalData.username=this.data.username;
        that.setData({
          name1 : res.data[0].name,
          name2 : res.data[1].name,
          name3 : res.data[2].name,
          name4 : res.data[3].name,
          name5 : res.data[4].name,
          playerId1 : res.data[0].player_id,
          playerId2 : res.data[1].player_id,
          playerId3: res.data[2].player_id,
          playerId4: res.data[3].player_id,
          playerId5: res.data[4].player_id,
          score1 : res.data[0].score,
          score2 : res.data[1].score,
          score3: res.data[2].score,
          score4: res.data[3].score,
          score5: res.data[4].score,
        })
       // console.log(this.data.playerId1);
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