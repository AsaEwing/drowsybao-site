---
title: "Test Blog"
date: 2024-07-15
imgdir: "painting"
featured_image: "p1.jpg"
description: "This is a test blog post with image processing"
resources:
  - src: "p1.jpg"
    title: "Sample Image 1"
    description: "Description for Sample Image 1"
---

# Test Blog Post

This is a sample blog post to test image processing and filters in Hugo.

## Images

Below are the images with applied filters:

{{ $imgdir := (.Params.imgdir | default "NULL") }}
{{ $images := resources.Match (printf "images/%s/*.jpg" $imgdir) }}

{{ range $image := $images }}
  {{ $imageFiltered := $image }}

  <!-- Apply Colorize filter -->
  {{ $imageFiltered = $imageFiltered | images.Colorize 30 80 80 }}

  <!-- Apply Brightness filter -->
  {{ $imageFiltered = $imageFiltered | images.Brightness -12 }}

  <!-- Output the filtered image -->
  <div class="gallery-item">
    <img src="{{ $imageFiltered.RelPermalink }}" alt="{{ $imageFiltered.Name }}" width="300">
    <h2>{{ $image.Title }}</h2>
    <p>{{ $image.Description }}</p>
  </div>

  <!-- JavaScript for logging to console -->
  <script>
    console.log("Filtered image path: {{ $imageFiltered.RelPermalink }}");
  </script>
{{ end }}