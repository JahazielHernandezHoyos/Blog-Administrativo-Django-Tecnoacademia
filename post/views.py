from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostListView(ListView):
    model = Post

class PostListDetailView(DetailView):
    model = Post

class PostListCreateView(CreateView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

class PostDeleteView(DetailView):
    model = Post