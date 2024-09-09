---
layout: default
title: Conferences
permalink: /conference/
---

<div class="conferences">
    <h1>Upcoming Conferences</h1>
    <div id="upcoming-conferences"></div>
    

    {% for conference in site.data.conferences %}
    {% include conferences.html name=conference.title date=conference.date location=conference.location country=conference.country link=conference.link %}
{% endfor %}
    <!-- <h1>Past Conferences</h1>
    <div id="past-conferences"></div> -->
</div>
