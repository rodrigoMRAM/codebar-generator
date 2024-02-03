from django.shortcuts import render

# Create your views here.
import barcode
from io import BytesIO
from barcode import Code39, EAN8, EAN13 , Code128 , EAN14
from .forms import MiFormulario
from barcode.writer import SVGWriter

def index(request):
    return render(request, 'main.html')



# def prueba(request):
    
#         rv = BytesIO()

#         pruea = Code39(str(1), writer=SVGWriter()).write(rv)
#         print(pruea)
#         # conversion = pruea.decode('utf-8')

#         context = {"svg" :pruea}

#         return render(request, 'prueba.html',context )

#FORMAT CODE 39 CODEBAR

def code39(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        print(formulario)
        desde = formulario.cleaned_data['desde']
        hasta = formulario.cleaned_data['hasta']

        rv = BytesIO()
        vacio = []
        for x in range(int(desde), int(hasta)+1):
            pruea = Code39(str(x), writer=SVGWriter()).render(rv)
            conversion = pruea.decode('utf-8')
            vacio.append(conversion)
            # conversion2 = conversion[144:]
        context = {"svg" :vacio}
        # Or to an actual file:
        with open("imagenes/somefile.jpeg", "wb") as f:
            Code39("2", writer=SVGWriter()).write(f)
        return render(request, 'exito.html',context )

    else:
        formulario = MiFormulario()
        return render(request, 'index.html', {'form': formulario})
    


#FORMAT CODE 128 CODEBAR
def code128(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        print(formulario)
        desde = formulario.cleaned_data['desde']
        hasta = formulario.cleaned_data['hasta']

        rv = BytesIO()
        vacio = []
        for x in range(int(desde), int(hasta)+1):
            pruea = Code128(str(x), writer=SVGWriter()).render(rv)
            conversion = pruea.decode('utf-8')
            vacio.append(conversion)
            # conversion2 = conversion[144:]
        context = {"svg" :vacio}
        # Or to an actual file:
        # with open("imagenes/somefile.jpeg", "wb") as f:
        #     Code39("2", writer=SVGWriter()).write(f)
        return render(request, 'exito.html',context )

    else:
        formulario = MiFormulario()
        return render(request, 'index.html', {'form': formulario})
    


#FORMAT EAN 8 CODEBAR
def ean8(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        print(formulario)
        desde = formulario.cleaned_data['desde']
        hasta = formulario.cleaned_data['hasta']

        rv = BytesIO()
        
        # EAN8(str(desde), writer=SVGWriter()).render(rv)
        vacio = []
        for x in range(int(desde), int(hasta)+1):
            ch = str(x).zfill(7)
            print(ch)
            pruea = EAN8(ch, writer=SVGWriter()).render(rv)
            conversion = pruea.decode('utf-8')
            print(conversion)
            vacio.append(conversion)
            # conversion2 = conversion[144:]
        context = {"svg" :vacio}
        # Or to an actual file:
        # with open("imagenes/somefile.jpeg", "wb") as f:
        #     EAN8("2", writer=SVGWriter()).write(f)
        return render(request, 'exito.html',context )

    else:
        formulario = MiFormulario()
        return render(request, 'index.html', {'form': formulario})


#FORMAT CODE 13 CODEBAR
def ean13(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        print(formulario)
        desde = formulario.cleaned_data['desde']
        hasta = formulario.cleaned_data['hasta']

        rv = BytesIO()
        
        # EAN8(str(desde), writer=SVGWriter()).render(rv)
        vacio = []
        for x in range(int(desde), int(hasta)+1):
            ch = str(x).zfill(12)
            print(ch)
            pruea = EAN13(ch, writer=SVGWriter()).render(rv)
            conversion = pruea.decode('utf-8')
            print(conversion)
            vacio.append(conversion)
            # conversion2 = conversion[144:]
        context = {"svg" :vacio}
        # Or to an actual file:
        # with open("imagenes/somefile.jpeg", "wb") as f:
        #     EAN8("2", writer=SVGWriter()).write(f)
        return render(request, 'exito.html',context )

    else:
        formulario = MiFormulario()
        return render(request, 'index.html', {'form': formulario})






#FORMAT EAN 14 CODEBAR


def ean14(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        print(formulario)
        desde = formulario.cleaned_data['desde']
        hasta = formulario.cleaned_data['hasta']

        rv = BytesIO()
        vacio = []
        for x in range(int(desde), int(hasta)+1):
            ch = str(x).zfill(13)
            print(ch)
            pruea = EAN14(ch, writer=SVGWriter()).render(rv)
            conversion = pruea.decode('utf-8')
            print(conversion)
            vacio.append(conversion)
            # conversion2 = conversion[144:]
        context = {"svg" :vacio}
        # Or to an actual file:
        # with open("imagenes/somefile.jpeg", "wb") as f:
        #     Code39("2", writer=SVGWriter()).write(f)
        return render(request, 'exito.html',context )

    else:
        formulario = MiFormulario()
        return render(request, 'index.html', {'form': formulario})




# def ejecutar(request):
#     rv = BytesIO()
#     Code39(str(2), writer=SVGWriter()).render(rv)
#     anular = Code39(str(), writer=SVGWriter()).render()

#     # anular.split('<svg')
#     context = {"svg" :anular }
# # Or to an actual file:
#     with open("imagenes/somefile.jpeg", "wb") as f:
#         Code39("2", writer=SVGWriter()).write(f)
#     return render(request, 'exito.html',context )

# def barcode_view(request, data_to_encode, barcode_format):
#     return generate_barcode(data_to_encode, barcode_format)


# def generate_barcode(data, barcode_format):
#     # Generate the barcode
#     code = barcode.get(barcode_format, data, writer=ImageWriter())
#     # Create a temporary in-memory buffer to store the image
#     buffer = BytesIO()
#     # Save the barcode to the buffer
#     code.save(buffer)
#     # Move the buffer's cursor to the beginning
#     buffer.seek(0)
#     # Return the buffer as a Django response with the appropriate content type
#     return HttpResponse(buffer.getvalue(), content_type='image/png')

# def barcode_view(request, data_to_encode, barcode_format):
#     return generate_barcode(data_to_encode, barcode_format)