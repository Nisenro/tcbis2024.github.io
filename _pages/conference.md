---
layout: default
title: Conferences
permalink: /conference/
---

<div class="conferences">
    <h1>Upcoming Conferences</h1>

    {% for conference in site.data.conferences %}
        {% include conferences.html name=conference.name date=conference.date location=conference.location link=conference.link %}
    {% endfor %}
</div>


