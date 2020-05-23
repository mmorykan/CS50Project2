document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', () => {

        document.querySelector('#form').onsubmit = () => {
            
            const content = document.querySelector('#message').value;
            const image = document.querySelector('#file').files[0];
            const reader = new FileReader();

            reader.onload = function() {
                let data = reader.result;
                socket.emit('send message', {'content': content, 'data': data});
            };

            if (image) {
                // Gets the src from an uploaded file
                reader.readAsDataURL(image);
            }
            else {
                socket.emit('send message', {'content': content})
            }

            // reset input fields
            document.querySelector('#message').value = '';
            document.querySelector('#file').value = '';

            // Delete the "no messages" message
            const empty = document.querySelector('#empty');
            if (empty) {
                empty.remove();
            }
            
            return false;
        };
    });

    socket.on('broadcast message', message => {
        const list = document.querySelector('#messages');
        const li = document.createElement('li');
        const img = document.createElement('img');
        const file = message.image;
        let name = message.username;
        name = name.fontcolor('green');
        
        if (message.content.length > 0) {
            li.innerHTML = `From ${name} at ${message.time}: ${message.content}`;
            list.append(li);
            if (file) {
                img.src = file;
                img.width = 200;
                list.append(img);
            }
        }
        
        else if (file) { 
            img.src = file
            img.width = 200;
            li.innerHTML = `From ${name} at ${message.time}: `;
            list.append(li);
            li.appendChild(img);
        }
        
    });
});
