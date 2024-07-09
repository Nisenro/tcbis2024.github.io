---
layout: default
title: Executive Committee
permalink: /executive-members/
---

<div class="executive-committee">
    <h1>Executive Committee Members</h1>

    {% for member in site.data.committee_members %}
        {% include committee_member.html name=member.name role=member.role org=member.org %}
    {% endfor %}
</div>