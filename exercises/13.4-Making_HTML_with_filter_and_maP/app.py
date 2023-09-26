all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
yey=[]
def generate_li(color):
    for x in color:
        nombre=x["label"]
        yey.append("<li>"+nombre+"</li>")
    return yey
    
def filter_colors(all_colors):
    sexy=list(filter(lambda hot: hot["sexy"], all_colors))
    return generate_li(sexy)

print(filter_colors(all_colors))