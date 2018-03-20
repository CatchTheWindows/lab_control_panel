from server import handler,run,post
from server import RequestHandler

@handler("index")
def printL(req):
    with open('index.html', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return 200,{"Content-type":"text/html"}, data

@handler("af","POST")
def answerpost(req):
        data1=str(post(req))
        data1=data1[1:]
        data="<head><title>Done</title>"
        if data1!="'yourPassword=1234'":
               data="<center><h1>You're wrong</h1><br/><a href='index'>Back</a></center>"
        else:
              with open('after.html', 'r') as myfile:
                   data=myfile.read().replace('\n', '')
        return 200,{"Content-type":"text/html"}, data


@handler("abc","POST")
def answerpost1(req):
     with open('info.html', 'r') as myfile:
             data=myfile.read().replace('\n', '')
     return 200,{"Content-type":"text/html"}, data
run()