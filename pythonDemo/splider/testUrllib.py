import urllib.request;
import urllib.error;
try:
    headers = {}
    resp =urllib.request.Request('http://python.org/',headers=headers);
    html = urllib.request.urlopen(resp);
    result = html.read().decode("utf-8");
    # result = resp.info();
except urllib.error.URLError as e:
    if hasattr(e,'reason'):
        print('错误原因是',str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e,'code'):
        print('错误状态码是',str(e.code));
else:
    print("请求成功通过")
    print(result);