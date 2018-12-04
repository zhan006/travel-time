function record(output){
var recorded=document.getElementById('record');
recorded.innerHTML=output
}
var json=(function(){var json=null;
$.ajax({'async':false,'global':false,'url':'./baidumap.json','dataType':"json",'success':function(data){json=data;}});
return json;
}
)();
console.log(json)
function addAvechart(){
$("#ave").append('<svg width='+json['Monday'][0]*3+' height=60></svg>')
$("#ave").append('<svg width='+json['Tuesday'][0]*3+' height=60></svg>')
$("#ave").append('<svg width='+json['Wednesday'][0]*3+' height=60></svg>')
$("#ave").append('<svg width='+json['Thursday'][0]*3+' height=60></svg>')
$("#ave").append('<svg width='+json['Friday'][0]*3+' height=60></svg>')
$("#ave").append('<svg width='+json['Saturday'][0]*3+' height=60></svg>')
$("#ave").append('<svg width='+json['Sunday'][0]*3+' height=60></svg>')
}
function addAvemark(){
$(".avemarks").append('<p id="avemarks" style="left:'+json['Monday'][0]*2.5+'px"><b>'+json['Monday'][0]+'</b></p>')
$(".avemarks").append('<p id="avemarks" style="left:'+json['Tuesday'][0]*2.5+'px"><b>'+json['Tuesday'][0]+'</b></p>')
$(".avemarks").append('<p id="avemarks" style="left:'+json['Wednesday'][0]*2.5+'px"><b>'+json['Wednesday'][0]+'</b></p>')
$(".avemarks").append('<p id="avemarks" style="left:'+json['Thursday'][0]*2.5+'px"><b>'+json['Thursday'][0]+'</b></p>')
$(".avemarks").append('<p id="avemarks" style="left:'+json['Friday'][0]*2.5+'px"><b>'+json['Friday'][0]+'</b></p>')
$(".avemarks").append('<p id="avemarks" style="left:'+json['Saturday'][0]*2.5+'px"><b>'+json['Saturday'][0]+'</b></p>')
$(".avemarks").append('<p id="avemarks" style="left:'+json['Sunday'][0]*2.5+'px"><b>'+json['Sunday'][0]+'</b></p>')
}
function addPeakchart(){
$("#peak").append('<svg width='+json['Monday'][1]*3+' height=60></svg>')
$("#peak").append('<svg width='+json['Tuesday'][1]*3+' height=60></svg>')
$("#peak").append('<svg width='+json['Wednesday'][1]*3+' height=60></svg>')
$("#peak").append('<svg width='+json['Thursday'][1]*3+' height=60></svg>')
$("#peak").append('<svg width='+json['Friday'][1]*3+' height=60></svg>')
$("#peak").append('<svg width='+json['Saturday'][1]*3+' height=60></svg>')
$("#peak").append('<svg width='+json['Sunday'][1]*3+' height=60></svg>')
}
function addPeakmark(){
$(".peakmarks").append('<p id="peakmarks" style="left:'+json['Monday'][1]*2.5+'px"><b>'+json['Monday'][1]+'</b></p>')
$(".peakmarks").append('<p id="peakmarks" style="left:'+json['Tuesday'][1]*2.5+'px"><b>'+json['Tuesday'][1]+'</b></p>')
$(".peakmarks").append('<p id="peakmarks" style="left:'+json['Wednesday'][1]*2.5+'px"><b>'+json['Wednesday'][1]+'</b></p>')
$(".peakmarks").append('<p id="peakmarks" style="left:'+json['Thursday'][1]*2.5+'px"><b>'+json['Thursday'][1]+'</b></p>')
$(".peakmarks").append('<p id="peakmarks" style="left:'+json['Friday'][1]*2.5+'px"><b>'+json['Friday'][1]+'</b></p>')
$(".peakmarks").append('<p id="peakmarks" style="left:'+json['Saturday'][1]*2.5+'px"><b>'+json['Saturday'][1]+'</b></p>')
$(".peakmarks").append('<p id="peakmarks" style="left:'+json['Sunday'][1]*2.5+'px"><b>'+json['Sunday'][1]+'</b></p>')
}
$(document).ready(function(){addAvechart();addAvemark();addPeakchart();addPeakmark();})