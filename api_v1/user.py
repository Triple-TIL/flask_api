from . import api
from flask import request
from flask import jsonify
from models import User, db


@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')

        if not (userid and username and password and re_password):
            return jsonify({'error': 'No arguments'}), 400

        if password != re_password:
            return jsonify({'error': 'Wrong password'}), 400

        user = User()
        user.userid = userid
        user.username = username
        user.password = password

        db.session.add(user)
        db.session.commit()

        return jsonify(), 201

    return jsonify()
