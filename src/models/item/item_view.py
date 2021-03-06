from flask import Blueprint, render_template, json, request, redirect, jsonify
from bson.json_util import dumps

from src.main import socketio
from src.common.database import Database
from src.models.item.item import Item
from src.models.item.returnedItem import ReturnedItem
from datetime import datetime

import sendgrid, os
from sendgrid.helpers.mail import *

import src.models.user.decorators as user_decorators

item_bp = Blueprint('lost_and_found', __name__)

@item_bp.route('/', methods=['GET','POST'])
@user_decorators.requires_login
def index():
    return render_template('lostAndFound/lostAndFound_home.html', date = dumps(datetime.today().isoformat()))


@item_bp.route('/new/<roomNo>/<itemDesc>/<date>', methods=['GET', 'POST'])
def report_new(roomNo, itemDesc, date):
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    date = datetime.strftime(date, '%Y-%m-%d')
    Item(roomNo, itemDesc, date).insert()
    return redirect('.')


@item_bp.route('/new', methods=['GET', 'POST'])
def add_new_item():
    data = (json.loads(request.data))
    item = data[0]
    id = Item(item['room_number'], item['item_description'], item['date']).insertOne()
    id = id.inserted_id
    socketio.emit('newItemAdded', [dumps(Database.find_one('losts', {"_id": id})), data[1]])
    return jsonify({'text': 'Item was Added Successfully'})


@item_bp.route('/returnItem', methods=['POST'])
def return_item():
    data = (json.loads(request.data))
    print(data)
    item = data[0]
    id = item['_id']
    guestName = item['guest_name']
    returnedBy = item['returned_by']
    returnDate = item['return_date']
    comments = item['comments']
    ReturnedItem.createNewReturn(id, guestName, returnedBy, returnDate, comments)
    socketio.emit('returnedItem', [id, data[1]])
    return jsonify({'text': 'Item was Successfully Added To Returned List'})


@item_bp.route('/deleteLostItem', methods=['POST'])
def deleteLostItem():
    data = (json.loads(request.data))
    id = data[0]
    Item.remove(id)
    socketio.emit('deletedLostItem', [id, data[1]])
    return jsonify({'text': 'ITEM DELETED SUCCESSFULLY'})


@item_bp.route('/deleteReturnedItem/<id>', methods=['GET'])
def deleteReturnedItem(id):
    ReturnedItem.remove(id)
    return jsonify({'text': 'ITEM DELETED SUCCESSFULLY'})


@item_bp.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    data = json.loads(request.data)
    Item.update(id, data)
    return redirect('/lostAndFound/')


@socketio.on('updateLostItem')
def handle_update_lost_item(data):
    item = data[0]
    Item.update(item['_id'], item)
    socketio.emit('updatedList', [item, data[1]])


@item_bp.route('/updateItem', methods=['POST'])
def edit_lost():
    data = (json.loads(request.data))
    item = data[0]
    Item.update(item['_id'], item)
    socketio.emit('updatedList', [item, data[1]])
    return jsonify({'text': 'ITEM WAS UPDATED SUCCESSFULLY'})


@item_bp.route('/updateReturnedItem', methods=['POST'])
def edit_returned():
    item = request.json
    ReturnedItem.update(item['_id'], item)
    return jsonify({'text': 'ITEM WAS UPDATED SUCCESSFULLY'})


@item_bp.route('/undoReturn', methods=['POST'])
def undo_return():
    item = request.json
    ReturnedItem.deleteReturn(item['_id'])
    return jsonify({'text': 'Item has been Successfully placed back in Lost & Found'})


@item_bp.route('/email', methods=['POST'])
def email():
    data = request.json
    item = Item.get_by_item_id(data['_id'])
    send_mail(item)
    return jsonify({'text': 'Jennfier has been notified about the request'})


def send_mail(item):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("reservations@northerngrand.ca")
    subject = 'Item Request from Front Desk'
    to_email = Email("housekeeping@northerngrand.ca", "jimmypalelil@gmail.com")
    msg = 'Front Desk has requested the following Item:     ' + \
          'Item Description: ' + item.item_description + \
          '|  Room No.: ' + item.room_number + \
          '|  Date Found: ' + item.date
    content = Content("text/plain", msg)
    mail = Mail(from_email, subject, to_email, content)
    sg.client.mail.send.post(request_body=mail.get())
