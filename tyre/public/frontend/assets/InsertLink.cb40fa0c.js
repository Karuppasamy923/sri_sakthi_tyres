import{_ as d,j as g,I as L,R as m,e as p,M as f,N as D,O as c,f as i,t as l,F as h,g as a,o as _,q as v,G as w}from"./vendor.2c1d9872.js";const x={name:"InsertLink",props:["editor"],components:{Button:g,Input:L,Dialog:m},data(){return{setLinkDialog:{url:"",show:!1}}},methods:{openDialog(){let t=this.editor.getAttributes("link").href;t&&(this.setLinkDialog.url=t),this.setLinkDialog.show=!0},setLink(t){t===""?this.editor.chain().focus().extendMarkRange("link").unsetLink().run():this.editor.chain().focus().extendMarkRange("link").setLink({href:t}).run(),this.setLinkDialog.show=!1,this.setLinkDialog.url=""},reset(){this.setLinkDialog=this.$options.data().setLinkDialog}}},V=w(" Save ");function C(t,e,R,B,n,s){const r=a("FormControl"),u=a("Button"),k=a("Dialog");return _(),p(h,null,[f(t.$slots,"default",D(c({onClick:s.openDialog}))),i(k,{options:{title:"Set Link"},modelValue:n.setLinkDialog.show,"onUpdate:modelValue":e[3]||(e[3]=o=>n.setLinkDialog.show=o),onAfterLeave:s.reset},{"body-content":l(()=>[i(r,{type:"text",label:"URL",modelValue:n.setLinkDialog.url,"onUpdate:modelValue":e[0]||(e[0]=o=>n.setLinkDialog.url=o),onKeydown:e[1]||(e[1]=v(o=>s.setLink(o.target.value),["enter"]))},null,8,["modelValue"])]),actions:l(()=>[i(u,{variant:"solid",onClick:e[2]||(e[2]=o=>s.setLink(n.setLinkDialog.url))},{default:l(()=>[V]),_:1})]),_:1},8,["modelValue","onAfterLeave"])],64)}var F=d(x,[["render",C]]);export{F as default};
