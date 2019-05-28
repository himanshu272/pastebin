var x = document.querySelectorAll("p.data");
var y = document.querySelectorAll("p.language");
var z = document.querySelectorAll("code");
var extras = document.querySelectorAll("p.extra");
                var i = x.length;
                var temp="";
                for(var a=0;a<i;a++)
                {
                    if(y[a].textContent=="python")
                        z[a].classList.add("language-python");
                    else if(y[a].textContent=="java")
                        z[a].classList.add("language-java");
                    else if(y[a].textContent=="javascript")
                        z[a].classList.add("language-javascript");
                    else if(y[a].textContent=="C++")
                        z[a].classList.add("language-C++");
                    else
                        z[a].classList.add("language-none");
                    var content = z[a].textContent;
                    if(content.length>50)
                    {
                        var username = x[a].textContent;
                        for(var j=0;j<50;j++)
                        {
                            temp = temp + content[j];
                        }
                        temp+="...";
                        var link ="<a href='/paste/detailed/"+ username +"'>Read More</a>"
                        z[a].innerHTML = temp;
                        extras[a].innerHTML = link;
                        temp = "";
                    }
                }