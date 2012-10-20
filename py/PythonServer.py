import urllib2
import json
import re
import cherrypy
from commons.classes.cpjsonResponse import SuccessResp, ErrorResp

class CherryController:
	def index(self):
		return "Hello World"
	index.exposed=True
	
	def multunus(self, **params):
		returnVal = []
		paramsMap = params
		twitterhandle = paramsMap['twitterhandle']
		try:
			url = 'https://api.twitter.com/1/statuses/user_timeline.json?suppress_response_codes&trim_user=true&count=200&screen_name=' + twitterhandle
			resp = urllib2.urlopen(url).read()
			respJ = json.loads(resp)
			sizeArr = []
			for tweet in respJ:
				tweet['text'] = re.sub(' +',' ',tweet['text'])
				sizeArr.append(len(tweet['text'].split(' ')))
			sizeArr.sort()
			returnVal = dict((i,sizeArr.count(i)) for i in sizeArr)
			return str(SuccessResp(None, returnVal))
		except:
			return str(ErrorResp(None, returnVal))
	multunus.exposed = True
	
	
if __name__ == '__main__':
#	cherrypy.config.update({'server.socket_host': '127.0.0.1',
#							'server.socket_port': 8000})
#	cherrypy.quickstart(CherryController())
	cherrypy.config.update({'server.socket_host': '127.0.0.1','server.socket_port': 1008})
	# cherrypy.quickstart(CherryController() , "/rapid")
	cherrypy.tree.mount(CherryController(), '/rapid')
	cherrypy.server.start()