# Prologue
   This is the notes/codes while taking udacity's backend nano degree. It's a mix of some old materials and looks not so popular. But I do like the style of lecture!

# Build a blog.

## diff between GET and POST in HTTP

1. GET for static contents
    * if you use GET for delete, some web crawler will make things bad.
    they just click your "delete" links lol

    1. good for requests can be cached
    2. fetching a document

2. POST is not cached, normally it updates something

# About google app engine
```
# get sample
git clone https://github.com/GoogleCloudPlatform/python-docs-samples
cd python-docs-samples/appengine/standard/hello_world
# test locally
dev_appserver.py .
# go to https://console.cloud.google.com/project?_ga=1.5984115.1185135686.1463291285
# create a new project or select the existing one
# upload to GoogleCloudPlatform, v1 for a example version name
appcfg.py -A <YOUR_PROJECT_ID> -V v1 update .

```
