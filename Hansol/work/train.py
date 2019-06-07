import gensim

# --------------------------------------------
#           word2vec
# --------------------------------------------
# w2v_thermalPaperList(688)
# w2v_1970s w2v_1980s w2v_1990s w2v_2000s w2v_2010s
# w2v_F_2000_2004s w2v_F_2005_2009s w2v_F_2010_2014s w2v_F_2015_2017s w2v_F_2014_2017s
# w2v_thermalPaperList_2000sAfter
# w2v_A24 w2v_A45 w2v_A47 w2v_A61 w2v_A62 w2v_A63 w2v_All_p
# --------------------------------------------
model = gensim.models.Word2Vec.load('/Users/atec/Desktop/hansol_crawling/model/w2v_thermalPaperList(688)'
                                    '.model')
most_silmilar_word = model.most_similar(positive=['thermal/JJ','paper/NN'], topn=500)
print(most_silmilar_word) #단어와 가장 가까운 단어
# 'recording/VBG', 'writing/VBG', 'printing/VBG'
# 'thermal/JJ','paper/NN'

arr ="roll/NN,feeding/NN,sheet/NN,conveyance/NN,feed/NN,feed/VBN,path/NN,sandwich/NN,front/JJ,head/NN,fee/VB," \
     "first/JJ,transfer/NN,platen/NN,ribbon/NN,mechanism/NN,conveyed/JJ,put/VBD,double-sided/JJ,second/JJ,press/NN,path/VBD,bring/VBG,arm/NN,section/NN,respect/NN,hold/NN,downstream/NN,contact/VB,elastic/JJ,position/NN,frame/NN,upstream/JJ,print/NN,reach/NN,arrange/NN,send/NN,dispose/NN,support/VBD,line/NN,lock/NN,rotates/NNS,gear/NN,mean/NN,mount/NN,motor/NN,spring/NN,jet/NN,roller/NN,cjpoinpit/NN,force/NN,psolution/NN,platen/JJ,state/NN,set/NN,bias/NN,swing/NN,main/JJ,shaft/NN,face/NN,oppose/JJ,counter-pressure/JJ,direction/NN,p/NN,contact/NN,member/NN,driven/JJ,cool/VB,feed/JJ,hold/VBN,move/NN,equip/VBN,detect/VB,print/VBN,urging/JJ,body/NN,simplex/JJ,printing/NN,frame/JJ,side/NN,draw/VBN,mount/VBN,scanning/JJ,configure/NN,close/JJ,printhead/NN,door/NN,planet/NN,rear/JJ,one-side/JJ,bearing/NN,housing/NN,rotate/NN,cut/VBD,job/NN,guide/NN,sensor/NN,perpendicular/NN,performs/NNS,opposite/NN,join/NN,flexible/JJ,plain/JJ,feed/VBD,support/VB,rotatable/JJ,rotation/NN,closed/JJ,press/VB,front/NN,cassette/NN,back/JJ,come/NN,start/VBN,pressing/JJ,gear/JJ,drive/NN,tension/NN,direct/JJ,unit/NN,control/VB,set/VBN,same/JJ,house/NN,follow/JJ,lie/NN,move/VBN,push/VBN,tip/NN,open/JJ,dispose/VBN,carriage/NN,fixed/JJ,attachment/JJ,counter-pressure/NN,take-up/JJ,sub-scanning/JJ,precise/JJ,arrange/VBN,bring/VB,comprise/NN,duplicate/NN,wind/VBN,locked/JJ,annular/JJ,relationship/NN,pcopyright/NN,transport/NN,carry/VBN,superpose/VBN,move/VB,double-side/JJ,erase/NN,original/JJ,pressure/NN,plain/VB,rotary/JJ,movement/NN,scanning/NN,linear/JJ,closing/NN,fan/NN,scan/JJ,print/VB,path/JJ,device/NN,type/NN,free/JJ,holder/NN,printer/NN,hold/VB,rate/NN,receive/VBN,heat-sensitive/JJ,rack/NN,load/NN,therebetween/NN,convey/NN,mark/NN,erasure/NN,disperse/JJ,attach/VBN,applies/NNS,d/NN,cartridge/NN,perform/VBN,other/JJ,downward/JJ,sensor/VBD,next/JJ,pressing/NN,lid/JJ,face/VB,release/VB,transmission/NN,core/NN,cjpoinpit/NN,turn/VB,ejection/NN,take/VB,stop/VBN,mode/NN,vertical/JJ,side/JJ,upward/JJ,scroll/NN,residual/JJ,d/NN,cover/NN,printing/JJ,energize/VB,flange/NN,print/JJ,finish/JJ,outer/NN,come/VBN,insert/NN,relative/NN,linearly/JJ,send/VBN,different/JJ,stencil/JJ,center/NN,operating/NN,angle/NN,accord/NN,ink/NN,step/NN,horizontal/JJ,assembly/NN,control/VBN,brake/NN,convey/VB,driving/NN,integral/JJ,slide/NN,manual/JJ,constitution/NN,reliability/NN,mounting/NN,home/NN,insert/VBN,attachable/JJ,drive/JJ,rotate/VBN,send/VB,stop/JJ,surface/JJ,outside/JJ,manner/NN,supply/NN,sticking/NN,setting/NN,distance/NN,outlet/NN,release/VBN,wound/NN,determine/VBN,determine/NN,printing/VBG,space/NN,medium/NN,interleave/JJ,speed/NN,notch/NN,act/NN,axis/NN,adjust/VB,receipt/NN,complete/JJ,supply/VBN,stopper/NN,wind/NN,detect/NN,store/NN,bankbook/NN,heat/VB,detachable/JJ,controller/NN,module/NN,discharge/VB,start/NN,width/NN,timing/NN,permit/NN,back/NN,thermal/VB,stocker/NN,load/VBN,passage/NN,procedure/NN,project/NN,prepare/VB,separate/JJ,extent/NN,repeat/NN,finish/NN,precede/NN,column/NN,appropriate/JJ,discharge/NN,data/NN,cut/VBN,interval/JJ,back-adhesive/JJ,jig/NN,d/NN,delivery/NN,cutter/NN,test/NN,convey/JJ,parallel/NN,fold/JJ,operator/NN,receive/VB,opening/NN,operation/NN,rubber/NN,ccd/NN,engage/NN,plain/NN,length/NN,lever/NN,row/NN,compact/JJ,energization/NN,attach/NN,single-side/JJ,button/NN,polygonal/JJ,inputted/VBN,integrate/JJ,damage/NN,shift/NN,be/VB,contacted/JJ,engage/JJ,conveying/NN,switch/VBN,movable/JJ,touch/NN,display/NN,diameter/NN,fee/NN,place/NN,bring/NN,easy/JJ,predetermine/JJ,actuator/NN,transmit/NN,reading/VBG,reverse/JJ,set/VBD,internal/JJ,detect/VBN,hole/NN,constitutionthermal/JJ,non-adhesive/JJ,subject/JJ,margin/NN,thereby/NN,right/JJ,feeder/NN,sublimation/NN,basis/NN,cjpoinpit/NN,detect/JJ,touch/JJ,set/VB,relative/JJ,pass/VBN,constitutionthe/NN,pen/JJ,switch/NN,carry/JJ,inner/JJ,bracket/NN,switching/NN,arrow/NN,dot/JJ,block/NN,"
result = arr.split(',')
for word in result:
    try:
        count = model.wv.vocab[word].count
    except:
        count = 0
    print(word, count)
