from webbrowser import get
from django.shortcuts import render ,redirect
from django.views.decorators.csrf import csrf_exempt
from myapp01.models import Board
# Create your views here.
UPLOAD_DIR = 'C:\\PYTHONWORK\\jango\\upload'

#write_form
def write_form(request):
    return render(request,'board/write.html')


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
    return redirect('/list/')

#전체보기
def list(request):
    boardList = Board.objects.all()
    context = {'boardList' : boardList}
    return render(request, 'board/list.html',context)

#상세보기
def detail_idx(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx = id)
    dto.hit_up()
    dto.save()
    return render(request,'board/detail.html',{'dto': dto})

#상세보기(dtail/5)
def detail(request,board_idx):
    dto = Board.objects.get(idx = board_idx)
    dto.hit_up()
    dto.save()
    return render(request,'board/detail.html',{'dto': dto})

def update(request,board_idx):
    dto = Board.objects.get(idx = board_idx)
    return render(request, 'board/update.html',{'dto': dto})

@csrf_exempt
def update_now(request):
    id = request.POST['idx']
    dto = Board.objects.get(idx=id)
    fname = dto.filename
    fsize = dto.filesize
    
    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s'%(UPLOAD_DIR,fname),'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    update_dto = Board(
        id,
        writer=request.POST['writer'],
        title=request.POST['title'],
        content=request.POST['content'],
        filename= fname,
        filesize= fsize
    )    
    update_dto.save()
    return redirect('/list')


def delete(request, board_idx):
    dto=Board.objects.get(idx = board_idx)
    dto.delete()
    return redirect('/list')