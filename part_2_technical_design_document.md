# Areas of Interest GeoTIFF Generator

This document describes the high level technical design for a system which is able to generate GeoTIFF files
from user inputted GeoJSON or Shapefiles.

## MVP

This section describes a simple system that meets the outlined requirements.

### High level technical diagram

```
| UX | - | Web Server | - | Async Message System |
                |
              | DB |
```

### Generation of GeoTIFF Files

The original MVP for this project consists of a Python script which ingests a Shapefile and produces a GeoTIFF file.
For a cloud based solution, this script can then be run inside an async task (e.g. Celery to RabbitMQ as the broker), 
so that multiple user requests can be handled independently. 
Additionally, the messaging cluster can be scaled to meet the required 1 hour SLA.

The async task can be triggered in a number of ways, but a good solution would be to have this triggered from a
web service (such as Django) running an API. This way the system can easily be integrated into other pipelines as needed,
and will provide additional benefits outlined below. The API should also include user specific authentication (such as
OAuth) to allow for linking specific requests to specific users.

Once the Celery task has been completed, it can upload the result GeoTIFF file to web storage (e.g. AWS S3), and another
task can be triggered to notify the user.

### UX

As mentioned above, by using an API a technical user can simply use any HTTP client (e.g. curl) to upload the files,
and additional metadata. However, a web service can also provide a user interface without much additional work.
Basic authentication and file upload can be quickly implemented to reduce friction with the system.

By using Django, it's possible to quickly extend the Django Admin system (which already includes required features such
as user authentication), to provide a basic web form for uploading the required files, and triggering the task.

If there is a pre-existing platform for running other tools, this could also be extended and connected to the API
instead.

### Notification of User

Once the task is complete and the GeoTIFF file is created, a new task should be triggered to notify the related user.
Because the API / UX both require some form of authentication, this can be linked to a specific user, which in turn
should allow access to a User data model containing a way to notify the user (such as email). The user can then be sent
an email either with the file directly (downloaded from web storage), or a link to the file itself.

### Job Data Model

To correctly track and audit all requests to the system, a database (such as Postgres) should be linked to the
web service.

When a job is initialised, a table entry should be created with the following information:
- User ID
- Input File (depending on size this may be better stored in web storage and a URL stored in it's place).
- Status (Pending, Ongoing, Complete, Error).
- Created At / Updated At timestamps.

During a job run, it's Status can then be moved to Ongoing, and eventually Complete or Error as needed. On successful
completion, the web storage url of the GeoTIFF file can be added, linking the input and output files together.

To created a fully audited process, a package such as Django History can be added to capture model changes.
