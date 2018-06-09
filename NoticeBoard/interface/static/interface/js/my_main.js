function editpostermodal(pid, callback) {
      var status;
      $.ajax({
            url: '/ajax/getposterdetails/',
            data: {
            'pid': pid,
            },
            dataType: 'json',
            async: false,
            success: function (data) {
                const p_id = data.poster.id
                if (data.success==1)
                    {
                        vex.dialog.open({
                            message: 'Poster Details',
                            input: `
                                    <div style="margin: 3vw;">
                                        <label for="filename">ID</label>
                                        <input class="full-width" type="text" placeholder="`+ p_id +`" name="id" readonly>
                                    </div>
                                    <div style="margin: 3vw;">
                                        <label for="filename">Filename</label>
                                        <input class="full-width" type="text" value="`+ data.poster.name +`" name="filename">
                                    </div>
                                    <div style="margin: 3vw;">
                                        <label for="filename">Creation Timestamp</label>
                                        <input class="full-width" type="text" placeholder="`+ data.poster.created_at +`" name="creationdate" readonly>
                                    </div>
                                    <div style="margin: 3vw;">
                                        <label for="filename">Currently Displaying</label>
                                        <input type="checkbox" class="switch_1" `+ ((data.poster.show)?'checked':'') +` name="show">
                                    </div>
                                    <div style="margin-left: 3vw;margin-bottom: 5vw;">
                                        <label for="filename">Delete</label>
                                        <input class="btn--danger" onclick="javascript:deleteposter(`+ p_id +`,reloadpage)" type="button" value="Delete" `+ ((data.poster.show)?'checked':'') +` name="show">
                                    </div>
                                    `,
                            buttons: [
                                $.extend({}, vex.dialog.buttons.YES, { text: 'Update' }),
                                $.extend({}, vex.dialog.buttons.NO, { text: 'Back' })
                            ],
                            callback: function (data) {
                                if (!data) {
                                    console.log('Cancelled')
                                } else {
                                    $.ajax({
                                        url: '/ajax/updateposter/',
                                        data: {
                                            'id': p_id,
                                            'data': data,
                                        },
                                        dataType: 'json',
                                        async: false,
                                        success: function (data_inner) {
                                            if(data_inner.success==1)
                                                setTimeout(callback(), 1500);
                                        }
                                    });
                                }
                            }
                        });

                    }
                else
                    {
                        vex.dialog.alert('Failed to retrieve data')
                    }
            }
        });
}

function reloadpage(){
    location.reload()
}

function deleteposter(pid,callback){
        $.ajax({
            url: '/ajax/deleteposter/',
            data: {
                'id': pid,
            },
            dataType: 'json',
            async: false,
            success: function (data) {
                if (data.success == 1) {
                    setTimeout(callback(), 1500);
                }

            }
        });
}