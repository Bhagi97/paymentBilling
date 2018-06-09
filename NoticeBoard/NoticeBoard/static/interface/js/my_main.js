function editpostermodal(pid) {
        $.ajax({
            url: '/ajax/getposterdetails/',
            data: {
            'pid': pid,
            },
            dataType: 'json',
            async: false,
            success: function (data) {
                if (data.success==1)
                    {
                        vex.dialog.open({
                            message: 'Poster details:',
                            input: `
                                    <div style="margin: 1vw;">
                                        <label for="filename">ID</label>
                                        <input class="full-width" type="text" value="`+ data.poster.id +`" name="id" readonly>
                                    </div>
                                    <div style="margin: 1vw;">
                                        <label for="filename">Filename</label>
                                        <input class="full-width" type="text" value="`+ data.poster.name +`" name="filename">
                                    </div>
                                    <div style="margin: 1vw;">
                                        <label for="filename">Creation Timestamp</label>
                                        <input class="full-width" type="text" placeholder="`+ data.poster.created_at +`" name="creationdate" readonly>
                                    </div>
                                    <div style="margin: 1vw;">
                                        <label for="filename">Currently Displaying</label>
                                        <input type="checkbox" class="switch_1" `+ ((data.poster.show)?'checked':'') +` name="show">
                                    </div>
                                    `,
                            buttons: [
                                $.extend({}, vex.dialog.buttons.YES, { text: 'Login' }),
                                $.extend({}, vex.dialog.buttons.NO, { text: 'Back' })
                            ],
                            callback: function (data) {
                                if (!data) {
                                    console.log('Cancelled')
                                } else {
                                    console.log('Username', data.username, 'Password', data.password)
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
