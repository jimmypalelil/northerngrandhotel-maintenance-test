from flask import Blueprint
from bson.json_util import dumps

from src.main import socketio
from src.models.chat.chat import Chat

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/getInitialMsgs', methods=['GET', 'POST'])
def get_initial_msgs():
    msgs = Chat.get_chats_by_number(50)
    return dumps(msgs)


@socketio.on('newMsg')
def handle_new_msg(chat):
    to_email = chat['to_email']
    from_email = chat['from_email']
    msg = chat['msg']
    date = chat['date']
    id = Chat(to_email,from_email,msg,date).insert_chat()
    chat['_id'] = id
    socketio.emit('newMsg', chat)


@socketio.on('deleteMsg')
def handle_del_msg(data):
    _id = data['_id']
    email = data['email']
    Chat.remove_msg(_id)
    socketio.emit('deletedMsg', {'_id': _id, 'email': email})
