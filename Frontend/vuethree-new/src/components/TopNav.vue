<template>
 
  <!-- <header class="header">
    <nav class="navbar">
      <img src="../assets/logo.jpg" style="width:50px">
      <a href="#">首頁</a>
    </nav>
  </header>  -->

  <nav class="navbar navbar-top navbar-expand navbar-dark border-bottom" style="background: #FFE8D6" id="navbarTop">
        <div class="container" >
            <a class="loopple-navbar-brand" href="landing.html" style="margin-right: 15px">
                <img src="../assets/image/logo.jpg" style="width:85px">
            </a>
            <a class="" style="color: #6B705C" href="landing.html" >首頁</a>
            <div class="collapse navbar-collapse" id="navbar-primary">                
                <ul class="navbar-nav ml-lg-auto">
                    <li class="nav-item">
                        <a class="nav-link" style="color: #6B705C" href="signIn.html">登入 |</a>
                        <router-link to="/">Home</router-link>
                        

                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link" style="color: #6B705C" href="signUp.html">註冊</a>                           
                    </li>
                </ul>
            </div>

        </div>
    </nav>
    <router-view/>







</template>

<script>
export default {
  name: 'TopNav',
  props: {
    msg: String
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

/* .header{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 25px 13%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
    background: #DDBEA9;
}

.navbar{
    height: 0px;
      
}

.navbar a{
    position: relative;
    font-size: 30px;
    color: #6B705C;
    margin-right: 30px;
    text-decoration: none;
    
}

.navbar a::after{
    content: "";
    position: absolute;
    left: 0;
    width: 100%;
    height: 2px;
    background: #fff;
    bottom: -5px;
    border-radius: 5px;
    transform: translateY(10px);
    opacity: 0;
    transition: .5s ease;
}

.navbar a:hover:after{
    transform: translateY(0);
    opacity: 1;
} */


</style>
