//app.js
App({
  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },
  globalData: {
    aa:[],
    userInfo: null,
    limit:'',
    page:'',
    pi:'',
    status:0,
    token:"",
    username:"",
    card:"",
    id:'',
    resid:'',
    timestamp:'',
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
    res:{},
    x:[],
    y:[],
    z:[],
    c1:[],
    c:[],
    detail:[
      {
        player_id:'',
        name:"",
        score:'',
        card:[
          "",
          "",
          ""
        ]

      },
      {
        player_id: '',
        name: "",
        score: '',
        card: [
          "",
          "",
          ""
        ]

      },
      {
        player_id: '',
        name: "",
        score: '',
        card: [
          "",
          "",
          ""
        ]

      },
      {
        player_id: '',
        name: "",
        score: '',
        card: [
          "",
          "",
          ""
        ]

      }

    ]
  }
})