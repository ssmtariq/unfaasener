from google.cloud import datastore

client = datastore.Client(project="unfaasenerdemo")

# Query all entities of kind "routingDecision"
query = client.query(kind="routingDecision")
results = list(query.fetch())

if results:
    print("Found Datastore entities:")
    for entity in results:
        print(entity)
else:
    print("No routingDecision entities found.")
