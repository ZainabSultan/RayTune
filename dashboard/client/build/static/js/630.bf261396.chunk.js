"use strict";(self.webpackChunkray_dashboard_client=self.webpackChunkray_dashboard_client||[]).push([[630],{2630:function(e,t,a){a.r(t),a.d(t,{default:function(){return y}});var n=a(885),o=a(8596),r=a(2206),i=a(9773),l=a(7631),d=a(6593),c=a(3486),s=a(2791),p="1.0.0",u=a(359),h=a(476),f=a(6641),g=a(1426),m=a(184),v=(0,o.Z)((function(e){return{root:{padding:e.spacing(2)},label:{fontWeight:"bold"}}})),x=function(e,t){return"containerMemory"===e?(0,g.r)(1024*t*1024):JSON.stringify(t)},Z=function(){var e=(0,s.useState)(),t=(0,n.Z)(e,2),a=t[0],o=t[1],r=(0,s.useState)([]),i=(0,n.Z)(r,2),l=i[0],d=i[1];return(0,s.useEffect)((function(){(0,h.U)("api/ray_config").then((function(e){var t,a;null!==e&&void 0!==e&&null!==(t=e.data)&&void 0!==t&&null!==(a=t.data)&&void 0!==a&&a.config&&o(e.data.data.config)}))}),[]),(0,s.useEffect)((function(){(0,f.b)().then((function(e){var t,a;null!==e&&void 0!==e&&null!==(t=e.data)&&void 0!==t&&null!==(a=t.data)&&void 0!==a&&a.summary&&d(e.data.data.summary)}))}),[]),{rayConfig:a,nodes:l}},y=function(){var e=Z().rayConfig,t=v();return(0,m.jsxs)("div",{className:t.root,children:[(0,m.jsxs)(u.Z,{title:(null===e||void 0===e?void 0:e.clusterName)||"SUMMARY",children:[(0,m.jsxs)("p",{children:["Dashboard Frontend Version: ",p]}),(null===e||void 0===e?void 0:e.imageUrl)&&(0,m.jsxs)("p",{children:["Image Url:"," ",(0,m.jsx)("a",{href:e.imageUrl,target:"_blank",rel:"noopener noreferrer",children:e.imageUrl})]}),(null===e||void 0===e?void 0:e.sourceCodeLink)&&(0,m.jsxs)("p",{children:["Source Code:"," ",(0,m.jsx)("a",{href:e.sourceCodeLink,target:"_blank",rel:"noopener noreferrer",children:e.sourceCodeLink})]})]}),e&&(0,m.jsx)(u.Z,{title:"Config",children:(0,m.jsxs)(r.Z,{children:[(0,m.jsxs)(i.Z,{children:[(0,m.jsx)(l.Z,{children:"Key"}),(0,m.jsx)(l.Z,{children:"Value"})]}),(0,m.jsx)(d.Z,{children:Object.entries(e).map((function(e){var a=(0,n.Z)(e,2),o=a[0],r=a[1];return(0,m.jsxs)(c.Z,{children:[(0,m.jsx)(l.Z,{className:t.label,children:o}),(0,m.jsx)(l.Z,{children:x(o,r)})]})}))})]})})]})}},1426:function(e,t,a){a.d(t,{r:function(){return n}});var n=function(e){return e<1024?"".concat(e.toFixed(4),"KB"):e<Math.pow(1024,2)?"".concat((e/Math.pow(1024,1)).toFixed(2),"KB"):e<Math.pow(1024,3)?"".concat((e/Math.pow(1024,2)).toFixed(2),"MB"):e<Math.pow(1024,4)?"".concat((e/Math.pow(1024,3)).toFixed(2),"GB"):e<Math.pow(1024,5)?"".concat((e/Math.pow(1024,4)).toFixed(2),"TB"):e<Math.pow(1024,6)?"".concat((e/Math.pow(1024,5)).toFixed(2),"TB"):""}},4642:function(e,t,a){var n=a(2791).createContext();t.Z=n},9521:function(e,t,a){var n=a(2791).createContext();t.Z=n},6593:function(e,t,a){var n=a(7462),o=a(5987),r=a(2791),i=a(8182),l=a(8317),d=a(9521),c={variant:"body"},s="tbody",p=r.forwardRef((function(e,t){var a=e.classes,l=e.className,p=e.component,u=void 0===p?s:p,h=(0,o.Z)(e,["classes","className","component"]);return r.createElement(d.Z.Provider,{value:c},r.createElement(u,(0,n.Z)({className:(0,i.Z)(a.root,l),ref:t,role:u===s?null:"rowgroup"},h)))}));t.Z=(0,l.Z)({root:{display:"table-row-group"}},{name:"MuiTableBody"})(p)},7631:function(e,t,a){var n=a(5987),o=a(7462),r=a(2791),i=a(8182),l=a(8317),d=a(1122),c=a(3108),s=a(4642),p=a(9521),u=r.forwardRef((function(e,t){var a,l,c=e.align,u=void 0===c?"inherit":c,h=e.classes,f=e.className,g=e.component,m=e.padding,v=e.scope,x=e.size,Z=e.sortDirection,y=e.variant,b=(0,n.Z)(e,["align","classes","className","component","padding","scope","size","sortDirection","variant"]),w=r.useContext(s.Z),C=r.useContext(p.Z),M=C&&"head"===C.variant;g?(l=g,a=M?"columnheader":"cell"):l=M?"th":"td";var N=v;!N&&M&&(N="col");var j=m||(w&&w.padding?w.padding:"normal"),k=x||(w&&w.size?w.size:"medium"),R=y||C&&C.variant,F=null;return Z&&(F="asc"===Z?"ascending":"descending"),r.createElement(l,(0,o.Z)({ref:t,className:(0,i.Z)(h.root,h[R],f,"inherit"!==u&&h["align".concat((0,d.Z)(u))],"normal"!==j&&h["padding".concat((0,d.Z)(j))],"medium"!==k&&h["size".concat((0,d.Z)(k))],"head"===R&&w&&w.stickyHeader&&h.stickyHeader),"aria-sort":F,role:a,scope:N},b))}));t.Z=(0,l.Z)((function(e){return{root:(0,o.Z)({},e.typography.body2,{display:"table-cell",verticalAlign:"inherit",borderBottom:"1px solid\n    ".concat("light"===e.palette.type?(0,c.$n)((0,c.Fq)(e.palette.divider,1),.88):(0,c._j)((0,c.Fq)(e.palette.divider,1),.68)),textAlign:"left",padding:16}),head:{color:e.palette.text.primary,lineHeight:e.typography.pxToRem(24),fontWeight:e.typography.fontWeightMedium},body:{color:e.palette.text.primary},footer:{color:e.palette.text.secondary,lineHeight:e.typography.pxToRem(21),fontSize:e.typography.pxToRem(12)},sizeSmall:{padding:"6px 24px 6px 16px","&:last-child":{paddingRight:16},"&$paddingCheckbox":{width:24,padding:"0 12px 0 16px","&:last-child":{paddingLeft:12,paddingRight:16},"& > *":{padding:0}}},paddingCheckbox:{width:48,padding:"0 0 0 4px","&:last-child":{paddingLeft:0,paddingRight:4}},paddingNone:{padding:0,"&:last-child":{padding:0}},alignLeft:{textAlign:"left"},alignCenter:{textAlign:"center"},alignRight:{textAlign:"right",flexDirection:"row-reverse"},alignJustify:{textAlign:"justify"},stickyHeader:{position:"sticky",top:0,left:0,zIndex:2,backgroundColor:e.palette.background.default}}}),{name:"MuiTableCell"})(u)},2206:function(e,t,a){var n=a(7462),o=a(5987),r=a(2791),i=a(8182),l=a(8317),d=r.forwardRef((function(e,t){var a=e.classes,l=e.className,d=e.component,c=void 0===d?"div":d,s=(0,o.Z)(e,["classes","className","component"]);return r.createElement(c,(0,n.Z)({ref:t,className:(0,i.Z)(a.root,l)},s))}));t.Z=(0,l.Z)({root:{width:"100%",overflowX:"auto"}},{name:"MuiTableContainer"})(d)},9773:function(e,t,a){var n=a(7462),o=a(5987),r=a(2791),i=a(8182),l=a(8317),d=a(9521),c={variant:"head"},s="thead",p=r.forwardRef((function(e,t){var a=e.classes,l=e.className,p=e.component,u=void 0===p?s:p,h=(0,o.Z)(e,["classes","className","component"]);return r.createElement(d.Z.Provider,{value:c},r.createElement(u,(0,n.Z)({className:(0,i.Z)(a.root,l),ref:t,role:u===s?null:"rowgroup"},h)))}));t.Z=(0,l.Z)({root:{display:"table-header-group"}},{name:"MuiTableHead"})(p)},3486:function(e,t,a){var n=a(7462),o=a(5987),r=a(2791),i=a(8182),l=a(8317),d=a(9521),c=a(3108),s=r.forwardRef((function(e,t){var a=e.classes,l=e.className,c=e.component,s=void 0===c?"tr":c,p=e.hover,u=void 0!==p&&p,h=e.selected,f=void 0!==h&&h,g=(0,o.Z)(e,["classes","className","component","hover","selected"]),m=r.useContext(d.Z);return r.createElement(s,(0,n.Z)({ref:t,className:(0,i.Z)(a.root,l,m&&{head:a.head,footer:a.footer}[m.variant],u&&a.hover,f&&a.selected),role:"tr"===s?null:"row"},g))}));t.Z=(0,l.Z)((function(e){return{root:{color:"inherit",display:"table-row",verticalAlign:"middle",outline:0,"&$hover:hover":{backgroundColor:e.palette.action.hover},"&$selected, &$selected:hover":{backgroundColor:(0,c.Fq)(e.palette.secondary.main,e.palette.action.selectedOpacity)}},selected:{},hover:{},head:{},footer:{}}}),{name:"MuiTableRow"})(s)}}]);
//# sourceMappingURL=630.bf261396.chunk.js.map