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
                        <!-- <div class="card-body" style="background: #DDBEA9"></div> -->
                        <div class="card-body" style="background: #DDBEA9"></div>
                        
                        <div class="card-body" style="background: #DDBEA9" >


                          <div class="row removable">  
                                <p class="text-lg-left" style="margin-left: 20px; font-size: 25px; font-weight: 500; color: #000; text-indent: 0%">輸入暱稱</p>                         
                                <div class="col-lg-9" style="margin-left: 20px"><input class="form-control" style="text-align: center" type="text" placeholder="輸入暱稱"></div>                                                
                            </div>

                            <div class="row removable">
                                <a class="text-lg-left" style="margin-left: 20px; font-size: 25px; font-weight: 500; color: #000; text-indent: 0%">Email</a>
                                <div class="col-lg-9" style="margin-left: 20px"><input class="form-control" style="text-align: center" type="email" placeholder="輸入Email"></div> 
                            </div>    

                            <div class="row removable">  
                                <p class="text-lg-left" style="margin-left: 20px; font-size: 25px; font-weight: 500; color: #000; text-indent: 0%">輸入密碼</p>                         
                                <div class="col-lg-9" style="margin-left: 20px"><input class="form-control" style="text-align: center" type="password" placeholder="輸入密碼"></div>                                                
                            </div>

                            <div class="row removable">  
                                <p class="text-lg-left" style="margin-left: 20px; font-size: 25px; font-weight: 500; color: #000; text-indent: 0%">確認密碼</p>                         
                                <div class="col-lg-9" style="margin-left: 20px"><input class="form-control" style="text-align: center" type="password" placeholder="確認密碼"></div>                                                
                            </div>

                            <p></p>

                            <div class="card-body" style="background: #DDBEA9"></div>
                            

                            <div class="row removable"> 
                                <div class="col-lg-12"><button class="btn btn-default col text-center" style="background:#CB997E"><router-link to="/about" style="color: #FFFFFF">註冊</router-link></button></div>                                        
                            </div>
                       
                            

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
                <div class="card-body"></div>
            </div>
        </footer>
    </div>
</body>

</template>



<!-- <script src="../assets/style/loopple.js"></script> -->
