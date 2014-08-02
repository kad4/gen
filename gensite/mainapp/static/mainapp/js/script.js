function ratepost(id,score)
{
	var request=$.ajax({
		url: "/rate/",
		type: "GET",
		data:{id:id,score:score}
	});
}