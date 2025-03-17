{{ title }} {# 60 char, keywords, emotion #}

{{ description }} {# Use keywords, first 200 characters are most important #}

# ▬ Contents of this video ▬▬▬▬▬▬▬▬▬▬▬▬

{% for chapter in chapters %}
{{ chapter.start }} {{ chapter.title }} ({{ chapter.emojis }})
{% endfor $}
{#
00:00 Intro & Background (👋)
01:18 Money Stashes (💰)\
02:25 Parka, Laptop, Flip Flops (🧥💻🩴)
...
#}

# ▬ More ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Website • https://gatlen.me/
GitHub • https://github.com/GatlenCulp
Medium • https://medium.com/@gatlenculp

{{ tags }}
{#
#travel #minimalism #onebag
First 3 show up in title, I believe up to 6
#}
