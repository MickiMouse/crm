(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-27e88d7e"],{"02f4":function(t,e,s){var a=s("4588"),i=s("be13");t.exports=function(t){return function(e,s){var n,l,r=String(i(e)),o=a(s),c=r.length;return o<0||o>=c?t?"":void 0:(n=r.charCodeAt(o),n<55296||n>56319||o+1===c||(l=r.charCodeAt(o+1))<56320||l>57343?t?r.charAt(o):n:t?r.slice(o,o+2):l-56320+(n-55296<<10)+65536)}}},"0390":function(t,e,s){"use strict";var a=s("02f4")(!0);t.exports=function(t,e,s){return e+(s?a(t,e).length:1)}},1477:function(t,e,s){},"28a5":function(t,e,s){"use strict";var a=s("aae3"),i=s("cb7c"),n=s("ebd6"),l=s("0390"),r=s("9def"),o=s("5f1b"),c=s("520a"),d=s("79e5"),v=Math.min,u=[].push,_="split",p="length",f="lastIndex",h=4294967295,m=!d((function(){RegExp(h,"y")}));s("214f")("split",2,(function(t,e,s,d){var C;return C="c"=="abbc"[_](/(b)*/)[1]||4!="test"[_](/(?:)/,-1)[p]||2!="ab"[_](/(?:ab)*/)[p]||4!="."[_](/(.?)(.?)/)[p]||"."[_](/()()/)[p]>1||""[_](/.?/)[p]?function(t,e){var i=String(this);if(void 0===t&&0===e)return[];if(!a(t))return s.call(i,t,e);var n,l,r,o=[],d=(t.ignoreCase?"i":"")+(t.multiline?"m":"")+(t.unicode?"u":"")+(t.sticky?"y":""),v=0,_=void 0===e?h:e>>>0,m=new RegExp(t.source,d+"g");while(n=c.call(m,i)){if(l=m[f],l>v&&(o.push(i.slice(v,n.index)),n[p]>1&&n.index<i[p]&&u.apply(o,n.slice(1)),r=n[0][p],v=l,o[p]>=_))break;m[f]===n.index&&m[f]++}return v===i[p]?!r&&m.test("")||o.push(""):o.push(i.slice(v)),o[p]>_?o.slice(0,_):o}:"0"[_](void 0,0)[p]?function(t,e){return void 0===t&&0===e?[]:s.call(this,t,e)}:s,[function(s,a){var i=t(this),n=void 0==s?void 0:s[e];return void 0!==n?n.call(s,i,a):C.call(String(i),s,a)},function(t,e){var a=d(C,t,this,e,C!==s);if(a.done)return a.value;var c=i(t),u=String(this),_=n(c,RegExp),p=c.unicode,f=(c.ignoreCase?"i":"")+(c.multiline?"m":"")+(c.unicode?"u":"")+(m?"y":"g"),b=new _(m?c:"^(?:"+c.source+")",f),y=void 0===e?h:e>>>0;if(0===y)return[];if(0===u.length)return null===o(b,u)?[u]:[];var g=0,w=0,x=[];while(w<u.length){b.lastIndex=m?w:0;var k,$=o(b,m?u:u.slice(w));if(null===$||(k=v(r(b.lastIndex+(m?0:w)),u.length))===g)w=l(u,w,p);else{if(x.push(u.slice(g,w)),x.length===y)return x;for(var j=1;j<=$.length-1;j++)if(x.push($[j]),x.length===y)return x;w=g=k}}return x.push(u.slice(g)),x}]}))},"48e6":function(t,e,s){},"56a5":function(t,e,s){"use strict";var a=s("48e6"),i=s.n(a);i.a},5804:function(t,e,s){"use strict";var a=s("1477"),i=s.n(a);i.a},"58f3":function(t,e,s){"use strict";s.r(e);var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"content"},[s("div",{staticClass:"row"},[s("div",{staticClass:"col-12"},[s("clients-table")],1)]),t.$store.getters.getClientDetails?s("div",{staticClass:"row py-3"},[s("div",{staticClass:"col-12"},[s("clients-details",{staticClass:"mb-3"}),s("clients-table-i-p",{staticClass:"mb-3"}),s("clients-table-workers",{staticClass:"mb-3"})],1),s("div",{staticClass:"col-6"},[s("notifications",{attrs:{items:[{agent:{user:{email:"admin@soft.com",full_name:"Dennis Pashnev",username:"admin"}},created_at:"09.26.2019 12:06:38",mess:"ТЕСТИМ"}],header:"Комментарии",icon:["far","comment-alt"]}})],1),s("div",{staticClass:"col-6"},[s("notifications",{attrs:{items:[{agent:{user:{email:"admin@soft.com",full_name:"Dennis Pashnev",username:"admin"}},created_at:"09.26.2019 12:06:38",mess:"ТЕСТИМ"}],header:"Последние уведомления",icon:["far","bell"]}})],1)]):t._e()])},i=[],n=(s("f850"),s("4aea"),s("c149")),l=(s("4ce1"),function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"card"},[s("div",{staticClass:"row header-wrapper pl-3"},[s("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[s("span",{staticClass:"table__icon"},[s("font-awesome-icon",{attrs:{icon:["fas","users"]}})],1),s("h6",{staticClass:"header ml-1"},[t._v("Клиенты")]),s("div",{staticClass:"header__search ml-auto mr-5 d-flex align-items-center"},[s("h6",{staticClass:"header"},[t._v("Поиск:")]),s("div",{staticClass:"header__search-inner ml-3"},[s("input",{directives:[{name:"model",rawName:"v-model",value:t.search,expression:"search"}],attrs:{type:"search"},domProps:{value:t.search},on:{input:function(e){e.target.composing||(t.search=e.target.value)}}}),s("label",[t._v("Логин, ФИО")]),s("font-awesome-icon",{staticClass:"header__search-icon",attrs:{icon:["fas","search"]}})],1)]),s("button",{staticClass:"more-btn ml-2",on:{click:function(e){t.isTableExpanded=!t.isTableExpanded}}},[t._v("Все")])])]),s("div",{staticClass:"row"},[s("div",{staticClass:"col-12"},[s("b-table",{staticClass:"mb-0",attrs:{striped:"",hover:"",items:t.filteredList,fields:t.fields,striped:!1,"per-page":t.visibleItems,responsive:"","sticky-header":!0},scopedSlots:t._u([{key:"cell(short_name)",fn:function(e){return[s("div",{staticClass:"text-nowrap",staticStyle:{cursor:"pointer"},on:{click:function(s){return t.getDetails(e.item.pk)}}},[t._v(t._s(e.item.short_name))])]}},{key:"cell(kind_of_activity)",fn:function(e){return t._l(e.kind_of_activity,(function(e){return s("div",{staticClass:"text-nowrap"},[t._v(t._s(e.activity))])}))}},{key:"cell(actions)",fn:function(t){return[s("div",{staticClass:"d-flex"},[s("action-button",{staticClass:"mx-1",attrs:{icon:["far","comment-alt"]}}),s("action-button",{staticClass:"mx-1",attrs:{icon:["far","bell"]}}),s("action-button",{staticClass:"mx-1",attrs:{icon:["far","edit"]}})],1)]}}])})],1)])])}),r=[],o=(s("386d"),s("6762"),s("2fdb"),s("7c0b")),c=s("bc3a"),d=s.n(c),v=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("button",{on:{click:t.handleClick}},[s("font-awesome-icon",{attrs:{icon:t.icon}})],1)},u=[],_={name:"ActionButton",methods:{handleClick:function(){this.$emit("click")}},props:{icon:Array}},p=_,f=(s("56a5"),s("2877")),h=Object(f["a"])(p,v,u,!1,null,"011b7419",null),m=h.exports,C={name:"ClientsTable",components:{ActionButton:m,ExpandTable:o["a"]},data:function(){return{isTableExpanded:!1,data:[],search:"",fields:[{key:"short_name",label:"Наиминование компании",class:"table-header table-accent text-nowrap"},{key:"kind_of_activity",label:"Вид деятельности",class:"table-header text-nowrap"},{key:"extra_address",label:"Доп. адрес",class:"table-header accent text-nowrap"},{key:"bin_iin",label:"БИН/ИНН",class:"table-header text-nowrap"},{key:"agent.user.full_name",label:"Агент",class:"table-header table-accent text-nowrap"},{key:"expiration_date",label:"Дата окончания",class:"table-header text-nowrap"},{key:"actions",label:"Действия",class:"table-header text-nowrap"}],items:[{tags:40,login:"Dickerson",full_name:"Macdonald",created_at:"2019/08/16",changed_ad:"2019/08/16",actions:""}]}},computed:{visibleItems:function(){return!1===this.isTableExpanded?5:this.items.length},filteredList:function(){var t=this;return this.data.filter((function(e){return JSON.stringify(e).toLowerCase().includes(t.search.toLowerCase())}))}},methods:{getData:function(){var t=this;d.a.get("".concat(this.$hostname,"/api/clients/")).then((function(e){t.data=e.data,console.log(e.data)}))},getDetails:function(t){this.$store.dispatch("loadClientDetails",t)}},mounted:function(){this.getData()}},b=C,y=Object(f["a"])(b,l,r,!1,null,"7a8a4c68",null),g=y.exports,w=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"mb-3"},[s("div",{staticClass:"card container-fluid"},[s("div",{staticClass:"row header-wrapper"},[s("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[s("h6",{staticClass:"header pr-1"},[t._v(t._s(t.$store.getters.getClientDetails.full_name))])])]),s("div",{staticClass:"row"},[s("div",{staticClass:"col-6"},[s("div",{staticClass:"row"},[t._m(0),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.organization))])])]),s("div",{staticClass:"row"},[t._m(1),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.kind_of_activity.map((function(t){}))))])])]),s("div",{staticClass:"row"},[t._m(2),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.full_name))])])]),s("div",{staticClass:"row"},[t._m(3),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.bin_iin))])])]),s("div",{staticClass:"row"},[t._m(4),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.address_physical))])])]),s("div",{staticClass:"row"},[t._m(5),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.address_legal))])])]),s("div",{staticClass:"row"},[t._m(6),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.extra_address))])])]),s("div",{staticClass:"row"},[t._m(7),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.phone_number))])])])]),s("div",{staticClass:"col-6"},[s("div",{staticClass:"row"},[t._m(8),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.bik))])])]),s("div",{staticClass:"row"},[t._m(9),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.iik))])])]),s("div",{staticClass:"row"},[t._m(10),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.bank_name))])])]),s("div",{staticClass:"row"},[t._m(11),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.kbe))])])]),s("div",{staticClass:"row"},[t._m(12),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.leader))])])]),s("div",{staticClass:"row"},[t._m(13),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.position_leader))])])]),s("div",{staticClass:"row"},[t._m(14),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.phone))])])]),s("div",{staticClass:"row"},[t._m(15),s("div",{staticClass:"col-8 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v(t._s(t.$store.getters.getClientDetails.tax.name))])])])])]),s("div",{staticClass:"row clients__info-wrapper py-2"},[s("div",{staticClass:"col-4 d-flex"},[s("span",{staticClass:"table__icon clients__icon"},[s("font-awesome-icon",{attrs:{icon:["fas","users"]}})],1),s("div",[s("p",{staticClass:"mb-0 clients__info"},[t._v("Дата создания: "+t._s(t.$store.getters.getClientDetails.date))]),s("p",{staticClass:"mb-0 clients__info"},[t._v("Дата изменения: ")])])]),s("div",{staticClass:"col-4 d-flex"},[s("span",{staticClass:"table__icon clients__icon"},[s("font-awesome-icon",{attrs:{icon:["fas","users"]}})],1),s("div",[s("p",{staticClass:"mb-0 clients__info"},[t._v("Дата подписания договора:\n                        "+t._s(t.$store.getters.getClientDetails.date))]),s("p",{staticClass:"mb-0 clients__info"},[t._v("Дата окончания договора: ")]),s("p",{staticClass:"mb-0 clients__info"},[t._v("Сумма договора: ")])])]),s("div",{staticClass:"col-4 d-flex"},[s("span",{staticClass:"table__icon clients__icon"},[s("font-awesome-icon",{attrs:{icon:["fas","users"]}})],1),s("div",[s("p",{staticClass:"mb-0 clients__info"},[t._v("Агент: "+t._s(t.$store.getters.getClientDetails.date))])])])])])])},x=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Организация:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Вид деятельности:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Наименование:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("БИН/ИНН:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Адрес (физ.):")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Адрес (юр.):")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Доп. адрес:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Контактный номер:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("БИК:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("ИИК:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Банк:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Кбе:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Руководитель:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Должность:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("Контактный номер:")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"col-4 py-3 justify-content-start"},[s("h6",{staticClass:"header"},[t._v("УГД:")])])}],k={name:"ClientsDetails"},$=k,j=(s("5804"),Object(f["a"])($,w,x,!1,null,"527aa3af",null)),D=j.exports,E=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("div",{staticClass:"card"},[s("div",{staticClass:"row header-wrapper pl-3"},[s("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[s("span",{staticClass:"table__icon"},[s("font-awesome-icon",{attrs:{icon:["fas","file-invoice"]}})],1),s("h6",{staticClass:"header ml-1"},[t._v("Таблица отчетности ИП")]),s("div",{staticClass:"choose-period__wrapper ml-auto"},[s("span",[t._v("Выбрать период:")]),s("select",{directives:[{name:"model",rawName:"v-model",value:t.date_from,expression:"date_from"}],on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.date_from=e.target.multiple?s:s[0]}}},[s("option",{attrs:{value:"1"}},[t._v("Январь")]),s("option",{attrs:{value:"2"}},[t._v("Февраль")]),s("option",{attrs:{value:"3"}},[t._v("Март")]),s("option",{attrs:{value:"4"}},[t._v("Апрель")]),s("option",{attrs:{value:"5"}},[t._v("Май")]),s("option",{attrs:{value:"6"}},[t._v("Июнь")]),s("option",{attrs:{value:"7"}},[t._v("Июль")]),s("option",{attrs:{value:"8"}},[t._v("Август")]),s("option",{attrs:{value:"9"}},[t._v("Сентябрь")]),s("option",{attrs:{value:"10"}},[t._v("Октябрь")]),s("option",{attrs:{value:"11"}},[t._v("Ноябрь")]),s("option",{attrs:{value:"12"}},[t._v("Декабрь")])]),t._v("\n                    -\n                    "),s("select",{directives:[{name:"model",rawName:"v-model",value:t.date_to,expression:"date_to"}],on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.date_to=e.target.multiple?s:s[0]}}},[s("option",{attrs:{value:"1"}},[t._v("Январь")]),s("option",{attrs:{value:"2"}},[t._v("Февраль")]),s("option",{attrs:{value:"3"}},[t._v("Март")]),s("option",{attrs:{value:"4"}},[t._v("Апрель")]),s("option",{attrs:{value:"5"}},[t._v("Май")]),s("option",{attrs:{value:"6"}},[t._v("Июнь")]),s("option",{attrs:{value:"7"}},[t._v("Июль")]),s("option",{attrs:{value:"8"}},[t._v("Август")]),s("option",{attrs:{value:"9"}},[t._v("Сентябрь")]),s("option",{attrs:{value:"10"}},[t._v("Октябрь")]),s("option",{attrs:{value:"11"}},[t._v("Ноябрь")]),s("option",{attrs:{value:"12"}},[t._v("Декабрь")])])]),s("button",{staticClass:"main-btn mx-3",on:{click:function(t){}}},[t._v("Добавить агента")])])]),s("div",{staticClass:"row"},[s("div",{staticClass:"col-12"},[s("b-table",{staticClass:"mb-0",attrs:{striped:"",hover:"",items:t.filteredList,fields:t.fields,striped:!1,"per-page":t.visibleItems,responsive:"","sticky-header":!0},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[s("div",{staticClass:"text-nowrap",on:{click:function(s){return t.getDetails(e.item.pk)}}},[t._v("details")])]}}])})],1)])])])},T=[],I=(s("28a5"),{name:"ClientsTableIP",components:{ExpandTable:o["a"]},data:function(){return{isTableExpanded:!1,data:{},fields:[{key:"month",label:"Месяц",class:"table-header table-accent text-nowrap"},{key:"earn",label:'ЗП "На руки"',class:"table-header text-nowrap"},{key:"profit",label:'ЗП "начисления"',class:"table-header accent text-nowrap"},{key:"pension_contrib",label:"ОПВ",class:"table-header text-nowrap"},{key:"income_for_so",label:"Доход для СО",class:"table-header table-accent text-nowrap"},{key:"social_contrib",label:"СО",class:"table-header text-nowrap"},{key:"osms",label:"ОСМС",class:"table-header text-nowrap"}],date_from:1,date_to:12}},computed:{visibleItems:function(){return!1===this.isTableExpanded?5:this.items.length},filteredList:function(){var t=this;return this.$store.getters.getClientTablesDetails.first.filter((function(e){return parseInt(e.month.split(".")[1])>=t.date_from&&parseInt(e.month.split(".")[1])<=t.date_to}))}},methods:{},mounted:function(){}}),A=I,S=Object(f["a"])(A,E,T,!1,null,"31e868b6",null),L=S.exports,N=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("div",{staticClass:"card"},[s("div",{staticClass:"row header-wrapper pl-3"},[s("div",{staticClass:"col-12 pt-1 d-flex align-items-center justify-content-start"},[s("span",{staticClass:"table__icon"},[s("font-awesome-icon",{attrs:{icon:["fas","file-invoice"]}})],1),s("h6",{staticClass:"header ml-1"},[t._v("Таблица отчетности работников")]),s("div",{staticClass:"choose-period__wrapper ml-auto"},[s("span",[t._v("Выбрать период:")]),s("select",{directives:[{name:"model",rawName:"v-model",value:t.date_from,expression:"date_from"}],on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.date_from=e.target.multiple?s:s[0]}}},[s("option",{attrs:{value:"1"}},[t._v("Январь")]),s("option",{attrs:{value:"2"}},[t._v("Февраль")]),s("option",{attrs:{value:"3"}},[t._v("Март")]),s("option",{attrs:{value:"4"}},[t._v("Апрель")]),s("option",{attrs:{value:"5"}},[t._v("Май")]),s("option",{attrs:{value:"6"}},[t._v("Июнь")]),s("option",{attrs:{value:"7"}},[t._v("Июль")]),s("option",{attrs:{value:"8"}},[t._v("Август")]),s("option",{attrs:{value:"9"}},[t._v("Сентябрь")]),s("option",{attrs:{value:"10"}},[t._v("Октябрь")]),s("option",{attrs:{value:"11"}},[t._v("Ноябрь")]),s("option",{attrs:{value:"12"}},[t._v("Декабрь")])]),t._v("\n                    -\n                    "),s("select",{directives:[{name:"model",rawName:"v-model",value:t.date_to,expression:"date_to"}],on:{change:function(e){var s=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.date_to=e.target.multiple?s:s[0]}}},[s("option",{attrs:{value:"1"}},[t._v("Январь")]),s("option",{attrs:{value:"2"}},[t._v("Февраль")]),s("option",{attrs:{value:"3"}},[t._v("Март")]),s("option",{attrs:{value:"4"}},[t._v("Апрель")]),s("option",{attrs:{value:"5"}},[t._v("Май")]),s("option",{attrs:{value:"6"}},[t._v("Июнь")]),s("option",{attrs:{value:"7"}},[t._v("Июль")]),s("option",{attrs:{value:"8"}},[t._v("Август")]),s("option",{attrs:{value:"9"}},[t._v("Сентябрь")]),s("option",{attrs:{value:"10"}},[t._v("Октябрь")]),s("option",{attrs:{value:"11"}},[t._v("Ноябрь")]),s("option",{attrs:{value:"12"}},[t._v("Декабрь")])])]),s("button",{staticClass:"main-btn ml-3",on:{click:function(t){}}},[t._v("Добавить работника")]),s("button",{staticClass:"main-btn mx-3",on:{click:function(t){}}},[t._v("Редактировать")])])]),s("div",{staticClass:"row"},[s("div",{staticClass:"col-12"},[s("b-table",{staticClass:"mb-0",attrs:{striped:"",hover:"",items:t.filteredList,fields:t.fields,striped:!1,"per-page":t.visibleItems,responsive:"","sticky-header":!0},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[s("div",{staticClass:"text-nowrap",on:{click:function(s){return t.getDetails(e.item.pk)}}},[t._v("details")])]}}])})],1)])])])},O=[],P={name:"ClientsTableWorkers",components:{ExpandTable:o["a"]},data:function(){return{isTableExpanded:!1,data:{},fields:[{key:"month",label:"Месяц",class:"table-header table-accent text-nowrap"},{key:"worker.last_name",label:"Работник",class:"table-header text-nowrap"},{key:"earn",label:'ЗП "На руки"',class:"table-header accent text-nowrap"},{key:"profit",label:'ЗП "начисления"',class:"table-header text-nowrap"},{key:"adjustment",label:"Корректировка",class:"table-header table-accent text-nowrap"},{key:"pension_contrib",label:"ОПВ",class:"table-header text-nowrap"},{key:"individual_income_tax",label:"ИПН",class:"table-header text-nowrap"},{key:"social_contrib",label:"СО",class:"table-header text-nowrap"},{key:"med_contrib",label:"ОСМС",class:"table-header text-nowrap"}],items:[{tags:40,login:"Dickerson",full_name:"Macdonald",created_at:"2019/08/16",changed_ad:"2019/08/16",actions:""}],date_from:1,date_to:12}},computed:{visibleItems:function(){return!1===this.isTableExpanded?5:this.items.length},filteredList:function(){var t=this;return this.$store.getters.getClientTablesDetails.second.filter((function(e){return parseInt(e.month.split(".")[1])>=t.date_from&&parseInt(e.month.split(".")[1])<=t.date_to}))}},methods:{},mounted:function(){console.log(this.$store.getters.getClientTablesDetails.second),this.$store.getters.getClientTablesDetails.second.filter((function(t){console.log(t.month.split(".")[1])}))}},J=P,M=(s("98e2"),Object(f["a"])(J,N,O,!1,null,"91499d2a",null)),R=M.exports,B={name:"Clients",components:{ClientsTableWorkers:R,ClientsTableIP:L,ClientsDetails:D,ClientsTable:g,Notifications:n["a"]},data:function(){return{data:[]}},beforeCreate:function(){this.$session.exists()||this.$router.push("/"),console.log(this.$store.getters.getAgentDetails)}},W=B,z=Object(f["a"])(W,a,i,!1,null,"0e55cafa",null);e["default"]=z.exports},"74bc":function(t,e,s){},"98e2":function(t,e,s){"use strict";var a=s("74bc"),i=s.n(a);i.a}}]);
//# sourceMappingURL=chunk-27e88d7e.78ad1975.js.map