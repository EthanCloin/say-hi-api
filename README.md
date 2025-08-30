# Goal
I want to have an API here that I can request from other applications to receive html fragments. 

Let's say I make 3 different websites and I have the 'Say Hi' component living on an endpoint in this app.
I would like those apps to all be able to GET 'mydomain.com/say-hi' and receive the component along with all its functionality.

# Concerns

## CORS
CORS is an issue here. I own all the domains involved, but I need to allow the request methods + headers that the 
shared components need to leverage.

## HTMX Functionality
HTMX defaults to relative URLs. So if I import the say-hi component to my portfolio site, it will look like this
```html
<div id="say-hi-widget" class="">
    <script src="/static/htmx.2.0.6.min.js"></script>
    <style>
        ...
    </style>
    <div class="hi-api__container">
        <button hx-post="/hi" hx-target="#say-hi-widget" hx-swap="outerHTML" class="hi-api__btn">Say Hi</button>
    </div>
</div>
```
Both the script tag importing HTMX and the hx-post going to `/hi` are expecting the client app to supply those endpoints.
Hmmm. This is obviously not what HTMX was designed to do, is it worth engineering around it?

### Options
I could always use absolute links in my HTML that is served from the component library.
I could add a wrapper which serves the HTML as a [Web Component](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) so I avoid any namespace clashes.


