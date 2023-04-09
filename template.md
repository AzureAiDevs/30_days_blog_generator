{% set image_url = static_img_path ~ '/banner-day' ~ day ~ '.png' -%}
{% set blog_url = daily_blog_url ~ '/' ~ slug ~ 'day' ~ day -%}
{% set twitter_description = description -%}
{% if tweet %}{% set twitter_description = tweet %}{% endif -%}
{% set twitter_description = emoji ~ "Welcome to day " ~ day ~ " of #" ~ campaign ~ ". " ~ twitter_description-%}
{% set discussion_url = 'https://github.com/AzureAiDevs/hub/discussions/categories/' ~ audience | lower | replace(" ", "-") -%}
---
slug: "day{{ day }}"
title: "{{ day }}. {{ emoji }}{{ title }}"
authors: {{ authors }}
{% if visible %}draft: false{% else %}draft: true{% endif %}
hide_table_of_contents: false
toc_min_heading_level: 2
toc_max_heading_level: 3
{% if keywords %}keywords: {{ keywords }}{% endif %}
{% if tags %}tags: {{ tags }}{% endif %}

image: {{ image_url }}
description: "{{ twitter_description }}"
---

import Social from '@site/src/components/social';

<head>

  <meta name="twitter:url" content="{{ blog_url }}" />
  <meta name="twitter:title" content="{{ title }}" />
  <meta name="twitter:description" content="{{ twitter_description }}" />
  <meta name="twitter:image" content="{{ image_url }}" />
  <meta name="twitter:card" content="summary_large_image" />

  {% if canonical -%}
  <link rel="canonical" {% if canonical %}href="{{ canonical }}" {% else %} href="{{ daily_blog_url }}/day{{ day }}" {% endif %} />
  {% endif -%}

</head>

{% if canonical -%}- 👓 [View today's article]({{ canonical }}){% endif %}
- 🍿 [Tune into the AI Show](https://aka.ms/ai-april-ai-show)
- 🧬 [Connect with Humans in AI](/hub/humans-in-ai)
- 🌤️ [Continue the Azure AI Cloud Skills Challenge](https://aka.ms/30-days-of-azure-ai-challenge)
- 🏫 [Bookmark the Azure AI Technical Community](https://aka.ms/ai-april-tech-community)
- ❤️ [Learn about the Microsoft MVP Program](https://aka.ms/ai-april-mvp-program)
- 💡 [Suggest a topic for a future post](https://github.com/AzureAiDevs/hub/discussions/categories/call-for-content)

### Please share

<Social
    page_url="{{ blog_url }}"
    image_url="{{ image_url }}"
    title="{{ title }}"
    description= "{{ twitter_description }}"
    hashtags="{% if social_tag %}{{ social_tag }}{% endif %}"
    hashtag="#30DaysOfAzureAi"
/>

## 🗓️ Day {{ day }} of #30DaysOfAzureAI

<!-- Short description section -->

**{{ description }}**

<!-- Intro section -->

{% include 'content/' + folder + '/intro.md' ignore missing %}

## 🎯 What we'll cover

<!-- What we'll cover section -->

{% set template = "## What We'll Cover" %}
{% include 'content/' + folder + '/covered.md' ignore missing %}


{% if canonical -%}
[![Image banner for day {{day}}]({{ static_img_folder }}/banner-day{{day}}.png)]({{ canonical }})
{% else %}
![Image banner for day {{day}}]({{ static_img_folder }}/banner-day{{day}}.png)
{% endif %}

<!-- Reference section -->

{% set reference_file = 'content/' ~ folder ~ '/references.md' -%}
{% set reference_file_exists = reference_file|path_exists -%}
{% if reference_file_exists %}

## 📚 References

{% include reference_file ignore missing %}
{% endif %}

<!-- Body section -->

{% set recap_file = 'content/' ~ folder ~ '/recap.md' -%}
{% set recap_file_exists = recap_file|path_exists -%}
{% if recap_file_exists %}
{% include recap_file ignore missing -%}
{%else%}
{% include 'content/' + folder + '/body.md' ignore missing -%}
{% endif %}

{% if canonical -%}

## 👓 View today's article

Today's [article]({{ canonical }}).
{% endif %}

## 🙋🏾‍♂️ Questions?

[You can ask questions about this post on GitHub Discussions]({{ discussion_url }})

## 📍 30 days roadmap

What's next? View the [#30DaysOfAzureAI Roadmap](/hub/roadmap/30days)

## 🧲 Subscribe

- 📬 [Subscribe to the monthly Azure AI and Machine Learning Tech Newsletter](https://aka.ms/azure-ai-dev-newsletter)
- [![The image is the blog RSS feed available icon]({{ static_img_folder }}/rss.png) Subscribe to the blog RSS XML feed](https://azureaidevs.github.io/hub/2023-aia/rss.xml)
