---
layout: default
title: Conferences
permalink: /conference/
---

<div class="conferences">
    <h1>Upcoming Conferences</h1>
    <div id="upcoming-conferences"></div>
    <h2>Past Conferences</h2>
    <div id="past-conferences"></div>

    {% for conference in site.data.conferences.json %}
        {% include conferences.html name=conference.name date=conference.date location=conference.location link=conference.link %}
    {% endfor %}
    
</div>



