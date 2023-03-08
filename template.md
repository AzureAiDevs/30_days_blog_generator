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

- 📧 [Sign up for the Azure AI Developer Newsletter](https://microsoft.github.io/Low-Code/subscribe)
- 📰 [Subscribe to the #30DaysOfAzureAI RSS feed](https://azureaidevs.github.io/hub/blog/rss.xml)
- 📌 [Ask a question about this post on GitHub Discussions](https://github.com/AzureAiDevs/Discussions/discussions/categories/{{ day }}-{{ title|lower|replace(":", "")|replace(" ", "-") }})
- 💡 [Suggest a topic for a future post](https://github.com/AzureAiDevs/Discussions/discussions/categories/call-for-content)

## Day _{{ day }}_ of #{{ campaign }}

<!-- README
The following description is also used for the tweet. So it should be action oriented and grab attention 
If you update the description, please update the description: in the frontmatter as well.
-->

**{{ description }}**

<!-- README
The following is the intro to the post. It should be a short teaser for the post.
-->

{% include 'content/' + folder + '/intro.md' ignore missing %}

## What we'll cover

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

![Image shows authors and product icons](banner.png)
<!-- ![Image shows authors and product icons](../../../static/img/2023/banner-day{{day}}) -->

<!-- README
Add or update a list relevant references here. These could be links to other blog posts, Microsoft Learn Module, videos, or other resources.
-->

{% if references %}
### References

{% for item in references -%}
- {{item}}
{% endfor -%}
{% endif %}

<!-- README
The following is the body of the post. It should be an overview of the post that you are referencing.
See the Learn More section, if you supplied a canonical link, then will be displayed here.
-->

{% set template = '## Introduction' %}
{% include 'content/' + folder + '/body.md' ignore missing %}

{% if canonical -%}

## Learn More

To learn more, check out this [article]({{ canonical }}).
{% endif %}

## Questions?

[Remember, you can ask a question about this post on GitHub Discussions](https://github.com/AzureAiDevs/Discussions/discussions/categories/{{ day }}-{{ title|lower|replace(":", "")|replace(" ", "-") }})
