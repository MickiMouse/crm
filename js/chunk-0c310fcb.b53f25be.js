(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-0c310fcb"],{"0bfb":function(t,e,a){"use strict";var s=a("cb7c");t.exports=function(){var t=s(this),e="";return t.global&&(e+="g"),t.ignoreCase&&(e+="i"),t.multiline&&(e+="m"),t.unicode&&(e+="u"),t.sticky&&(e+="y"),e}},"214f":function(t,e,a){"use strict";a("b0c5");var s=a("2aba"),n=a("32e9"),r=a("79e5"),i=a("be13"),c=a("2b4c"),l=a("520a"),o=c("species"),d=!r((function(){var t=/./;return t.exec=function(){var t=[];return t.groups={a:"7"},t},"7"!=="".replace(t,"$<a>")})),u=function(){var t=/(?:)/,e=t.exec;t.exec=function(){return e.apply(this,arguments)};var a="ab".split(t);return 2===a.length&&"a"===a[0]&&"b"===a[1]}();t.exports=function(t,e,a){var _=c(t),f=!r((function(){var e={};return e[_]=function(){return 7},7!=""[t](e)})),h=f?!r((function(){var e=!1,a=/a/;return a.exec=function(){return e=!0,null},"split"===t&&(a.constructor={},a.constructor[o]=function(){return a}),a[_](""),!e})):void 0;if(!f||!h||"replace"===t&&!d||"split"===t&&!u){var v=/./[_],p=a(i,_,""[t],(function(t,e,a,s,n){return e.exec===l?f&&!n?{done:!0,value:v.call(e,a,s)}:{done:!0,value:t.call(a,e,s)}:{done:!1}})),g=p[0],C=p[1];s(String.prototype,t,g),n(RegExp.prototype,_,2==e?function(t,e){return C.call(t,this,e)}:function(t){return C.call(t,this)})}}},"2d89":function(t,e,a){},"2fdb":function(t,e,a){"use strict";var s=a("5ca1"),n=a("d2c8"),r="includes";s(s.P+s.F*a("5147")(r),"String",{includes:function(t){return!!~n(this,t,r).indexOf(t,arguments.length>1?arguments[1]:void 0)}})},"386d":function(t,e,a){"use strict";var s=a("cb7c"),n=a("83a1"),r=a("5f1b");a("214f")("search",1,(function(t,e,a,i){return[function(a){var s=t(this),n=void 0==a?void 0:a[e];return void 0!==n?n.call(a,s):new RegExp(a)[e](String(s))},function(t){var e=i(a,t,this);if(e.done)return e.value;var c=s(t),l=String(this),o=c.lastIndex;n(o,0)||(c.lastIndex=0);var d=r(c,l);return n(c.lastIndex,o)||(c.lastIndex=o),null===d?-1:d.index}]}))},"4aea":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"card container-fluid"},[a("div",{staticClass:"row card__header header-wrapper"},[a("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Клиенты агента")]),a("button",{staticClass:"main-btn ml-auto",on:{click:function(t){}}},[t._v("Добавить агента")]),a("button",{staticClass:"more-btn ml-2",on:{click:function(e){t.isTableExpanded=!t.isTableExpanded}}},[t._v("Все")])])]),a("div",{staticClass:"row"},[t._m(0),t._l(t.$store.getters.getAgentDetails.agent.clients,(function(e){return a("div",{staticClass:"col-12 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header table-accent"},[t._v(t._s(e.short_name))])])}))],2)])},n=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-12 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Наиминование")])])}],r={name:"AgentsClients"},i=r,c=a("2877"),l=Object(c["a"])(i,s,n,!1,null,"48188c8e",null);e["a"]=l.exports},"4ce1":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"div"},[a("div",{staticClass:"card container-fluid"},[a("div",{staticClass:"row card__header header-wrapper"},[a("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[a("h6",{staticClass:"header pr-1"},[t._v(t._s(t.$store.getters.getAgentDetails.agent.user.full_name))]),a("div",{staticClass:"header-border"}),a("span",{staticClass:"card__header__email ml-1"},[t._v("\n               "+t._s(t.$store.getters.getAgentDetails.agent.user.email)+"\n            ")])])]),a("div",{staticClass:"row"},[t._m(0),a("div",{staticClass:"col-8 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getAgentDetails.agent.user.full_name))])])]),a("div",{staticClass:"row"},[t._m(1),a("div",{staticClass:"col-8 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getAgentDetails.agent.user.email))])])]),a("div",{staticClass:"row"},[t._m(2),a("div",{staticClass:"col-8 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getAgentDetails.agent.phone))])])]),a("div",{staticClass:"row"},[t._m(3),a("div",{staticClass:"col-8 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getAgentDetails.agent.clients.length))])])])]),a("div",{staticClass:"card card-dark container-fluid my-3"},[t._m(4),a("div",{staticClass:"row"},[t._m(5),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.plan_taxes))])]),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.plan_accounting_services))])])]),a("div",{staticClass:"row"},[t._m(6),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.fact_taxes))])]),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.fact_accounting_services))])])]),a("div",{staticClass:"row"},[t._m(7),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.deflection_taxes))])]),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.deflection_accounting_services))])])]),a("div",{staticClass:"row"},[t._m(8),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.notified))])]),t._m(9)]),a("div",{staticClass:"row"},[t._m(10),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v(t._s(t.$store.getters.getAgentDetails.not_notified))])]),t._m(11)])])])},n=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("ФИО:")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("E-mail:")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Номер телефона:")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Клиентов:")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"row"},[a("div",{staticClass:"col-4 card__header"}),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Учтено налогов")])]),a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Оплата БУ")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("План")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Факт")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Отколнение")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Уведомлено")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v("test@mail.ru")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"header"},[t._v("Не уведомлено")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"col-4 py-3 card__header justify-content-start"},[a("h6",{staticClass:"subheader"},[t._v("test@mail.ru")])])}],r={name:"AgentsDetails"},i=r,c=a("2877"),l=Object(c["a"])(i,s,n,!1,null,"2a0758f5",null);e["a"]=l.exports},5147:function(t,e,a){var s=a("2b4c")("match");t.exports=function(t){var e=/./;try{"/./"[t](e)}catch(a){try{return e[s]=!1,!"/./"[t](e)}catch(n){}}return!0}},"520a":function(t,e,a){"use strict";var s=a("0bfb"),n=RegExp.prototype.exec,r=String.prototype.replace,i=n,c="lastIndex",l=function(){var t=/a/,e=/b*/g;return n.call(t,"a"),n.call(e,"a"),0!==t[c]||0!==e[c]}(),o=void 0!==/()??/.exec("")[1],d=l||o;d&&(i=function(t){var e,a,i,d,u=this;return o&&(a=new RegExp("^"+u.source+"$(?!\\s)",s.call(u))),l&&(e=u[c]),i=n.call(u,t),l&&i&&(u[c]=u.global?i.index+i[0].length:e),o&&i&&i.length>1&&r.call(i[0],a,(function(){for(d=1;d<arguments.length-2;d++)void 0===arguments[d]&&(i[d]=void 0)})),i}),t.exports=i},"5f1b":function(t,e,a){"use strict";var s=a("23c6"),n=RegExp.prototype.exec;t.exports=function(t,e){var a=t.exec;if("function"===typeof a){var r=a.call(t,e);if("object"!==typeof r)throw new TypeError("RegExp exec method returned something other than an Object or null");return r}if("RegExp"!==s(t))throw new TypeError("RegExp#exec called on incompatible receiver");return n.call(t,e)}},"635e":function(t,e,a){"use strict";var s=a("2d89"),n=a.n(s);n.a},"672a":function(t,e,a){"use strict";var s=a("7291"),n=a.n(s);n.a},6762:function(t,e,a){"use strict";var s=a("5ca1"),n=a("c366")(!0);s(s.P,"Array",{includes:function(t){return n(this,t,arguments.length>1?arguments[1]:void 0)}}),a("9c6c")("includes")},7291:function(t,e,a){},"7c0b":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"card"},[a("div",{staticClass:"row header-wrapper pl-3"},[a("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[a("span",{staticClass:"table__icon"},[a("font-awesome-icon",{attrs:{icon:t.icon}})],1),a("h6",{staticClass:"header ml-1"},[t._v(t._s(t.header))]),a("button",{staticClass:"more-btn ml-auto",on:{click:function(e){t.isTableExpanded=!t.isTableExpanded}}},[t._v("Все")])])]),a("div",{staticClass:"row"},[a("div",{staticClass:"col-12"},[a("b-table",{staticClass:"mb-0",attrs:{striped:"",hover:"",items:t.items,fields:t.fields,striped:!1,"per-page":t.visibleItems,fixed:!0}})],1)])])},n=[],r={name:"expandTable",data:function(){return{isTableExpanded:!1}},props:{items:Array,fields:Array,header:String,icon:Array},computed:{visibleItems:function(){return!1===this.isTableExpanded?5:this.items.length}}},i=r,c=(a("635e"),a("2877")),l=Object(c["a"])(i,s,n,!1,null,"1df11c86",null);e["a"]=l.exports},"83a1":function(t,e){t.exports=Object.is||function(t,e){return t===e?0!==t||1/t===1/e:t!=t&&e!=e}},aae3:function(t,e,a){var s=a("d3f4"),n=a("2d95"),r=a("2b4c")("match");t.exports=function(t){var e;return s(t)&&(void 0!==(e=t[r])?!!e:"RegExp"==n(t))}},b0c5:function(t,e,a){"use strict";var s=a("520a");a("5ca1")({target:"RegExp",proto:!0,forced:s!==/./.exec},{exec:s})},c149:function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"card container-fluid"},[a("div",{staticClass:"row header-wrapper pl-3"},[a("div",{staticClass:"col-12 pl-0 pt-1 d-flex align-items-center justify-content-start"},[t.icon?a("span",{staticClass:"icon"},[a("font-awesome-icon",{attrs:{icon:t.icon}})],1):t._e(),a("h6",{staticClass:"header",class:{"ml-1":t.icon}},[t._v(t._s(t.header))]),a("button",{staticClass:"more-btn",on:{click:function(e){t.isTableExpanded=!t.isTableExpanded}}},[t._v("Все")])])]),a("div",{staticClass:"row"},t._l(t.items,(function(e){return a("div",{staticClass:"col-12 notification text-left"},[a("h6",{staticClass:"notification__username"},[t._v("\n                "+t._s(e.agent.user.full_name)+"\n            ")]),a("p",{staticClass:"notification__message"},[t._v("\n                "+t._s(e.mess)+"\n            ")]),a("span",{staticClass:"notification__date"},[t._v("\n                 "+t._s(e.created_at)+"\n            ")])])})),0)])},n=[],r={name:"Notifications",data:function(){return{isTableExpanded:!1}},props:{items:Array,header:String,icon:Array},computed:{visibleItems:function(){return!1===this.isTableExpanded?5:11}},mounted:function(){}},i=r,c=(a("672a"),a("2877")),l=Object(c["a"])(i,s,n,!1,null,"c975dd8a",null);e["a"]=l.exports},d2c8:function(t,e,a){var s=a("aae3"),n=a("be13");t.exports=function(t,e,a){if(s(e))throw TypeError("String#"+a+" doesn't accept regex!");return String(n(t))}},f850:function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticClass:"card"},[a("div",{staticClass:"row header-wrapper pl-3"},[a("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[a("span",{staticClass:"table__icon"},[a("font-awesome-icon",{attrs:{icon:["fas","users"]}})],1),a("h6",{staticClass:"header ml-1"},[t._v("Агенты")]),a("div",{staticClass:"header__search ml-auto mr-5 d-flex align-items-center"},[a("h6",{staticClass:"header"},[t._v("Поиск:")]),a("div",{staticClass:"header__search-inner ml-3"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.search,expression:"search"}],attrs:{type:"search"},domProps:{value:t.search},on:{input:function(e){e.target.composing||(t.search=e.target.value)}}}),a("label",[t._v("Логин, ФИО")]),a("font-awesome-icon",{staticClass:"header__search-icon",attrs:{icon:["fas","search"]}})],1)]),a("router-link",{staticClass:"main-btn ml-5",attrs:{to:"/agents/add"}},[t._v("Добавить агента")]),a("button",{staticClass:"more-btn ml-2",on:{click:function(e){t.isTableExpanded=!t.isTableExpanded}}},[t._v("Все")])],1)]),a("div",{staticClass:"row"},[a("div",{staticClass:"col-12"},[a("b-table",{staticClass:"mb-0",attrs:{striped:"",hover:"",items:t.filteredList,fields:t.fields,striped:!1,"per-page":t.visibleItems,responsive:"","sticky-header":!0},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[a("div",{staticClass:"text-nowrap",on:{click:function(a){return t.showDetails(e.item.pk)}}},[t._v("details")])]}}])})],1)])])])},n=[],r=(a("386d"),a("6762"),a("2fdb"),a("7c0b")),i=a("bc3a"),c=a.n(i),l={name:"AgentsTable",components:{ExpandTable:r["a"]},data:function(){return{isTableExpanded:!1,data:[],search:"",fields:[{key:"tags",label:"Тэг",class:"table-header text-nowrap"},{key:"user.email",label:"Логин",class:"table-header table-accent text-nowrap"},{key:"user.full_name",label:"ФИО",class:"table-header accent text-nowrap"},{key:"created_at",label:"Дата создания",class:"table-header text-nowrap"},{key:"last_change",label:"Дата изменения",class:"table-header text-nowrap"},{key:"actions",label:"Действия",class:"table-header text-nowrap"}],items:[{tags:40,login:"Dickerson",full_name:"Macdonald",created_at:"2019/08/16",changed_ad:"2019/08/16",actions:""}]}},computed:{visibleItems:function(){return this.isTableExpanded?this.filteredList.length:5},filteredList:function(){var t=this;return this.data.filter((function(e){return JSON.stringify(e).toLowerCase().includes(t.search.toLowerCase())}))}},methods:{getData:function(){var t=this;c.a.get("".concat(this.$hostname,"/api/agents/")).then((function(e){t.data=e.data,console.log(e.data)}))},showDetails:function(t){this.$store.dispatch("loadAgentDetails",t),this.$router.push({path:"/agents"})}},mounted:function(){this.getData()}},o=l,d=a("2877"),u=Object(d["a"])(o,s,n,!1,null,"10af0728",null);e["a"]=u.exports}}]);
//# sourceMappingURL=chunk-0c310fcb.b53f25be.js.map