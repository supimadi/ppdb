$(document).ready(() => {

    function shuffle(a) {
        var j, x, i;
        for (i = a.length - 1; i > 0; i--) {
            j = Math.floor(Math.random() * (i + 1));
            x = a[i];
            a[i] = a[j];
            a[j] = x;
        }
        return a;
    }

    let answer = [];
    $(".card .answer").each(function() {
        answer.push($(this).attr('id'));
    });

    for (let a = 0; a < answer.length; a++) {
        let examPk = answer[a].split('-')[0];
        let answerPk = answer[a].split('-')[2];
        $.ajax({
            url: `/exam/${examPk}/taken/${answerPk}/`,
            method: "GET",
            async: true,
            beforeSend: () => {
                $(`#${answer[a]}`).html(`<div class="m-auto"><span class="spinner-border spinner-border-lg text-danger" role="status" aria-hidden="true"></span></div>`)
            },
            success: (data) => {
                $(`#${answer[a]}`).html(data);


                $("#answer-form").change(() => {
                    $.ajax({
                        url: `/exam/${examPk}/taken/${answerPk}/`,
                        type: "POST",
                        data: $("#answer-form").serialize(),
                        dataType: 'json',
                        success: () => {
                            console.log('Success');
                        },
                    });
                    return false;
                });
            },
        });
    }



});