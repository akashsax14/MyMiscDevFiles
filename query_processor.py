# -*- coding: utf-8 -*-
import codecs,sys, random, os, webbrowser

index={}
lexicon={}
query=[]
#Reads Lexicon
with codecs.open('lexicon.txt','r+',encoding='utf-8') as fileo, codecs.open('Index.txt','r+',encoding ='utf-8') as filo:
    for line in fileo:
        line1 = line.strip()
        list2 = line1.split(':')
        ex = list2[0].replace(',','')
        post = list2[1].strip()
        x = post.split()
        lexicon[ex] = [x[0],x[1]]
        query.append(ex)
    # Reads Index
    for line in filo:     
        liner = line.decode('utf-8').strip()
        list1 = liner.split(':')
        key = list1[0].replace(',','')
        a = list1[1].strip()
        index[key] = a
        
def q_process(input_query):
    ''' Takes input query, finds posting list and returns top 20 html pages.
    Opens in webbrowser
    '''
    path ='C://Users//Shaank08//workspace//Final_WSE'
    
    #SET UP Output path for top 20 HTML pages
    if not os.path.exists(path+'//HTML'):
        os.makedirs(path+'//HTML')
    pro = []
    arc_ids=[]
    article_lex = {}
    
    start = int(lexicon[input_query][0])
    end = int(lexicon[input_query][1])
    
    with codecs.open('article_lexicon.txt','r+',encoding = 'utf-8') as fim:
        for line in fim:
            line =  line.strip()
            x = line.split(':')
            key =  int(x[0])
            y = x[1].split()
            start_a = int(y[0])
            end_a = int(y[1])
            article_lex[key] = [start_a,end_a]
    

    with codecs.open('Index.txt','r+',encoding = 'utf-8') as fie:
        fie.seek(start)
        posting = fie.read(end)
        post_list = posting.split()[1:]
        #print 'post list: '
        #print post_list
    
        ##Top K results (10)
        for i in range(0,10):
            k = random.randrange(0,len(post_list))
            if not k in pro:
                pro.append(k)
                arc_ids.append(int(post_list[k]))
         
    num = 0
    with codecs.open('articles.txt','r+',encoding='utf-8') as file_obj:
        for a in arc_ids:
            #print 'a: ' + str(a)
            lex = article_lex[a]
            start_offset = lex[0]
            end_offset = lex[1]
            #print lex
            #print start_offset, end_offset
            file_obj.seek(start_offset)
            content = file_obj.read(end_offset)
            ##
            #print content
            with open(path+'//HTML//'+str(num)+'test.html','w+') as filo:
                filo.write(content)
                num+=1
                
    xp =os.listdir(path+'//HTML//')
    
    ## Open top 20 pages
    #webbrowser.open(path+'//HTML//'+str(xp[0]), 0)
    for filer in xp:
        webbrowser.open_new_tab(path+'//HTML//'+filer)

## Program execution starts here..
for q in query:
    print q
print '\n'

input_query = raw_input('select one query from above..\n')
q_process(input_query)
             
          
        
        
 
    


    
        







