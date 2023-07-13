<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/> -->


    <nav class="navbar navbar-top navbar-expand navbar-dark border-bottom" style="background: #FFE8D6" id="navbarTop">
            <div class="container" >
                
                <a class="loopple-navbar-brand" href="#" style="margin-right: 15px; color: #6B705C">
                    <img src="./assets/image/logo.jpg" style="width:50px">
                    <a class="" href="#" ><router-link to="/" style="color: #6B705C">首頁 </router-link></a>
                    
                </a>

                <div class="topnav-right">
                    <a class="" href="#" ><router-link to="/register" style="color: #6B705C">註冊 | </router-link></a>
                    <a class="" href="#" ><router-link to="/about" style="color: #6B705C">登入</router-link> </a> 
                </div>

            </div>
    </nav>


    


     <router-view/>

</template>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
