from django.http import HttpResponse
from main.models import Todo

def index(request):
   todo = Todo.objects.all().first()
   context = f"""
   <h1>Todo`s</h1>
   <ul>
      <li>
         <p>{todo}</p>
      </li>
   </ul>
   """
   return HttpResponse(context)

def show(request,id):
   todos = Todo.objects.filter(id=id)
   items = []
   if todos:
      for todo in todos:
         for item in todo.items.all():
            items.append(item)
   return HttpResponse(f"""
                  <ul>
                       <li>
                           <p>{items[0].text}</p>
                       </li>
                  </ul>
                  <ul>
                       <li>
                           <p>{items[1].text}</p>
                       </li>
                  </ul>""")
   