class UI {
    toggleFilter() {

        var filter = document.querySelector('#site')
        if (window.location.href.includes("jobs")) {

            //ENABLE THE FILTER FUNCTIONALITY IF THE JOBS ARE RENDERED
            console.log("Jobs rendered!");
            filter.disabled = false
        } else {

            console.log("Jobs not yet rendered!");
            filter.disabled = true
        }
    }

    careers24Issue() {
        var c24 = $('.CAREERS24');
        //c24.removeAttr('target');
        //c24.removeClass('btn btn-sm btn-block btn-outline-secondary')
        //c24.text(c24.attr('href'))
        //c24.attr("href", "")
        var a = $(c24.find('a')[0])
        c24.html(`<div class="card plinkcard"><div class="card-body"><p class="plink">${a.attr('href')}</p>
        <button class="btn cp-btn btn-sm btn-outline-secondary">Copy</button>
        </div></div>`)
            /*
        c24.click(e => {
            var url = e.target.value;
            url.select();
            url.setSelectionRange(0, 99999);

            document.execCommand("copy")
            alert("Url copied! Paste it on a new tab and hit enter!")
        })
*/



    }


}


class Functionality {

    copyToClipboard(element) {
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($(element).text()).select();
        //$temp.setSelectionRange(0, 99999);
        document.execCommand("copy");
        alert("Url copied! Paste it on a new tab and hit enter!")
        $temp.remove();
    }

}
$(document).ready(() => {
    //$(".full_desc").fadeOut()

    if (window.innerWidth <= 540) {
        $('#full-desc').hide()
    }

    var ui = new UI()
    ui.toggleFilter()
    ui.careers24Issue()

    var functionality = new Functionality()


    function copy() {

        //COPY URL TO CLIPBOARD ON BUTTON CLICK
        var btn = $('.cp-btn')
        var plinkcard = btn.parent()


        //console.log(url);
        btn.click(e => {
            var url = $(e.target).siblings()[0];
            functionality.copyToClipboard(url)

        })
    }
    copy()

    $('#loc').click(e => {
        //$(e.target).hide()
        var parentDiv = $(e.target.parentElement)
        if (parentDiv.hasClass('bt')) {
            parentDiv.removeClass('bt')

            $(e.target.parentElement).html('<input class="form-control" type="text" placeholder="Type a location">')
        }
    })


    var options = document.querySelector('#site').options;

    $('select').change(ev => {

        for (let i = 0; i < options.length; i++) {
            var val = options[i].value
            $(`.${val}`).hide()
            if (val.toLowerCase() == ev.target.value.toLowerCase()) {
                $(`.${val}`).show()
                console.log(val);
            } else if (ev.target.value == "All") {
                $('.job').show()
            }
        }

        console.log(ev.target.value);
    })



})