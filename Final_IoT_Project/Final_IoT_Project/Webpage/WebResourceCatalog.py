import cherrypy
import os
import requests
import json


class MuseumsWP (object):
    exposed = True
    def GET(self, *uri, **params):

        with open ('config_file.json', 'r') as json_data_file:
            obj = json.load (json_data_file)
            url = str(obj["reSourceCatalog"]["url"])

        inidata = requests.get(url)
        json_inidata = json.loads(inidata.text)

        if uri[0] == "index":

            return '''  <!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                            <!-- Meta, title, CSS, favicons, etc. -->
                            <meta charset="utf-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1">

                            <title>Admon Museums | </title>

                            <!-- Bootstrap -->
                            <link href="/static/vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
                            <!-- Font Awesome -->
                            <link href="/static/vendors/font-awesome-4.7.0/css/font-awesome.min.css" rel="stylesheet">
                            <!-- NProgress -->
                            <link href="/static/vendors/nprogress/nprogress.css" rel="stylesheet">
                            <!-- iCheck -->
                            <link href="/static/vendors/iCheck/skins/flat/green.css" rel="stylesheet">

                            <!-- bootstrap-progressbar -->
                            <link href="/static/vendors/bootstrap-progressbar/css/bootstrap-progressbar-3.3.4.min.css" rel="stylesheet">
                            <!-- JQVMap -->
                            <link href="/static/vendors/jqvmap/dist/jqvmap.min.css" rel="stylesheet"/>
                            <!-- bootstrap-daterangepicker -->
                            <link href="/static/vendors/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

                            <!-- Custom Theme Style -->
                            <link href="/static/build/css/custom.min.css" rel="stylesheet">
                          </head>

                          <body class="nav-md">
                            <div class="container body">
                              <div class="main_container">
                                <div class="col-md-3 left_col">
                                  <div class="left_col scroll-view">
                                    <div class="navbar nav_title" style="border: 0;">
                                      <a href="index" class="site_title"><i class="fa fa-paw"></i> <span>Admon Museum!</span></a>
                                    </div>

                                    <div class="clearfix"></div>

                                    <!-- menu profile quick info -->
                                    <div class="profile clearfix">
                                      <div class="profile_pic">
                                        <img src="/static/production/images/Carla.jpeg" alt="..." class="img-circle profile_img">
                                      </div>
                                      <div class="profile_info">
                                        <span>Welcome,</span>
                                        <h2>Carla Corona </h2>
                                      </div>
                                    </div>
                                    <!-- /menu profile quick info -->

                                    <br />

                                    <!-- sidebar menu -->
                                    <div id="sidebar-menu" class="main_menu_side hidden-print main_menu">
                                      <div class="menu_section">
                                        <h3>General</h3>
                                        <ul class="nav side-menu">
                                          <li><a><i class="fa fa-home"></i> Room 1 <span class="fa fa-chevron-down"></span></a>
                                            <ul class="nav child_menu">
                                              <li><a href="dash1">Dashboard</a></li>
                                            </ul>
                                          </li>

                                        </ul>
                                      </div>
                                      <div class="menu_section">

                                      </div>

                                    </div>
                                    <!-- /sidebar menu -->

                                    <!-- /menu footer buttons -->
                                    <div class="sidebar-footer hidden-small">
                                      <a data-toggle="tooltip" data-placement="top" title="Logout" href="/static/production/login.html">
                                        <span class="glyphicon glyphicon-off" aria-hidden="true"></span>
                                      </a>
                                    </div>
                                    <!-- /menu footer buttons -->
                                  </div>
                                </div>

                                <!-- top navigation -->
                                <div class="top_nav">
                                  <div class="nav_menu">
                                    <nav>
                                      <div class="nav toggle">
                                        <a id="menu_toggle"><i class="fa fa-bars"></i></a>
                                      </div>

                                      <ul class="nav navbar-nav navbar-right">
                                        <li class="">
                                          <a href="javascript:;" class="user-profile dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                                            <img src="/static/production/images/Carla.jpeg" alt="">Carla Corona
                                            <span class=" fa fa-angle-down"></span>
                                          </a>
                                          <ul class="dropdown-menu dropdown-usermenu pull-right">
                                            <li><a href="javascript:;"> Profile</a></li>
                                            <li>
                                              <a href="javascript:;">
                                                <span class="badge bg-red pull-right">50%</span>
                                                <span>Settings</span>
                                              </a>
                                            </li>
                                            <li><a href="javascript:;">Help</a></li>
                                            <li><a href="/static/production/login.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
                                          </ul>
                                        </li>

                                        <!-- Envelope notificactions -->
                                        <li role="presentation" class="dropdown">
                                          <a href="javascript:;" class="dropdown-toggle info-number" data-toggle="dropdown" aria-expanded="false">
                                            <i class="fa fa-envelope-o"></i>
                                            <span class="badge bg-green">6</span>
                                          </a>
                                          <ul id="menu1" class="dropdown-menu list-unstyled msg_list" role="menu">
                                            <li>
                                              <a>
                                                <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                                <span>
                                                  <span>John Smith</span>
                                                  <span class="time">3 mins ago</span>
                                                </span>
                                                <span class="message">
                                                  Film festivals used to be do-or-die moments for movie makers. They were where...
                                                </span>
                                              </a>
                                            </li>
                                            <li>
                                              <a>
                                                <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                                <span>
                                                  <span>John Smith</span>
                                                  <span class="time">3 mins ago</span>
                                                </span>
                                                <span class="message">
                                                  Film festivals used to be do-or-die moments for movie makers. They were where...
                                                </span>
                                              </a>
                                            </li>
                                            <li>
                                              <a>
                                                <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                                <span>
                                                  <span>John Smith</span>
                                                  <span class="time">3 mins ago</span>
                                                </span>
                                                <span class="message">
                                                  Film festivals used to be do-or-die moments for movie makers. They were where...
                                                </span>
                                              </a>
                                            </li>
                                            <li>
                                              <a>
                                                <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                                <span>
                                                  <span>John Smith</span>
                                                  <span class="time">3 mins ago</span>
                                                </span>
                                                <span class="message">
                                                  Film festivals used to be do-or-die moments for movie makers. They were where...
                                                </span>
                                              </a>
                                            </li>
                                            <li>
                                              <div class="text-center">
                                                <a>
                                                  <strong>See All Alerts</strong>
                                                  <i class="fa fa-angle-right"></i>
                                                </a>
                                              </div>
                                            </li>
                                          </ul>
                                        </li>
                                      </ul>
                                    </nav>
                                  </div>
                                </div>
                                <!-- /top navigation -->

                                <!-- page content -->

                                <style>
                                    /*form {width:100%; height:450px; margin:auto; position:relative;}*/
                                    input.normalheight{height: 28px; }
                                    input.small { width:24.9%;}
                                    input.thingspeak{float: left; width:71%;font-weight:normal;}
                                    form.big { line-height: 2;}
                                    label.thingspeak{ float: left;clear: left; width: 150px; text-align: left;font-weight:normal;}
                                    label.smallthingspeak{clear: left;width: 150px; font-weight:normal;}
                                </style>

                                <div class="right_col" role="main">
                                  <!-- top tiles -->
                                  <div class="row tile_count">
                                    <h2>Current thresholds values: </h2><br>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-thermometer-full"></i> Maximum temperature</span>
                                      <div class="count"> '''+ str(json_inidata["thresholds"]["max_temp"])+'''</div>
                                    </div>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-thermometer-quarter"></i> Minimum temperature</span>
                                      <div class="count">'''+ str(json_inidata["thresholds"]["min_temp"])+'''</div>
                                    </div>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-circle"></i> Maximum humidity</span>
                                      <div class="count">'''+ str(json_inidata["thresholds"]["max_hum"])+'''</div>
                                    </div>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-circle-o.."></i> Minimum humidity</span>
                                      <div class="count">'''+ str(json_inidata["thresholds"]["min_hum"])+'''</div>
                                    </div>

                                  </div>
                                  <!-- /top tiles -->



                                  <div class="row">

                                    <div class="column">
                                      <div class="col-md-4 col-sm-4 col-xs-12">
                                        <div class="x_panel tile fixed_height_350">
                                          <div class="x_title">
                                            <h2>Change thresholds</h2>
                                            <div class="clearfix"></div>
                                          </div>
                                          <div class="x_content">
                                            <div align="center">
                                              <form style="font-size:15px" action="/replytresh" method="POST">
                                                    Maximum temperature:   <input type="number" value="'''+ str(json_inidata["thresholds"]["max_temp"])+'''" name="maxt" >
                                                    <br/>
                                                    Minimum temperature:   <input type="text" value="'''+ str(json_inidata["thresholds"]["min_temp"])+'''" name="mint">
                                                    <br/>
                                                    Maximum humidity:   <input type="text" value="'''+ str(json_inidata["thresholds"]["max_hum"])+'''" name="maxh">
                                                    <br/>
                                                    Minimum humidity:   <input type="text" value="'''+ str(json_inidata["thresholds"]["min_hum"])+'''" name="minh">
                                                    <br/>
                                                    <br/>
                                                    <button class="btn btn-success btn-sm" style="width:30%;" > Submit </button>
                                                    <!--input type="submit"-->
                                              </form>
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                    </div>

                                    <div class="column">
                                      <div class="col-md-8 col-sm-4 col-xs-12">
                                        <div class="x_panel tile fixed_height_350">
                                          <div class="x_title" >
                                            <h2>Thingspeak Connection</h2>
                                            <ul class="nav navbar-right panel_toolbox">
                                              <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                              </li>
                                              <li><a class="close-link"><i class="fa fa-close"></i></a>
                                              </li>
                                            </ul>
                                            <div class="clearfix"></div>

                                          </div>
                                          <div class="x_content" style="display:none;">


                                            <div align="left">
                                              <form class="big" id="thingspeak" style="font-size:15px" action="/replything" method="POST">
                                                    <label class="thingspeak">Thingspeak_HOST:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["THINGSPEAK_HOST"])+'''" name="tkHost" >
                                                    <br/>
                                                    <label class="thingspeak">mqtt HOST:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["mqttHost"])+'''" name="mqttHost">
                                                    <br/>
                                                    <label class="thingspeak">tPort:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["tPort"])+'''" name="tPort">
                                                    <br/>
                                                    <label class="thingspeak">Channel ID:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["channelID"])+'''" name="chanId">
                                                    <br/>
                                                    <label class="thingspeak">tTransport:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["tTransport"])+'''" name="tTrans">
                                                    <br/>
                                                    <br/>
                                                    <label class="smallthingspeak">ACCESS TOKEN:</label><input class="normalheight small" type="text" value="'''+ str(json_inidata["thingspeak"]["ACCESS_TOKEN"])+'''" name="accTok">
                                                    <label style="width: 120px; font-weight:normal;">READ API KEY:</label><input class="normalheight small" type="text" value="'''+ str(json_inidata["thingspeak"]["READ_API_KEY"])+'''" name="rApi">
                                                    <br/>
                                                    <button class="btn btn-success btn-sm" id="bthingspeak" style="width:30%;"> Submit </button>
                                                    <!--input type="submit"-->
                                              </form>
                                            </div>
                                          </div>
                                        </div>
                                      </div>

                                      <div class="col-md-8 col-sm-4 col-xs-12">
                                        <div class="x_panel tile fixed_height_350">
                                          <div class="x_title" >
                                            <h2>Broker Connection</h2>
                                            <ul class="nav navbar-right panel_toolbox">
                                              <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                              </li>
                                              <li><a class="close-link"><i class="fa fa-close"></i></a>
                                              </li>
                                            </ul>
                                            <div class="clearfix"></div>

                                          </div>
                                          <div class="x_content" style="display:none;">


                                            <div align="left">
                                              <form class="big" id="broker" style="font-size:15px" action="/replybroker" method="POST">
                                                    <label class="thingspeak">Broker IP:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Broker_IP"])+'''" name="brokerIP" >
                                                    <br/>
                                                    <label class="thingspeak">Broker Port:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Broker_port"])+'''" name="brokerPort">
                                                    <br/>
                                                    <label class="thingspeak">DHT Topic:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["DHT_Topic"])+'''" name="dhtTop">
                                                    <br/>
                                                    <label class="thingspeak">AC Topic:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["AC_Topic"])+'''" name="acTop">
                                                    <br/>
                                                    <label class="thingspeak">Counter Topic:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Counter_Topic"])+'''" name="counTop">
                                                    <br/>
                                                    <label class="thingspeak">AC Status:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Ac_Status"])+'''" name="acStatus">
                                                    <br/>
                                                    <br/>
                                                    <button class="btn btn-success btn-sm" id="bbroker" style="width:30%;"> Submit </button>
                                                    <!--input type="submit"-->
                                              </form>
                                            </div>
                                          </div>
                                        </div>
                                      </div>

                                      <div class="col-md-8 col-sm-4 col-xs-12">
                                        <div class="x_panel tile fixed_height_350">
                                          <div class="x_title" >
                                            <h2>Telegram Connection</h2>
                                            <ul class="nav navbar-right panel_toolbox">
                                              <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                              </li>
                                              <li><a class="close-link"><i class="fa fa-close"></i></a>
                                              </li>
                                            </ul>
                                            <div class="clearfix"></div>

                                          </div>
                                          <div class="x_content" style="display:none;">


                                            <div align="left">
                                              <form class="big" id="telegram" style="font-size:15px" action="/replytele" method="POST">
                                                    <label class="thingspeak">Port:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["telegram"]["Port"])+'''" name="telPort" >
                                                    <br/>
                                                    <label class="thingspeak">ChatID:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["telegram"]["chatID"])+'''" name="telchatid" >
                                                    <br/>
                                                    <button class="btn btn-success btn-sm" id="thingspeak" style="width:30%;"> Submit </button>
                                                    <!--input type="submit"-->
                                              </form>
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                      <div class="col-md-8 col-sm-4 col-xs-12">
                                        <div class="x_panel tile fixed_height_350">
                                          <div class="x_title" >
                                            <h2>Data to REST</h2>
                                            <ul class="nav navbar-right panel_toolbox">
                                              <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                              </li>
                                              <li><a class="close-link"><i class="fa fa-close"></i></a>
                                              </li>
                                            </ul>
                                            <div class="clearfix"></div>

                                          </div>
                                          <div class="x_content" style="display:none;">


                                            <div align="left">
                                              <form class="big" id="datatorest" style="font-size:15px" action="/replydatatorest" method="POST">
                                                    <label class="thingspeak">Host IP:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["dataToRest"]["Host_IP"])+'''" name="hostIP" >
                                                    <br/>
                                                    <label class="thingspeak">Port:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["dataToRest"]["port"])+'''" name="dtrport" >
                                                    <br/>
                                                    <button class="btn btn-success btn-sm" id="thingspeak" style="width:30%;"> Submit </button>
                                                    <!--input type="submit"-->
                                              </form>
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                  </div>

                                </div>

                                <!-- /page content -->

                                <!-- footer content -->
                                <footer>
                                  <div class="pull-right">
                                    Gentelella - Bootstrap Admin Template by <a href="https://colorlib.com">Colorlib</a>
                                  </div>
                                  <div class="clearfix"></div>
                                </footer>
                                <!-- /footer content -->
                              </div>
                            </div>

                            <!-- jQuery -->
                            <script src="/static/vendors/jquery/dist/jquery.min.js"></script>
                            <!-- Bootstrap -->
                            <script src="/static/vendors/bootstrap/dist/js/bootstrap.min.js"></script>
                            <!-- FastClick -->
                            <script src="/static/vendors/fastclick/lib/fastclick.js"></script>
                            <!-- NProgress -->
                            <script src="/static/vendors/nprogress/nprogress.js"></script>
                            <!-- Chart.js -->
                            <script src="/static/vendors/Chart.js/dist/Chart.min.js"></script>
                            <!-- gauge.js -->
                            <script src="/static/vendors/gauge.js/dist/gauge.min.js"></script>
                            <!-- bootstrap-progressbar -->
                            <script src="/static/vendors/bootstrap-progressbar/bootstrap-progressbar.min.js"></script>
                            <!-- iCheck -->
                            <script src="/static/vendors/iCheck/icheck.min.js"></script>
                            <!-- Skycons -->
                            <script src="/static/vendors/skycons/skycons.js"></script>
                            <!-- Flot -->
                            <script src="/static/vendors/Flot/jquery.flot.js"></script>
                            <script src="/static/vendors/Flot/jquery.flot.pie.js"></script>
                            <script src="/static/vendors/Flot/jquery.flot.time.js"></script>
                            <script src="/static/vendors/Flot/jquery.flot.stack.js"></script>
                            <script src="/static/vendors/Flot/jquery.flot.resize.js"></script>
                            <!-- Flot plugins -->
                            <script src="/static/vendors/flot.orderbars/js/jquery.flot.orderBars.js"></script>
                            <script src="/static/vendors/flot-spline/js/jquery.flot.spline.min.js"></script>
                            <script src="/static/vendors/flot.curvedlines/curvedLines.js"></script>
                            <!-- DateJS -->
                            <script src="/static/vendors/DateJS/build/date.js"></script>
                            <!-- JQVMap -->
                            <script src="/static/vendors/jqvmap/dist/jquery.vmap.js"></script>
                            <script src="/static/vendors/jqvmap/dist/maps/jquery.vmap.world.js"></script>
                            <script src="/static/vendors/jqvmap/examples/js/jquery.vmap.sampledata.js"></script>
                            <!-- bootstrap-daterangepicker -->
                            <script src="/static/vendors/moment/min/moment.min.js"></script>
                            <script src="/static/vendors/bootstrap-daterangepicker/daterangepicker.js"></script>

                            <!-- Custom Theme Scripts -->
                            <script src="/static/build/js/custom.min.js"></script>

                          </body>
                        </html>



                    '''

        elif (uri[0] == "maxTemp"):
            return (str(json_inidata["thresholds"]["max_temp"]))
        elif (uri[0] == "minTemp"):
            return (str (json_inidata["thresholds"]["min_temp"]))
        elif (uri[0] == "maxHum"):
            return (str (json_inidata["thresholds"]["max_hum"]))
        elif (uri[0] == "minHum"):
            return (str (json_inidata["thresholds"]["min_hum"]))
        elif (uri[0] == "readAPIkey"):
            return (str(json_inidata["thingspeak"]["READ_API_KEY"]))
        elif (uri[0] == "accToken"):
            return (str(json_inidata["thingspeak"]["ACCESS_TOKEN"]))
        elif (uri[0] == "tTrans"):
            return (str(json_inidata["thingspeak"]["tTransport"]))
        elif (uri[0] == "chanID"):
            return (str(json_inidata["thingspeak"]["channelID"]))
        elif (uri[0] == "tPort"):
            return (str(json_inidata["thingspeak"]["tPort"]))
        elif (uri[0] == "mqttHost"):
            return (str(json_inidata["thingspeak"]["mqttHost"]))
        elif (uri[0] == "thingHost"):
            return (str(json_inidata["thingspeak"]["THINGSPEAK_HOST"]))
        elif (uri[0] == "brokerIP"):
            return (str(json_inidata["broker"]["Broker_IP"]))
        elif (uri[0] == "brokerPort"):
            return (str(json_inidata["broker"]["Broker_port"]))
        elif (uri[0] == "acTop"):
            return (str(json_inidata["broker"]["AC_Topic"]))
        elif (uri[0] == "dhtTop"):
            return (str(json_inidata["broker"]["DHT_Topic"]))
        elif (uri[0] == "counTop"):
            return (str(json_inidata["broker"]["Counter_Topic"]))
        elif (uri[0] == "acStat"):
            return (str(json_inidata["broker"]["Ac_Status"]))
        elif (uri[0] == "telegPort"):
            return (str(json_inidata["telegram"]["Port"]))
        elif (uri[0] == "telegChatid"):
            return (str(json_inidata["telegram"]["chatID"]))
        elif (uri[0] == "dash1"):

            return open('static_dashboard_mqtt.html')


            # else:
            #    if cherrypy.request.method in cherrypy.request.methods_with_bodies:
            #       return (cherrypy.request.body.read())

    def POST(self, *uri, **params):
        # obj = cherrypy.request.body.read()
        data = {}

        if uri[0]== "replytresh":

            data ={'thresholds': {"max_temp": str(params['maxt']),
                                 "min_temp": str(params['mint']),
                                 "max_hum": str(params['maxh']),
                                 "min_hum": str(params['minh'])}}

            json_data = json.dumps(data)

        elif uri[0]=="replything":
            obj['thingspeak'] = {"READ_API_KEY": str(params['rApi']),
                                 "ACCESS_TOKEN": str(params['accTok']),
                                 "tTransport": str(params['tTrans']),
                                 "channelID": str(params['chanId']),
                                 "tPort": str(params['tPort']),
                                 "mqttHost": str(params['mqttHost']),
                                 "THINGSPEAK_HOST": str(params['tkHost'])}
        elif uri[0]=="replybroker":
            obj['broker'] = {"Broker_IP": str(params['brokerIP']),
                                 "AC_Topic": str(params['acTop']),
                                 "Broker_port": str(params['brokerPort']),
                                 "DHT_Topic": str(params['dhtTop']),
                                 "Counter_Topic": str(params['counTop'])}
        elif uri[0]=="replytele":
            obj['telegram'] = {"Port": str(params['telPort']),
                               "chatID": str(params['telchatid'])}



        with open ('initial_data.json', 'w') as json_data_file:
            json.dump (obj, json_data_file)
        return '''  <!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                        <!-- Meta, title, CSS, favicons, etc. -->
                        <meta charset="utf-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1">

                        <title>Admon Museums | </title>

                        <!-- Bootstrap -->
                        <link href="/static/vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
                        <!-- Font Awesome -->
                        <link href="/static/vendors/font-awesome-4.7.0/css/font-awesome.min.css" rel="stylesheet">
                        <!-- NProgress -->
                        <link href="/static/vendors/nprogress/nprogress.css" rel="stylesheet">
                        <!-- iCheck -->
                        <link href="/static/vendors/iCheck/skins/flat/green.css" rel="stylesheet">

                        <!-- bootstrap-progressbar -->
                        <link href="/static/vendors/bootstrap-progressbar/css/bootstrap-progressbar-3.3.4.min.css" rel="stylesheet">
                        <!-- JQVMap -->
                        <link href="/static/vendors/jqvmap/dist/jqvmap.min.css" rel="stylesheet"/>
                        <!-- bootstrap-daterangepicker -->
                        <link href="/static/vendors/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

                        <!-- Custom Theme Style -->
                        <link href="/static/build/css/custom.min.css" rel="stylesheet">
                      </head>

                      <body class="nav-md">
                        <div class="container body">
                          <div class="main_container">
                            <div class="col-md-3 left_col">
                              <div class="left_col scroll-view">
                                <div class="navbar nav_title" style="border: 0;">
                                  <a href="index" class="site_title"><i class="fa fa-paw"></i> <span>Admon Museum!</span></a>
                                </div>

                                <div class="clearfix"></div>

                                <!-- menu profile quick info -->
                                <div class="profile clearfix">
                                  <div class="profile_pic">
                                    <img src="/static/production/images/Carla.jpeg" alt="..." class="img-circle profile_img">
                                  </div>
                                  <div class="profile_info">
                                    <span>Welcome,</span>
                                    <h2>Carla Corona </h2>
                                  </div>
                                </div>
                                <!-- /menu profile quick info -->

                                <br />

                                <!-- sidebar menu -->
                                <div id="sidebar-menu" class="main_menu_side hidden-print main_menu">
                                  <div class="menu_section">
                                    <h3>General</h3>
                                    <ul class="nav side-menu">
                                      <li><a><i class="fa fa-home"></i> Room 1 <span class="fa fa-chevron-down"></span></a>
                                        <ul class="nav child_menu">
                                          <li><a href="dash1">Dashboard</a></li>
                                        </ul>
                                      </li>

                                    </ul>
                                  </div>
                                  <div class="menu_section">

                                  </div>

                                </div>
                                <!-- /sidebar menu -->

                                <!-- /menu footer buttons -->
                                <div class="sidebar-footer hidden-small">
                                  <a data-toggle="tooltip" data-placement="top" title="Logout" href="/static/production/login.html">
                                    <span class="glyphicon glyphicon-off" aria-hidden="true"></span>
                                  </a>
                                </div>
                                <!-- /menu footer buttons -->
                              </div>
                            </div>

                            <!-- top navigation -->
                            <div class="top_nav">
                              <div class="nav_menu">
                                <nav>
                                  <div class="nav toggle">
                                    <a id="menu_toggle"><i class="fa fa-bars"></i></a>
                                  </div>

                                  <ul class="nav navbar-nav navbar-right">
                                    <li class="">
                                      <a href="javascript:;" class="user-profile dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                                        <img src="/static/production/images/Carla.jpeg" alt="">Carla Corona
                                        <span class=" fa fa-angle-down"></span>
                                      </a>
                                      <ul class="dropdown-menu dropdown-usermenu pull-right">
                                        <li><a href="javascript:;"> Profile</a></li>
                                        <li>
                                          <a href="javascript:;">
                                            <span class="badge bg-red pull-right">50%</span>
                                            <span>Settings</span>
                                          </a>
                                        </li>
                                        <li><a href="javascript:;">Help</a></li>
                                        <li><a href="/static/production/login.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
                                      </ul>
                                    </li>

                                    <!-- Envelope notificactions -->
                                    <li role="presentation" class="dropdown">
                                      <a href="javascript:;" class="dropdown-toggle info-number" data-toggle="dropdown" aria-expanded="false">
                                        <i class="fa fa-envelope-o"></i>
                                        <span class="badge bg-green">6</span>
                                      </a>
                                      <ul id="menu1" class="dropdown-menu list-unstyled msg_list" role="menu">
                                        <li>
                                          <a>
                                            <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                            <span>
                                              <span>John Smith</span>
                                              <span class="time">3 mins ago</span>
                                            </span>
                                            <span class="message">
                                              Film festivals used to be do-or-die moments for movie makers. They were where...
                                            </span>
                                          </a>
                                        </li>
                                        <li>
                                          <a>
                                            <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                            <span>
                                              <span>John Smith</span>
                                              <span class="time">3 mins ago</span>
                                            </span>
                                            <span class="message">
                                              Film festivals used to be do-or-die moments for movie makers. They were where...
                                            </span>
                                          </a>
                                        </li>
                                        <li>
                                          <a>
                                            <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                            <span>
                                              <span>John Smith</span>
                                              <span class="time">3 mins ago</span>
                                            </span>
                                            <span class="message">
                                              Film festivals used to be do-or-die moments for movie makers. They were where...
                                            </span>
                                          </a>
                                        </li>
                                        <li>
                                          <a>
                                            <span class="image"><img src="/static/production/images/img.jpg" alt="Profile Image" /></span>
                                            <span>
                                              <span>John Smith</span>
                                              <span class="time">3 mins ago</span>
                                            </span>
                                            <span class="message">
                                              Film festivals used to be do-or-die moments for movie makers. They were where...
                                            </span>
                                          </a>
                                        </li>
                                        <li>
                                          <div class="text-center">
                                            <a>
                                              <strong>See All Alerts</strong>
                                              <i class="fa fa-angle-right"></i>
                                            </a>
                                          </div>
                                        </li>
                                      </ul>
                                    </li>
                                  </ul>
                                </nav>
                              </div>
                            </div>
                            <!-- /top navigation -->

                            <!-- page content -->

                            <style>
                                /*form {width:100%; height:450px; margin:auto; position:relative;}*/
                                input.normalheight{height: 28px; }
                                input.small { width:24.9%;}
                                input.thingspeak{float: left; width:71%;font-weight:normal;}
                                form.big { line-height: 2;}
                                label.thingspeak{ float: left;clear: left; width: 150px; text-align: left;font-weight:normal;}
                                label.smallthingspeak{clear: left;width: 150px; font-weight:normal;}
                            </style>

                            <div class="right_col" role="main">
                              <!-- top tiles -->
                              <div class="row tile_count">
                                <h2>Current thresholds values: </h2><br>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-thermometer-full"></i> Maximum temperature</span>
                                  <div class="count"> '''+ str(json_inidata["thresholds"]["max_temp"])+'''</div>
                                </div>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-thermometer-quarter"></i> Minimum temperature</span>
                                  <div class="count">'''+ str(json_inidata["thresholds"]["min_temp"])+'''</div>
                                </div>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-circle"></i> Maximum humidity</span>
                                  <div class="count">'''+ str(json_inidata["thresholds"]["max_hum"])+'''</div>
                                </div>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-circle-o.."></i> Minimum humidity</span>
                                  <div class="count">'''+ str(json_inidata["thresholds"]["min_hum"])+'''</div>
                                </div>

                              </div>
                              <!-- /top tiles -->



                              <div class="row">

                                <div class="column">
                                  <div class="col-md-4 col-sm-4 col-xs-12">
                                    <div class="x_panel tile fixed_height_350">
                                      <div class="x_title">
                                        <h2>Change thresholds</h2>
                                        <div class="clearfix"></div>
                                      </div>
                                      <div class="x_content">
                                        <div align="center">
                                          <form style="font-size:15px" action="/replytresh" method="POST">
                                                Maximum temperature:   <input type="number" value="'''+ str(json_inidata["thresholds"]["max_temp"])+'''" name="maxt" >
                                                <br/>
                                                Minimum temperature:   <input type="text" value="'''+ str(json_inidata["thresholds"]["min_temp"])+'''" name="mint">
                                                <br/>
                                                Maximum humidity:   <input type="text" value="'''+ str(json_inidata["thresholds"]["max_hum"])+'''" name="maxh">
                                                <br/>
                                                Minimum humidity:   <input type="text" value="'''+ str(json_inidata["thresholds"]["min_hum"])+'''" name="minh">
                                                <br/>
                                                <br/>
                                                <button class="btn btn-success btn-sm" style="width:30%;" > Submit </button>
                                                <!--input type="submit"-->
                                          </form>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>

                                <div class="column">
                                  <div class="col-md-8 col-sm-4 col-xs-12">
                                    <div class="x_panel tile fixed_height_350">
                                      <div class="x_title" >
                                        <h2>Thingspeak Connection</h2>
                                        <ul class="nav navbar-right panel_toolbox">
                                          <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                          </li>
                                          <li><a class="close-link"><i class="fa fa-close"></i></a>
                                          </li>
                                        </ul>
                                        <div class="clearfix"></div>

                                      </div>
                                      <div class="x_content" style="display:none;">


                                        <div align="left">
                                          <form class="big" id="thingspeak" style="font-size:15px" action="/replything" method="POST">
                                                <label class="thingspeak">Thingspeak_HOST:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["THINGSPEAK_HOST"])+'''" name="tkHost" >
                                                <br/>
                                                <label class="thingspeak">mqtt HOST:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["mqttHost"])+'''" name="mqttHost">
                                                <br/>
                                                <label class="thingspeak">tPort:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["tPort"])+'''" name="tPort">
                                                <br/>
                                                <label class="thingspeak">Channel ID:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["channelID"])+'''" name="chanId">
                                                <br/>
                                                <label class="thingspeak">tTransport:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["thingspeak"]["tTransport"])+'''" name="tTrans">
                                                <br/>
                                                <br/>
                                                <label class="smallthingspeak">ACCESS TOKEN:</label><input class="normalheight small" type="text" value="'''+ str(json_inidata["thingspeak"]["ACCESS_TOKEN"])+'''" name="accTok">
                                                <label style="width: 120px; font-weight:normal;">READ API KEY:</label><input class="normalheight small" type="text" value="'''+ str(json_inidata["thingspeak"]["READ_API_KEY"])+'''" name="rApi">
                                                <br/>
                                                <button class="btn btn-success btn-sm" id="bthingspeak" style="width:30%;"> Submit </button>
                                                <!--input type="submit"-->
                                          </form>
                                        </div>
                                      </div>
                                    </div>
                                  </div>

                                  <div class="col-md-8 col-sm-4 col-xs-12">
                                    <div class="x_panel tile fixed_height_350">
                                      <div class="x_title" >
                                        <h2>Broker Connection</h2>
                                        <ul class="nav navbar-right panel_toolbox">
                                          <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                          </li>
                                          <li><a class="close-link"><i class="fa fa-close"></i></a>
                                          </li>
                                        </ul>
                                        <div class="clearfix"></div>

                                      </div>
                                      <div class="x_content" style="display:none;">


                                        <div align="left">
                                          <form class="big" id="broker" style="font-size:15px" action="/replybroker" method="POST">
                                                <label class="thingspeak">Broker IP:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Broker_IP"])+'''" name="brokerIP" >
                                                <br/>
                                                <label class="thingspeak">Broker Port:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Broker_port"])+'''" name="brokerPort">
                                                <br/>
                                                <label class="thingspeak">DHT Topic:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["DHT_Topic"])+'''" name="dhtTop">
                                                <br/>
                                                <label class="thingspeak">AC Topic:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["AC_Topic"])+'''" name="acTop">
                                                <br/>
                                                <label class="thingspeak">Counter Topic:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Counter_Topic"])+'''" name="counTop">
                                                <br/>
                                                <label class="thingspeak">AC Status:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["broker"]["Ac_Status"])+'''" name="acStatus">
                                                <br/>
                                                <br/>
                                                <button class="btn btn-success btn-sm" id="bbroker" style="width:30%;"> Submit </button>
                                                <!--input type="submit"-->
                                          </form>
                                        </div>
                                      </div>
                                    </div>
                                  </div>

                                  <div class="col-md-8 col-sm-4 col-xs-12">
                                    <div class="x_panel tile fixed_height_350">
                                      <div class="x_title" >
                                        <h2>Telegram Connection</h2>
                                        <ul class="nav navbar-right panel_toolbox">
                                          <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                          </li>
                                          <li><a class="close-link"><i class="fa fa-close"></i></a>
                                          </li>
                                        </ul>
                                        <div class="clearfix"></div>

                                      </div>
                                      <div class="x_content" style="display:none;">


                                        <div align="left">
                                          <form class="big" id="telegram" style="font-size:15px" action="/replytele" method="POST">
                                                <label class="thingspeak">Port:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["telegram"]["Port"])+'''" name="telPort" >
                                                <br/>
                                                <label class="thingspeak">ChatID:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["telegram"]["chatID"])+'''" name="telchatid" >
                                                <br/>
                                                <button class="btn btn-success btn-sm" id="thingspeak" style="width:30%;"> Submit </button>
                                                <!--input type="submit"-->
                                          </form>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="col-md-8 col-sm-4 col-xs-12">
                                    <div class="x_panel tile fixed_height_350">
                                      <div class="x_title" >
                                        <h2>Data to REST</h2>
                                        <ul class="nav navbar-right panel_toolbox">
                                          <li><a class="collapse-link"><i class="fa fa-chevron-down" ></i></a>
                                          </li>
                                          <li><a class="close-link"><i class="fa fa-close"></i></a>
                                          </li>
                                        </ul>
                                        <div class="clearfix"></div>

                                      </div>
                                      <div class="x_content" style="display:none;">


                                        <div align="left">
                                          <form class="big" id="datatorest" style="font-size:15px" action="/replydatatorest" method="POST">
                                                <label class="thingspeak">Host IP:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["dataToRest"]["Host_IP"])+'''" name="hostIP" >
                                                <br/>
                                                <label class="thingspeak">Port:</label><input class="thingspeak normalheight" type="text" value="'''+ str(json_inidata["dataToRest"]["port"])+'''" name="dtrport" >
                                                <br/>
                                                <button class="btn btn-success btn-sm" id="thingspeak" style="width:30%;"> Submit </button>
                                                <!--input type="submit"-->
                                          </form>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </div>

                            </div>

                            <!-- /page content -->

                            <!-- footer content -->
                            <footer>
                              <div class="pull-right">
                                Gentelella - Bootstrap Admin Template by <a href="https://colorlib.com">Colorlib</a>
                              </div>
                              <div class="clearfix"></div>
                            </footer>
                            <!-- /footer content -->
                          </div>
                        </div>

                        <!-- jQuery -->
                        <script src="/static/vendors/jquery/dist/jquery.min.js"></script>
                        <!-- Bootstrap -->
                        <script src="/static/vendors/bootstrap/dist/js/bootstrap.min.js"></script>
                        <!-- FastClick -->
                        <script src="/static/vendors/fastclick/lib/fastclick.js"></script>
                        <!-- NProgress -->
                        <script src="/static/vendors/nprogress/nprogress.js"></script>
                        <!-- Chart.js -->
                        <script src="/static/vendors/Chart.js/dist/Chart.min.js"></script>
                        <!-- gauge.js -->
                        <script src="/static/vendors/gauge.js/dist/gauge.min.js"></script>
                        <!-- bootstrap-progressbar -->
                        <script src="/static/vendors/bootstrap-progressbar/bootstrap-progressbar.min.js"></script>
                        <!-- iCheck -->
                        <script src="/static/vendors/iCheck/icheck.min.js"></script>
                        <!-- Skycons -->
                        <script src="/static/vendors/skycons/skycons.js"></script>
                        <!-- Flot -->
                        <script src="/static/vendors/Flot/jquery.flot.js"></script>
                        <script src="/static/vendors/Flot/jquery.flot.pie.js"></script>
                        <script src="/static/vendors/Flot/jquery.flot.time.js"></script>
                        <script src="/static/vendors/Flot/jquery.flot.stack.js"></script>
                        <script src="/static/vendors/Flot/jquery.flot.resize.js"></script>
                        <!-- Flot plugins -->
                        <script src="/static/vendors/flot.orderbars/js/jquery.flot.orderBars.js"></script>
                        <script src="/static/vendors/flot-spline/js/jquery.flot.spline.min.js"></script>
                        <script src="/static/vendors/flot.curvedlines/curvedLines.js"></script>
                        <!-- DateJS -->
                        <script src="/static/vendors/DateJS/build/date.js"></script>
                        <!-- JQVMap -->
                        <script src="/static/vendors/jqvmap/dist/jquery.vmap.js"></script>
                        <script src="/static/vendors/jqvmap/dist/maps/jquery.vmap.world.js"></script>
                        <script src="/static/vendors/jqvmap/examples/js/jquery.vmap.sampledata.js"></script>
                        <!-- bootstrap-daterangepicker -->
                        <script src="/static/vendors/moment/min/moment.min.js"></script>
                        <script src="/static/vendors/bootstrap-daterangepicker/daterangepicker.js"></script>

                        <!-- Custom Theme Scripts -->
                        <script src="/static/build/js/custom.min.js"></script>

                      </body>
                    </html>



                '''

    def PUT(self, *uri, **params):
        return

    def DELETE(self, *uri, **params):
        return


if __name__ == "__main__":
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher ( ),
            'tools.sessions.on': True,
            # 'server.socket_host' : '0.0.0.0',
            # 'tools.staticdir.root' : os.path.abspath(os.getcwd())
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join (os.getcwd ( ), "gentelella-master")}
    }
    # cherrypy.quickstart(MuseumsWP(), '/', conf)

    cherrypy.tree.mount (MuseumsWP ( ), '/', conf)
    cherrypy.server.socket_host = 'localhost'
    cherrypy.server.socket_port = 8083
    cherrypy.engine.start ( )
    cherrypy.engine.block ( )