(this["webpackJsonpschema-collaboration-react"]=this["webpackJsonpschema-collaboration-react"]||[]).push([[0],{269:function(t,e,n){"use strict";function o(t,e){e||(e=window.location.href),t=t.replace(/[[\]]/g,"\\$&");var n=new RegExp("[?&]"+t+"(=([^&#]*)|&|#|$)").exec(e);return n?n[2]?decodeURIComponent(n[2].replace(/\+/g," ")):"":null}n.r(e),n.d(e,"getParameterFromUrlByName",(function(){return o}))},273:function(t,e,n){t.exports=n(274)},274:function(t,e,n){"use strict";n.r(e);n(0),n(276);var o=n(143),a=n.n(o),r=n(631).EditorSchemaCollaborationButtons;console.log(r),a.a.render(a.a.EditorPackage,{descriptor:{},Buttons:r},document.getElementById("root"))},276:function(t,e,n){},327:function(t,e){},329:function(t,e){},356:function(t,e){},358:function(t,e){},438:function(t,e,n){var o={"./geojson.json":216,"./table-schema.json":439,"./topojson.json":217};function a(t){var e=r(t);return n(e)}function r(t){if(!n.o(o,t)){var e=new Error("Cannot find module '"+t+"'");throw e.code="MODULE_NOT_FOUND",e}return o[t]}a.keys=function(){return Object.keys(o)},a.resolve=r,t.exports=a,a.id=438},505:function(t,e){},507:function(t,e){},508:function(t,e){},514:function(t,e){},516:function(t,e){},534:function(t,e){},536:function(t,e){},548:function(t,e){},551:function(t,e){},574:function(t,e,n){var o={"./data-package.json":575,"./data-resource.json":576,"./fiscal-data-package.json":577,"./registry.json":578,"./tabular-data-package.json":579,"./tabular-data-resource.json":580};function a(t){var e=r(t);return n(e)}function r(t){if(!n.o(o,t)){var e=new Error("Cannot find module '"+t+"'");throw e.code="MODULE_NOT_FOUND",e}return o[t]}a.keys=function(){return Object.keys(o)},a.resolve=r,t.exports=a,a.id=574},631:function(t,e,n){var o=n(31),a=n(0),r=n(0).useEffect,c=n(19).connect,i=n(270).ToastContainer,l=n(632).onSaveToServer,u=n(269).getParameterFromUrlByName;function s(t){var e=this,n=t.encodedDescriptor,o=t.onUploadChange,c=t.onValidateClick,u=t.onLoadFromServer;return r((function(){return e.loadFromServerButton.click()}),[]),a.createElement("div",null,a.createElement(i,null),a.createElement("label",{className:"btn btn-lg btn-success",title:"Upload a data package from your local drive",htmlFor:"load-descriptor"},a.createElement("input",{type:"file",id:"load-descriptor",value:"",style:{display:"none"},onChange:o}),"Upload"),a.createElement("button",{className:"btn btn-lg btn-info",title:"Validate the data package verifying its metadata",onClick:c},"Validate"),a.createElement("a",{className:"btn btn-lg btn-success",href:"data: ".concat(n),download:"datapackage.json",title:"Download the data package to your local drive"},"Download"),a.createElement("button",{className:"btn btn-lg btn-info",title:"Save current schema to the server",onClick:function(){return l("".concat(decodeURIComponent(n)))}},"Save to server"),a.createElement("button",{className:"btn btn-lg btn-info",title:"Load from the server",onClick:u,ref:function(t){e.loadFromServerButton=t}},"Load from the server"))}var d=c(null,(function(t){return{onUploadChange:function(e){var n=new window.FileReader;n.readAsText(e.target.files[0]),n.onload=function(){t({type:"UPLOAD_PACKAGE",payload:JSON.parse(n.result)})}},onValidateClick:function(){t({type:"VALIDATE_PACKAGE"})},onLoadFromServer:function(){var e=u("load");o.get("/api/datapackage/"+e+"/").then((function(e){console.log(e.data),t({type:"UPLOAD_PACKAGE",payload:e.data})}))}}}))(s);t.exports={EditorSchemaCollaborationButtons:d,EditorSchemaCollaborationButtonsPure:s}},632:function(t,e,n){"use strict";n.r(e),n.d(e,"onSaveToServer",(function(){return c}));var o=n(31),a=n(270).toast,r=n(269).getParameterFromUrlByName;function c(t){var e=r("load"),n="",c="";return null===e?(n="/api/datapackage/",c="POST"):(n="/api/datapackage/"+e+"/",c="PUT"),o(n,{method:c,data:t}).then((function(t){return console.log(t),a("Saved! UUID: "+t.data.uuid),t})).catch((function(t){return t}))}}},[[273,1,2]]]);
//# sourceMappingURL=main.d245f927.chunk.js.map