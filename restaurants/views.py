from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context ={
        "my_list": [
            {
            "restaurant_name": "Little Rubys",
            "food_type": "Yummy"
        },
        {
            "restaurant_name": "Tatami",
            "food_type": "Japanese"
        },
        {
            "restaurant_name": "Burger King",
            "food_type": "Fast food"
        },
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context ={
        "my_object":
        {
            "restaurant_name": "Little Rubys",
            "food_type": "Yummy"
        }

    }
    return render(request, 'detail.html', context)
