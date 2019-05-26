var x = document.querySelectorAll("li.list-group-item");
                var i = x.length;
                var temp="";
                for(var a=0;a<i;a++)
                {
                    var content = x[a].textContent;
                    if(content.length>50)
                    {
                        var username = x[a-1].textContent;
                        for(var j=0;j<50;j++)
                        {
                            temp = temp + content[j];
                        }
                        temp+="...";
                        var link ="<a href='/paste/detailed/"+ username +"'>Read More</a>"
                        x[a].innerHTML = temp + link;
                        temp = "";
                    }
                }