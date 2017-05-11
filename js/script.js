$('.img_class').click(function(){
   $("#head_div").animate({width:280}, 2000);
   $.ajax({
   	url: "google.kg/feed"
   	success: function(msg){
   		$('#head_div').text=msg['content']
   	}
   })
}) 
