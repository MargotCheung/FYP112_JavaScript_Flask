<template>
    <!-- <div class="about">
      <h1>This is an about page</h1>
    </div> -->
  
    <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700">
      <link rel="stylesheet" href="https://rawcdn.githack.com/Loopple/loopple-public-assets/ad60f16c8a16d1dcad75e176c00d7f9e69320cd4/argon-dashboard/css/nucleo/css/nucleo.css">
      <link rel="stylesheet" href="../assets/css/theme.css">
      <link rel="stylesheet" href="../assets/css/loopple/loopple.css">
      <!-- Bootstrap -->
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  
  <body class="g-sidenav-show" >    
  
      <div class="main-content" id="panel">

        <!-- submit 事件觸發時，執行 login -->
        <form @submit.prevent="login">

          <div class="container-fluid pt-3" style="background: #FFE8D6">
              <div class="row removable" >
  
                  <!-- Left container -->
                  <div class="col-lg-6">
                      <!-- <div class="card bg-danger">  -->
                      
                          <div class="card-header"  style="background: #FFE8D6">                                            
                              <div class="card-body"></div>
                              <div class="card-body"></div>
                              <div class="card-body"></div>
                              <div class="card-body" style="text-indent: 18%"> 
                                  <p class="text-lg-left" style="font-size: 50px; font-weight: 400; color: #6B705C">逢甲選課避雷手札</p>
                                  <p class="text-lg-left" style="font-size: 30px; font-weight: 200; color: #6B705C">總有一些課不適合您 ¯\_(ツ)_/¯</p>
                              </div>                           
                              <div class="card-body"></div>
                              <div class="card-body"></div>
                              <div class="card-body"></div>
                              <div class="card-body"></div>
                              <div class="card-body"></div>
                              <div class="card-body"></div>                      
                          </div>
                      <!-- </div> -->
                  </div>
  
                  <!-- Right container -->
                  <div class="col-lg-6">
                      <div class="card-header"  style="background: #FFE8D6">
                          <div class="card-body" style="background: #DDBEA9"></div>
                          <div class="card-body" style="background: #DDBEA9"></div>
                          
                          <div class="card-body" style="background: #DDBEA9" >
  
                              <div class="row removable">
                                  <a class="text-lg-left" style="margin-left: 20px; font-size: 25px; font-weight: 500; color: #000; text-indent: 0%">Email</a>
                                  <div class="col-lg-9" style="margin-left: 20px"> 
                                    <input type="email"
                                        class="form-control"
                                        id="inputEmail"
                                        aria-describedby="emailHelp"
                                        v-model="user.email" 
                                        style="text-align: center" 
                                        placeholder="輸入賬號" />
                                    </div> 
                              </div>    
  
                              <p></p>
  
                              <div class="row removable">  
                                  <p class="text-lg-left" style="margin-left: 20px; font-size: 25px; font-weight: 500; color: #000; text-indent: 0%">密碼</p>                         
                                  <div class="col-lg-9" style="margin-left: 20px">
                                    <input type="password"
                                        class="form-control"
                                        id="inputPassword"
                                        v-model="user.password" 
                                        style="text-align: center" 
                                        placeholder="輸入密碼" />
                                  </div>                                                
                              </div>
  
                              <p></p>
  
                              <div class="card-body" style="background: #DDBEA9"></div>
                              <div class="card-body"></div>
                              <div class="card-body"></div>
                              <div class="card-body" style="background: #DDBEA9"></div>
  
                              <div class="row removable">                                 
                                  <div class="col-lg-12">
                                    <!-- type 為 submit 讓按下後得以觸發 submit -->
                                    <button type="submit" class="btn btn-default col text-center" style="background:#CB997E">
                                    <router-link to="/myProfile" style="color: #FFFFFF">登入</router-link></button>
                                  </div>                                 
                              </div>



                             
                         
                              <ul class="nav nav-footer justify-content-center justify-content-lg-end">
                                  <li class="nav-item">
                                      <a class="" href="#" ><router-link to="/register" style="color: #FFFFFF">沒有賬號 ？馬上註冊</router-link></a>

                                  </li>                            
                              </ul>
  
                              <div class="card-body" style="background: #DDBEA9"></div>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
          <!-- Footer -->
          <footer class="footer pt-0 px-4" style="background: #FFE8D6">
              <div class="row align-items-center justify-content-lg-between">
                  <div class="col-lg-6">
                      <div class="copyright text-center  text-lg-left  text-muted" style="text-indent: 20%">
                          © 來源參考:
                          <a href="https://www.creative-tim.com/product/argon-dashboard" class="font-weight-bold ml-1" target="_blank" style="color: #6B705C">Argon Dashboard</a>
                          &amp;<a href="https://www.loopple.com" class="font-weight-bold ml-1" target="_blank" style="color: #6B705C">Loopple</a>
                      </div>
                  </div>
                  <div class="col-lg-6">
                      <ul class="nav nav-footer justify-content-center justify-content-lg-end">
                          <li class="nav-item">
                              <a href="javascript:void(0);" class="nav-link" style="color: #6B705C ;">網站投訴電話 : 04-24517250</a>
                          </li>
                          <li class="nav-item">
                              <a href="javascript:;" class="nav-link" style="margin-right:150px; color: #6B705C">網站負責人：校霸</a>                           
                          </li> 
                      </ul>
                  </div>
                  <div class="card-body"></div>
              </div>
          </footer>
          </form> 
        </div>
  </body> 
</template>
  
  
<script>
// 記得要先 import axois
import axios from "axios";
export default {
name: "Login",
data() {
    return {
    // 與使用者輸入的帳密欄位 v-model 雙向綁定
    user: {
        email: "",
        password: "",
    },
    // getData 時會先從瀏覽器 cookie 叫出 Token 存來此元件
    token: "",
    };
},
methods: {
    login() {
    // 如果一開始沒有 import axios 的話
    // 用 require("axios").default 也可以讓我們使用 axios
    // const axios = require("axios").default;
    axios
        .post(`你的 api 喔`, this.user)
        .then((res) => {
        const token = res.data.token;
        const expired = res.data.expired;
        // 將 token 與他的到期時間存到瀏覽器 cookie 裡
        document.cookie = `loginToken = ${token}; expires = ${new Date(
            expired * 1000
        )};`;
        });
    },
    getData() {
    // 先從瀏覽器 cookie 取得 token
    this.token = document.cookie.replace(/(?:(?:^|.*;\s*)loginToken\s*=\s*([^;]*).*$)|^.*$/, "$1");
    const api = `你的 api 喔`;

    // https://github.com/axios/axios#global-axios-defaults
    // 並且 header 按照後端 api 文件的規格要求填上 Bearer token 字樣
    axios.defaults.headers.common.Authorization = `this.token`;
    axios.get(api).then((res) => {
        console.log(res);
    });
    },
    logout() {
    // 清除瀏覽器 cookie 的 Token
    document.cookie = `loginToken = ""; expires = "";`;
    },
},
};
</script>