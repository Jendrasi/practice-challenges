## Question Description

Refactor the _AlertService_ and _MapAlertDAO_ classes:

- Create a new package-private interface, named _AlertDAO_, that contains the same methods as _MapAlertDAO_.
- _MapAlertDAO_ should implement the _AlertDAO_ interface.
- _AlertService_ should have a public constructor that accepts _AlertDAO_.
- the _raiseAlert_ and _getAlertTime_ methods should use the object passed through the constructor.

## Notes

There isn't much to say about this one. It was rightly graded **"Easy"** and was very straightforward.