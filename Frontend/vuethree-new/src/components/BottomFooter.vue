<template>
  
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
                            <a href="javascript:void(0);" class="nav-link">網站投訴電話 : 04-24517250</a>
                        </li>
                        <li class="nav-item">
                            <a href="javascript:;" class="nav-link" style="margin-right: 150px">網站負責人：校霸</a>
                        </li> 
                    </ul>
                </div>
            </div>
  </footer>

  <router-view/>


</template>

<script>
export default {
  name: 'BottomFooter',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
</style>
