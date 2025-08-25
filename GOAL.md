i kinda just want to know if anybody ever visits my websites

but i’m less interested in actually monitoring traffic than just making something; i’m sure there’s a great tool out there like googleanalytics i could just hook into if i want/need.

so the idea is more to spin up a microservice on my domain that exposes an endpoint which will send over a request for a widget.

that widget will have a little message and a button that lets them say hello. that ‘hello’ should add a record to my database with timeCreated

i want to make this a hypermedia API, so the consuming application uses htmx to request the service and expects that the response will be html to replace the calling element. Python and Flask bc that's all I need. Would consider using Go or .NET or Java but not the point to build w something new rn.
