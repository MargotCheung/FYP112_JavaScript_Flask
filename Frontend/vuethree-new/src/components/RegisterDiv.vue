<template>
      
    <div class="login-card-container">

        <div class="content">
            <div class="logo-text">
                <h2>逢甲避雷手冊</h2>
                <p>總有一些課適合你</p>
            </div>
        </div>

        <div class="login-section">

            <div class="form-box register">
                <form action="">
                    <h2>注冊</h2>
                    <div class="input-box">
                        <span class="icon material-symbols-rounded">person</span>
                        <input type="text" required autofocus>
                        <label for="">帳號</label>
                    </div>
                    <div class="input-box">
                        <span class="icon material-symbols-rounded">mail</span>
                        <input type="email" required>
                        <label for="">Email</label>
                    </div>
                    <div class="input-box">
                        <span class="icon material-symbols-rounded">lock</span>
                        <input type="password" required>
                        <label for="">密碼</label>
                    </div>
                    <div class="input-box">
                        <span class="icon material-symbols-rounded">lock</span>
                        <input type="password" required>
                        <label for="">確認密碼</label>
                    </div>
                    <div class="remember-password">
                        <label for=""><input type="checkbox">我同意會員規範及隱私權政策。</label>
                    </div>
                    <button class="btn">注冊</button>
                    <div class="create-account">
                        <p>已經有帳號？<a href="#" class="login-link">登入</a></p>
                    </div>
                </form>             
            </div>

            <div class="form-box login">
                <form action="">
                    <h2>登入</h2>
                    <div class="input-box">
                        <span class="icon material-symbols-rounded">person</span>
                        <input type="text" required autofocus>
                        <label for="">帳號</label>
                    </div>
                    <div class="input-box">
                        <span class="icon material-symbols-rounded">lock</span>
                        <input type="password" required>
                        <label for="">密碼</label>
                    </div>
                    <div class="remember-password">
                        <label for=""><input type="checkbox">記住我</label>
                        <a href="#">忘記密碼</a>
                    </div>
                    <button class="btn">登入</button>
                    <div class="create-account">
                        <p>還沒有帳號嗎？<a href="#" class="register-link">注冊新帳號</a></p>
                    </div>
                </form>
            </div>

            
        </div>
    </div>

</template>

<script>
export default {
  name: 'RegisterDiv',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

body{
    height: 100vh;
    width: 100%;
    background-color: rgba(255, 232, 214, 1);
}

.header{
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

.navbar a{
    position: relative;
    font-size: 16px;
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
}

.login-card-container{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    width: 75%;
    height: 550px;
    margin-top: 20px;
    background: #DDBEA9;
    border-radius: 20px;
    overflow: hidden;
}

.content{
    position: absolute;
    top: 0;
    left: 0;
    width: 58%;
    height: 100%;
    color: #6B705C;
    background: #DDBEA9;
    padding: 80px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    border-radius: 20px;
}

.logo-text{
    position: absolute;
    top: 45%;
}

.logo-text h2{
    font-size: 40px;
    line-height: 1;
}

.logo-text p{
    font-size: 16px;
    margin: 20px;
}

.login-card-container .login-section{
    position: absolute;
    top: 0;
    right: 0;
    width: calc(100% - 58%);
    height: 100%;
    color: #6B705C;
}

.login-section .form-box{
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}

.login-section .form-box.register{
    transform: translateX(430px);
    transition: transform .6s ease;
    transition-delay: 0s;
}

.login-section.active .form-box.register{
    transform: translateX(0px);
    transition-delay: .7s;
}

.login-section .form-box.login{
    transform: translateX(0px);
    transition: transform .6s ease;
    transition-delay: .7s;
}

.login-section.active .form-box.login{
    transform: translateX(430px);
    transition-delay: 0s;
}

.login-section .form-box h2{
    text-align: center;
    font-size: 25px;
}

.form-box .input-box{
    width: 340px;
    height: 50px;
    border-bottom: 2px solid #fff;
    margin: 30px 0;
    position: relative;
}

.input-box input{
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    font-size: 16px;
    padding-right: 28px;
}

.input-box label{
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    font-size: 16px;
    font-weight: 600px;
    pointer-events: none;
    transition: .5s ease;
}

.input-box .icon{
    position: absolute;
    top: 13px;
    right: 0;
    font-size: 19px;
}

.input-box input:focus~label,
.input-box input:valid~label{
    top: -5px;
}

.remember-password{
    font-size: 14px;
    font-weight: 500;
    margin: -15px 0 15px;
    display: flex;
    justify-content: space-between;
}

.remember-password label input{
    accent-color: #fff;
    margin-right: 3px;
}

.remember-password a{
    color: #6B705C;
    text-decoration: none;
}

.remember-password a:hover{
    text-decoration: underline;
}

.btn{
    background: rgba(203, 153, 126, 1);
    width: 100%;
    height: 45px;
    outline: none;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    color: #fff;
    box-shadow: rgba(0, 0, 0, 0.4);
}

.create-account{
    font-size: 14.5px;
    text-align: center;
    margin: 25px;
}

.create-account p a{
    color: #A5A58D;
    font-weight: 600px;
    text-decoration: none;
}

.create-account p a:hover{
    text-decoration: underline;
}

</style>
