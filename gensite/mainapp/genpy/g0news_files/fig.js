(function(){
var o={'uk':0,
'ck':0,
'ad':1,
'ap':0,
'mb':0};
window.orb=window.orb||{};
orb.fig=orb.fig||function(k){return (arguments.length)? o[k]:o};
window.define && define('orb/fig', o); })();

orb._clientsideRedirect=function(d,l){var h=false,j;l=l||window;j=(l.document.cookie.match(/ckps_d=(.)/)?RegExp.$1:"");if(orb._redirectionIsEnabled(l)&&orb._dependenciesSatisfied(d,l)){var m=l.location.hostname,a=l.location.href,i={isUk:/(^|\.)bbc\.co\.uk$/i.test(m),isInt:/(^|\.)bbc\.com$/i.test(m),isMb:/^m\./i.test(m),isDesk:/^(www|pal)\./i.test(m)},c={isUk:d("uk"),isMb:d("mb")},k,b;if(l.bbcredirection.geo===true){if(i.isInt===true&&c.isUk===1){b=a.replace(/^(.+?bbc)\.com/i,"$1.co.uk")}else{if(i.isUk===true&&c.isUk===0){b=a.replace(/^(.+?bbc)\.co\.uk/i,"$1.com")}}}k=b||a;if(l.bbcredirection.device===true){if(i.isDesk===true&&(j==="m"||(!j&&c.isMb===1))){k=k.replace(/^(https?:\/\/)(www|pal)\./i,"$1m.")}else{if(i.isMb===true&&(j==="d"||(!j&&c.isMb===0))){k=k.replace(/^(https?:\/\/)m\./i,"$1www.")}}}if(k&&a.toLowerCase()!==k.toLowerCase()){h=true;try{l.location.replace(k)}catch(g){h=false;l.require(["istats-1"],function(e){e.log("redirection_fail","",{})})}}}return h};orb._redirectionIsEnabled=function(a){return(a.bbcredirection&&(a.bbcredirection.geo===true||a.bbcredirection.device===true))};orb._dependenciesSatisfied=function(b,a){return(typeof b==="function"&&typeof a.location.replace!=="undefined")};
    orb._clientsideRedirect(window.mockFig || window.orb.fig, window.mockWindow || window);
