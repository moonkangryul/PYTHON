from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp02.models import Board
import math
from django.db.models import Q
from django.http.response import JsonResponse, HttpResponse
import urllib.parse
from django.core.paginator import Paginator
from myapp02.models import Comments

UPLOAD_DIR = 'C:\\PYTHONWORK\\jango\\upload'

# Create your views here.
def index(request):
    return render(request,'base.html')

    #write_form
def write_form(request):
    return render(request,'board/insert.html')


#insert
@csrf_exempt
def insert(request):
    fname = ''
    fsize = 0
    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s'%(UPLOAD_DIR,fname),'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    dto = Board(writer=request.POST['writer'],
                title=request.POST['title'],
                content=request.POST['content'],
                filename= fname,
                filesize= fsize
    )    
    dto.save()
    return redirect('/base')

def list_page(request):
    page = request.GET.get('page',1)
    word = request.GET.get('word','')

    boardCount = Board.objects.filter(Q(writer__contains=word)|
                                      Q(title__contains=word)|
                                      Q(content__contains=word)).count()
    boardList = Board.objects.filter(Q(writer__contains=word)|
                                      Q(title__contains=word)|
                                      Q(content__contains=word)).order_by('-idx')

    pageSize = 5

    #페이징 처리
    paginator = Paginator(boardList,pageSize)
    page_obj = paginator.get_page(page)
    print(boardCount)

    context={'page_list':page_obj,
             'page':page,
             'word':word,
             'boardCount':boardCount}

    return render(request, 'board/list_page.html',context)

def list(request):
    page = request.GET.get('page',1)
    word = request.GET.get('word','')
    field = request.GET.get('field', 'title')

    if field =='all':
        boardCount=Board.objects.filter(Q(writer__contains=word)|Q(title__contains=word)|Q(content__contains=word)).count()
    elif field == 'writer':
        boardCount=Board.objects.filter(Q(writer__contains=word)).count()
    elif field =='title':
        boardCount=Board.objects.filter(Q(title__contains=word)).count()
    elif field == 'content':
        boardCount=Board.objects.filter(Q(content__contains=word)).count()
    else:
        boardCount=Board.objects.all().count()

    pageSize= 5 # 한 화면에 게시글 수
    blockPage = 3 # 보이는 페이지 수
    currentPage = int(page)
    #게시글 수 32 : pagesize:5
    start=(currentPage-1)*pageSize
    totPage =  math.ceil(boardCount/pageSize)# 게시글의 전체 페이지 수
    startPage = math.floor((currentPage - 1)/blockPage)*blockPage + 1
    endPage = startPage + blockPage -1
    
    if endPage > totPage :
        endPage = totPage # endPage = 7
    
    if field == 'all':
        boardList=Board.objects.filter(Q(writer__contains=word)|Q(title__contains=word)|Q(content__contains=word)).order_by('-idx')[start:start+pageSize]
    elif field == 'writer':
        boardList=Board.objects.filter(Q(writer__contains=word)).order_by('-idx')[start:start+pageSize]
    elif field == 'title':
        boardList=Board.objects.filter(Q(title__contains=word)).order_by('-idx')[start:start+pageSize]
    elif field == 'content':
        boardList=Board.objects.filter(Q(content__contains=word)).order_by('-idx')[start:start+pageSize]
    else:
        boardList=Board.objects.all().order_by('-idx')[start:start+pageSize]
    
    context={'boardList':boardList,
             'startPage':startPage,
             'blockPage':blockPage,
             'endPage':endPage,
             'totPage':totPage,
             'boardCount':boardCount,
             'currentPage':currentPage,
             'field':field,
             'word':word,
             'range':range(startPage, endPage+1)}
    return render(request,'board/list.html',context)


    #다운로드 횟수
def download_count(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    dto.down_up()
    dto.save()
    count = dto.down
    return JsonResponse({'idx': id, 'count': count})

#다운로드
def download(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    path = UPLOAD_DIR+dto.filename
    filename = urllib.parse.quote(dto.filename)

    with open(path,'rb') as file:
        response = HttpResponse(file.read(),
        content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment;filename*=UTF-8''{0}'.format(filename)
    return response

def detail(request,board_idx):
    dto = Board.objects.get(idx = board_idx)
    dto.hit_up()
    dto.save()
    
    # commentList= Comments.objects.filter(board_idx=board_idx).order_by('-idx')

    return render(request,'board/detail.html',{'dto': dto})
