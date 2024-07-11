---
title: "Gallery"
date: 2024-07-05
menus:
  main:
    name: Home
    weight: -1
---
{{ $filter := images.Grayscale }}
{{ with resources.Get "painting/p1.jpg" }}
  {{ with . | images.Filter $filter }}
    <img src="{{ .RelPermalink }}" width="{{ .Width }}" height="{{ .Height }}" alt="">
  {{ end }}
{{ end }}