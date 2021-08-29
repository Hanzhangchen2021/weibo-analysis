<div align="left">
    
 </div>

# Weibo Search & Weibo text Analysis and Visualization
AB26477<br>
King's College, London Master Graduation thesis
## Weibo Search ##
The search section uses the code of chen (2021)<br>

Chen. 2021. GitHub -dataabc/weibo-search. [online] Available at: <https://github.com/dataabc/weibo-search> [Accessed 30 July 2021].

###  Function
Continuously obtain one or more * * Weibo keyword search * * results, and write the results to the file (optional), database (optional), and so on. The so-called Weibo keyword search is: * * search body contains specified keywords Weibo * *, you can specify the time range of the search.<br>

### instructions
All the configuration of this program is completed in the setting.py file, which is located in "weibo-search\weibo\settings.py".

## Output
- Weibo id: the id of the Weibo, in the form of a string of numbers
- Weibo content: Weibo text
- Original picture url: original Weibo picture and url, of the picture in the reason for forwarding on Weibo if there are multiple pictures in a Weibo, each url is separated by an English comma. If there is no picture, the value is''.
- Weibo posting location: location in Weibo
- Weibo release time: Weibo release time, accurate to days
- Number of likes: the number of likes on Weibo
- Number of retweets: number of Weibo retweets
- Number of comments: number of comments on Weibo
- Weibo publishing tools: Weibo publishing tools, such as iPhone client, HUAWEI Mate 20 Pro, etc. If not, the value is''.
- Topic: Weibo topic, that is, the content in two #. If there are multiple topics, each url is separated by an English comma. If not, the value is''.
- Result file: Save it in the folder named by the keyword under the "Result File" folder in the current directory
- Weibo pictures: pictures in Weibo, saved in the images folder under the keyword folder


### Set up cookie
DEFAULT_REQUEST_HEADERS中的cookie Is the value we need to fill in，After obtaining it, replace "your cookie" with a real cookie.
### Set search keywords
Modify the KEYWORD_LIST parameter in the setting.py folder.

### Run the program
```bash
$ scrapy crawl search -s JOBDIR=crawls/search
```

### How to get cookie
1.Open it with Chrome <https://passport.weibo.cn/signin/login>；<br>
2.Enter the user name and password of Weibo, and log in, as shown in the figure:
![](https://picture.cognize.me/cognize/github/weibospider/cookie1.png)
After a successful login, you will jump to <https://m.weibo.cn>;<br>
3.Press F12 to open the Chrome developer tool, type in the address bar and jump to<https://weibo.cn>，After the jump, a similar interface is displayed as follows:
4.Click weibo.cn- > Headers- > Request Headers, "Cookie:" in Network- > Name in the Chrome developer tool, and the value is the cookie value we are looking for. Just copy it, as shown in the figure:
![](https://picture.cognize.me/cognize/github/weibospider/cookie3.png)



## Weibo text Analysis and Visualization ##

### 1.  Data preprocessing

1. **prepro.pyy**


2. **zh_wiki.py、langconv.py**  

   These two py files are used to convert traditional Chinese into simplified ones without modification.

### 2.  Data analysis and visualization

1. **Word cloud：wc.py**（Need to finish running prepro.py）

 <div>
       <img
   src='/Users/chz/Downloads/weibo-analysis-main/weibo_analysis_and_visualization/images/img_1.png'         
            >
   </div>

   

2. **Heat map：** **map.py**（Need to finish running prepro.py）


   <div>
       <img
   src='/Users/chz/Downloads/weibo-analysis-main/weibo_analysis_and_visualization/images/img.png'         
            >
   </div>

 