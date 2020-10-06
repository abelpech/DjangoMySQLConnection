from django.shortcuts import render
import random
# Create your views here.

def index(request):
    r = random.randint(1,10)
    context = {
        "message":"This better work",
        "variable": r * 5
    }
    return render(request, "reportes/index.html", context)

#def reporte1(request):
#    from django.db import connection
#    with connection.cursor() as cursor:
#        cursor.execute("select * from reportes_usuarios")
#        #cursor.callproc('Read_Users')
#        rawData = cursor.fetchall()
#        result = []
#        for r in rawData:
#            result.append(list(r))
#        contexto = {'lista': result}
#       cursor.close()
#    return render(request, "reportes/consulta.html", contexto)

def reporte1(request):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.callproc( "Reporte1")
        Data = cursor.fetchall()
        result = []
        for r in Data:
            result.append(list(r))
        contexto = {
            'lista': result
        }
        cursor.close()
    return render(request, "reportes/reporte1.html", contexto)