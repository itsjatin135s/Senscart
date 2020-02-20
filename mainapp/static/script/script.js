
// toggler btn

// $('.navbar-toggler').click(function() {

// 	$('.navbar-toggler').toggleClass('change')
// })


// sticky navbar less paddin

// $(window).scroll(function() {

// 	let position = $(window).scrollTop();

// 	if(position>=824) {
// 		$('navbar').addClass('navbar-background');
// 		$('navbar').addClass('fixed-top');
// 	}else {
// 		$('navbar').removeClass('navbar-background');
// 		$('navbar').removeClass('fixed-top');
// 	}
// })



// smooth scroll

// $('.nav-item a, .header-link, #back-to-top').click(function(link) {

// 	link.preventDefaukt();

// 	let traget = $(this).attr('href');

// 	$('html, body').stop().animate({
// 		scrollTop: $(traget).offset().top - 25
// 	}, 3000);
// })


// back-to-top

// $(window).scroll(function() {

// 	let position = $(this).scrollTop();

// 	if(position>=718) {
// 		$('back-to-top').addClass('scrollTop');
// 	}else {
// 		$('back-to-top').removeClass('scrollTop');
// 	}
// });

// sticky navbar and arrow back to top

window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var back = document.getElementById("back-to-top")
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
    navbar.classList.add("bg-color")
    
  } else if (window.pageYOffset >=418) {
  	back.classList.add("scrollTop")
  	    navbar.classList.remove("sticky");
    navbar.classList.remove("bg-color")
  }else 
  {
    navbar.classList.remove("sticky");
    navbar.classList.remove("bg-color")
    back.classList.remove("scrollTop")

}
}

// $(document).ready(function() {
// 	$(window).scroll(function(){
// 		var position = $(document).scrollTop();
// 		if(position >= 772) {
// 			$('#come-down').addClass()
// 		}
// 		console.log(position);
// 	});
// });
$(document).ready(function(){

	$('#header').ripples({
	  dropRadius: 10,
	  perturbance: 0.10,
	});
});

// // Magnific popup
// $(document).ready(function(){
// $('.parent-container').magnificPopup({
//   delegate: 'a', // child items selector, by clicking on it popup will open
//   type: 'image'
//   // other options
//   gallery:{
//   	enabled:true
//   },
//     type: 'image'
// });


