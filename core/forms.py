#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: News Aggregator
File: core/forms.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-02
Updated: 2025-11-02
License: MIT License (see LICENSE file for details)
=

Description:
Simple form to add/edit a Source (optional UI feature).

Usage:
Used in sources view for quick bootstrap.

Notes:
- Basic validation only.

===============================================================================================================
"""
from django import forms
from .models import Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ["name", "homepage", "parser_name", "is_active"]