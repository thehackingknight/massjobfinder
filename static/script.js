$(document).ready(()=>{
    //$(".full_desc").fadeOut()

    if (window.innerWidth <= 540){
        $('#full-desc').hide()
    }
    $('body').click(e=>{

        var el = $(e.target)
        var par = $(e.target).parents()[0]

       if(par.id !== "loc") {
        if ($('#loc').hasClass('bt') != true){
            $('#loc').addClass('bt')
            $('#loc').html(`<a class="btn btn-outline-secondary" id="loc-btn">
            Location
          </a>`)
            }
       }
    })
   $('#loc').click(e=>{
        //$(e.target).hide()
        var parentDiv = $(e.target.parentElement)
        if (parentDiv.hasClass('bt')){
            parentDiv.removeClass('bt')
            
        $(e.target.parentElement).html('<input class="form-control" type="text" placeholder="Type a location">')
        }
    })

    
    $(".more-form").submit(e=>{
        e.preventDefault();

        var parent = $(e.target).parents(".desc")[0]
       
        //console.log(e.target)
        if ($(e.target).hasClass("more")) {
            $(e.target).addClass('less')
            $(e.target).removeClass('more')

            //$(meta).hide()

            var url = e.target.more.id
            var data = {url, site : e.target.dataset.url}
            $("#full-desc div").html("<p class='center mt-100 loading'>Loading...</p>")
            $.ajax({

                url: "/jobs",
                type: "POST",
                contentType: "application/json",
                data : JSON.stringify(data),
                success: function(res){
                    console.log(res)
                    $("#full-desc div").html(res)

                    //Untoogle other buttons
                    
                    if ($(".show-more").hasClass("btn-secondary")) {
                        $(".show-more").val("More")
                        $(".show-more").removeClass("btn-secondary")
                        $(".show-more").addClass("btn-outline-secondary")
                        $(".more-form").removeClass('less')
                        $(".more-form").addClass('more')

                    }

                    $(e.target.more).val("Less")
                    $(e.target.more).addClass("btn-secondary")
                    $(e.target.more).removeClass("btn-outline-secondary")
                },

                error: function(err){
                    console.log(err)
                }

            })
        }

        else if ($(e.target).hasClass("less")) {


            $(e.target).removeClass('less')
            $(e.target).addClass('more')
            $(e.target.more).val("More")
            $(e.target.more).removeClass("btn-secondary")
            $(e.target.more).addClass("btn-outline-secondary")
            $("#full-desc div").html("")
            //$(meta).show()
        }


       


    })

var options = document.querySelector('#site').options;

    $('select').change(ev=>{

        for (let i = 0; i < options.length; i++) {
            var val = options[i].value 
            $(`.${val}`).hide()
            if (val.toLowerCase() == ev.target.value.toLowerCase()) {
                $(`.${val}`).show()
                console.log(val);
            }
        }

        console.log(ev.target.value);
    })

})

