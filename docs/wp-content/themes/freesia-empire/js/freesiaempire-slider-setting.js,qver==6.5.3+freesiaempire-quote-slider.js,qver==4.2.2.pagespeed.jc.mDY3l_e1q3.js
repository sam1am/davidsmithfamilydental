var mod_pagespeed_MsFfgawBbn = "jQuery(window).load(function(){var e=freesiaempire_slider_value.transition_effect,t=freesiaempire_slider_value.transition_delay,i=freesiaempire_slider_value.transition_duration;jQuery(\".layer-slider\").cycle({timeout:t,fx:e,activePagerClass:\"active\",pager:\".slider-button\",pause:1,pauseOnPagerHover:1,width:\"100%\",containerResize:0,fit:1,next:\"#next2\",prev:\"#prev2\",speed:i,after:function(){jQuery(this).parent().css(\"height\",jQuery(this).height())},cleartypeNoBg:!0})});";
var mod_pagespeed_a_pYqTxEVj = "jQuery(document).ready(function(){!function(){function e(e){var t=\"\",s=\"\";for(i=0;i<e;i++)t+=\"<li title='next'>\"+(i+1)+\"</li>\";s=\"<ul class='next-prev'>\"+t+\"</ul>\",jQuery(\".quote-wrapper\").after(s)}var t,s={init:function(i){var s=1e4,a=2500,n=jQuery(\".quotes\").length,o=i;-1===i&&(e(n),o=0),jQuery(\".quotes\").animate({opacity:0},0).removeClass(\"showing\"),jQuery(\".quotes\").eq(o).animate({opacity:1},1e3).addClass(\"showing\"),jQuery(\".next-prev li\").eq(o).addClass(\"active\"),t=setInterval(function(){jQuery(\".testimonials\").hasClass(\"stop\")||(jQuery(\".quotes\").eq(o).animate({opacity:0},a).removeClass(\"showing\"),o==n-1?o=0:o++,jQuery(\".quotes\").eq(o).animate({opacity:1},a).addClass(\"showing\"),jQuery(\".next-prev li\").removeClass(\"active\"),jQuery(\".next-prev li\").eq(o).addClass(\"active\"))},s)}};s.init(-1),jQuery(\".testimonials\").on(\"click\",\".next-prev li\",function(){clearInterval(t),jQuery(\".next-prev li\").removeClass(\"active\"),s.init(jQuery(this).index())}),jQuery(\".quotes\").on(\"mouseenter touchstart\",function(){jQuery(\".testimonials\").addClass(\"stop\")}),jQuery(\".quotes\").on(\"mouseleave touchend\",function(){jQuery(\".testimonials\").removeClass(\"stop\")})}()});";