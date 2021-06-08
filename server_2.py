from flask import Flask
from flask import request
from flask import json
from flask.json import jsonify

app = Flask(__name__)

@app.route('/read', methods=['GET'])
def read():
    txt = """Aliquam erat volutpat. Suspendisse malesuada, ante at dictum ultrices, augue neque varius sem, non finibus tortor elit sit amet lacus. Donec aliquam cursus magna, non rutrum lorem lacinia sed. Curabitur congue ante nec erat interdum posuere ac nec purus. Nam et leo in odio suscipit cursus. Aliquam lorem nulla, egestas vitae bibendum euismod, pharetra eget est. Donec sed sodales lacus.
            Aliquam molestie elit et lacus mollis volutpat. Curabitur maximus tortor ac tortor luctus venenatis. Nullam ac lorem sed purus vestibulum feugiat. Curabitur vehicula dolor imperdiet sapien venenatis, eu congue velit consequat. Morbi dapibus blandit augue, eget congue tellus consectetur eget. Ut iaculis, magna sit amet dictum posuere, tortor mauris pretium nulla, in eleifend sem augue a mauris. Morbi sit amet turpis ornare, venenatis sapien faucibus, dictum lacus. Duis egestas feugiat ipsum eget euismod. Nunc egestas hendrerit sapien, et interdum nisi. Aliquam vel venenatis massa. Phasellus id nisi aliquam, efficitur augue placerat, gravida turpis.
            In sollicitudin pharetra quam, nec auctor libero commodo vulputate. Mauris orci elit, laoreet sit amet mi nec, luctus commodo urna. Nulla facilisi. Etiam consectetur luctus tincidunt. Praesent elementum lorem laoreet lorem bibendum rutrum. In hac habitasse platea dictumst. Sed in leo purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            In faucibus, nisi posuere molestie porttitor, nunc ligula laoreet augue, et iaculis ligula dui eget lectus. Vivamus pellentesque tortor vel ex dignissim, sit amet fringilla sem scelerisque. Aenean luctus at ante id dignissim. Phasellus sit amet quam leo. In mauris ante, iaculis nec odio et, venenatis congue mi. Cras quis ultricies erat. Suspendisse id maximus neque. Sed a augue lectus. Sed gravida elit augue, ut pretium tortor volutpat quis. Quisque eu ligula lobortis, dapibus quam at, tempus mi.   
            In dictum mi et augue pulvinar, ac dignissim purus pulvinar. Suspendisse ac faucibus quam. In hac habitasse platea dictumst. Integer maximus tempus libero, in laoreet nulla pharetra sed. Aliquam sodales volutpat augue sit amet cursus. Pellentesque vel hendrerit sem. Pellentesque id mollis lorem. Sed pellentesque commodo nisi nec molestie. Aliquam erat volutpat. Aenean suscipit diam vel malesuada convallis. Proin vulputate lectus sed diam placerat, et facilisis felis vulputate. Aliquam erat volutpat. Suspendisse aliquet tempus dictum. Etiam in turpis vel nunc consequat posuere in sollicitudin odio. Nam hendrerit fringilla vulputate."""
    return jsonify({
        'status': True,
        'data': txt,
        'message': 'read succesful'
    })

def start_server():
    app.run(debug=True, port='5002')



if __name__ == "__main__":
    start_server()