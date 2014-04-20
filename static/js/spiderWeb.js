var RadarChart={draw:function(e,t,n){var r={radius:5,w:250,h:250,factor:1,factorLegend:.85,levels:3,maxValue:0,radians:2*Math.PI,opacityArea:.5,color:d3.scale.category10()};if("undefined"!==typeof n){for(var i in n){if("undefined"!==typeof n[i]){r[i]=n[i]}}}r.maxValue=Math.max(r.maxValue,d3.max(t,function(e){return d3.max(e.map(function(e){return e.value}))}));var s=t[0].map(function(e,t){return e.axis});var o=s.length;var u=r.factor*Math.min(r.w/2,r.h/2);d3.select(e).select("svg").remove();var a=d3.select(e).append("svg").attr("width",r.w).attr("height",r.h).append("g");var f;for(var l=0;l<r.levels;l++){var c=r.factor*u*((l+1)/r.levels);a.selectAll(".levels").data(s).enter().append("svg:line").attr("x1",function(e,t){return c*(1-r.factor*Math.sin(t*r.radians/o))}).attr("y1",function(e,t){return c*(1-r.factor*Math.cos(t*r.radians/o))}).attr("x2",function(e,t){return c*(1-r.factor*Math.sin((t+1)*r.radians/o))}).attr("y2",function(e,t){return c*(1-r.factor*Math.cos((t+1)*r.radians/o))}).attr("class","line").style("stroke","grey").style("stroke-width","0.5px").attr("transform","translate("+(r.w/2-c)+", "+(r.h/2-c)+")");}series=0;var h=a.selectAll(".axis").data(s).enter().append("g").attr("class","axis");h.append("line").attr("x1",r.w/2).attr("y1",r.h/2).attr("x2",function(e,t){return r.w/2*(1-r.factor*Math.sin(t*r.radians/o))}).attr("y2",function(e,t){return r.h/2*(1-r.factor*Math.cos(t*r.radians/o))}).attr("class","line").style("stroke","grey").style("stroke-width","1px");h.append("text").attr("class","legend").text(function(e){return e}).style("font-family","sans-serif").style("font-size","10px").attr("transform",function(e,t){return"translate(0, -10)"}).attr("x",function(e,t){return r.w/2*(1-r.factorLegend*Math.sin(t*r.radians/o))-20*Math.sin(t*r.radians/o)}).attr("y",function(e,t){return r.h/2*(1-Math.cos(t*r.radians/o))+20*Math.cos(t*r.radians/o)});t.forEach(function(e,t){dataValues=[];a.selectAll(".nodes").data(e,function(e,t){dataValues.push([r.w/2*(1-parseFloat(Math.max(e.value,0))/r.maxValue*r.factor*Math.sin(t*r.radians/o)),r.h/2*(1-parseFloat(Math.max(e.value,0))/r.maxValue*r.factor*Math.cos(t*r.radians/o))])});dataValues.push(dataValues[0]);a.selectAll(".area").data([dataValues]).enter().append("polygon").attr("class","radar-chart-serie"+series).style("stroke-width","2px").style("stroke",r.color(series)).attr("points",function(e){var t="";for(var n=0;n<e.length;n++){t=t+e[n][0]+","+e[n][1]+" "}return t}).style("fill",function(e,t){return r.color(series)}).style("fill-opacity",r.opacityArea).on("mouseover",function(e){z="polygon."+d3.select(this).attr("class");a.selectAll("polygon").transition(200).style("fill-opacity",.1);a.selectAll(z).transition(200).style("fill-opacity",.7)}).on("mouseout",function(){a.selectAll("polygon").transition(200).style("fill-opacity",r.opacityArea)});series++});series=0;t.forEach(function(e,t){a.selectAll(".nodes").data(e).enter().append("svg:circle").attr("class","radar-chart-serie"+series).attr("r",r.radius).attr("alt",function(e){return Math.max(e.value,0)}).attr("cx",function(e,t){dataValues.push([r.w/2*(1-parseFloat(Math.max(e.value,0))/r.maxValue*r.factor*Math.sin(t*r.radians/o)),r.h/2*(1-parseFloat(Math.max(e.value,0))/r.maxValue*r.factor*Math.cos(t*r.radians/o))]);return r.w/2*(1-Math.max(e.value,0)/r.maxValue*r.factor*Math.sin(t*r.radians/o))}).attr("cy",function(e,t){return r.h/2*(1-Math.max(e.value,0)/r.maxValue*r.factor*Math.cos(t*r.radians/o))}).attr("data-id",function(e){return e.axis}).style("fill",r.color(series)).style("fill-opacity",.9).on("mouseover",function(e){newX=parseFloat(d3.select(this).attr("cx"))-10;newY=parseFloat(d3.select(this).attr("cy"))-5;f.attr("x",newX).attr("y",newY).text(e.value).transition(200).style("opacity",1);z="polygon."+d3.select(this).attr("class");a.selectAll("polygon").transition(200).style("fill-opacity",.1);a.selectAll(z).transition(200).style("fill-opacity",.7)}).on("mouseout",function(){f.transition(200).style("opacity",0);a.selectAll("polygon").transition(200).style("fill-opacity",r.opacityArea)}).append("svg:title").text(function(e){return Math.max(e.value,0)});series++});f=a.append("text").style("opacity",0).style("font-family","sans-serif").style("font-size",13)}}