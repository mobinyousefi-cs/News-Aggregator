#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/views.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Views for listing articles, viewing sources, and article details.

Usage:
Mapped in core/urls.py

Notes:
- Paginated index.

===============================================================================================================
"""
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Article, Source
from .forms import SourceForm


def index(request):
    qs = Article.objects.select_related("source").all()
    paginator = Paginator(qs, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/index.html", {"page_obj": page_obj})


def sources(request):
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:sources")
    else:
        form = SourceForm()
    return render(request, "core/sources.html", {"sources": Source.objects.all(), "form": form})


def article_detail(request, pk: int):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "core/article_detail.html", {"article": article, "now": timezone.now()})