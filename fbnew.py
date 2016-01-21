import fb

token = "get token from graph explorer"

facebook = fb.graph.api(token)

#To publish to group
facebook.publish(cat="feed", id="group Id", message="jai balayya")
