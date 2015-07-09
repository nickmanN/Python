from flask import Flask, url_for, request, render_template;
from app import app;
import redis;

@app.route('/')
def home():
	#Connect to redis data store
	r = redis.StrictRedis(host='localhost', port=6379, db=0);

	return render_template("index.html");