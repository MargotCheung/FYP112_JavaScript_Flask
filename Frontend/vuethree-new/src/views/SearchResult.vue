<template>
  
    <head>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">
      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700">
      <link rel="stylesheet" href="https://rawcdn.githack.com/Loopple/loopple-public-assets/ad60f16c8a16d1dcad75e176c00d7f9e69320cd4/argon-dashboard/css/nucleo/css/nucleo.css">
      <link rel="stylesheet" href="../assets/style/theme.css">
      <link rel="stylesheet" href="../assets/style/loopple.css">
      <!-- Bootstrap -->
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  
      
  
  
  
    </head>
  
  <body class="g-sidenav-show">
    
    <!-- Backup SideNav -->
    <!-- <nav class="sidenav navbar navbar-vertical fixed-left navbar-expand-xs navbar-light loopple-fixed-start" id="sidenav-main" style="background: #FFE8D6">
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
                        <a class="nav-link" href="uploadPaper.html">    
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
    </nav> -->

    <div class="main-content" id="panel">


        <!-- Backup TopNav -->
        <!-- <nav class="navbar navbar-top navbar-expand navbar-dark border-bottom" id="navbarTop" style="background: #FFE8D6" >
            <div class="container-fluid" >
                <div class="collapse navbar-collapse" id="navbarSupportedContent" >
                    <form class="navbar-search navbar-search-light form-inline mr-sm-3 mb-0" id="navbar-search-main" >
                        <div class="form-group mb-0" >
                            <div class="input-group input-group-alternative input-group-merge" style="background: #fff">
                                <div class="input-group-prepend">
                                    <span class="input-group-text"><i class="fas fa-search"></i></span>
                                </div>
                                <input class="form-control me-2" type="search" placeholder="輸入課名 / 教師" aria-label="Search">
                            </div>
                        </div>
                        <button type="button" class="close" data-action="search-close" data-target="#navbar-search-main" aria-label="Close">
                            <span aria-hidden="true">�</span>
                        </button>
                    </form>
                    <ul class="navbar-nav align-items-center  ml-md-auto ">
                        <li class="nav-item d-xl-none">
                            <div class="pr-3 sidenav-toggler sidenav-toggler-dark active" data-action="sidenav-pin" data-target="#sidenav-main">
                                <div class="sidenav-toggler-inner">
                                    <i class="sidenav-toggler-line"></i>
                                    <i class="sidenav-toggler-line"></i>
                                    <i class="sidenav-toggler-line"></i>
                                </div>
                            </div>
                        </li>
                        <li class="nav-item d-sm-none">
                            <a class="nav-link" href="#" data-action="search-show" data-target="#navbar-search-main">
                                <i class="ni ni-zoom-split-in"></i>
                            </a>
                        </li>       
                    </ul>
                    <ul class="navbar-nav align-items-center  ml-auto ml-md-0 ">
                        <li class="nav-item dropdown">
                            <a class="nav-link pr-0" href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <div class="media align-items-center">
                                    <span class="avatar avatar-sm rounded-circle">
                                        <img alt="Image placeholder" src="https://loopple.s3.eu-west-3.amazonaws.com/images/35KfK97H5GmsfgcsnwAvfd71jurL9kOFjMP8E8bW.png">
                                    </span>
                                    <div class="media-body  ml-2  d-none d-lg-block">
                                        <span class="mb-0 text-sm  font-weight-bold" style="color: black">粉頭</span>
                                    </div>
                                </div>
                            </a>                          
                        </li>
                    </ul>
                </div>
            </div>
        </nav> -->



        <div class="container-fluid pt-3" style="background: #FFE8D6">
            <div class="row removable">

                <!-- Left container -->
                <div class="col-lg-2">                    
                     <!-- SideNav -->
                    <div class="navbar-inner" style="background: #FFE8D6">
                        <div class="navbar-collapse" id="sidenav-collapse-main">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                    <a class="nav-link" href="#">
                                        <i class="fa fa-desktop text-primary"></i>                            
                                        <span class="nav-link-text"> <router-link to="/myProfile" style="color: #212529"> 我的資料</router-link></span>

                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#">    
                                        <i class="fa fa-globe text-info"></i>
                                        <span class="nav-link-text"> <router-link to="/uploadPaper" style="color: #212529"> 上傳考古題</router-link></span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="javascript:">
                                        <i class="fa fa-map-marker text-warning"></i>
                                        <span class="nav-link-text"> <router-link to="/lessonPage" style="color: #212529"> LessonPage</router-link></span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="javascript:">
                                        <i class="fa fa-table text-dark"></i>
                                        <span class="nav-link-text"> <router-link to="/searchResult" style="color: #212529"> SearchResult</router-link></span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="javascript:">
                                        <i class="fa fa-lock text-danger"></i>
                                        <span class="nav-link-text"> COIN錢包</span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="javascript:">
                                        <i class="fa fa-key text-success"></i>
                                        <span class="nav-link-text"> 設定</span>
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
                                        <span class="nav-link-text"> 大一</span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="javascript:">
                                        <i class="fa fa-palette"></i>
                                        <span class="nav-link-text"> 大二</span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="javascript:">
                                        <i class="fa fa-chart-pie"></i>
                                        <span class="nav-link-text"> 大三</span>
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="javascript:">
                                        <i class="fa fa-puzzle-piece"></i>
                                        <span class="nav-link-text"> 大四</span>
                                    </a>
                                </li>
                            </ul>
                            
                        </div>
                        
                    </div>
                </div>



                <!-- Main Sesrch Result MIDDLE column -->
                <div class="col-lg-8">
                    <div class="row removable">
                        <div class="col-lg-12"></div>
                    </div>
                    <div class="row removable">
                        <div class="card-body col-lg-12" style="background: #FFF">
                            <p class="h1 text-center" >帖子內容</p>
                        </div>
                    </div>

                    <!-- Dropdown Searh filter -->
                    <div class="row removable">
                        <div class="col-lg-12" style="background: #FFF">
                            <div class="row removable">
                                <div class="col-lg-3">
                                    <div class="dropdown">
                                        <button class="btn btn-dark dropdown-toggle mr-0" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">年份</button>
                                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 42px, 0px);" x-placement="bottom-start">
                                            <a class="dropdown-item" href="#">Action</a>
                                            <a class="dropdown-item" href="#">Another action</a>
                                            <a class="dropdown-item" href="#">Something else here</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-3">
                                    <div class="dropdown">
                                        <button class="btn btn-dark dropdown-toggle mr-0" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">課程</button>
                                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 42px, 0px);" x-placement="bottom-start">
                                            <a class="dropdown-item" href="#">Action</a>
                                            <a class="dropdown-item" href="#">Another action</a>
                                            <a class="dropdown-item" href="#">Something else here</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-3">
                                    <div class="dropdown">
                                        <button class="btn btn-dark dropdown-toggle mr-0" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">授課老師</button>
                                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 42px, 0px);" x-placement="bottom-start">
                                            <a class="dropdown-item" href="#">Action</a>
                                            <a class="dropdown-item" href="#">Another action</a>
                                            <a class="dropdown-item" href="#">Something else here</a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-3"><button class="btn btn-dark">搜尋</button></div>
                            </div>
                        </div>
                    </div>
                    <!-- End of Dropdown Searh filter -->


                    <div class="row removable">
                        <div class="card-body col-lg-12" style="background: #FFF">
                            
                            <div class="row removable">
                                <div class="col-lg-1"></div>
                                <div class="card-body col-lg-10" style="background: #FFF3F3">
                                    <p></p>
                                    <div class="row removable">
                                        <div class="col-lg-6" >                                           
                                            <p class="h3">課程名稱 XXX老師</p>
                                        </div>
                                        
                                    </div>
                                    <div class="row removable">
                                        <div class="col-lg-6">
                                            <p class="h4">帖子內容</p>
                                        </div>
                                        
                                    </div>
                                    <div class="row removable">
                                        <div class="col-lg-6">
                                            <p class="h6">作者: John Doe</p>
                                        </div>
                                        
                                    </div>
                                </div>                               
                                <div class="col-lg-1"></div>
                            </div>
                            <!-- 白色row -->
                            <div class="card-body"></div>


                            <div class="row removable">
                                <div class="col-lg-1"></div>
                                <div class="card-body col-lg-10" style="background: #FFF3F3">
                                    <p></p>
                                    <div class="row removable">
                                        <div class="col-lg-6" >                                           
                                            <p class="h3">帖子標題 2</p>
                                        </div>
                                        
                                    </div>
                                    <div class="row removable">
                                        <div class="col-lg-6">
                                            <p class="h4">帖子內容</p>
                                        </div>
                                        
                                    </div>
                                    <div class="row removable">
                                        <div class="col-lg-6">
                                            <p class="h6">作者: John Doe</p>
                                        </div>
                                        
                                    </div>
                                </div>                               
                                <div class="col-lg-1"></div>
                            </div>
                            <!-- 白色row -->
                            <div class="card-body"></div>


                            <div class="row removable">
                                <div class="col-lg-1"></div>
                                <div class="card-body col-lg-10" style="background: #FFF3F3">
                                    <p></p>
                                    <div class="row removable">
                                        <div class="col-lg-6" >                                           
                                            <p class="h3">帖子標題 3</p>
                                        </div>
                                        
                                    </div>
                                    <div class="row removable">
                                        <div class="col-lg-6">
                                            <p class="h4">帖子內容</p>
                                        </div>
                                        
                                    </div>
                                    <div class="row removable">
                                        <div class="col-lg-6">
                                            <p class="h6">作者: John Doe</p>
                                        </div>
                                        
                                    </div>
                                </div>                               
                                <div class="col-lg-1"></div>
                            </div>
                            <!-- 白色row -->
                            <div class="card-body"></div>
                        </div>
                    </div>
                    <div class="row removable">
                        <div class="col-lg-12"></div>
                    </div>
                    </div>


                <!-- Grading RIGHT column -->
                <div class="col-lg-2">
                    <div class="row removable">
                        <div class="col-lg-12">
                            <p class="">評分</p>
                        </div>
                    </div>
                    <div class="row removable">
                        <div class="col-lg-12">
                            <p class="">A</p>
                            <p class="">B</p>
                            <p class="">C</p>
                            <p class="">D</p>
                            <p class="">E</p>
                            <p class="">F</p>
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
    </div>

</body>

  </template>
  
  
  <!-- <script src="../assets/style/loopple.js"></script> -->
  