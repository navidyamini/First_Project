import cherrypy
import os
import requests
import json


class MuseumsWP(object):
    exposed = True

    def GET(self, *uri, **params):
        with open('initial_data.json', 'r') as json_data_file:
            obj = json.load(json_data_file)
        if (uri[0] == "index"):

            return '''<!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                            <!-- Meta, title, CSS, favicons, etc. -->
                            <meta charset="utf-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1">

                            <title>Admon Museums | </title>

                            <!-- Bootstrap -->
                            <link href="../vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
                            <!-- Font Awesome -->
                            <link href="../vendors/font-awesome-4.7.0/css/font-awesome.min.css" rel="stylesheet">
                            <!-- NProgress -->
                            <link href="../vendors/nprogress/nprogress.css" rel="stylesheet">
                            <!-- iCheck -->
                            <link href="../vendors/iCheck/skins/flat/green.css" rel="stylesheet">

                            <!-- bootstrap-progressbar -->
                            <link href="../vendors/bootstrap-progressbar/css/bootstrap-progressbar-3.3.4.min.css" rel="stylesheet">
                            <!-- JQVMap -->
                            <link href="../vendors/jqvmap/dist/jqvmap.min.css" rel="stylesheet"/>
                            <!-- bootstrap-daterangepicker -->
                            <link href="../vendors/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

                            <!-- Custom Theme Style -->
                            <link href="../build/css/custom.min.css" rel="stylesheet">
                          </head>

                          <body class="nav-md">
                            <div class="container body">
                              <div class="main_container">
                                <div class="col-md-3 left_col">
                                  <div class="left_col scroll-view">
                                    <div class="navbar nav_title" style="border: 0;">
                                      <a href="index.html" class="site_title"><i class="fa fa-paw"></i> <span>Admon Museum!</span></a>
                                    </div>

                                    <div class="clearfix"></div>

                                    <!-- menu profile quick info -->
                                    <div class="profile clearfix">
                                      <div class="profile_pic">
                                        <img src="images/Carla.jpeg" alt="..." class="img-circle profile_img">
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
                                          <li><a><i class="fa fa-home"></i> Rooms <span class="fa fa-chevron-down"></span></a>
                                            <ul class="nav child_menu">
                                              <li><a href="indexXimevs1.html">Room 1</a></li>
                                              <li><a href="index2.html">Room 2</a></li>
                                              <li><a href="index3.html">Room 3</a></li>
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
                                      <a data-toggle="tooltip" data-placement="top" title="Logout" href="login.html">
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
                                            <img src="images/Carla.jpeg" alt="">Carla Corona
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
                                            <li><a href="login.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
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
                                                <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                                                <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                                                <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                                                <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                                <div class="right_col" role="main">
                                  <!-- top tiles -->
                                  <div class="row tile_count">
                                    <h2>Current thresholds values: </h2><br>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-thermometer-full"></i> Maximum temperature</span>
                                      <div id="label_max_temp"> ''' + str(obj["thresholds"]["max_temp"])+'''</div>
                                    </div>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-thermometer-quarter"></i> Minimum temperature</span>
                                      <div class="count">'''+ str(obj["thresholds"]["min_temp"])+'''</div>
                                    </div>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-circle"></i> Maximum humidity</span>
                                      <div class="count">'''+ str(obj["thresholds"]["max_hum"])+'''</div>
                                    </div>
                                    <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                      <span class="count_top"><i class="fa fa-circle-o.."></i> Minimum humidity</span>
                                      <div class="count">'''+ str(obj["thresholds"]["min_hum"])+'''</div>
                                    </div>

                                  </div>
                                  <!-- /top tiles -->



                                  <div class="row">


                                    <div class="col-md-4 col-sm-4 col-xs-12">
                                      <div class="x_panel tile fixed_height_350">
                                        <div class="x_title">
                                          <h2>Change thresholds</h2>
                                          <div class="clearfix"></div>
                                        </div>
                                        <div class="x_content">
                                          <div align="center">
                                            <form style="font-size:15px" action="/reply" method="POST">
                                                  Maximum temperature:   <input type="text" name="maxt" >
                                                  <br/>
                                                  Minimum temperature:   <input type="text" name="mint">
                                                  <br/>
                                                  Maximum humidity:   <input type="text" name="maxh">
                                                  <br/>
                                                  Minimum humidity:   <input type="text" name="minh">
                                                  <br/>
                                                  <br/>
                                                  <button> Submit </button>
                                                  <!--input type="submit"-->
                                            </form>
                                          </div>
                                        </div>
                                      </div>
                                    </div>

                                    <div class="col-md-8 col-sm-4 col-xs-12">
                                      <div class="x_panel tile fixed_height_320">
                                        <div class="x_title">
                                          <h2>App Versions</h2>
                                          <ul class="nav navbar-right panel_toolbox">
                                            <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                                            </li>
                                            <li class="dropdown">
                                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><i class="fa fa-wrench"></i></a>
                                              <ul class="dropdown-menu" role="menu">
                                                <li><a href="#">Settings 1</a>
                                                </li>
                                                <li><a href="#">Settings 2</a>
                                                </li>
                                              </ul>
                                            </li>
                                            <li><a class="close-link"><i class="fa fa-close"></i></a>
                                            </li>
                                          </ul>
                                          <div class="clearfix"></div>
                                        </div>
                                        <div class="x_content">
                                          <h4>App Usage across versions</h4>
                                          <div class="widget_summary">
                                            <div class="w_left w_25">
                                              <span>0.1.5.2</span>
                                            </div>
                                            <div class="w_center w_55">
                                              <div class="progress">
                                                <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 66%;">
                                                  <span class="sr-only">60% Complete</span>
                                                </div>
                                              </div>
                                            </div>
                                            <div class="w_right w_20">
                                              <span>123k</span>
                                            </div>
                                            <div class="clearfix"></div>
                                          </div>

                                          <div class="widget_summary">
                                            <div class="w_left w_25">
                                              <span>0.1.5.3</span>
                                            </div>
                                            <div class="w_center w_55">
                                              <div class="progress">
                                                <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 45%;">
                                                  <span class="sr-only">60% Complete</span>
                                                </div>
                                              </div>
                                            </div>
                                            <div class="w_right w_20">
                                              <span>53k</span>
                                            </div>
                                            <div class="clearfix"></div>
                                          </div>
                                          <div class="widget_summary">
                                            <div class="w_left w_25">
                                              <span>0.1.5.4</span>
                                            </div>
                                            <div class="w_center w_55">
                                              <div class="progress">
                                                <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 25%;">
                                                  <span class="sr-only">60% Complete</span>
                                                </div>
                                              </div>
                                            </div>
                                            <div class="w_right w_20">
                                              <span>23k</span>
                                            </div>
                                            <div class="clearfix"></div>
                                          </div>
                                          <div class="widget_summary">
                                            <div class="w_left w_25">
                                              <span>0.1.5.5</span>
                                            </div>
                                            <div class="w_center w_55">
                                              <div class="progress">
                                                <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 5%;">
                                                  <span class="sr-only">60% Complete</span>
                                                </div>
                                              </div>
                                            </div>
                                            <div class="w_right w_20">
                                              <span>3k</span>
                                            </div>
                                            <div class="clearfix"></div>
                                          </div>
                                          <div class="widget_summary">
                                            <div class="w_left w_25">
                                              <span>0.1.5.6</span>
                                            </div>
                                            <div class="w_center w_55">
                                              <div class="progress">
                                                <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 2%;">
                                                  <span class="sr-only">60% Complete</span>
                                                </div>
                                              </div>
                                            </div>
                                            <div class="w_right w_20">
                                              <span>1k</span>
                                            </div>
                                            <div class="clearfix"></div>
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
                            <script src="../vendors/jquery/dist/jquery.min.js"></script>
                            <!-- Bootstrap -->
                            <script src="../vendors/bootstrap/dist/js/bootstrap.min.js"></script>
                            <!-- FastClick -->
                            <script src="../vendors/fastclick/lib/fastclick.js"></script>
                            <!-- NProgress -->
                            <script src="../vendors/nprogress/nprogress.js"></script>
                            <!-- Chart.js -->
                            <script src="../vendors/Chart.js/dist/Chart.min.js"></script>
                            <!-- gauge.js -->
                            <script src="../vendors/gauge.js/dist/gauge.min.js"></script>
                            <!-- bootstrap-progressbar -->
                            <script src="../vendors/bootstrap-progressbar/bootstrap-progressbar.min.js"></script>
                            <!-- iCheck -->
                            <script src="../vendors/iCheck/icheck.min.js"></script>
                            <!-- Skycons -->
                            <script src="../vendors/skycons/skycons.js"></script>
                            <!-- Flot -->
                            <script src="../vendors/Flot/jquery.flot.js"></script>
                            <script src="../vendors/Flot/jquery.flot.pie.js"></script>
                            <script src="../vendors/Flot/jquery.flot.time.js"></script>
                            <script src="../vendors/Flot/jquery.flot.stack.js"></script>
                            <script src="../vendors/Flot/jquery.flot.resize.js"></script>
                            <!-- Flot plugins -->
                            <script src="../vendors/flot.orderbars/js/jquery.flot.orderBars.js"></script>
                            <script src="../vendors/flot-spline/js/jquery.flot.spline.min.js"></script>
                            <script src="../vendors/flot.curvedlines/curvedLines.js"></script>
                            <!-- DateJS -->
                            <script src="../vendors/DateJS/build/date.js"></script>
                            <!-- JQVMap -->
                            <script src="../vendors/jqvmap/dist/jquery.vmap.js"></script>
                            <script src="../vendors/jqvmap/dist/maps/jquery.vmap.world.js"></script>
                            <script src="../vendors/jqvmap/examples/js/jquery.vmap.sampledata.js"></script>
                            <!-- bootstrap-daterangepicker -->
                            <script src="../vendors/moment/min/moment.min.js"></script>
                            <script src="../vendors/bootstrap-daterangepicker/daterangepicker.js"></script>

                            <!-- Custom Theme Scripts -->
                            <script src="../build/js/custom.min.js"></script>

                          </body>
                        </html>


                    '''

        elif (uri[0] == "maxTemp"):
            return (str(obj["thresholds"]["max_temp"]))
        elif (uri[0] == "minTemp"):
            return (str(obj["thresholds"]["min_temp"]))
        elif (uri[0] == "maxHum"):
            return (str(obj["thresholds"]["max_hum"]))
        elif (uri[0] == "minHum"):
            return (str(obj["thresholds"]["min_hum"]))
        else:
            return cherrypy.request.body.read()

    def POST(self, *uri, **params):
        # obj = cherrypy.request.body.read()

        with open('initial_data.json', 'r') as json_data_file:
            obj = json.load(json_data_file)

        dict_data = obj['thresholds']
        obj['thresholds'] = {"max_temp": float(params['maxt']),
                             "min_temp": float(params['mint']),
                             "max_hum": float(params['maxh']),
                             "min_hum": float(params['minh'])}


        with open('initial_data.json', 'w') as json_data_file:
            json.dump(obj, json_data_file)
        return '''<!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                        <!-- Meta, title, CSS, favicons, etc. -->
                         <meta charset="utf-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1">

                        <title>Admon Museums | </title>

                        <!-- Bootstrap -->
                        <link href="../vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
                        <!-- Font Awesome -->
                        <link href="../vendors/font-awesome-4.7.0/css/font-awesome.min.css" rel="stylesheet">
                        <!-- NProgress -->
                        <link href="../vendors/nprogress/nprogress.css" rel="stylesheet">
                        <!-- iCheck -->
                        <link href="../vendors/iCheck/skins/flat/green.css" rel="stylesheet">

                        <!-- bootstrap-progressbar -->
                        <link href="../vendors/bootstrap-progressbar/css/bootstrap-progressbar-3.3.4.min.css" rel="stylesheet">
                        <!-- JQVMap -->
                        <link href="../vendors/jqvmap/dist/jqvmap.min.css" rel="stylesheet"/>
                        <!-- bootstrap-daterangepicker -->
                        <link href="../vendors/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

                        <!-- Custom Theme Style -->
                        <link href="../build/css/custom.min.css" rel="stylesheet">
                      </head>

                      <body class="nav-md">
                        <div class="container body">
                          <div class="main_container">
                            <div class="col-md-3 left_col">
                              <div class="left_col scroll-view">
                                <div class="navbar nav_title" style="border: 0;">
                                  <a href="index.html" class="site_title"><i class="fa fa-paw"></i> <span>Admon Museum!</span></a>
                                </div>

                                <div class="clearfix"></div>

                                <!-- menu profile quick info -->
                                <div class="profile clearfix">
                                  <div class="profile_pic">
                                    <img src="images/Carla.jpeg" alt="..." class="img-circle profile_img">
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
                                      <li><a><i class="fa fa-home"></i> Rooms <span class="fa fa-chevron-down"></span></a>
                                        <ul class="nav child_menu">
                                          <li><a href="indexXimevs1.html">Room 1</a></li>
                                          <li><a href="index2.html">Room 2</a></li>
                                          <li><a href="index3.html">Room 3</a></li>
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
                                  <a data-toggle="tooltip" data-placement="top" title="Logout" href="login.html">
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
                                        <img src="images/Carla.jpeg" alt="">Carla Corona
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
                                        <li><a href="login.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
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
                                            <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                                            <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                                            <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                                            <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
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
                            <div class="right_col" role="main">
                              <!-- top tiles -->
                              <div class="row tile_count">
                                <h2>Current thresholds values: </h2><br>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-thermometer-full"></i> Maximum temperature</span>
                                  <div id="label_max_temp"> ''' + str(obj["thresholds"]["max_temp"])+'''</div>
                                </div>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-thermometer-quarter"></i> Minimum temperature</span>
                                  <div class="count">'''+ str(obj["thresholds"]["min_temp"])+'''</div>
                                </div>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-circle"></i> Maximum humidity</span>
                                  <div class="count">'''+ str(obj["thresholds"]["max_hum"])+'''</div>
                                </div>
                                <div class="col-md-2 col-sm-4 col-xs-6 tile_stats_count">
                                  <span class="count_top"><i class="fa fa-circle-o.."></i> Minimum humidity</span>
                                  <div class="count">'''+ str(obj["thresholds"]["min_hum"])+'''</div>
                                </div>

                              </div>
                              <!-- /top tiles -->



                              <div class="row">


                                <div class="col-md-4 col-sm-4 col-xs-12">
                                  <div class="x_panel tile fixed_height_350">
                                    <div class="x_title">
                                      <h2>Change thresholds</h2>
                                      <div class="clearfix"></div>
                                    </div>
                                    <div class="x_content">
                                      <div align="center">
                                        <form style="font-size:15px" action="/reply" method="POST">
                                              Maximum temperature:   <input type="text" name="maxt" >
                                              <br/>
                                              Minimum temperature:   <input type="text" name="mint">
                                              <br/>
                                              Maximum humidity:   <input type="text" name="maxh">
                                              <br/>
                                              Minimum humidity:   <input type="text" name="minh">
                                              <br/>
                                              <br/>
                                              <button> Submit </button>
                                              <!--input type="submit"-->
                                        </form>
                                      </div>
                                    </div>
                                  </div>
                                </div>

                                <div class="col-md-8 col-sm-4 col-xs-12">
                                  <div class="x_panel tile fixed_height_320">
                                    <div class="x_title">
                                      <h2>App Versions</h2>
                                      <ul class="nav navbar-right panel_toolbox">
                                        <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                                        </li>
                                        <li class="dropdown">
                                          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><i class="fa fa-wrench"></i></a>
                                          <ul class="dropdown-menu" role="menu">
                                            <li><a href="#">Settings 1</a>
                                            </li>
                                            <li><a href="#">Settings 2</a>
                                            </li>
                                          </ul>
                                        </li>
                                        <li><a class="close-link"><i class="fa fa-close"></i></a>
                                        </li>
                                      </ul>
                                      <div class="clearfix"></div>
                                    </div>
                                    <div class="x_content">
                                      <h4>App Usage across versions</h4>
                                      <div class="widget_summary">
                                        <div class="w_left w_25">
                                          <span>0.1.5.2</span>
                                        </div>
                                        <div class="w_center w_55">
                                          <div class="progress">
                                            <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 66%;">
                                              <span class="sr-only">60% Complete</span>
                                            </div>
                                          </div>
                                        </div>
                                        <div class="w_right w_20">
                                          <span>123k</span>
                                        </div>
                                        <div class="clearfix"></div>
                                      </div>

                                      <div class="widget_summary">
                                        <div class="w_left w_25">
                                          <span>0.1.5.3</span>
                                        </div>
                                        <div class="w_center w_55">
                                          <div class="progress">
                                            <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 45%;">
                                              <span class="sr-only">60% Complete</span>
                                            </div>
                                          </div>
                                        </div>
                                        <div class="w_right w_20">
                                          <span>53k</span>
                                        </div>
                                        <div class="clearfix"></div>
                                      </div>
                                      <div class="widget_summary">
                                        <div class="w_left w_25">
                                          <span>0.1.5.4</span>
                                        </div>
                                        <div class="w_center w_55">
                                          <div class="progress">
                                            <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 25%;">
                                              <span class="sr-only">60% Complete</span>
                                            </div>
                                          </div>
                                        </div>
                                        <div class="w_right w_20">
                                          <span>23k</span>
                                        </div>
                                        <div class="clearfix"></div>
                                      </div>
                                      <div class="widget_summary">
                                        <div class="w_left w_25">
                                          <span>0.1.5.5</span>
                                        </div>
                                        <div class="w_center w_55">
                                          <div class="progress">
                                            <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 5%;">
                                              <span class="sr-only">60% Complete</span>
                                            </div>
                                          </div>
                                        </div>
                                        <div class="w_right w_20">
                                          <span>3k</span>
                                        </div>
                                        <div class="clearfix"></div>
                                      </div>
                                      <div class="widget_summary">
                                        <div class="w_left w_25">
                                          <span>0.1.5.6</span>
                                        </div>
                                        <div class="w_center w_55">
                                          <div class="progress">
                                            <div class="progress-bar bg-green" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 2%;">
                                              <span class="sr-only">60% Complete</span>
                                            </div>
                                          </div>
                                        </div>
                                        <div class="w_right w_20">
                                          <span>1k</span>
                                        </div>
                                        <div class="clearfix"></div>
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
                        <script src="../vendors/jquery/dist/jquery.min.js"></script>
                        <!-- Bootstrap -->
                        <script src="../vendors/bootstrap/dist/js/bootstrap.min.js"></script>
                        <!-- FastClick -->
                        <script src="../vendors/fastclick/lib/fastclick.js"></script>
                        <!-- NProgress -->
                        <script src="../vendors/nprogress/nprogress.js"></script>
                        <!-- Chart.js -->
                        <script src="../vendors/Chart.js/dist/Chart.min.js"></script>
                        <!-- gauge.js -->
                        <script src="../vendors/gauge.js/dist/gauge.min.js"></script>
                        <!-- bootstrap-progressbar -->
                        <script src="../vendors/bootstrap-progressbar/bootstrap-progressbar.min.js"></script>
                        <!-- iCheck -->
                        <script src="../vendors/iCheck/icheck.min.js"></script>
                        <!-- Skycons -->
                        <script src="../vendors/skycons/skycons.js"></script>
                        <!-- Flot -->
                        <script src="../vendors/Flot/jquery.flot.js"></script>
                        <script src="../vendors/Flot/jquery.flot.pie.js"></script>
                        <script src="../vendors/Flot/jquery.flot.time.js"></script>
                        <script src="../vendors/Flot/jquery.flot.stack.js"></script>
                        <script src="../vendors/Flot/jquery.flot.resize.js"></script>
                        <!-- Flot plugins -->
                        <script src="../vendors/flot.orderbars/js/jquery.flot.orderBars.js"></script>
                        <script src="../vendors/flot-spline/js/jquery.flot.spline.min.js"></script>
                        <script src="../vendors/flot.curvedlines/curvedLines.js"></script>
                        <!-- DateJS -->
                        <script src="../vendors/DateJS/build/date.js"></script>
                        <!-- JQVMap -->
                        <script src="../vendors/jqvmap/dist/jquery.vmap.js"></script>
                        <script src="../vendors/jqvmap/dist/maps/jquery.vmap.world.js"></script>
                        <script src="../vendors/jqvmap/examples/js/jquery.vmap.sampledata.js"></script>
                        <!-- bootstrap-daterangepicker -->
                        <script src="../vendors/moment/min/moment.min.js"></script>
                        <script src="../vendors/bootstrap-daterangepicker/daterangepicker.js"></script>

                        <!-- Custom Theme Scripts -->
                        <script src="../build/js/custom.min.js"></script>

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
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        }
    }
    cherrypy.tree.mount(MuseumsWP(), '/', conf)
    #cherrypy.server.socket_host = '192.168.1.71'
    #cherrypy.server.socket_port = 8081
    cherrypy.engine.start()
    cherrypy.engine.block()