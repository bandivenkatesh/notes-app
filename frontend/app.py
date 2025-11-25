#!/usr/bin/env python3
from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json
import uuid
import datetime

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, 'notes.json')
USERS_FILE = os.path.join(BASE_DIR, 'users.json')


def load_notes():
	try:
		with open(DATA_FILE, 'r', encoding='utf-8') as f:
			return json.load(f)
	except FileNotFoundError:
		return []
	except json.JSONDecodeError:
		return []


def load_users():
	try:
		with open(USERS_FILE, 'r', encoding='utf-8') as f:
			return json.load(f)
	except FileNotFoundError:
		return []
	except json.JSONDecodeError:
		return []


def save_users(users):
	with open(USERS_FILE, 'w', encoding='utf-8') as f:
		json.dump(users, f, ensure_ascii=False, indent=2)


def save_notes(notes):
	with open(DATA_FILE, 'w', encoding='utf-8') as f:
		json.dump(notes, f, ensure_ascii=False, indent=2)


app = Flask(__name__, static_folder='static', template_folder='templates')
# simple secret for session signing; set FLASK_SECRET in env for production
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret-change-me')


@app.route('/')
def index():
	return render_template('landing.html')


@app.route('/app')
def notes_page():
	if not session.get('user'):
		return redirect(url_for('login'))
	return render_template('notes.html')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/register')
def register():
	return render_template('register.html')


@app.route('/api/notes', methods=['GET'])
def get_notes():
	return jsonify(load_notes())


@app.route('/api/notes', methods=['POST'])
def create_note():
	data = request.get_json() or {}
	title = (data.get('title') or '').strip()
	content = (data.get('content') or '').strip()
	if not (title or content):
		return jsonify({'error': 'title or content required'}), 400
	note = {
		'id': uuid.uuid4().hex,
		'title': title,
		'content': content,
		'created_at': datetime.datetime.utcnow().isoformat() + 'Z'
	}
	notes = load_notes()
	notes.insert(0, note)
	save_notes(notes)
	return jsonify(note), 201


@app.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
	notes = load_notes()
	new = [n for n in notes if n.get('id') != note_id]
	if len(new) == len(notes):
		return jsonify({'error': 'not found'}), 404
	save_notes(new)
	return ('', 204)


@app.route('/api/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
	data = request.get_json() or {}
	notes = load_notes()
	for n in notes:
		if n.get('id') == note_id:
			n['title'] = data.get('title', n.get('title', ''))
			n['content'] = data.get('content', n.get('content', ''))
			n['updated_at'] = datetime.datetime.utcnow().isoformat() + 'Z'
			save_notes(notes)
			return jsonify(n)
	return jsonify({'error': 'not found'}), 404


# --- Auth API ---
@app.route('/api/register', methods=['POST'])
def api_register():
	data = request.get_json() or {}
	username = (data.get('username') or '').strip()
	password = (data.get('password') or '')
	if not username or not password:
		return jsonify({'error': 'username and password required'}), 400
	users = load_users()
	if any(u.get('username') == username for u in users):
		return jsonify({'error': 'username taken'}), 400
	user = {
		'username': username,
		'password_hash': generate_password_hash(password),
		'created_at': datetime.datetime.utcnow().isoformat() + 'Z'
	}
	users.append(user)
	save_users(users)
	session['user'] = username
	return jsonify({'username': username}), 201


@app.route('/api/login', methods=['POST'])
def api_login():
	data = request.get_json() or {}
	username = (data.get('username') or '').strip()
	password = (data.get('password') or '')
	users = load_users()
	for u in users:
		if u.get('username') == username and check_password_hash(u.get('password_hash', ''), password):
			session['user'] = username
			return jsonify({'username': username})
	return jsonify({'error': 'invalid credentials'}), 401


@app.route('/api/logout', methods=['POST'])
def api_logout():
	session.pop('user', None)
	return ('', 204)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)