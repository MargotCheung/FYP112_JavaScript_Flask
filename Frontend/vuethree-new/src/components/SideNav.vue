<template>
 
  <!-- <header class="header">
    <nav class="navbar">
      <img src="../assets/logo.jpg" style="width:50px">
      <a href="#">首頁</a>
    </nav>
  </header>  -->

  <nav class="sidenav navbar navbar-vertical fixed-left navbar-expand-xs navbar-light loopple-fixed-start" id="sidenav-main" style="background: #FFE8D6">
        <div class="sidenav-header  align-items-center" style="background: #FFE8D6">
            <a class="navbar-brand" href="landing.html">
                <img src="https://loopple.s3.eu-west-3.amazonaws.com/images/22o5oO1wY68wvY8fZpQXGyvVE1HDdROKOoGyGNWX.jpg" class="navbar-brand-img" alt="..."> 首頁
            </a>           
        </div>
        <div class="navbar-inner" style="background: #FFE8D6">
            <div class="collapse navbar-collapse" id="sidenav-collapse-main">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="profile.html">
                            <i class="fa fa-desktop text-primary"></i>
                            <span class="nav-link-text">我的資料</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="uploadPaper.html">    <!-- <a class="nav-link active" href="javascript:" remove 'active'> -->
                            <i class="fa fa-globe text-info"></i>
                            <span class="nav-link-text">上傳考古題</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-map-marker text-warning"></i>
                            <span class="nav-link-text">我的貼文</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-table text-dark"></i>
                            <span class="nav-link-text">我的收藏</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-lock text-danger"></i>
                            <span class="nav-link-text">COIN錢包</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-key text-success"></i>
                            <span class="nav-link-text">設定</span>
                        </a>
                    </li>
                </ul>                

                <hr class="my-3">
                <h6 class="navbar-heading p-0 text-muted">
                    <span class="docs-normal">學年</span>
                </h6>
                <ul class="navbar-nav mb-md-3">
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-rocket"></i>
                            <span class="nav-link-text">大一</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-palette"></i>
                            <span class="nav-link-text">大二</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-chart-pie"></i>
                            <span class="nav-link-text">大三</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:">
                            <i class="fa fa-puzzle-piece"></i>
                            <span class="nav-link-text">大四</span>
                        </a>
                    </li>
                </ul>
                
            </div>
            
            

        </div>
    </nav>
    <router-view/>


</template>

<script>
export default {
  name: 'SideNav',
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
