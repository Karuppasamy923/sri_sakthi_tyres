import{L as d,e as m,f as e,x as n,g as t,o as u,n as p,u as f,M as _,J as w}from"./vendor.f54e4fb2.js";import{s as r}from"./index.fea849ee.js";const x={class:"m-3 flex flex-row items-center justify-center"},g=["onSubmit"],h=w("Login"),B=d({setup(b){function l(s){let o=new FormData(s.target);r.login.submit({email:o.get("email"),password:o.get("password")})}return(s,o)=>{const a=t("Input"),i=t("Button"),c=t("Card");return u(),m("div",x,[e(c,{title:"Login to your FrappeUI App!",class:"w-full max-w-md mt-4"},{default:n(()=>[p("form",{class:"flex flex-col space-y-2 w-full",onSubmit:_(l,["prevent"])},[e(a,{required:"",name:"email",type:"text",placeholder:"johndoe@email.com",label:"User ID"}),e(a,{required:"",name:"password",type:"password",placeholder:"\u2022\u2022\u2022\u2022\u2022\u2022",label:"Password"}),e(i,{loading:f(r).login.loading,variant:"solid"},{default:n(()=>[h]),_:1},8,["loading"])],40,g)]),_:1})])}}});export{B as default};