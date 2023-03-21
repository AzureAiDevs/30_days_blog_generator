{% set image_url = static_img_path ~ '/banner-day' ~ day ~ '.png' -%}
{% set blog_url = daily_blog_url ~ '/' ~ slug ~ 'day' ~ day -%}
{% set twitter_description = description -%}
{% if tweet %}{% set twitter_description = tweet %}{% endif -%}
{% set twitter_description = emoji ~ "Welcome to day " ~ day ~ " of #" ~ campaign ~ ". " ~ twitter_description -%}
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
description: "{{ emoji }}Welcome to day {{day}} of #{{ campaign }}. {{ description }} {{ daily_blog_url }}/day{{ day }}"
---

import Social from '@site/src/components/social';

<head>

  <meta name="twitter:url" content="{{ blog_url }}" />
  <meta name="twitter:title" content="{{ title }}" />
  <meta name="twitter:description" content="{{ emoji }}Welcome to day {{day}} of #{{ campaign }}. {{ description }}" />
  <meta name="twitter:image" content="{{ image_url }}" />
  <meta name="twitter:card" content="summary_large_image" />

  <meta property="og:url" content="{{ blog_url }}" />
  <meta property="og:title" content="Welcome to day {{day}} {{ emoji }}{{ title }}" />
  <meta property="og:description" content="{{ description }} {{ blog_url }} {{ social_tags }} {% if social_tag %}{{ social_tag }}{% endif %}" />
  <meta property="og:image" content="{{ image_url }}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Azure AI Developer" />

  <link rel="canonical" {% if canonical %}href="{{ canonical }}" {% else %} href="{{ daily_blog_url }}/day{{ day }}" {% endif %} />

</head>

{% if canonical -%}- 👓 [View today's article]({{ canonical }}){% endif %}
- 🌤️ [Continue the Azure AI Cloud Skills Challenge](https://aka.ms/30-days-of-azure-ai-challenge)
- 🏫 [Bookmark the Azure AI Technical Community](https://techcommunity.microsoft.com/t5/artificial-intelligence-and/ct-p/AI)
- 🙋🏾‍♂️ [Ask a question about this post on GitHub Discussions](https://github.com/AzureAiDevs/hub/discussions/categories/{{ day }}-{{ title|lower|replace(":", "")|replace(" ", "-") | replace("/", "") }})
- 💡 [Suggest a topic for a future post](https://github.com/AzureAiDevs/hub/discussions/categories/call-for-content)

### Please share

<Social
    page_url="{{ blog_url }}"
    image_url="{{ image_url }}"
    title="{{ title }}"
    description= "{% if tweet %}{{ emoji}}Day {{ day }} of #{{ campaign }}. {{ tweet }}{% else %}{{ twitter_description }}{% endif %}"
    hashtags="{{ social_tags }}{% if social_tag %},{{ social_tag }}{% endif %}"
    hashtag="#30DaysOfAzureAi"
/>

## 🗓️ Day {{ day }} of #30DaysOfAzureAI

<!-- README
The following description is also used for the tweet. So it should be action oriented and grab attention 
If you update the description, please update the description: in the frontmatter as well.
-->

**{{ description }}**

<!-- README
The following is the intro to the post. It should be a short teaser for the post.
-->

{% include 'content/' + folder + '/intro.md' ignore missing %}

## 🎯 What we'll cover

<!-- README
The following list is the main points of the post. There should be 3-4 main points.
 -->

{% set template = "## What We'll Cover" %}
{% include 'content/' + folder + '/covered.md' ignore missing %}

<!-- 
- Main point 1
- Main point 2
- Main point 3 
- Main point 4
-->

![Image banner for day {{day}}]({{ static_img_folder }}/banner-day{{day}}.png)

<!-- README
Add or update a list relevant references here. These could be links to other blog posts, Microsoft Learn Module, videos, or other resources.
-->

{% if no_reference_section != true %}

## 📚 References

{% include 'content/' + folder + '/references.md' ignore missing %}
{% endif %}

<!-- README
The following is the body of the post. It should be an overview of the post that you are referencing.
See the Learn More section, if you supplied a canonical link, then will be displayed here.
-->

{% set template = '## 🚌 Introduction' %}
{% include 'content/' + folder + '/body.md' ignore missing %}

{% if canonical -%}

## 👓 View today's article

Today's [article]({{ canonical }}).
{% endif %}

## 🙋🏾‍♂️ Questions?

[Remember, you can ask a question about this post on GitHub Discussions](https://github.com/AzureAiDevs/hub/discussions/categories/{{ day }}-{{ title|lower|replace(":", "")|replace(" ", "-") | replace("/", "") }})

## 📍 30 days roadmap

What's next? View the [#30DaysOfAzureAI Roadmap](/hub/roadmap/30days)

[![]({{ static_img_folder }}/rss.png) Click to subscribe](https://azureaidevs.github.io/hub/2023-aia/rss.xml)
