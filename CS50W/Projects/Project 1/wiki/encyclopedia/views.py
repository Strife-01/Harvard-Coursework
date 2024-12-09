from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from random import randint
from markdown import markdown

from . import util

NOT_FOUND = """
                <h1>404</h1>
                <h2>PAGE NOT FOUND</h2>
            """

NAME_ERROR = """
                <h1>There is already a page with this name in the database!</h1>
            """

CONTENT_ERROR = """
                <h1>Add valid content!</h1>
"""

class NewPageForm(forms.Form):
    name = forms.CharField(label="Page Name")
    content = forms.CharField(widget=forms.Textarea, label="Content")

    # def pore_populate(self, name, content):
    #     self.name = name
    #     self.content = content

def index(request):
    if request.method == "POST":
        r = request.POST["q"]
        if r in util.list_entries():
            return HttpResponseRedirect(f"/wiki/{r}")
        else:
            return render(request, "encyclopedia/index.html", {
            "entries": [entry for entry in util.list_entries() if r in entry.lower() and r != ""]
            })


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, wiki):
    if wiki not in util.list_entries():
        return render(request, "encyclopedia/errors.html", {
            "name": "404: Not Found",
            "content": NOT_FOUND
        })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "name": wiki,
            "content": markdown(util.get_entry(wiki))
        })

def add(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form["name"].value() in util.list_entries():
            return render(request, "encyclopedia/errors.html", {
            "name": "Error",
            "content": NAME_ERROR
            })
        elif not form["content"].value():
            return render(request, "encyclopedia/errors.html", {
            "name": "Error",
            "content": CONTENT_ERROR
            })
        else:
            with open(f"entries/{form['name'].value()}.md", "w") as new_page:
                new_page.write(form['content'].value())
            return render(request, "encyclopedia/wiki.html", {
                "name": form['name'].value(),
                "content": markdown(util.get_entry(form['name'].value()))
            })
    
    return render(request, "encyclopedia/add.html", {
        "form": NewPageForm()
    })

def edit(request, name):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if not form["content"].value():
            return render(request, "encyclopedia/errors.html", {
            "name": "Error",
            "content": CONTENT_ERROR
            })
        else:
            with open(f"entries/{form['name'].value()}.md", "w") as file:
                file.write(form["content"].value())
            return render(request, "encyclopedia/wiki.html", {
                "name": form['name'].value(),
                "content": markdown(util.get_entry(form['name'].value()))
            })
    else:

        form = NewPageForm()

        content = None

        with open(f"entries/{name}.md", "r") as file:
            content = file.read()

        form.initial["name"] = name
        field = form.fields["name"]
        field.widget = field.hidden_widget()

        form.initial["content"] = content

        return render(request, "encyclopedia/edit.html", {
            "form": form
        })

def random(request):
    index = randint(0, len(util.list_entries()) - 1)
    return HttpResponseRedirect(f"/wiki/{util.list_entries()[index]}")