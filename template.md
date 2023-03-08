---
slug: {{slug}}-day{{day}}
title: "{{ day }}. {{ emoji }}{{ title }}"
authors: {{ authors }}
draft: false
hide_table_of_contents: false
toc_min_heading_level: 2
toc_max_heading_level: 3
{% if keywords %}keywords: {{ keywords }}{% endif %}
{% if tags %}tags: {{ tags }}{% endif %}

image: "{{site_url}}/img/{{slug}}/banner-day{{day}}.png"
description: "{{ description }}"
---

<head>

  <link rel="canonical" {% if canonical %}href="{{ canonical }}" {% else %} href="{{ blog_url }}/{{ slug }}-day{{ day }}" {% endif %} />

</head>

- 📧 [Subscribe to the Azure AI Developer Newsletter](https://microsoft.github.io/Low-Code/subscribe)
- 📌 [Ask a question about this post on GitHub Discussions](https://github.com/AzureAiDevs/Discussions/discussions/categories/{{ day }}-{{ title|lower|replace(":", "")|replace(" ", "-") }})
- 💡 [Suggest a topic for a future post](https://github.com/AzureAiDevs/Discussions/discussions/categories/call-for-content)

## Day _{{ day }}_ of #{{ campaign }}

**{{ description }}**

{% include 'content/' + folder + '/intro.md' ignore missing %}

## What we'll cover

{% set template = "## What We'll Cover" %}
{% include 'content/' + folder + '/covered.md' ignore missing %}

<!-- 
- Main point 1
- Main point 2
- Main point 3 
-->

![Image shows authors and product icons](banner.png)
<!-- ![Image shows authors and product icons](../../../static/img/2023/banner-day{{day}}) -->

{% if references %}
### References

{% for item in references -%}
- {{item}}
{% endfor -%}
{% endif %}


{% set template = '## Introduction' %}
{% include 'content/' + folder + '/body.md' ignore missing %}

<!-- Content for the day goes here. -->

{% if canonical -%}

## Learn More

To learn more, check out this [article]({{ canonical }}).
{% endif %}

## Questions?

[Remember, you can ask a question about this post on GitHub Discussions](https://github.com/AzureAiDevs/Discussions/discussions/categories/{{ day }}-{{ title|lower|replace(":", "")|replace(" ", "-") }})
