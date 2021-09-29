(function(e){function t(t){for(var n,u,o=t[0],s=t[1],i=t[2],p=0,b=[];p<o.length;p++)u=o[p],Object.prototype.hasOwnProperty.call(a,u)&&a[u]&&b.push(a[u][0]),a[u]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(e[n]=s[n]);l&&l(t);while(b.length)b.shift()();return c.push.apply(c,i||[]),r()}function r(){for(var e,t=0;t<c.length;t++){for(var r=c[t],n=!0,o=1;o<r.length;o++){var s=r[o];0!==a[s]&&(n=!1)}n&&(c.splice(t--,1),e=u(u.s=r[0]))}return e}var n={},a={app:0},c=[];function u(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,u),r.l=!0,r.exports}u.m=e,u.c=n,u.d=function(e,t,r){u.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},u.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,t){if(1&t&&(e=u(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(u.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)u.d(r,n,function(t){return e[t]}.bind(null,n));return r},u.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return u.d(t,"a",t),t},u.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},u.p="/static/numapi/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],s=o.push.bind(o);o.push=t,o=o.slice();for(var i=0;i<o.length;i++)t(o[i]);var l=s;c.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"5135c":function(e,t,r){},"56d7":function(e,t,r){"use strict";r.r(t);r("e260"),r("e6cf"),r("cca6"),r("a79d");var n=r("7a23"),a={id:"app",class:"bg-dark"};function c(e,t,r,c,u,o){var s=Object(n["f"])("NumberForm");return Object(n["e"])(),Object(n["b"])("div",a,[Object(n["d"])(s)])}var u={class:"container"},o={class:"col-md-6 offset-md-3"},s=Object(n["c"])("div",{class:"row"},[Object(n["c"])("h3",{class:"text-white h3 mb-3"},"Number Form")],-1),i={class:"row text-start"},l={class:"text-white"},p={class:"form-group"},b=Object(n["c"])("label",{for:"numberInput",class:"text-white"},"Input number: ",-1),d={class:"form-group spacer"},f={class:"spacer"},m={class:"spacer"},v=["disabled"],h={class:"spinner-border spinner-border-sm text-danger"},j={class:"row"};function O(e,t,r,a,c,O){return Object(n["e"])(),Object(n["b"])("div",u,[Object(n["c"])("div",o,[s,Object(n["c"])("div",i,[Object(n["c"])("form",l,[Object(n["c"])("div",p,[b,Object(n["j"])(Object(n["c"])("input",{type:"text",class:"form-control",id:"numberInput",placeholder:"Enter number to translate to English","onUpdate:modelValue":t[0]||(t[0]=function(e){return c.number=e})},null,512),[[n["h"],c.number]])]),Object(n["c"])("div",d,[Object(n["c"])("span",f,[Object(n["c"])("button",{id:"btn-get",class:"btn btn-outline-primary",onClick:t[1]||(t[1]=function(){return O.get&&O.get.apply(O,arguments)})},"GET")]),Object(n["c"])("span",m,[Object(n["c"])("button",{id:"btn-post",class:"btn btn-outline-danger","data-bs-toggle":"modal",onClick:t[2]||(t[2]=function(){return O.post&&O.post.apply(O,arguments)}),disabled:c.loading},[Object(n["j"])(Object(n["c"])("span",null,"POST",512),[[n["i"],!c.loading]]),Object(n["j"])(Object(n["c"])("span",h,null,512),[[n["i"],c.loading]])],8,v)])])]),Object(n["c"])("div",j,[Object(n["j"])(Object(n["c"])("div",{id:"error-text",class:"text-danger"},Object(n["g"])(c.translationError),513),[[n["i"],null!=c.translationError&&c.translationError.length>0]]),Object(n["j"])(Object(n["c"])("div",{id:"translation-text",class:"text-white"}," Translated number: "+Object(n["g"])(c.translatedNumber),513),[[n["i"],null!=c.translatedNumber&&c.translatedNumber.length>0]])])])])])}var g=r("1da1"),w=(r("96cf"),"ok"),y="Unknown error.",x={name:"NumberForm",inject:["numberTranslationService"],methods:{get:function(e){var t=this;return Object(g["a"])(regeneratorRuntime.mark((function r(){return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return r.prev=0,e.preventDefault(),t.clearOutput(),r.t0=t,r.next=6,t.numberTranslationService.get(t.number);case 6:r.t1=r.sent,r.t0.updateDisplay.call(r.t0,r.t1),r.next=14;break;case 10:r.prev=10,r.t2=r["catch"](0),console.error(r.t2),t.updateDisplay({status:y});case 14:case"end":return r.stop()}}),r,null,[[0,10]])})))()},post:function(e){var t=this;return Object(g["a"])(regeneratorRuntime.mark((function r(){var n;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return r.prev=0,t.loading=!0,e.preventDefault(),t.clearOutput(),r.next=6,t.numberTranslationService.post(t.number);case 6:n=r.sent,t.updateDisplay(n),t.loading=!1,r.next=15;break;case 11:r.prev=11,r.t0=r["catch"](0),console.error(r.t0),t.updateDisplay({status:y});case 15:return r.prev=15,t.loading=!1,r.finish(15);case 18:case"end":return r.stop()}}),r,null,[[0,11,15,18]])})))()},updateDisplay:function(e){var t=e.status,r=e.numToEnglish;this.translationError=t===w?"":t,this.translatedNumber=r},clearOutput:function(){this.translatedNumber="",this.translationError=""}},data:function(){return{number:"",translatedNumber:"",translationError:"",loading:!1}}},k=(r("9bb8"),r("6b0d")),E=r.n(k),T=E()(x,[["render",O]]),N={name:"App",components:{NumberForm:T}},S=(r("b0b7"),E()(N,[["render",c]])),_=r("d4ec"),P=r("bee2"),R=(r("d3b7"),r("bc3a")),D=r.n(R),F=r("4870"),M="/num_to_english?number=",I="/num_to_english",C=Object(F["a"])(D.a.create()),J=function(){return{status:"Error communicating with translation service",numToEnglish:null}},U=function(){function e(){Object(_["a"])(this,e)}return Object(P["a"])(e,[{key:"get",value:function(){var e=Object(g["a"])(regeneratorRuntime.mark((function e(t){var r,n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,C.get("".concat(M).concat(t));case 3:return r=e.sent,n=r.data,e.abrupt("return",n);case 8:return e.prev=8,e.t0=e["catch"](0),e.abrupt("return",J());case 11:case"end":return e.stop()}}),e,null,[[0,8]])})));function t(t){return e.apply(this,arguments)}return t}()},{key:"post",value:function(){var e=Object(g["a"])(regeneratorRuntime.mark((function e(t){var r,n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,new Promise((function(e){return setTimeout(e,5e3)}));case 3:return e.next=5,C.post(I,{number:t});case 5:return r=e.sent,n=r.data,e.abrupt("return",n);case 10:return e.prev=10,e.t0=e["catch"](0),e.abrupt("return",J());case 13:case"end":return e.stop()}}),e,null,[[0,10]])})));function t(t){return e.apply(this,arguments)}return t}()}]),e}();r("f9e3"),r("a347");Object(n["a"])(S).provide("numberTranslationService",new U).mount("#app")},8376:function(e,t,r){},"9bb8":function(e,t,r){"use strict";r("5135c")},a347:function(e,t,r){},b0b7:function(e,t,r){"use strict";r("8376")}});
//# sourceMappingURL=app.2a167303.js.map